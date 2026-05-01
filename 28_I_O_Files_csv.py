import pandas as pd
from pathlib import Path

file_to_convert = Path('C:/Temp/excel_file.xlsx')

df = pd.read_excel(file_to_convert)
df.to_csv(Path('C:/Temp/file_converted.csv'), index=False, quoting=1, quotechar='"', encoding='utf-8')
# quoting=1 ensures all fields are quoted (csv.QUOTE_ALL)
print('The file has been converted')
