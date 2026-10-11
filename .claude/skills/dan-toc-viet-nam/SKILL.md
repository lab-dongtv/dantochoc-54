---
name: dan-toc-viet-nam
description: Kiến thức về 54 dân tộc Việt Nam theo 8 nhóm ngôn ngữ, kèm liên kết với các tộc người cùng nguồn ở Đông Nam Á (Lào, Thái Lan, Myanmar, Campuchia, Malaysia, Indonesia, Philippines, Đài Loan) và Trung Quốc (Choang, Miêu, Dao, Di, Hà Nhì, Lê…). Dùng khi người dùng hỏi về một dân tộc cụ thể, so sánh các dân tộc, tộc người xuyên biên giới, hoặc chuẩn bị/thuyết minh chuyến tham quan Bảo tàng Dân tộc học Việt Nam (VME, vme.org.vn). Song ngữ Việt/Nhật (日本語の質問にも対応：ベトナム54民族、民族学博物館).
---

# 54 dân tộc Việt Nam & liên kết khu vực

Skill này phục vụ chuyến tham quan **Bảo tàng Dân tộc học Việt Nam** (Nguyễn Văn Huyên, Cầu Giấy, Hà Nội) ngày 11/10/2026, nhưng dùng được cho mọi câu hỏi về các dân tộc Việt Nam.

## Cách dùng

1. Xác định dân tộc hoặc nhóm ngôn ngữ người dùng hỏi, tra bảng dưới để biết file.
2. Đọc **chỉ** file `references/<nhóm>.md` cần thiết (mỗi file có phần mở đầu về nhóm + từng dân tộc).
3. Cần dữ liệu ngắn, song ngữ Việt/Nhật hoặc so sánh nhiều dân tộc → đọc `data/<nhóm>.json` (schema bên dưới).
4. Trả lời theo ngôn ngữ người hỏi. Với người Nhật, dùng tên katakana + 族 trong trường `ja`, và khi có thể thì liên hệ với Nhật Bản (vd: văn hoá lúa nước, nhà sàn ~ kho thóc thời Yayoi, nhuộm chàm ~ 藍染, tục ăn trầu…), nhưng không suy diễn quá mức.
5. Khi nói về “liên kết khu vực”, phân biệt rõ 3 mức: **cùng tộc người** (bị biên giới chia cắt), **gần gũi ngôn ngữ** (cùng nhánh), **chung ngữ hệ/xa**. Không đánh đồng tên gọi giữa các nước.

## 8 nhóm ngôn ngữ — 54 dân tộc

| Nhóm (file) | Ngữ hệ | Dân tộc | Họ hàng ngoài biên giới tiêu biểu |
|---|---|---|---|
| Việt–Mường (`viet-muong`) | Nam Á | Kinh, Mường, Thổ, Chứt | Người Kinh ở Đông Hưng (京族, Quảng Tây); các nhóm Vietic ở Lào (Arem, Maleng) |
| Tày–Thái (`tay-thai`) | Kra–Dai | Tày, Thái, Nùng, Sán Chay, Giáy, Lào, Lự, Bố Y | Choang 壮族, Bố Y 布依族, Thái 傣族 (CN); Lào; Thái Lan; Shan (MM) |
| Mông–Dao (`hmong-dao`) | Hmông–Miền | Mông, Dao, Pà Thẻn | Miêu 苗族, Dao 瑶族 (CN); Hmong/Iu Mien ở Lào, Thái, Mỹ, Pháp |
| Ka Đai (`kadai`) | Kra–Dai | La Chí, La Ha, Cờ Lao, Pu Péo | Ngật Lão 仡佬族 (CN), Lê 黎族 (Hải Nam) |
| Môn–Khmer (`mon-khmer`) | Nam Á | 21 dân tộc: Khmer, Ba Na, Xơ Đăng, Hrê, Cơ Ho, Mnông, Xtiêng, Bru-Vân Kiều, Cơ Tu, Giẻ Triêng, Tà Ôi, Mạ, Co, Chơ Ro, Xinh Mun, Kháng, Mảng, Khơ Mú, Rơ Măm, Brâu, Ơ Đu | Khmer (KH), Môn (MM/TH), Khmu/Katu/Bru (LA), Ngõa 佤族, Bố Lãng 布朗族 (CN) |
| Nam Đảo (`nam-dao`) | Nam Đảo | Gia Rai, Ê Đê, Chăm, Raglai, Chu Ru | Chăm (KH), Mã Lai (MY), Indonesia, Philippines, thổ dân Đài Loan, 回辉人 (Hải Nam) |
| Hán (`han`) | Hán–Tạng | Hoa, Ngái, Sán Dìu | Người Hán Quảng Đông/Phúc Kiến/Hakka; Hoa kiều Đông Nam Á |
| Tạng–Miến (`tang-mien`) | Hán–Tạng | Hà Nhì, Phù Lá, La Hủ, Lô Lô, Cống, Si La | Hà Nhì 哈尼族/Akha, La Hủ 拉祜族/Lahu, Di 彝族 (CN, TH, LA, MM) |

