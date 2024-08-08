import os
import pandas as pd

file = '../casedata/case.xlsx'  # 修改工作路径

df = pd.read_excel(file, sheet_name='Sheet1')	# 返回一个workbook数据类型的值



if __name__ == '__main__':
    print(df)