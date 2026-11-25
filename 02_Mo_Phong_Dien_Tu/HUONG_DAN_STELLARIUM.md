# 🌌 Hướng Dẫn Sử Dụng Stellarium — Mô Phỏng Bầu Trời Sao Tại Trường THPT Kinh Môn

Bộ tài liệu này gồm 2 file đã cấu hình sẵn cho phần mềm **Stellarium** (phần mềm giáo viên giới thiệu):
- `stellarium/thpt_kinh_mon_sky_demo.ssc` — Kịch bản tự động mô phỏng bầu trời sao tại Trường THPT Kinh Môn.
- `stellarium/user_locations.txt` — File cấu hình vị trí cố định **Trường THPT Kinh Môn (20.99° N, 106.55° E)**.

---

## 1. Tải và cài đặt Stellarium (nếu máy chưa có)
- Tải miễn phí bản Windows tại trang chủ: https://stellarium.org/
- Cài đặt bình thường, sau đó mở Stellarium và đổi ngôn ngữ sang **Tiếng Việt** bằng cách nhấn `F2` → tab **Chính (Main)** → chọn **Tiếng Việt** ở mục *Ngôn ngữ chương trình* và *Ngôn ngữ bầu trời*.

---

## 2. Đưa vị trí THPT Kinh Môn & Kịch bản tự chạy vào Stellarium

### Bước A: Cài vị trí Trường THPT Kinh Môn
1. Nhấn tổ hợp phím `Win + R`, gõ `%APPDATA%\Stellarium\data` rồi nhấn **Enter**.
2. Chép file `user_locations.txt` vào thư mục này.
3. Mở Stellarium → nhấn **`F6`** (Cửa sổ Vị trí) → tìm **`Truong THPT Kinh Mon`** → tích chọn **"Sử dụng vị trí hiện tại làm mặc định"**.

> **Mẹo (nếu trình chiếu trên máy tính ở lớp mà chưa copy file):**  
> Nhấn `F6` → nhập thủ công:
> - **Vĩ độ (Latitude):** `N 20° 59' 24"` (hoặc `20.99° N`)
> - **Kinh độ (Longitude):** `E 106° 33' 00"` (hoặc `106.55° E`)
> - **Độ cao (Elevation):** `10 m`
> - **Tên:** `Truong THPT Kinh Mon` → nhấn **Thêm vào danh sách**.

### Bước B: Cài và chạy kịch bản tự động (`.ssc`)
1. Nhấn `Win + R`, gõ `%APPDATA%\Stellarium\scripts` rồi nhấn **Enter** (nếu chưa có thư mục `scripts`, bạn tự tạo mới thư mục tên `scripts` trong `%APPDATA%\Stellarium\`).
2. Chép file `thpt_kinh_mon_sky_demo.ssc` vào thư mục `scripts`.
3. Mở Stellarium → nhấn **`F2`** (Cửa sổ Cấu hình) → chọn tab **Kịch bản (Scripts)**.
4. Chọn **`Mo phong Bau troi sao - Truong THPT Kinh Mon`** rồi nhấn nút **Chạy (▶)**.
5. Hoặc nhấn **`F12`** để mở cửa sổ Script Console, mở trực tiếp file `thpt_kinh_mon_sky_demo.ssc` và nhấn **Run** (cách này cực nhanh, không cần copy vào `%APPDATA%`!).

*(Lưu ý: Bạn có thể mở file `thpt_kinh_mon_sky_demo.ssc` bằng Notepad để đổi dòng `2026-11-24T13:00:00` thành đúng ngày bạn thuyết trình; nhớ `13:00 UTC = 20:00 giờ Việt Nam`.)*

---

## 3. Bộ phím tắt "vàng" khi thao tác trực tiếp trên lớp

| Phím tắt | Tác dụng |
| :---: | :--- |
| **`F6`** | Mở bảng chọn vị trí (chọn *Truong THPT Kinh Mon*) |
| **`F5`** | Mở bảng chọn ngày và giờ quan sát |
| **`C`** | Bật / tắt **đường nối chòm sao** |
| **`V`** | Bật / tắt **tên chòm sao** |
| **`R`** | Bật / tắt **hình vẽ minh họa chòm sao** (rất đẹp khi chiếu) |
| **`Q`** | Bật / tắt chữ chỉ phương hướng (**Bắc, Nam, Đông, Tây**) |
| **`E`** | Bật / tắt **lưới tọa độ xích đạo** (nhìn rõ tâm quay tại Sao Bắc Cực) |
| **`L`** | Tua nhanh thời gian (nhấn nhiều lần để quay nhanh hơn) |
| **`K`** | Quay về tốc độ thời gian thực |
| **`J`** | Tua ngược thời gian |
| **`Ctrl + S`** | Chụp ảnh bầu trời hiện tại để chèn vào slide / báo cáo Word |

---

## 4. Gợi ý kịch bản thuyết trình 4 phút (Kết hợp cả 2 định dạng)
1. **Mở đầu (30 giây):** Giới thiệu vị trí quan sát là **Trường THPT Kinh Môn** có tọa độ `20.99° N, 106.55° E` (nằm ở Bắc bán cầu, gần chí tuyến Bắc).
2. **Trình diễn Định dạng 1 — Bản đồ sao quay điện tử (`ban_do_sao_quay_thpt_kinh_mon.html` — 1,5 phút):**
   - Kéo chuột xoay đĩa sao trực tiếp để minh họa cách bản đồ sao quay hoạt động (vòng ngày khớp với vòng giờ, cửa sổ bầu dục cắt đúng chân trời vĩ độ 21°N).
   - Bật chế độ **Chỉ dẫn tìm Sao Bắc Cực** (nối 2 sao *Merak → Dubhe* của Gấu Lớn kéo dài 5 lần gặp *Polaris*) và giải thích cách xác định 4 hướng Bắc - Nam - Đông - Tây.
   - Bấm thử 4 nút **Xuân / Hạ / Thu / Đông** để chỉ ra sự thay đổi của các chòm sao theo mùa (ví dụ mùa đông có Lạp Hộ, mùa hè có Bọ Cạp và Tam giác mùa hè).
3. **Trình diễn Định dạng 2 — Mô phỏng bầu trời 3D bằng Stellarium (2 phút):**
   - Nhấn `F12` chạy file `thpt_kinh_mon_sky_demo.ssc`.
   - Khi kịch bản chạy qua **Phần 1 & 2**, chỉ cho lớp thấy Sao Bắc Cực cao khoảng `21°` ở hướng chính Bắc (bằng đúng vĩ độ của Kinh Môn!) và hầu như đứng yên trong khi các chòm sao khác quay ngược chiều kim đồng hồ quanh nó.
   - Khi sang **Phần 3 & 4**, giới thiệu đường Hoàng đạo đi qua 12 chòm sao Hoàng Đạo và chế độ toàn bầu trời 360°.
