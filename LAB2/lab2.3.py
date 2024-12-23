# Đọc dữ liệu từ file
with open('C:\\Users\\hieud\\OneDrive\\Desktop\\BAI TAP LAB\\LAB2\\efficiency.txt', 'r') as f:
    efficiency = [float(line.strip()) for line in f]

with open('C:\\Users\\hieud\\OneDrive\\Desktop\\BAI TAP LAB\\LAB2\\shifts.txt', 'r') as f:
    shifts = [line.strip() for line in f]

print("Dữ liệu hiệu suất:", efficiency)
print("Dữ liệu ca làm việc:", shifts)





import numpy as np

# Tạo numpy array từ shifts
np_shifts = np.array(shifts)
print("\nMảng np_shifts:", np_shifts)
print("Kiểu dữ liệu của np_shifts:", np_shifts.dtype)





# Tạo numpy array từ efficiency
np_efficiency = np.array(efficiency)
print("\nMảng np_efficiency:", np_efficiency)
print("Kiểu dữ liệu của np_efficiency:", np_efficiency.dtype)



# Tính hiệu suất trung bình của ca Morning
morning_efficiency = np_efficiency[np_shifts == 'Morning']
avg_morning = np.mean(morning_efficiency)

print("\nHiệu suất trung bình của ca 'Morning':", avg_morning)


# Tính hiệu suất trung bình của các ca khác
non_morning_efficiency = np_efficiency[np_shifts != 'Morning']
avg_non_morning = np.mean(non_morning_efficiency)

print("\nHiệu suất trung bình của các ca khác (không phải 'Morning'):", avg_non_morning)

# Tạo mảng dữ liệu có cấu trúc
workers = np.array(list(zip(np_shifts, np_efficiency)),
                   dtype=[('shift', 'U10'), ('efficiency', 'float')])

print("\nMảng workers với cấu trúc:")
print(workers)


# Sắp xếp worker theo efficiency
sorted_workers = np.sort(workers, order='efficiency')

# Ca làm việc có hiệu suất cao nhất và thấp nhất
highest_efficiency_shift = sorted_workers[-1]['shift']
lowest_efficiency_shift = sorted_workers[0]['shift']

print("\nMảng workers sau khi sắp xếp theo efficiency:")
print(sorted_workers)

print("\nCa làm việc có hiệu suất cao nhất:", highest_efficiency_shift)
print("Ca làm việc có hiệu suất thấp nhất:", lowest_efficiency_shift)

