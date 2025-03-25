
import pandas as pd
from pathlib import Path

# df = pd.DataFrame([1,2,3])
# compression_opts = dict(method='zip',
#                                 archive_name='dist_revenue_report_stat.csv')
# df.to_csv("output.zip", index=False, header=True, compression=compression_opts )

# read csv
# df = pd.read_csv("../resources/csv/text.csv", header = 0)
# print(df)

# read excel
df = pd.read_excel("../resources/excel/text.xlsx","Input",skiprows=1, header = 0, usecols = 'B:D', index_col=0)
print(df)
df.to_csv(r"../resources/result/result.csv")