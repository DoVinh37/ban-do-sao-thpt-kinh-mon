# 🎬 Kịch Bản Quay Video Hướng Dẫn Dùng Stellarium Từ A–Z (2,5 – 3 Phút)

> **Mục tiêu:** Trình bày rõ ràng cách tải, cài vị trí **Trường THPT Kinh Môn (Phường Kinh Môn, Hải Phòng — 20.99° N, 106.55° E)**, thiết lập mốc **20h00**, bật các lớp quan sát cơ bản và chạy kịch bản tự động `.ssc` — quay một lượt bằng Windows Game Bar (`Win + Alt + R`) hoặc OBS là nộp được ngay.

---

## Bước 0 — Chuẩn bị trước khi bấm quay (30 giây)
1. Mở sẵn 2 tab trình duyệt: **Tab 1:** `https://stellarium-web.org/` (bản Web xem nhanh không cần cài) và **Tab 2:** `https://stellarium.org/` (trang tải bản máy tính).
2. Mở sẵn phần mềm **Stellarium 26.3** trên máy tính (chạy trên card NVIDIA GTX 1650 cho mượt 60 FPS).
3. Để sẵn thư mục `02_Mo_Phong_Dien_Tu\stellarium` gồm file `thpt_kinh_mon_sky_demo.ssc` và `user_locations.txt`.

---

## Kịch bản 6 phân đoạn (Tổng ~3 phút 15 giây)

### Cảnh 1: Dùng nhanh Stellarium bản Web không cần cài đặt (45 giây)
- **Thao tác màn hình:**
  1. Mở tab `https://stellarium-web.org/`.
  2. Bấm nút **Vị trí (góc dưới bên trái)** $\rightarrow$ tìm **Kinh Môn** (hoặc nhập `20.99, 106.55`) $\rightarrow$ bấm **Use this location**.
  3. Bấm nút **Ngày/Giờ (góc dưới bên phải)** $\rightarrow$ chỉnh về **`20:00`** (kéo nhẹ thanh giờ cho thấy sao xoay).
  4. Bấm các nút ở thanh dưới cùng: *Constellations* (đường nối), *Constellations Art* (hình vẽ), *Equatorial Grid* (lưới xích đạo), *Night Mode* (chế độ đêm đỏ) $\rightarrow$ xoay hướng **N (Bắc)** bấm vào **Polaris** chỉ độ cao `~21°`.
- **Lời đọc gợi ý:** *"Chào cô và các bạn, đây là video hướng dẫn sử dụng Stellarium từ A đến Z cho Trường THPT Kinh Môn. Cách nhanh nhất không cần cài đặt là mở trang `stellarium-web.org` trên máy tính hoặc điện thoại: chọn vị trí Kinh Môn góc dưới trái, chỉnh mốc mặc định 20 giờ ở góc dưới phải, bật đường nối, hình vẽ chòm sao và lưới xích đạo ở thanh dưới. Xoay về hướng Bắc bấm vào Sao Bắc Cực ta thấy độ cao đúng xấp xỉ 21 độ. Tuy nhiên bản Web không chạy được kịch bản tự động `.ssc` nên để đầy đủ tính năng nhất, nhóm em hướng dẫn cài bản máy tính ngay sau đây."*

### Cảnh 2: Tải phần mềm Stellarium bản máy tính chính thức (15 giây)
- **Thao tác màn hình:** Hiện trang chủ `https://stellarium.org/`, rê chuột vào nút tải bản Windows 64-bit.
- **Lời đọc gợi ý:** *"Chào cô và các bạn, đây là video hướng dẫn sử dụng phần mềm Stellarium để mô phỏng bầu trời sao tại Trường THPT Kinh Môn từ A đến Z. Đầu tiên, mọi người truy cập trang chủ `stellarium.org` để tải bản cài đặt miễn phí cho Windows."*

### Cảnh 3: Đổi sang Tiếng Việt & Cài tọa độ Trường THPT Kinh Môn (40 giây)
- **Thao tác màn hình:**
  1. Mở Stellarium $\rightarrow$ nhấn **`F2`** $\rightarrow$ tab **Chính (Main)** $\rightarrow$ chỉ vào mục chọn **Tiếng Việt**.
  2. Nhấn **`F6`** (Cửa sổ Vị trí) $\rightarrow$ gõ/chọn **`Truong THPT Kinh Mon`** (hoặc chỉ rõ tọa độ `20°59'24" N`, `106°33'00" E`, độ cao `10 m`, múi giờ `Asia/Ho_Chi_Minh`) $\rightarrow$ tích **"Sử dụng vị trí hiện tại làm mặc định"**.
