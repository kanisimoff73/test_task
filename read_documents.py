import pandas as pd
import csv


def read_documents(input_data: str, table_register: str, table_journal: str, table_res_inf: str, table_incheck: str):
    """Функция считывает данные с файлов и при помощи циклов нормализует данные для дальнейшей работы с ними"""
    value_in_register = dict()
    total_value_in_journal = dict()
    status_res_inf = list()

    with (
        open(table_register, encoding="ANSI") as table_register,
        open(table_journal, encoding="ANSI") as table_journal,
        open(table_res_inf, encoding="ANSI") as table_res_inf,
        open(table_incheck, encoding="ANSI") as table_incheck
    ):
        read_table_register = list(csv.reader(table_register, delimiter=";"))
        read_table_journal = list(csv.reader(table_journal, delimiter=";"))
        read_table_res_inf = list(csv.reader(table_res_inf, delimiter=";"))
        read_table_incheck = list(csv.reader(table_incheck, delimiter=";"))

        for row in read_table_register:
            if "BK" in row[2]:
                mark = row[2].replace(
                    "СМЕХ", "GNLZ"
                ).replace(
                    "_I_", "1"
                ).replace(
                    "_", ""
                ).replace(
                    " ", ""
                ).replace(
                    "BKETI11SE02C", "BKET11SE02C"
                )
                meters = row[4].replace("м.", "")
                value_in_register[mark] = int(meters)

        for row in read_table_journal:
            mark = row[2].replace("ВКЕО115Е02С_2.5 СМЕХ", "BKE011SE02C_2.5_GNLZ")
            if "BK" in mark:
                mark = mark.split(" ")[0].replace("_", "")
                value = int(row[3])
                if mark in str(total_value_in_journal):
                    total_value_in_journal[mark] += value
                else:
                    total_value_in_journal[mark] = value

        for row in read_table_res_inf:
            mark = row[1].replace("В", "B").replace("К", "K").replace("Е", "E")
            if "BK" in mark:
                mark = mark.replace("_", "")
                status_res_inf.append(mark)

    for_search = list()  # список был отдельно создан для поиска в файле 'table_incheck.csv'
    input_mark = list()
    input_value = list()
    read_input_data = pd.read_excel(input_data)
    for index, row in read_input_data.iterrows():
        row = list(row)
        search = row[1]
        mark = row[1].replace("_", "")
        meters = row[2]
        for_search.append(search)
        input_mark.append(mark)
        input_value.append([meters])

    return (
        for_search,
        input_mark,
        input_value,
        value_in_register,
        total_value_in_journal,
        status_res_inf,
        read_table_incheck
    )
