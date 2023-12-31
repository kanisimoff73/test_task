import openpyxl


def write_result(result_data):
    """
    Функция формирует excel-файл с результатом работы функции 'check_documents()'.
    Сохранение производиться в ту же директорию, в которой находится файл с исходными данными.
    """
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    title = ['input mark', 'input value', 'value in register',
             'total value in journal', 'status res inf', "status incheck"]
    workbook.save('write_result.xlsx')
    workbook.close()

    workbook = openpyxl.load_workbook('write_result.xlsx')
    worksheet = workbook['Sheet']
    worksheet.append(title)
    for key, value in result_data:
        worksheet.append(value)
    workbook.save('write_result.xlsx')
    workbook.close()
