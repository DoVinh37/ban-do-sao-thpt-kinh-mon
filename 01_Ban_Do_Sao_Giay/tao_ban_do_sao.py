import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import Circle, Wedge, Polygon
import matplotlib.patheffects as pe

# Cấu hình font Unicode hỗ trợ đầy đủ tiếng Việt
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Arial", "Liberation Sans"]
plt.rcParams["pdf.fonttype"] = 42

# ==============================================================================
# 1. THÔNG SỐ KỸ THUẬT & TỶ LỆ 1:1 KHỔ A4 (ĐƠN VỊ: mm)
# ==============================================================================
A4_W, A4_H = 210.0, 297.0
CX, CY = 105.0, 145.0          # Tâm bản đồ trên trang A4

LAT_DEG = 21.0                 # Vĩ độ phường Kinh Môn, Hải Phòng (21° Bắc)
LON_OFFSET_DEG = 1.55          # Hiệu chỉnh kinh độ: 106.55°Đ - 105.00°Đ (UTC+7)

R_DISC1_OUT = 95.0             # Bán kính đĩa sao Trang 1 (ĐK 190 mm)
R_DISC1_SKY = 82.0             # Bán kính vùng trời xanh đêm trên đĩa sao
R_DISC2_OUT = 82.0             # Bán kính mặt che Trang 2 (ĐK 164 mm)
R_HOUR_IN = 72.0               # Bán kính trong vành chia giờ
R_MAX_HORIZON = 67.5           # Bán kính cực đại của cửa sổ chân trời phía Nam

# Hệ số tỷ lệ phép chiếu phương vị cách đều: r(dec) = K_SCALE * (90 - dec)
DEC_MIN = LAT_DEG - 90.0       # -69.0°
K_SCALE = R_MAX_HORIZON / (90.0 - DEC_MIN)  # ~0.42453 mm/độ

# Bảng màu
C_SKY_BG = "#102158"           # Xanh đêm đậm (Trang 1)
C_COVER_BG = "#1746a2"         # Xanh dương đậm (Trang 2)
C_GOLD = "#FFD54F"             # Vàng chữ & viền nét đứt
C_LIGHT_BLUE = "#B3E5FC"       # Xanh nhạt phụ đề
C_RED = "#E53935"              # Đỏ tâm Sao Bắc Cực & chữ thập
C_STAR_LINE = "#5C85D6"        # Xanh nối chòm sao
C_LABEL_STAR = "#E3F2FD"       # Trắng xanh tên chòm sao


def radec_to_xy(ra_hours, dec_deg):
    """Chuyển đổi (Xích kinh giờ, Xích vĩ độ) sang tọa độ (x, y) mm trên Trang 1.
    Quy ước: RA = 0h nằm ở đỉnh 12h (90°), tăng CÙNG chiều kim đồng hồ.
    """
    r = K_SCALE * (90.0 - np.asarray(dec_deg))
    theta = np.deg2rad(90.0 - 15.0 * np.asarray(ra_hours))
    x = CX + r * np.cos(theta)
    y = CY + r * np.sin(theta)
    return x, y


def draw_calibration_ruler(ax):
    """Vẽ thanh thước kiểm chuẩn 5,0 cm (50,0 mm) ở đáy mỗi trang A4."""
    x0, x1 = CX - 25.0, CX + 25.0
    y_bar = 24.0
    ax.plot([x0, x1], [y_bar, y_bar], color="#111111", lw=1.2, zorder=50)
    for i in range(6):
        xt = x0 + i * 10.0
        tick_h = 2.6 if i in (0, 5) else 1.6
        ax.plot([xt, xt], [y_bar - tick_h, y_bar + tick_h], color="#111111", lw=1.0, zorder=50)
    ax.text(
        CX, y_bar - 6.2, "5,0 cm (Tỷ lệ in 100% A4)",
        ha="center", va="top", fontsize=7.5, fontweight="bold", color="#111111", zorder=50
    )


def create_a4_figure():
    fig = plt.figure(figsize=(A4_W / 25.4, A4_H / 25.4), dpi=300)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, A4_W)
    ax.set_ylim(0, A4_H)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


