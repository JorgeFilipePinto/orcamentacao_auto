from openpyxl import workbook, load_workbook

x = load_workbook('orcamentacao_auto.xlsx')
xs = x.active
print(xs)
