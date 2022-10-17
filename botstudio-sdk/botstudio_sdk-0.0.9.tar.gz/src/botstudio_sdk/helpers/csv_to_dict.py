import csv
import json


def count_columns_csv(file_name):
    with open(file_name, mode="r") as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                return len(row)


def convert_csv_with_2_columns(
    csv_input_file: str,
    py_output_file: str,
    name_dict: str,
):
    with open(csv_input_file, mode="r") as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        mydict = {}
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if row[0] not in mydict:
                    mydict[row[0]] = int(row[1])
    with open(py_output_file, mode="w") as py_file:
        py_file.write(f"{name_dict} = " + json.dumps(mydict, indent=4))


def convert_csv_with_3_columns(
    csv_input_file: str,
    py_output_file: str,
    name_dict: str,
):
    with open(csv_input_file, mode="r") as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        mydict = {}
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if row[0] not in mydict:
                    mydict[row[0]] = {}
                if row[1] not in mydict[row[0]]:
                    mydict[row[0]][row[1]] = int(row[2])
    with open(py_output_file, mode="w") as py_file:
        py_file.write(f"{name_dict} = " + json.dumps(mydict, indent=4))


def convert_csv_with_4_columns(
    csv_input_file: str,
    py_output_file: str,
    name_dict: str,
):
    with open(csv_input_file, mode="r") as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        mydict = {}
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if row[0] not in mydict:
                    mydict[row[0]] = {}
                if row[1] not in mydict[row[0]]:
                    mydict[row[0]][row[1]] = {}
                if row[2] not in mydict[row[0]][row[1]]:
                    mydict[row[0]][row[1]][row[2]] = int(row[3])
    with open(py_output_file, mode="w") as py_file:
        py_file.write(f"{name_dict} = " + json.dumps(mydict, indent=4))


def convert_csv_with_5_columns(
    csv_input_file: str,
    py_output_file: str,
    name_dict: str,
):
    with open(csv_input_file, mode="r") as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        mydict = {}
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if row[0] not in mydict:
                    mydict[row[0]] = {}
                if row[1] not in mydict[row[0]]:
                    mydict[row[0]][row[1]] = {}
                if row[2] not in mydict[row[0]][row[1]]:
                    mydict[row[0]][row[1]][row[2]] = {}
                if row[3] not in mydict[row[0]][row[1]][row[2]]:
                    mydict[row[0]][row[1]][row[2]][row[3]] = int(row[4])

    with open(py_output_file, mode="w") as py_file:
        py_file.write(f"{name_dict} = " + json.dumps(mydict, indent=4))


if __name__ == "__main__":
    _csv_input_file = "Prijsijst - prijslijst totaal.csv"
    _py_output_file = "prijslijst.py"
    _name_dict = "prijslijst"

    count = count_columns_csv(_csv_input_file)
    print(type(count))
    if count == 2:
        convert_csv_with_2_columns(
            csv_input_file=_csv_input_file,
            py_output_file=_py_output_file,
            name_dict=_name_dict,
        )
    elif count == 3:
        convert_csv_with_3_columns(
            csv_input_file=_csv_input_file,
            py_output_file=_py_output_file,
            name_dict=_name_dict,
        )
    elif count == 4:
        convert_csv_with_4_columns(
            csv_input_file=_csv_input_file,
            py_output_file=_py_output_file,
            name_dict=_name_dict,
        )
    elif count == 5:
        convert_csv_with_5_columns(
            csv_input_file=_csv_input_file,
            py_output_file=_py_output_file,
            name_dict=_name_dict,
        )
    else:
        print("Function not available yet.")