# ==============================================================================
# 2. DỮ LIỆU 33 CHÒM SAO SÁNG (TỌA ĐỘ J2000 & ĐƯỜNG NỐI CHÒM SAO)
# Cấu trúc: "Tên tiếng Việt": ([(ra, dec, mag), ...], [(idx1, idx2), ...], (ra_nhãn, dec_nhãn))
# ==============================================================================
CONSTELLATIONS = {
    "Gấu Nhỏ": (
        [(2.53, 89.26, 2.0), (16.77, 82.04, 4.2), (15.73, 77.79, 4.3), (14.85, 74.16, 2.1),
         (15.35, 71.83, 3.0), (16.29, 75.76, 4.9), (17.54, 86.59, 4.4)],
        [(0, 6), (6, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 2)],
        (15.3, 80.5)
    ),
    "Gấu Lớn": (
        [(11.06, 61.75, 1.8), (11.03, 56.38, 2.4), (11.90, 53.69, 2.4), (12.26, 57.03, 3.3),
         (12.90, 55.96, 1.8), (13.40, 54.93, 2.2), (13.79, 49.31, 1.9)],
        [(0, 1), (1, 2), (2, 3), (3, 0), (3, 4), (4, 5), (5, 6)],
        (12.3, 48.0)
    ),
    "Thiên Hậu": (
        [(0.15, 59.15, 2.3), (0.68, 56.54, 2.2), (0.95, 60.72, 2.5), (1.43, 60.24, 2.7), (1.91, 63.67, 3.4)],
        [(0, 1), (1, 2), (2, 3), (3, 4)],
        (1.0, 66.5)
    ),
    "Tiên Vương": (
        [(21.31, 62.59, 2.4), (21.48, 70.56, 3.2), (23.66, 77.63, 3.2), (22.83, 66.20, 3.5), (22.18, 58.20, 3.4)],
        [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (1, 3)],
        (22.4, 73.5)
    ),
    "Thiên Long": (
        [(17.94, 51.49, 2.2), (17.51, 52.30, 2.8), (17.15, 65.71, 3.2), (16.40, 61.51, 2.7),
         (15.42, 58.97, 3.3), (14.07, 64.38, 3.6), (12.56, 69.79, 3.9), (11.52, 69.33, 3.8)],
        [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)],
        (17.6, 58.5)
    ),
    "Thiên Nga": (
        [(20.69, 45.28, 1.3), (20.37, 40.26, 2.2), (19.51, 27.96, 3.1), (19.75, 45.13, 2.9), (20.77, 33.97, 2.5)],
        [(0, 1), (1, 2), (3, 1), (1, 4)],
        (20.9, 40.0)
    ),
    "Thiên Cầm - Chức Nữ": (
        [(18.62, 38.78, 0.0), (18.74, 37.60, 4.3), (18.83, 36.90, 4.3), (18.98, 32.69, 3.2), (18.83, 33.36, 3.5)],
        [(0, 1), (0, 2), (1, 2), (2, 3), (3, 4), (4, 1)],
        (18.7, 27.5)
    ),
    "Thiên Ưng - Ngưu Lang": (
        [(19.85, 8.87, 0.8), (19.77, 10.61, 2.7), (19.92, 6.41, 3.7), (19.09, 13.86, 3.0), (19.42, 3.11, 3.4)],
        [(1, 0), (0, 2), (1, 3), (2, 4)],
        (19.9, -1.5)
    ),
    "Lạp Hộ": (
        [(5.92, 7.41, 0.4), (5.42, 6.35, 1.6), (5.53, -0.30, 2.2), (5.60, -1.20, 1.7),
         (5.68, -1.94, 1.8), (5.24, -8.20, 0.1), (5.80, -9.67, 2.1)],
        [(0, 1), (0, 2), (1, 4), (2, 3), (3, 4), (4, 5), (2, 6), (5, 6)],
        (5.5, 11.8)
    ),
    "Đại Khuyển - Thiên Lang": (
        [(6.75, -16.72, -1.4), (6.38, -17.96, 2.0), (6.98, -28.97, 1.5), (7.14, -26.39, 1.8), (7.40, -29.30, 2.5)],
        [(1, 0), (0, 3), (3, 2), (3, 4)],
        (6.8, -33.5)
    ),
    "Tiểu Khuyển": (
        [(7.65, 5.22, 0.4), (7.45, 8.29, 2.9)],
        [(0, 1)],
        (7.7, 11.5)
    ),
    "Song Tử": (
        [(7.58, 31.89, 1.6), (7.76, 28.03, 1.1), (6.63, 16.40, 1.9), (6.38, 22.51, 2.9),
         (6.73, 25.13, 3.1), (7.07, 20.57, 3.8)],
        [(0, 1), (0, 4), (4, 3), (1, 5), (5, 2)],
        (7.1, 35.8)
    ),
    "Kim Ngưu": (
        [(4.60, 16.51, 0.9), (4.48, 15.63, 3.8), (4.33, 15.62, 3.7), (4.38, 17.54, 3.7),
         (4.48, 19.18, 3.5), (5.44, 28.61, 1.7), (5.63, 21.14, 3.0), (3.79, 24.11, 2.9)],
        [(0, 1), (1, 2), (2, 3), (3, 4), (0, 6), (4, 5)],
        (4.3, 10.5)
    ),
    "Ngự Phu": (
        [(5.28, 46.00, 0.1), (5.99, 44.95, 1.9), (5.99, 37.21, 2.6), (4.95, 33.17, 2.7), (5.03, 43.82, 3.0)],
        [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)],
        (5.5, 50.0)
    ),
    "Anh Tiên": (
        [(3.41, 49.86, 1.8), (3.14, 40.96, 2.1), (3.08, 53.51, 2.9), (3.96, 40.01, 2.9), (3.90, 31.88, 2.9)],
        [(2, 0), (0, 1), (0, 3), (3, 4)],
        (3.3, 36.0)
    ),
    "Bạch Dương": (
        [(2.12, 23.46, 2.0), (1.91, 20.81, 2.6), (1.89, 19.29, 3.9)],
        [(0, 1), (1, 2)],
        (2.1, 27.0)
    ),
    "Song Ngư": (
        [(23.29, 3.28, 3.7), (23.46, 6.38, 4.0), (23.72, 5.63, 4.1), (23.66, 1.78, 4.5),
         (2.03, 2.76, 3.8), (1.52, 15.35, 3.6)],
        [(0, 1), (1, 2), (2, 3), (3, 0), (2, 4), (4, 5)],
        (0.8, 9.0)
    ),
    "Kình Ngư": (
        [(3.04, 4.09, 2.5), (2.72, 3.24, 3.5), (1.86, -10.33, 3.7), (1.40, -8.18, 3.6),
         (0.73, -17.99, 2.0), (0.32, -8.82, 3.5)],
        [(0, 1), (1, 2), (2, 3), (3, 5), (5, 4), (4, 2)],
        (1.6, -15.5)
    ),
    "Phi Mã": (
        [(23.06, 15.21, 2.5), (23.08, 28.08, 2.4), (0.14, 29.09, 2.1), (0.22, 15.18, 2.8),
         (21.74, 9.88, 2.4), (22.72, 10.83, 3.4)],
        [(0, 1), (1, 2), (2, 3), (3, 0), (0, 5), (5, 4)],
        (23.5, 21.5)
    ),
    "Bảo Bình": (
        [(22.10, -0.32, 3.0), (21.53, -5.57, 2.9), (22.36, -1.39, 3.8), (22.48, -0.02, 4.0),
         (22.91, -7.58, 3.7), (22.91, -15.82, 3.3)],
        [(1, 0), (0, 2), (2, 3), (2, 4), (4, 5)],
        (22.1, -11.5)
    ),
    "Ma Kết": (
        [(20.29, -12.51, 3.6), (20.35, -14.78, 3.1), (21.67, -16.66, 3.7), (21.78, -16.13, 2.9), (20.77, -25.27, 3.7)],
        [(0, 1), (1, 4), (4, 2), (2, 3), (3, 0)],
        (20.9, -20.5)
    ),
    "Nhân Mã": (
        [(18.35, -34.38, 1.8), (18.47, -29.83, 2.8), (18.92, -26.30, 2.1), (19.04, -29.88, 2.6),
         (19.16, -21.02, 2.9), (18.10, -30.42, 3.0), (18.01, -24.43, 3.8)],
        [(0, 5), (5, 1), (1, 2), (2, 3), (3, 0), (1, 3), (2, 4), (5, 6), (6, 1)],
        (18.7, -38.5)
    ),
    "Bọ Cạp": (
        [(16.49, -26.43, 1.0), (16.01, -22.62, 2.6), (15.98, -26.11, 2.3), (16.00, -19.81, 2.6),
         (16.84, -34.29, 2.3), (17.20, -43.24, 3.3), (17.62, -42.99, 1.9), (17.56, -37.10, 1.6)],
        [(3, 1), (1, 2), (1, 0), (0, 4), (4, 5), (5, 6), (6, 7)],
        (16.4, -40.5)
    ),
    "Xà Phu": (
        [(17.58, 12.56, 2.1), (16.95, 9.38, 3.2), (17.72, 4.57, 2.8), (16.24, -3.69, 2.7),
         (16.62, -10.57, 2.6), (17.17, -15.72, 2.4)],
        [(0, 1), (0, 2), (1, 3), (3, 4), (4, 5), (5, 2)],
        (17.0, -3.0)
    ),
    "Vũ Tiên": (
        [(17.24, 14.39, 3.1), (16.69, 31.60, 2.8), (16.72, 38.92, 3.5), (17.25, 37.15, 3.2),
         (17.39, 24.84, 3.1), (16.50, 21.49, 2.8)],
        [(1, 2), (2, 3), (3, 4), (4, 1), (1, 5), (5, 0), (4, 0)],
        (16.9, 29.0)
    ),
    "Bắc Miện": (
        [(15.58, 26.71, 2.2), (15.46, 29.11, 3.7), (15.71, 26.30, 3.8), (15.83, 25.92, 4.1), (15.96, 26.88, 4.2)],
        [(1, 0), (0, 2), (2, 3), (3, 4)],
        (15.6, 32.8)
    ),
    "Mục Phu": (
        [(14.26, 19.18, -0.05), (14.53, 38.31, 3.0), (15.03, 40.39, 3.5), (15.26, 33.31, 3.5),
         (14.75, 27.07, 2.4), (13.91, 18.40, 2.7)],
        [(0, 5), (5, 1), (1, 2), (2, 3), (3, 4), (4, 0)],
        (14.5, 31.0)
    ),
    "Xử Nữ": (
        [(13.42, -11.16, 1.0), (12.69, -1.45, 2.7), (13.04, 10.96, 2.8), (12.33, -0.67, 3.9),
         (11.84, 1.76, 3.6), (13.58, -0.60, 3.4)],
        [(0, 1), (1, 2), (1, 3), (3, 4), (1, 5)],
        (13.2, -16.5)
    ),
    "Sư Tử": (
        [(10.14, 11.97, 1.4), (10.12, 16.76, 3.5), (10.33, 19.84, 2.0), (10.28, 23.42, 3.4),
         (9.76, 23.77, 3.0), (11.24, 20.52, 2.6), (11.24, 15.43, 3.3), (11.82, 14.57, 2.1)],
        [(0, 1), (1, 2), (2, 3), (3, 4), (2, 5), (5, 7), (7, 6), (6, 0)],
        (10.8, 10.5)
    ),
    "Trường Xà": (
        [(9.46, -8.66, 2.0), (8.78, 6.42, 3.4), (8.63, 5.70, 3.1), (8.89, 5.95, 3.9),
         (10.83, -16.19, 3.1), (11.55, -31.86, 3.5), (13.32, -23.17, 3.0), (14.11, -26.68, 3.3)],
        [(1, 2), (2, 3), (3, 0), (0, 4), (4, 5), (5, 6), (6, 7)],
        (10.2, -23.0)
    ),
    "Ô Nha": (
        [(12.26, -17.54, 2.6), (12.57, -23.40, 2.7), (12.49, -16.52, 2.9), (12.17, -24.73, 3.0)],
        [(0, 2), (2, 1), (1, 3), (3, 0)],
        (12.3, -28.5)
    ),
    "Bán Nhân Mã": (
        [(14.66, -60.84, -0.01), (14.06, -60.37, 0.6), (13.93, -47.29, 2.6), (13.66, -53.47, 2.3), (14.11, -36.37, 2.1)],
        [(0, 1), (1, 3), (3, 2), (2, 4)],
        (14.3, -51.0)
    ),
    "Nam Thập Tự": (
        [(12.44, -63.10, 0.8), (12.52, -57.11, 1.6), (12.80, -59.69, 1.3), (12.25, -58.75, 2.8)],
        [(0, 1), (2, 3)],
        (12.5, -67.0)
    ),
}


