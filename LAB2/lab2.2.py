import numpy as np
import pandas as pd

# Đọc dữ liệu từ file CSV
file_path = 'C:\\Users\\hieud\\OneDrive\\Desktop\\BAI TAP LAB\\LAB2\\diem_hoc_phan.csv'

data = pd.read_csv(file_path)

# Chuyển dữ liệu thành list và NumPy array
data_list = data.values.tolist()
data_numpy = data.iloc[:, 2:].to_numpy()  # Chỉ lấy các cột điểm HP1, HP2, HP3

print("Dữ liệu gốc:")
print(data)
print("\nDữ liệu dạng NumPy array:")
print(data_numpy)


def quy_doi_diem(diem):
    if 8.5 <= diem <= 10:
        return 'A'
    elif 8.0 <= diem < 8.5:
        return 'B+'
    elif 7.0 <= diem < 8.0:
        return 'B'
    elif 6.5 <= diem < 7.0:
        return 'C+'
    elif 5.5 <= diem < 6.5:
        return 'C'
    elif 5.0 <= diem < 5.5:
        return 'D+'
    elif 4.0 <= diem < 5.0:
        return 'D'
    else:
        return 'F'

# Áp dụng quy đổi điểm
grades = np.vectorize(quy_doi_diem)(data_numpy)

print("\nBảng điểm quy đổi sang điểm tín chỉ:")
print(grades)

# Tách dữ liệu theo học phần
hp1_scores = data_numpy[:, 0]
hp2_scores = data_numpy[:, 1]
hp3_scores = data_numpy[:, 2]

print("\nĐiểm HP1:", hp1_scores)
print("Điểm HP2:", hp2_scores)
print("Điểm HP3:", hp3_scores)


# Hàm tính toán tổng, trung bình, và độ lệch chuẩn
def analyze_scores(scores, hp_name):
    total = np.sum(scores)
    mean = np.mean(scores)
    std_dev = np.std(scores)
    print(f"\nPhân tích điểm {hp_name}:")
    print(f"Tổng điểm: {total}")
    print(f"Điểm trung bình: {mean:.2f}")
    print(f"Độ lệch chuẩn: {std_dev:.2f}")

# Phân tích từng học phần
analyze_scores(hp1_scores, "HP1")
analyze_scores(hp2_scores, "HP2")
analyze_scores(hp3_scores, "HP3")

# Tạo bảng tổng hợp số lượng sinh viên đạt từng loại điểm chữ trên tất cả học phần
all_grades = grades.flatten()
unique_grades, counts = np.unique(all_grades, return_counts=True)

grade_summary = dict(zip(unique_grades, counts))

print("\nPhân tích điểm tổng hợp (trên tất cả học phần):")
for grade, count in grade_summary.items():
    print(f"Loại điểm {grade}: {count} sinh viên")