Tổng: 4 + 8 + 3 + 4 + 21 + 5 + 3 + 6 = **54**. Dân số theo **Tổng điều tra dân số 2019** (Kinh ≈ 85,3%).

## Myanmar và các nước khác (bổ sung 11/10/2026, theo infobox Wikipedia tiếng Anh)

- **Myanmar (8 dân tộc):** Hà Nhì ↔ Akha (~200.000), La Hủ ↔ Lahu (~150.000), Lự ↔ Tai Lue (~60.000), Thái ↔ Shan (gần gũi), Hoa ↔ Hoa kiều Myanmar (~1,64 triệu), Mông (~3.000), Dao (Iu Mien), Khơ Mú. Mức ngữ hệ: Môn, Palaung, Wa (Nam Á).
- **Xa hơn:** Munda (Ấn Độ, Bangladesh), Senoi (Malaysia) ↔ Môn–Khmer; Đài Loan → Philippines → Indonesia → Madagascar ↔ Nam Đảo.
- **Di cư:** Mỹ, Pháp, Canada, Úc (Mông, Iu Mien, Lào, Khơ Mú, Khmer Krom, Chăm).
- Đếm theo `data/*.json`: CN 26 · LA 24 · TH 12 · US 11 · KH 10 · MM 8 · MY 7 · FR 6.

## Gợi ý dẫn tham quan VME (~3 giờ)

- **Toà Trống Đồng** (trong nhà): đi theo nhóm ngôn ngữ — Việt–Mường → Tày–Thái/Ka Đai → Mông–Dao → Tạng–Miến, Hán → Trường Sơn–Tây Nguyên (Môn–Khmer + Nam Đảo) → Chăm, Khmer Nam Bộ.
- **Vườn kiến trúc** (ngoài trời): nhà dài Ê Đê, nhà rông Ba Na, nhà mồ Gia Rai, nhà Chăm, nhà Việt, nhà sàn Tày, nhà Mông, nhà Dao, nhà trình tường Hà Nhì, nhà Cơ Tu… (xem `vme_vi` trong JSON).
- **Toà Cánh Diều**: trưng bày Đông Nam Á — chỗ tốt nhất để đối chiếu “họ hàng” xuyên biên giới.
- Câu hỏi gợi mở cho đoàn có ở cuối mỗi mục dân tộc trong `references/`.

## Schema `data/<nhóm>.json`

```json
{
  "id": "e-de", "vi": "Ê Đê", "ja": "エデ族", "alt": "Ra-đê",
  "group": "nam-dao", "pop": 398671,
  "region_vi": "…", "region_ja": "…",
  "hi_vi": "đặc trưng nổi bật", "hi_ja": "特徴",
  "kin": [{"c": "KH", "vi": "…", "ja": "…"}],
  "vme_vi": "xem gì ở bảo tàng", "vme_ja": "博物館での見どころ"
}
```

`kin[].c` là mã nước ISO 3166-1 alpha-2 (CN, LA, TH, MM, KH, MY, ID, PH, TW, US, FR…).

## Dân số & tuổi (so sánh Việt Nam – Trung Quốc – Nhật Bản)

`data/demography.json`: dân số và tuổi trung vị 1950–2100 (UN WPP 2024; ước tính đến 2023, dự báo phương án trung bình từ 2024), số Tổng điều tra 2009/2019 của Tổng cục Thống kê, năm đạt đỉnh dân số (VN ~2049, CN 2021, JP 2009). Số chính thức gần nhất: dân số trung bình 2025 là 102,3 triệu (Cục Thống kê). Khi trích dẫn, ghi rõ số là của LHQ hay của Cục Thống kê.

## Cập nhật trang hướng dẫn

Trang `aq-dantochoc/index.html` nhúng dữ liệu từ `data/*.json`. Sau khi sửa JSON, chạy:

```bash
python3 aq-dantochoc/build.py
```

## Lưu ý độ chính xác

- Danh mục 54 dân tộc là danh mục chính thức của Nhà nước (1979); một số nhóm tự nhận khác danh mục — tôn trọng tên tự gọi.
- Trưng bày VME có thể thay đổi; nếu không chắc vị trí hiện vật, nói “tìm trong khu trưng bày nhóm …” thay vì khẳng định.