# ==============================================================================
# 3. VẼ TRANG 1: ĐĨA SAO TRÒN (ĐƯỜNG KÍNH 190 mm)
# ==============================================================================
def build_page_1(pdf):
    fig, ax = create_a4_figure()

    # Vòng ngoài đĩa sao 190 mm (nền trắng vành chia tháng) + đường cắt ngoài
    ax.add_patch(Circle((CX, CY), R_DISC1_OUT, facecolor="#FFFFFF", edgecolor="#111111", lw=1.2, zorder=1))
    # Vùng bầu trời đêm xanh đậm (R = 82 mm)
    ax.add_patch(Circle((CX, CY), R_DISC1_SKY, facecolor=C_SKY_BG, edgecolor="#0B163D", lw=0.8, zorder=2))

    # Các tia Xích kinh mờ (mỗi 2h) để cân đối thị giác
    for h in range(0, 24, 2):
        x_end, y_end = radec_to_xy(h, DEC_MIN)
        ax.plot([CX, x_end], [CY, y_end], color="#1B347A", lw=0.45, zorder=3)

    # Đường Xích đạo trời (Dec = 0°, nét đứt xanh nhạt)
    r_eq = K_SCALE * 90.0
    ax.add_patch(Circle(
        (CX, CY), r_eq, fill=False, edgecolor="#82B1FF",
        linestyle=(0, (4, 3)), lw=0.65, alpha=0.85, zorder=4
    ))

    # Đường Hoàng đạo (độ nghiêng 23.44°, nét đứt vàng)
    ra_ecl = np.linspace(0, 24, 360)
    dec_ecl = np.rad2deg(np.arctan(np.tan(np.deg2rad(23.44)) * np.sin(np.deg2rad(15.0 * ra_ecl))))
    xe, ye = radec_to_xy(ra_ecl, dec_ecl)
    ax.plot(xe, ye, color=C_GOLD, linestyle=(0, (3, 2.5)), lw=0.75, alpha=0.9, zorder=5)

    # Vẽ 33 chòm sao (đường nối + sao + nhãn tiếng Việt)
    halo = [pe.withStroke(linewidth=1.6, foreground=C_SKY_BG)]
    for name, (stars, lines, (ra_lbl, dec_lbl)) in CONSTELLATIONS.items():
        xs, ys, sizes = [], [], []
        for ra, dec, mag in stars:
            x, y = radec_to_xy(ra, dec)
            xs.append(x)
            ys.append(y)
            sizes.append(max(1.8, (4.8 - mag) * 3.1))

        for i1, i2 in lines:
            ax.plot([xs[i1], xs[i2]], [ys[i1], ys[i2]], color=C_STAR_LINE, lw=0.65, alpha=0.88, zorder=6)

        ax.scatter(xs, ys, s=sizes, color="#FFFFFF", edgecolors="none", zorder=7)

        xl, yl = radec_to_xy(ra_lbl, dec_lbl)
        ax.text(
            xl, yl, name, fontsize=5.1, fontweight="bold", color=C_LABEL_STAR,
            ha="center", va="center", path_effects=halo, zorder=8
        )

    # Tâm Sao Bắc Cực màu đỏ
    ax.add_patch(Circle((CX, CY), 1.35, facecolor=C_RED, edgecolor="#FFFFFF", lw=0.45, zorder=15))

    # Vành ngoài chia 12 tháng (cùng chiều kim đồng hồ, neo 21/03 tại 12h / 90°)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_names = [f"THÁNG {m}" for m in range(1, 13)]
    vernal_equinox_day_idx = 31 + 28 + 20  # 21/03 (index 79 từ 01/01)
    deg_per_day = 360.0 / 365.0

    day_counter = 0
    for m_idx, n_days in enumerate(days_in_month):
        # Góc đầu tháng & giữa tháng
        theta_start = 90.0 - (day_counter - vernal_equinox_day_idx) * deg_per_day
        theta_mid = 90.0 - (day_counter + n_days / 2.0 - vernal_equinox_day_idx) * deg_per_day

        # Vạch ngăn tháng (từ 82 mm ra 95 mm)
        rad_s = np.deg2rad(theta_start)
        ax.plot(
            [CX + R_DISC1_SKY * np.cos(rad_s), CX + R_DISC1_OUT * np.cos(rad_s)],
            [CY + R_DISC1_SKY * np.sin(rad_s), CY + R_DISC1_OUT * np.sin(rad_s)],
            color="#111111", lw=0.85, zorder=10
        )

        # Tên tháng in hoa nằm vòng theo mép trong vành trắng
        rad_m = np.deg2rad(theta_mid)
        r_m_txt = 84.8
        rot_m = theta_mid - 90.0
        if -90.0 > (rot_m % 360.0 - 360.0) and np.sin(rad_m) < -0.15:
            rot_m += 180.0
        ax.text(
            CX + r_m_txt * np.cos(rad_m), CY + r_m_txt * np.sin(rad_m),
            month_names[m_idx], fontsize=5.8, fontweight="bold", color="#102158",
            ha="center", va="center", rotation=rot_m, rotation_mode="anchor", zorder=11
        )

        # Vạch chia từng ngày & nhãn 5–10–15–20–25
        for d in range(1, n_days + 1):
            theta_d = 90.0 - (day_counter - vernal_equinox_day_idx) * deg_per_day
            rad_d = np.deg2rad(theta_d)
            if d in (5, 10, 15, 20, 25):
                r_in = 91.4
                ax.plot(
                    [CX + r_in * np.cos(rad_d), CX + R_DISC1_OUT * np.cos(rad_d)],
                    [CY + r_in * np.sin(rad_d), CY + R_DISC1_OUT * np.sin(rad_d)],
                    color="#111111", lw=0.6, zorder=10
                )
                r_num = 89.2
                rot_num = theta_d - 90.0
                if np.sin(rad_d) < -0.15:
                    rot_num += 180.0
                ax.text(
                    CX + r_num * np.cos(rad_d), CY + r_num * np.sin(rad_d),
                    str(d), fontsize=4.6, fontweight="bold", color="#222222",
                    ha="center", va="center", rotation=rot_num, rotation_mode="anchor", zorder=11
                )
            elif d != 1:
                r_in = 93.0
                ax.plot(
                    [CX + r_in * np.cos(rad_d), CX + R_DISC1_OUT * np.cos(rad_d)],
                    [CY + r_in * np.sin(rad_d), CY + R_DISC1_OUT * np.sin(rad_d)],
                    color="#444444", lw=0.35, zorder=10
                )
            day_counter += 1

    draw_calibration_ruler(ax)
    pdf.savefig(fig)
    plt.close(fig)


