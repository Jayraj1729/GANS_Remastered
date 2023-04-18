import openpyxl
import os




wb = openpyxl.load_workbook('data.xlsx')
sheet = wb.active
list(sheet.columns)[0]

for cellObj in list(sheet.columns)[0]:
    os.system("grype %s >result/%s.txt"% (cellObj.value, cellObj.value.replace("/","_")))
    os.system("docker rmi %s"%cellObj.value.replace("/", "_"))
   #print(cellObj.value)


print(check for change.)

print(check for change test run 2.)
