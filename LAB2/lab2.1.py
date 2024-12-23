import numpy as np

# Tạo dữ liệu nhiệt độ
np.random.seed(0)  # Để đảm bảo tính ngẫu nhiên có thể tái lập
nhiet_do = np.round(np.random.uniform(15, 35, 30), 2)  # 30 ngày, nhiệt độ trong khoảng 15-35 độ C

# Tính nhiệt độ trung bình
nhiet_do_tb = np.mean(nhiet_do)

print("Dữ liệu nhiệt độ:", nhiet_do)
print("Nhiệt độ trung bình trong tháng là:", round(nhiet_do_tb, 2))


# Xác định ngày có nhiệt độ cao nhất và thấp nhất
nhiet_do_max = np.max(nhiet_do)
nhiet_do_min = np.min(nhiet_do)
max_day = np.argmax(nhiet_do) + 1  # Thêm 1 để lấy ngày (bắt đầu từ 1)
min_day = np.argmin(nhiet_do) + 1

# Thống kê sự chênh lệch nhiệt độ giữa các ngày
do_chenh_lech_nhiet_do = np.abs(np.diff(nhiet_do))
do_chenh_lech_max = np.max(do_chenh_lech_nhiet_do)
ngay_chenh_lech_max = np.argmax(do_chenh_lech_nhiet_do) + 1  # Ngày đầu tiên của sự chênh lệch

print(f"Nhiệt độ cao nhất: {nhiet_do_max}°C, vào ngày thứ {max_day}")
print(f"Nhiệt độ thấp nhất: {nhiet_do_min}°C, vào ngày thứ {min_day}")
print(f"Sự chênh lệch nhiệt độ lớn nhất là {round(do_chenh_lech_max, 2)}°C, giữa ngày thứ {ngay_chenh_lech_max} và ngày thứ {ngay_chenh_lech_max + 1}")

# Các ngày có nhiệt độ cao hơn 20 độ C
ngay_qua_20_do = np.where(nhiet_do > 20)[0] + 1  # Thêm 1 để lấy ngày
nhiet_do_qua_20 = nhiet_do[nhiet_do > 20]

# Nhiệt độ của ngày 5, 10, 15, 20, và 25
ngay = [5, 10, 15, 20, 25]
selected_temps = nhiet_do[np.array(ngay) - 1]  # Trừ 1 để chuyển sang chỉ mục

# Nhiệt độ của các ngày trên trung bình
nhiet_do_ngay_tren_tb = nhiet_do[nhiet_do > nhiet_do_tb]
ngay_co_nhiet_do_tren_tb = np.where(nhiet_do > nhiet_do_tb)[0] + 1

# Nhiệt độ của các ngày chẵn/lẻ
nhiet_do_ngay_chan = nhiet_do[1::2]  # Ngày chẵn (index lẻ)
nhiet_do_ngay_le = nhiet_do[0::2]  # Ngày lẻ (index chẵn)

print("Các ngày có nhiệt độ cao hơn 20°C:", ngay_qua_20_do)
print("Nhiệt độ các ngày cao hơn 20°C:", nhiet_do_qua_20)
print(f"Nhiệt độ của ngày 5, 10, 15, 20, 25: {selected_temps}")
print("Các ngày có nhiệt độ trên trung bình:", ngay_co_nhiet_do_tren_tb)
print("Nhiệt độ của các ngày trên trung bình:", nhiet_do_ngay_tren_tb)
print("Nhiệt độ của các ngày chẵn:", nhiet_do_ngay_chan)
print("Nhiệt độ của các ngày lẻ:", nhiet_do_ngay_le)