- **Lời đọc gợi ý:** *"Sau khi mở Stellarium, nhấn `F2` để đổi ngôn ngữ sang Tiếng Việt. Tiếp theo nhấn `F6` để thiết lập vị trí quan sát là Trường THPT Kinh Môn, phường Kinh Môn, Hải Phòng với tọa độ 20,99 độ vĩ Bắc, 106,55 độ kinh Đông, múi giờ UTC+7 và tích chọn làm vị trí mặc định."*

### Cảnh 4: Đặt giờ quan sát 20h00 & Thao tác các phím tắt cơ bản (45 giây)
- **Thao tác màn hình:**
  1. Nhấn **`F5`** $\rightarrow$ chỉnh giờ về **`20:00:00`** (có thể nhấp đổi thử tháng khác để chứng minh xoay được cả năm!).
  2. Lần lượt bấm các phím tắt để màn hình bật từng lớp:
     - **`Q`** (hiện 4 hướng Đông – Tây – Nam – Bắc)
     - **`C`** (đường nối chòm sao) $\rightarrow$ **`V`** (tên chòm sao) $\rightarrow$ **`R`** (hình vẽ minh họa chòm sao)
     - **`E`** (lưới tọa độ xích đạo quanh Sao Bắc Cực)
  3. Dùng chuột kéo xoay về hướng **Bắc**, bấm chọn vào **Sao Bắc Cực (Polaris)** cho hiện bảng thông số độ cao góc **Alt ≈ 21°**.
  4. Nhấn **`L`** 2–3 lần để tua nhanh thấy các chòm sao quay ngược chiều kim đồng hồ quanh Sao Bắc Cực, rồi nhấn **`K`** về bình thường.
  5. Bật thử nút **Chế độ ban đêm (Night Mode - màu đỏ)** ở thanh công cụ dưới cùng.
- **Lời đọc gợi ý:** *"Nhấn `F5` để chỉnh thời gian về mốc mặc định 20 giờ tối — mọi người có thể đổi sang bất kỳ ngày nào trong năm. Tiếp theo dùng bộ phím tắt nhanh: `C` bật đường nối, `V` bật tên, `R` bật hình vẽ chòm sao và `E` bật lưới xích đạo. Khi quay về hướng Bắc và bấm vào Sao Bắc Cực, ta thấy độ cao góc đúng bằng khoảng 21 độ — trùng với vĩ độ trường mình. Nhấn `L` để tua nhanh sẽ thấy bầu trời quay ngược chiều kim đồng hồ quanh Sao Bắc Cực. Khi mang máy ra sân trường buổi tối, nhớ bật Chế độ ban đêm màu đỏ để không bị chói mắt."*

### Cảnh 5: Chạy kịch bản tự động `.ssc` của nhóm bằng `F12` (45 giây)
- **Thao tác màn hình:**
  1. Nhấn **`F12`** mở **Script Console**.
  2. Bấm nút **Mở file (Open)** $\rightarrow$ chọn `thpt_kinh_mon_sky_demo.ssc` $\rightarrow$ bấm **Chạy (Run ▶)** rồi đóng cửa sổ `F12` cho đẹp khung hình.
  3. Cho kịch bản tự chạy qua đoạn định vị Sao Bắc Cực / chuyển động nhật động / Đường Hoàng đạo / Toàn cảnh 360° (chỉ cần quay minh họa 20–30 giây mượt mà).
- **Lời đọc gợi ý:** *"Để tiết kiệm thời gian khi thuyết trình trên lớp, nhóm em đã viết sẵn kịch bản tự động `thpt_kinh_mon_sky_demo.ssc`. Mọi người chỉ cần nhấn `F12`, chọn file kịch bản của nhóm rồi bấm Chạy — phần mềm sẽ tự động đưa về tọa độ THPT Kinh Môn lúc 20 giờ tối và trình diễn lần lượt từ tìm Sao Bắc Cực, chuyển động nhật động, đường Hoàng đạo đến bản đồ sao 360 độ."*

### Cảnh 6: Kết thúc (15 giây)
- **Thao tác màn hình:** Hiện nhanh trang cổng `index.html` hoặc thư mục Google Drive của nhóm chứa đủ file tải.
- **Lời đọc gợi ý:** *"Toàn bộ tệp cấu hình, kịch bản `.ssc`, bản đồ sao Web HTML và bản đồ giấy PDF nhóm em đã để sẵn trong thư mục dự án. Cảm ơn cô và các bạn đã theo dõi!"*
