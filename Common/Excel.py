import openpyxl
class Excel:
    def __init__(self,file_name,sheet_name):
        self.file_name = file_name
        self.sheet_name = sheet_name
    def open(self):
        self.wb = openpyxl.load_workbook(self.file_name)
        self.sh = self.wb[self.sheet_name]
    def read_data(self):
        """读取数据"""
        self.open()
        res = list(self.sh.rows)
        title = [i.value for i in res[0]]
        case_data = []
        for row in res[1:]:
            data = []
            for cell in row:
                data.append(cell.value)
            case = dict(zip(title,data))
            case_data.append(case)
        return case_data

    def write_data(self,row,column,value):
        """写数据"""
        self.open()
        self.sh.cell(row=row,column=column,value=value)
        self.wb.save(self.file_name)

if __name__ =="__main__":
    excel = Excel(file_name="../Data/Excel.xlsx", sheet_name="Sheet1")
    excel.write_excel(6,6,"仅仅是")
