from pandas import read_excel

print("Hello World!")

file=read_excel(r'''H:\Python example\New Microsoft Excel Worksheet.xlsx''', sheet_name='Sheet1')

print(file) 
print()

print(file.iloc[0:2,0:2])
