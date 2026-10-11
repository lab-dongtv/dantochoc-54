#!/usr/bin/env python3
"""Nhúng dữ liệu 54 dân tộc + dân số (demography.json) từ skill vào index.html.

Nguồn: .claude/skills/dan-toc-viet-nam/data/*.json
Chạy:  python3 aq-dantochoc/build.py
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent
DATA_DIR = ROOT / ".claude/skills/dan-toc-viet-nam/data"
GROUPS = ["viet-muong", "tay-thai", "hmong-dao", "kadai", "mon-khmer", "nam-dao", "han", "tang-mien"]
REQUIRED = ["id", "vi", "ja", "group", "pop", "region_vi", "region_ja", "hi_vi", "hi_ja", "kin"]

rows = []
for g in GROUPS:
    f = DATA_DIR / f"{g}.json"
    if not f.exists():
        sys.exit(f"thiếu {f}")
    for r in json.loads(f.read_text(encoding="utf-8")):
        missing = [k for k in REQUIRED if k not in r]
        if missing or r["group"] != g:
            sys.exit(f"{f.name}: {r.get('id')} lỗi schema {missing or r['group']}")
        rows.append(r)

# ảnh trang phục: assets/costume/credits-*.json → trường "photo"
photos = {}
for cf in sorted((ROOT / "assets/costume").glob("credits-*.json")):
    photos.update(json.loads(cf.read_text(encoding="utf-8")))
for r in rows:
    ph = photos.get(r["id"])
    if ph and (ROOT / "assets" / ph["file"]).exists():
        r["photo"] = {k: ph.get(k, "") for k in ("file", "page", "author", "license", "desc_vi", "desc_ja")}
    else:
        r.pop("photo", None)

ids = [r["id"] for r in rows]
dup = {i for i in ids if ids.count(i) > 1}
if dup:
    sys.exit(f"trùng id: {dup}")
if len(rows) != 54:
    print(f"CẢNH BÁO: {len(rows)} dân tộc (cần 54)", file=sys.stderr)

payload = json.dumps(rows, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
page = ROOT / "index.html"
html = page.read_text(encoding="utf-8")
pat = re.compile(r'(<script id="ethnic-data" type="application/json">)(.*?)(</script>)', re.S)
if not pat.search(html):
    sys.exit("không tìm thấy <script id=ethnic-data>")
html = pat.sub(lambda m: m.group(1) + "\n" + payload + "\n" + m.group(3), html, count=1)
# ảnh cho từng khu/công trình (chỉ nhúng file có thật trong assets/)
ARCH_IMAGES = {
    "trong-dong": [("wm-hero.jpg", "Toà Trống Đồng", "銅鼓館"), ("wm-vme-in-1.jpg", "", ""), ("wm-vme-in-2.jpg", "", ""),
                   ("wm-vme-in-3.jpg", "", ""), ("wm-vme-in-4.jpg", "", "")],
    "vuon": [("wm-vme-exterior.jpg", "Khuôn viên bảo tàng", "博物館の敷地"), ("wm-vme-thuydinh.jpg", "Thuỷ đình", "水上人形劇の舞台")],
    "canh-dieu": [("wm-vme-kite.jpg", "Toà Cánh Diều", "凧館"), ("wm-vme-kite-2.jpg", "", "")],
    "bana": [("wm-bahnar-nharong.jpg", "", ""), ("wm-vme-bana-2.jpg", "", "")],
    "ede": [("wm-ede-nhadai.jpg", "", ""), ("wm-vme-ede-2.jpg", "", "")],
    "giarai": [("wm-giarai-nhamo.jpg", "", "")],
    "cotu": [("wm-cotu-nhamo.jpg", "", "")],
    "hani": [("wm-hani-nhatrinh.jpg", "", "")],
    "cham": [("wm-vme-cham.jpg", "", "")],
    "viet": [("wm-vme-viet.jpg", "", "")],
    "tay": [("wm-vme-tay.jpg", "", "")],
    "dao": [("wm-vme-dao.jpg", "", "")],
    "hmong": [("wm-vme-hmong.jpg", "", "")],
}
CAPTIONS_FILE = ROOT / "assets/captions.json"  # tuỳ chọn: {"file.jpg": ["vi", "ja"]}
captions = json.loads(CAPTIONS_FILE.read_text(encoding="utf-8")) if CAPTIONS_FILE.exists() else {}
arch_file = DATA_DIR / "vme-architecture.json"
arch = json.loads(arch_file.read_text(encoding="utf-8")) if arch_file.exists() else []
for a in arch:
    imgs = []
    for f, vi, ja in ARCH_IMAGES.get(a["id"], []):
        if (ROOT / "assets" / f).exists():
            cvi, cja = captions.get(f, [vi, ja])
            imgs.append({"f": f, "vi": cvi or vi, "ja": cja or ja})
    a["img"] = imgs
apat = re.compile(r'(<script id="arch-data" type="application/json">)(.*?)(</script>)', re.S)
html = apat.sub(lambda m: m.group(1) + "\n" + json.dumps(arch, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") + "\n" + m.group(3), html, count=1)

demo = json.loads((DATA_DIR / "demography.json").read_text(encoding="utf-8"))
dpat = re.compile(r'(<script id="demo-data" type="application/json">)(.*?)(</script>)', re.S)
if not dpat.search(html):
    sys.exit("không tìm thấy <script id=demo-data>")
html = dpat.sub(lambda m: m.group(1) + "\n" + json.dumps(demo, ensure_ascii=False, separators=(",", ":")) + "\n" + m.group(3), html, count=1)
from html import escape
cred = "".join(
    f'<div>{escape(r["vi"])}: <a href="{escape(r["photo"]["page"])}">{escape(r["photo"]["file"].split("/")[-1])}</a>'
    f' — {escape(r["photo"]["author"])}, {escape(r["photo"]["license"])}</div>'
    for r in rows if r.get("photo"))
cpat = re.compile(r'(<!--COSTUME-CREDITS-->)(.*?)(<!--/COSTUME-CREDITS-->)', re.S)
html = cpat.sub(lambda m: m.group(1) + cred + m.group(3), html, count=1)
page.write_text(html, encoding="utf-8")
print(f"index.html: {len(rows)} dân tộc, tổng dân số {sum(r['pop'] for r in rows):,}; ảnh trang phục: {sum(1 for r in rows if r.get('photo'))}/54; kiến trúc: {len(arch)} mục, {sum(len(a['img']) for a in arch)} ảnh")
