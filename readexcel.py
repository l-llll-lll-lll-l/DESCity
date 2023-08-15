import json

import openpyxl
import RegistSheet
if __name__ == '__main__':
    rst = []
    sc = open('source.json', 'w')
    for path in RegistSheet.regist_excel:
        workbook = openpyxl.load_workbook(path)
        sheet = workbook.active
        ls1=[]
        ls2=[]
        for row in sheet.iter_rows(min_row=2, values_only=True):
            ls1.append(row[0])
            ls2.append(row[1])
        name=path.split('.')[-2]
        name=name.split('/')[-1]
        rst.append([[ls1[0],ls1[-1]],ls2,name])
    json.dump(rst,sc)
    sc.close()