# ==============================================================================
# 4. VẼ TRANG 2: MẶT CHE TRÒN (ĐƯỜNG KÍNH 164 mm, CỬA SỔ BẦU DỤC 21° BẮC)
# ==============================================================================
def build_page_2(pdf):
    fig, ax = create_a4_figure()

    # Hình tròn mặt che 164 mm nền xanh dương đậm #1746a2
    ax.add_patch(Circle((CX, CY), R_DISC2_OUT, facecolor=C_COVER_BG, edgecolor="#0D2863", lw=1.2, zorder=1))
    # Vòng phân cách trong của vành chia giờ (R = 72 mm)
    ax.add_patch(Circle((CX, CY), R_HOUR_IN, fill=False, edgecolor="#6495ED", lw=0.65, zorder=2))

    # Vành chia 24 giờ (0h ở đỉnh, tăng NGƯỢC chiều kim đồng hồ: 1h..12h trái, 23h..13h phải)
    for step in range(96):  # Mỗi bước = 15 phút
        h_val = step * 0.25
        psi = np.deg2rad(90.0 + 15.0 * h_val + LON_OFFSET_DEG)
        if step % 4 == 0:
            hour_int = int(round(h_val)) % 24
            r_in = 78.2
            ax.plot(
                [CX + r_in * np.cos(psi), CX + R_DISC2_OUT * np.cos(psi)],
                [CY + r_in * np.sin(psi), CY + R_DISC2_OUT * np.sin(psi)],
                color="#FFFFFF", lw=0.85, zorder=4
            )
            r_lbl = 74.9
            rot_h = np.rad2deg(psi) - 90.0
            if np.sin(psi) < -0.15:
                rot_h += 180.0
            ax.text(
                CX + r_lbl * np.cos(psi), CY + r_lbl * np.sin(psi),
                f"{hour_int}h", fontsize=6.6, fontweight="bold", color="#FFFFFF",
                ha="center", va="center", rotation=rot_h, rotation_mode="anchor", zorder=5
            )
        elif step % 2 == 0:
            r_in = 79.6
            ax.plot(
                [CX + r_in * np.cos(psi), CX + R_DISC2_OUT * np.cos(psi)],
                [CY + r_in * np.sin(psi), CY + R_DISC2_OUT * np.sin(psi)],
                color="#DCE8FF", lw=0.5, zorder=4
            )
        else:
            r_in = 80.7
            ax.plot(
                [CX + r_in * np.cos(psi), CX + R_DISC2_OUT * np.cos(psi)],
                [CY + r_in * np.sin(psi), CY + R_DISC2_OUT * np.sin(psi)],
                color="#B3E5FC", lw=0.35, zorder=4
            )

    # Cửa sổ chân trời bầu dục trắng viền nét đứt vàng cho vĩ độ 21° Bắc
    ha_rad = np.linspace(0, 2 * np.pi, 720, endpoint=False)
    tan_lat = np.tan(np.deg2rad(LAT_DEG))
    dec_hor = np.rad2deg(np.arctan(-np.cos(ha_rad) / tan_lat))
    r_hor = K_SCALE * (90.0 - dec_hor)
    psi_hor = np.deg2rad(270.0) + ha_rad  # HA=0 -> Nam (270°), HA=-90° -> Đông (180°), HA=+90° -> Tây (0°)

    xh = CX + r_hor * np.cos(psi_hor)
    yh = CY + r_hor * np.sin(psi_hor)
    horizon_verts = np.column_stack([xh, yh])

    ax.add_patch(Polygon(
        horizon_verts, closed=True, facecolor="#FFFFFF", edgecolor=C_GOLD,
        linestyle=(0, (4, 2.5)), lw=1.35, zorder=6
    ))

    # 4 hướng chữ vàng BẮC (trên), ĐÔNG (trái), TÂY (phải), NAM (dưới)
    r_north = K_SCALE * LAT_DEG
    r_ew = K_SCALE * 90.0
    r_south = R_MAX_HORIZON

    ax.text(CX, CY + r_north + 4.2, "BẮC", fontsize=8.0, fontweight="bold", color=C_GOLD, ha="center", va="center", zorder=8)
    ax.text(CX - r_ew - 6.8, CY, "ĐÔNG", fontsize=8.0, fontweight="bold", color=C_GOLD, ha="center", va="center", zorder=8)
    ax.text(CX + r_ew + 6.5, CY, "TÂY", fontsize=8.0, fontweight="bold", color=C_GOLD, ha="center", va="center", zorder=8)
    ax.text(CX, CY - r_south - 2.3, "NAM", fontsize=6.6, fontweight="bold", color=C_GOLD, ha="center", va="center", zorder=8)

    # Cụm tiêu đề phía trên hướng Bắc
    ax.text(CX, CY + 51.5, "BẢN ĐỒ SAO QUAY", fontsize=13.0, fontweight="bold", color=C_GOLD, ha="center", va="center", zorder=8)
    ax.text(CX, CY + 43.0, "TRƯỜNG THPT KINH MÔN", fontsize=9.8, fontweight="bold", color="#FFFFFF", ha="center", va="center", zorder=8)
    ax.text(
        CX, CY + 36.2, "VĨ ĐỘ 21° BẮC • PHƯỜNG KINH MÔN, HẢI PHÒNG",
        fontsize=6.4, fontweight="bold", color=C_LIGHT_BLUE, ha="center", va="center", zorder=8
    )

    # Dấu chữ thập đỏ ở tâm chốt xoay
    cross_half = 2.4
    ax.plot([CX - cross_half, CX + cross_half], [CY, CY], color=C_RED, lw=1.15, zorder=15)
    ax.plot([CX, CX], [CY - cross_half, CY + cross_half], color=C_RED, lw=1.15, zorder=15)
    ax.add_patch(Circle((CX, CY), 0.75, fill=False, edgecolor=C_RED, lw=0.65, zorder=15))

    draw_calibration_ruler(ax)
    pdf.savefig(fig)
    plt.close(fig)


if __name__ == "__main__":
    output_pdf = "BanDoSaoQuay_THPT_KinhMon_A4.pdf"
    with PdfPages(output_pdf) as pdf:
        build_page_1(pdf)
        build_page_2(pdf)
    print(f"Đã xuất thành công file PDF 2 trang A4 tỷ lệ 1:1: {output_pdf}")