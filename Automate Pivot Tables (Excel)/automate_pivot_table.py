import pandas as pd

data_frame = pd.read_excel("supermarket_sales.xlsx")
# print(data_frame)

data_frame = data_frame[['Gender', 'Product line', 'Total']]
pivot_table = data_frame.pivot_table(index='Gender', columns='Product line', values='Total',
                                     aggfunc='sum').round(0)
pivot_table.to_excel('pivot_table.xlsx', 'Report', startrow=4)
