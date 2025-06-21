import pandas as pd

# Đọc file Excel
df = pd.read_excel('company data.xlsx', sheet_name=None)

# Lấy các sheet cần thiết
visitors_df = df['Visitors data']
products_df = df['Products'].set_index('Product id')
cities_df = df['Cities'].set_index('City id')
channels_df = df['Traffic channels'].set_index('Channel id')
pricing_plans_df = df['Pricing plans'].set_index('Pricing plan id')
prices_df = df['Prices']

prices_df = prices_df.set_index(prices_df.columns[0])

# 1. Map Channel
visitors_df['Channel'] = visitors_df['Channel id'].map(channels_df['Channel'])

# 2. Map Products
visitors_df['Products'] = visitors_df['Product id'].map(products_df['Product'])

# 3. Map Pricing Plan
visitors_df['Pricing Plan'] = visitors_df['Pricing plan id'].map(pricing_plans_df['Pricing plan'])

# 4. Map City
visitors_df['City'] = visitors_df['City id'].map(cities_df['City'])

# 5. Tính Income dựa trên Prices
def calculate_income(row):
    if row['Product id'] == -1 or row['Pricing plan id'] == -1:
        return 0
    product = products_df.loc[row['Product id'], 'Product']
    pricing_plan = pricing_plans_df.loc[row['Pricing plan id'], 'Pricing plan']
    return prices_df.loc[pricing_plan, product]

visitors_df['Income'] = visitors_df.apply(calculate_income, axis=1)

# Sắp xếp lại các cột theo yêu cầu
columns_order = [
    'Visitor id', 'Channel id', 'Channel', 'Device type', 'Bought', 'Order id',
    'Product id', 'Products', 'Pricing plan id', 'Pricing Plan', 'City id', 'City',
    'Day of week (num)', 'Day of week', 'Income'
]
visitors_df = visitors_df[columns_order]

# Cập nhật lại dictionary df với sheet Visitors data đã chỉnh sửa
df['Visitors data'] = visitors_df

# Lưu toàn bộ file Excel ban đầu với sheet Visitors data đã cập nhật
with pd.ExcelWriter('company data.xlsx', engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    for sheet_name, data in df.items():
        data.to_excel(writer, sheet_name=sheet_name, index=False)

print("Đã hoàn thành mapping dữ liệu và lưu lại vào sheet 'Visitors data' trong file 'company data.xlsx'")