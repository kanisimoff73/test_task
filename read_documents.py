import pandas as pd
import csv


def read_documents(input_data, table_register, table_journal, table_res_inf, table_incheck):
    input_mark = []
    input_value = []
    read_xlsx_file = pd.read_excel(input_data)

    for index, row in read_xlsx_file.iterrows():
        for cell in row[1:3]:
            if type(cell) == str:
                input_mark.append(cell)
            else:
                input_value.append(cell)
    res = list(zip(input_mark, input_value))

    value_in_register = []
    with open(table_register, encoding="ANSI") as table_register:
        read_csv_file = csv.reader(table_register)
        for row in read_csv_file:
            if len(row) > 1:
                mark = row[-1].split(";")[-3]
                meters = row[-1].split(";")[-1].replace("м.", "")
                value_in_register.append((mark, int(meters)))

    total_value_in_journal = []
    with open(table_journal, encoding="ANSI") as table_journal:
        read_csv_file = csv.reader(table_journal)
        for row in read_csv_file:
            if len(row) > 1:
                mark = row[0].split(";")[-1].split(" ")[0]
                meters = row[-1].split(";")[0]
                if "L" in meters:
                    total_value_in_journal.append((mark, int(meters.split(" ")[-2])))
                else:
                    total_value_in_journal.append((mark, 0))

    status_res_inf = []
    with open(table_res_inf, encoding="ANSI") as table_res_inf:
        read_csv_file = csv.reader(table_res_inf)
        for row in read_csv_file:
            mark = row[0].split(";")[1]
            status_res_inf.append(mark)
    status_res_inf.pop(0)
    status_res_inf.pop(0)

    status_incheck = []
    with open(table_incheck, encoding="ANSI") as table_incheck:
        read_csv_file = csv.reader(table_incheck)
        for row in read_csv_file:
            status_incheck.append(row)

    return res, value_in_register, total_value_in_journal, status_res_inf, status_incheck


print(read_documents(
    "input_data.xlsx",
    "./table_data/table_register.csv",
    "./table_data/table_journal.csv",
    "./table_data/table_res_inf.csv",
    "./table_data/table_incheck.csv",
))
