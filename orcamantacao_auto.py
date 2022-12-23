from openpyxl import workbook, load_workbook

x = load_workbook('orcamentacao_auto.xlsx')
xb = x.active
print(xb)