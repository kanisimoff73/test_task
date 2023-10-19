import openpyxl

from write_result import write_result
from read_documents import read_documents

result = read_documents(
    "input_data.xlsx",
    "./table_data/table_register.csv",
    "./table_data/table_journal.csv",
    "./table_data/table_res_inf.csv",
    "./table_data/table_incheck.csv",
)


def check_documents(
        for_search: list,
        input_mark: list,
        input_value: list,
        value_in_register: dict,
        total_value_in_journal: dict,
        status_res_inf: list,
        read_table_incheck: list
) -> dict:
    """
    Функция проверяет прочитанные данные на соответствие с исходными, для это использовались циклы и условные
    операторы
    """
    dict_data = dict(zip(input_mark, input_value))

    # цикл заполняет поле 'value in register' значениями из файла 'table_register.csv', соответствующими исходным данным
    for key in dict_data.keys():
        if key in value_in_register:
            dict_data[key].append(value_in_register[key])
        else:
            dict_data[key].append(0)

    # цикл заполняет поле 'total value in journal' общей суммой значений значениями из файла 'table_journal.csv',
    # которые также соответствуют исходным данным
    for key in dict_data.keys():
        if key in total_value_in_journal:
            dict_data[key].append(total_value_in_journal[key])
        else:
            dict_data[key].append(0)

    # цикл заполняет поле 'status res inf', в данном поле отображается статус значения 'input mark' в данных файла
    # 'table_res_inf.csv'
    for key in dict_data.keys():
        if key in status_res_inf:
            dict_data[key].append("OK")
        else:
            dict_data[key].append("Не найден!")

    # последний цикл, который заполняет поле 'status inchek', поле отображает статус значения 'input mark' в данных
    # файла 'table_incheck.csv'
    for el in for_search:
        if el in str(read_table_incheck):
            dict_data[el.replace("_", "")].append("OK")
        else:
            dict_data[el.replace("_", "")].append("Не найден!")  # цикл не полностью выполняется требования,
            # прописанные в ТЗ, отсутствует вывод номера.

    # конструкция сделана для корректого отображения данных в терминале и записи в excel-файл
    value_list = list(dict_data.values())
    result_data = list(zip(for_search, value_list))
    for key, value in result_data:
        value.insert(0, key)

    print(f"input mark | "
          f"input value | "
          f"value in register | "
          f"total value in journal | "
          f"status res inf | "
          f"status incheck")
    for key, value in result_data:
        print(f"{key} | {value[1]} | {value[2]} | {value[3]} | {value[4]} | {value[5]}")

    write_result(result_data)  # данный вывоз функции производить запись данных в excel-таблицу

    return dict_data


check_documents(result[0], result[1], result[2], result[3], result[4], result[5], result[6])
