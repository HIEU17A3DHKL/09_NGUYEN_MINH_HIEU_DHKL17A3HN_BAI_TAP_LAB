# import os

# import pandas as pd

# # Tạo thư mục DATA nếu chưa tồn tại
# data_dir = "DATA"
# os.makedirs(data_dir, exist_ok=True)

# # Tạo dữ liệu cho stocks1.csv
# stocks1_data = {
#     "date": ["2024-01-01", "2024-01-01"],
#     "symbol": ["AAPL", "GOOG"],
#     "open": [145, 2750],
#     "high": [150, 2800],
#     "low": [144, 2700],
#     "close": [148, 2780],
#     "volume": [1000000, 500000],
# }

# # Tạo DataFrame và lưu vào stocks1.csv
# stocks1_df = pd.DataFrame(stocks1_data)
# stocks1_path = os.path.join(data_dir, "stocks1.csv")
# stocks1_df.to_csv(stocks1_path, index=False)

# # Tạo dữ liệu cho stocks2.csv
# stocks2_data = {
#     "date": ["2024-01-02", "2024-01-02"],
#     "symbol": ["AAPL", "GOOG"],
#     "open": [150, 2800],
#     "high": [155, 2850],
#     "low": [148, 2750],
#     "close": [152, 2830],
#     "volume": [1200000, 600000],
# }

# # Tạo DataFrame và lưu vào stocks2.csv
# stocks2_df = pd.DataFrame(stocks2_data)
# stocks2_path = os.path.join(data_dir, "stocks2.csv")
# stocks2_df.to_csv(stocks2_path, index=False)

# # Tạo dữ liệu cho companies.csv
# companies_data = {
#     "name": ["AAPL", "GOOG"],
#     "employees": [147000, 156500],
#     "headquarters_city": ["Cupertino", "Mountain View"],
#     "headquarters_state": ["California", "California"],
# }

# # Tạo DataFrame và lưu vào companies.csv
# companies_df = pd.DataFrame(companies_data)
# companies_path = os.path.join(data_dir, "companies.csv")
# companies_df.to_csv(companies_path, index=False)

# print(f"Các file CSV đã được tạo trong thư mục '{data_dir}':")
# print(f"- {stocks1_path}")
# print(f"- {stocks2_path}")
# print(f"- {companies_path}")





# import os

import pandas as pd

# # Đường dẫn tới file stocks1.csv
# data_dir = "DATA"
# stocks1_path = os.path.join(data_dir, "C:\\Users\\hieud\\OneDrive\\Desktop\\BAI TAP LAB\\LAB3\\stocks1.csv")

# 1. Đọc file stocks1.csv vào DataFrame stocks1
stocks1 = pd.read_csv("C:\\Users\\hieud\\OneDrive\\Desktop\\BAI TAP LAB\\LAB3\\stocks1.csv")

# 2. Hiển thị 5 dòng đầu tiên của stocks1
print("5 dòng đầu tiên của stocks1:")
print(stocks1.head())

# 3. Hiển thị kiểu dữ liệu (dtype) của mỗi cột trong stocks1
print("\nKiểu dữ liệu (dtype) của mỗi cột trong stocks1:")
print(stocks1.dtypes)

# 4. Xem thông tin tổng quan (info) của stocks1
print("\nThông tin tổng quan (info) của stocks1:")
stocks1.info()



