import xlrd
wb = xlrd.open_workbook('censuspopdata.xlsx', on_demand=True)
ws = wb.sheet_by_index(0)
print(ws.cell(0, 0).value)
