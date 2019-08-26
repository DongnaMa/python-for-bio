import xlrd
import sys

excel = xlrd.open_workbook(sys.argv[1])
st = excel.sheets()[0]
rows = st.nrows
txt = open(sys.argv[2], 'w')
for i in range(rows):
    a = str(st.row_values(i))
    b = a.replace('[', '').replace(']', '').replace('\'', '').replace(',', '\t')
    txt.write(b+'\n')
