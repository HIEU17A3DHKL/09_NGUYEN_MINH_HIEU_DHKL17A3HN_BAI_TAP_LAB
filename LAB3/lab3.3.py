import pandas as pd

stocks1 = pd.read_csv("C:\\Users\\hieud\\OneDrive\\Desktop\\BAI TAP LAB\\LAB3\\stocks1.csv")
# 1. Đọc file stocks2.csv vào DataFrame stocks2
stocks2 = pd.read_csv(r"C:\Users\hieud\OneDrive\Desktop\BAI TAP LAB\LAB3\stocks2.csv")

# 2. Gộp stocks1 và stocks2 thành DataFrame mới tên là stocks
stocks = pd.concat([stocks1, stocks2], ignore_index=True)

# 3. Tính giá trung bình (open, high, low, close) cho mỗi ngày
average_prices = stocks.groupby("date")[["open", "high", "low", "close"]].mean()

# 4. Hiển thị 5 dòng đầu tiên của kết quả
print("5 dòng đầu tiên của giá trung bình (open, high, low, close) theo ngày:")
print(average_prices.head())
