from win32com import client
import win32api

input_file = 'D:\\py_project\\python_note\\sample_3.xlsx'
#give your file name with valid path 
output_file = 'D:\\py_project\\python_note\\sample_3_output.pdf'
#give valid output file name and path
app = client.DispatchEx("Excel.Application")
app.Interactive = False
app.Visible = False

Workbook = app.Workbooks.Open(input_file)
ws = Workbook.Worksheets[0]
ws.PageSetup.Orientation = 2  # 轉橫向
# ws.PageSetup.PaperSize = 8  # 紙張大小A3
ws.PageSetup.PaperSize = 9  # 紙張大小A4
ws.PageSetup.BottomMargin = 50

try:
    Workbook.ActiveSheet.ExportAsFixedFormat(0, output_file)
except Exception as e:
    print("Failed to convert in PDF format.Please confirm environment meets all the requirements  and try again")
    print(str(e))
finally:
    Workbook.Close(False)
