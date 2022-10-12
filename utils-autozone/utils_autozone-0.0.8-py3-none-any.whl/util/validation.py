from datetime import datetime, timedelta
import re
import logging


def separate(string, delimiter):
    delimiter_separated_list = []

    chunk = ''
    in_quotes = False

    for character in string:
        if character == delimiter and not in_quotes:
            delimiter_separated_list.append(chunk)
            chunk = ''

        elif character == '"':
            in_quotes = False if in_quotes else True

        else:
            chunk += character

    delimiter_separated_list.append(chunk)
    return delimiter_separated_list


def transform_date(types, date_format, datetime_format, values):
    transformed = False
    for i, value in enumerate(values):
        if len(values) != len(types):
            continue
        if types[i] == "DATE" and value:
            try:
                if date_format:
                    dt = datetime.strptime(value, date_format)
                    values[i] = dt.strftime('%Y-%m-%d')
                    transformed = True
            except:
                print(f"Date format provided does not match incoming value and is not able to be converted to %Y-%m-%d")
                pass
        if types[i] == "DATETIME" or types[i] == "TIMESTAMP" and value:
            try:
                if datetime_format:
                    dt = datetime.strptime(value, datetime_format)
                    values[i] = dt.strftime('%Y-%m-%d %H:%M:%S')
                    transformed = True
            except:
                print(f"Date format provided does not match incoming value and is not able to be converted to %Y-%m-%d %H:%M:%S")
                pass
            value = value.strip()
            value = value.strip('"')
            try:
                datetime.strptime(value, "%Y-%m-%d %H")
                date = datetime.strptime(value,"%Y-%m-%d %H")
                modified_date = date + timedelta(minutes=00)
                modified_date = modified_date + timedelta(seconds=00)
                str_datetime = datetime.strftime(modified_date, "%Y-%m-%d %H:%M:%S")
                values[i] = str_datetime
                transformed = True
            except:
                pass
            try:
                datetime.strptime(value, "%Y-%m-%d %H:%M")
                date = datetime.strptime(value,"%Y-%m-%d %H:%M")
                modified_date = date + timedelta(seconds=00)
                str_datetime = datetime.strftime(modified_date, "%Y-%m-%d %H:%M:%S")
                values[i] = str_datetime
                transformed = True
            except:
                pass
            try:
                if len(value) > 19: # check to see if microseconds are in date
                    if values[i][10:13] == ' 24':
                        values[i] = values[i][0:10] + ' 00' + values[i][13:]
                        date = datetime.strptime(values[i],"%Y-%m-%d %H:%M:%S.%f")
                        modified_date = date + timedelta(days=1)
                        str_datetime = datetime.strftime(modified_date, "%Y-%m-%d %H:%M:%S.%f")
                        values[i] = str_datetime
                        transformed = True
                else:
                    if values[i][10:13] == ' 24':
                        values[i] = values[i][0:10] + ' 00' + values[i][13:]
                        date = datetime.strptime(values[i],"%Y-%m-%d %H:%M:%S")
                        modified_date = date + timedelta(days=1)
                        str_datetime = datetime.strftime(modified_date, "%Y-%m-%d %H:%M:%S")
                        values[i] = str_datetime
                        transformed = True
            except:
                pass
    return values, transformed


def is_schema_valid(types, modes, names, values):
    # Check number of columns in element
    if len(values) != len(types):
        logging.info(f"Column count does not match. Schema definition has {len(types)} columns and incoming row has {len(values)} columns.")
        return False
    # Loop through values and check if types match
    for i, value in enumerate(values):
        if modes[i] == "REQUIRED" and not value:
            logging.info(f"Column {names[i]} is required but incoming value is NULL")
            return False
        value = value.strip()
        value = value.strip('"')
        if types[i] == "INTEGER" and value:
            try:
                int(value)
            except:
                logging.info(f"Column {names[i]} is defined as INT but incoming value is not INT")
                return False
        if types[i] == "FLOAT" and value:
            try:
                float(value)
            except:
                logging.info(f"Column {names[i]} is defined as FLOAT but incoming value is not FLOAT")
                return False
        if types[i] == "DATE" and value:
            try:
                value = value.strip()
                datetime.strptime(value, "%Y-%m-%d")
            except ValueError:
                logging.info(f"Column {names[i]} is defined as DATE but incoming value is not DATE")
                return False
        if types[i] == "DATETIME" or types[i] == "TIMESTAMP" and value:
            try:
                value = value.strip()
                if len(value) > 23:
                    datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f+00:00")
                elif len(value) > 19: # check to see if microseconds are in date
                    datetime.strptime(value, "%Y-%m-%d %H:%M:%S.%f")
                else:
                    datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                logging.info(f"Column {names[i]} is defined as DATETIME but incoming value is not DATETIME")
                return False
    return True


def validation_checks(names, types, validations, values):
    if len(validations) > 0:
        for i, value in enumerate(values):
            value = value.strip()
            value = value.strip('"')
            for validation in validations:
                if names[i] in validation["columns"]:
                    if (types[i] == "INTEGER"):
                        if "min" in validation and int(value) < validation["min"]:
                            logging.info(f"Column {names[i]} failed minimum value check of {validation['min']}")
                            return False
                        if "max" in validation and int(value) > validation["max"]:
                            logging.info(f"Column {names[i]} failed maximum value check of {validation['max']}")
                            return False
                        if "regex" in validation:
                            if not re.fullmatch(validation["regex"], value):
                                logging.info(f"Column {names[i]} failed regex check of {validation['regex']}")
                                return False
                    if (types[i] == "STRING"):
                        if "min" in validation and len(value) < validation["min"]:
                            logging.info(f"Column {names[i]} failed min string length check of {validation['min']}")
                            return False
                        if "max" in validation and len(value) > validation["max"]:
                            logging.info(f"Column {names[i]} failed max string length check of {validation['max']}")
                            return False
                        if "regex" in validation:
                            if not re.fullmatch(validation["regex"], value):
                                logging.info(f"Column {names[i]} failed regex check of {validation['regex']}")
                                return False
                    if (types[i] == "FLOAT"):
                        if "int_check" in validation and value.isdigit():
                            logging.info(f"Column {names[i]} is defined as FLOAT but value is INT at row {i+1}")
                            return False
    return True