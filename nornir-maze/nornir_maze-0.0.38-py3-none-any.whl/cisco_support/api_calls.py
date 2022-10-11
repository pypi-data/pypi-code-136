#!/usr/bin/env python3
"""
This module contains functions to get data from the Cisco Support APIs.

The functions are ordered as followed:
- Cisco support API call functions in Nornir stdout style
"""


import sys
import json
import time
import requests
from cisco_support import SNI, EoX
from cisco_support.utils import getToken as cisco_support_get_token
from nornir_maze.utils import (
    print_task_name,
    task_host,
    task_info,
    task_error,
    iterate_all,
)


#### Cisco API call functions in Nornir stdout style #########################################################


def cisco_support_check_authentication(api_client_creds, verbose=False, silent=False):
    """
    This function checks to Cisco support API authentication by generating an bearer access token. In case
    of an invalid API client key or secret a error message is printed and the script exits.
    """
    task_name = "CISCO-API check OAuth2 client credentials grant flow"

    try:
        # Try to generate an barer access token
        token = cisco_support_get_token(*api_client_creds, verify=None, proxies=None)

        if not silent:
            print_task_name(text=task_name)
            print(task_info(text=task_name, changed="False"))
            print("'Bearer access token generation' -> CISCOAPIResult <Success: True>")
            if verbose:
                print(f"\n-> Bearer token: {token}\n")

        return True

    except KeyError:
        if not silent:
            ansi_red_bold = "\033[1m\u001b[31m"
            ansi_reset = "\033[0m"
            print_task_name(text=task_name)
            print(task_error(text=task_name, changed="False"))
            print("'Bearer access token generation' -> CISCOAPIResult <Success: False>")
            print("\n\U0001f4a5 ALERT: INVALID API CREDENTIALS PROVIDED! \U0001f4a5")
            print(f"{ansi_red_bold}-> Verify the API client key and secret{ansi_reset}\n")

        return False


def verify_cisco_support_api_data(serials_dict, verbose=False, silent=False):
    """
    This function verifies the serials_dict which has been filled with data by various functions of these
    module like eox_by_serial_numbers, sni_get_coverage_summary_by_serial_numbers, etc. and verifies that
    there are no invalid serial numbers. In case of invalid serial numbers, the script quits with an error
    message.
    """
    task_text = "Verify Cisco support API data"
    print_task_name(text=task_text)

    # Verify that the serials_dict dictionary contains no wrong serial numbers
    for value in iterate_all(iterable=serials_dict, returned="value"):
        if value is not None:
            if "No product IDs were found" in value or "No records found" in value:
                if not silent:
                    print(task_error(text=task_text, changed="False"))
                    print(f"'{task_text}' -> Result <Success: False>")
                    print(
                        "\n\U0001f4a5 ALERT: INVALID SERIAL NUMBERS PROVIDED! \U0001f4a5\n"
                        "\033[1m\u001b[31m"
                        "-> Analyse the output for failed tasks to identify the invalid serial numbers\n"
                        "-> Run the script with valid serial numbers only again\033[0m\n\n"
                    )
                return False

    if not silent:
        print(task_info(text=task_text, changed="False"))
        print(f"'{task_text}' -> Result <Success: True>")
        if verbose:
            print("\n" + json.dumps(serials_dict, indent=4))

    return True


def get_sni_owner_coverage_by_serial_number(serial_dict, api_client_creds):
    """
    This function takes the serial_dict which contains all serial numbers and the Cisco support API creds to
    run get the owner coverage by serial number with the cisco-support library. The result of each serial will
    be added with a new key to the dict. The function returns the updated serials dict. The format of the
    serials_dict need to be as below.
    "<serial>": {
        "host": "<hostname>",
        ...
    },
    """
    # pylint: disable=invalid-name,too-many-locals

    task_text = "CISCO-API get owner coverage status by serial number"

    # Backoff sleep and attempt values
    RETRY_ATTEMPTS = 20
    SLEEP = 1
    SLEEP_MULTIPLIER = 1
    # Maximum serial number API parameter value
    MAX_SR_NO = 75

    sni = SNI(*api_client_creds)

    # Create a dictionary with the key "serial_numbers" to fill with the API response chunks
    owner_coverage_status = {}
    owner_coverage_status["serial_numbers"] = []

    # Loop over a list with all serial numbers with a step incrementation of MAX_SR_NO
    for index in range(0, len(list(serial_dict.keys())), MAX_SR_NO):

        # Re-try the Cisco support API call with a backoff again in case of an error
        for _ in range(RETRY_ATTEMPTS):
            # Create a chunk list with the maximum allowed elements specified by MAX_SR_NO
            serial_chunk = list(serial_dict.keys())[index : index + MAX_SR_NO]

            # Call the Cisco support API for the serial_chunk list
            try:
                response = sni.getOwnerCoverageStatusBySerialNumbers(sr_no=serial_chunk)
            except requests.exceptions.JSONDecodeError:
                continue

            # Break out of the range() loop if ErrorResponse is not present in the API response
            if "ErrorResponse" not in response:
                # Update the owner_coverage_status dict
                for item in response["serial_numbers"]:
                    owner_coverage_status["serial_numbers"].append(item)
                break

            # SLEEP and continue with next range() loop attempt
            time.sleep(SLEEP)
            SLEEP = SLEEP * SLEEP_MULTIPLIER

        # Ending for loop as iterable exhausted
        else:
            print_task_name(text=task_text)
            print(task_error(text=task_text, changed="False"))
            print("'Get SNI data' -> CISCOAPIResult <Success: False>\n")
            for key, value in response["ErrorResponse"]["APIError"][0].items():
                print(f"-> {key}: {value}")
            print(
                "\n\U0001f4a5 "
                f"ALERT: GET CISCO SUPPORT API DATA FAILED AFTER {RETRY_ATTEMPTS} RETRY ATTEMPTS! "
                "\U0001f4a5\n"
                "\033[1m\u001b[31m-> Analyse the error message and identify the root cause\033[0m\n\n"
            )
            sys.exit(1)

    # Add all records to the serial_dict dictionary
    for record in owner_coverage_status["serial_numbers"]:
        # sr_no = record["sr_no"]
        serial_dict[record["sr_no"]]["SNIgetOwnerCoverageStatusBySerialNumbers"] = record

    return serial_dict


def print_sni_owner_coverage_by_serial_number(serial_dict, verbose=False):
    """
    This function prints the result of get_sni_owner_coverage_by_serial_number() in Nornir style to stdout.
    """
    task_text = "CISCO-API get owner coverage status by serial number"
    print_task_name(text=task_text)

    for sr_no, items in serial_dict.items():
        record = items["SNIgetOwnerCoverageStatusBySerialNumbers"]
        print(task_host(host=f"HOST: {items['host']} / SN: {sr_no}", changed="False"))
        # Verify if the serial number is associated with the CCO ID
        if "YES" in record["sr_no_owner"]:
            print(task_info(text="Verify provided CCO ID", changed="False"))
            print("'Is associated to the provided CCO ID' -> CISCOAPIResult <Success: True>")
        else:
            print(task_error(text="Verify provided CCO ID", changed="False"))
            print("'Is not associated to the provided CCO ID' -> CISCOAPIResult <Success: False>")

        # Verify if the serial is covered by a service contract
        if "YES" in record["is_covered"]:
            print(task_info(text="Verify service contract", changed="False"))
            print("'Is covered by a service contract' -> CISCOAPIResult <Success: True>")
            # Verify the end date of the service contract coverage
            if record["coverage_end_date"]:
                print(task_info(text="Verify service contract end date", changed="False"))
                print(
                    f"'Coverage end date is {record['coverage_end_date']}' -> CISCOAPIResult <Success: True>"
                )
            else:
                print(task_error(text="Verify service contract end date", changed="False"))
                print("'Coverage end date not available' -> CISCOAPIResult <Success: False>")
        else:
            print(task_error(text="Verify service contract", changed="False"))
            print("'Is not covered by a service contract' -> CISCOAPIResult <Success: False>")

        if verbose:
            print("\n" + json.dumps(record, indent=4))


def get_sni_coverage_summary_by_serial_numbers(serial_dict, api_client_creds):
    """
    This function takes the serial_dict which contains all serial numbers and the Cisco support API creds to
    run get the coverage summary by serial number with the cisco-support library. The result of each serial
    will be added with a new key to the dict. The function returns the updated serials dict. The format of
    the serials_dict need to be as below.
    "<serial>": {
        "host": "<hostname>",
        ...
    },
    """
    # pylint: disable=invalid-name,too-many-locals

    task_text = "CISCO-API get coverage summary data by serial number"

    # Backoff sleep and attempt values
    RETRY_ATTEMPTS = 20
    SLEEP = 1
    SLEEP_MULTIPLIER = 1
    # Maximum serial number API parameter value
    MAX_SR_NO = 75

    sni = SNI(*api_client_creds)

    # Create a dictionary with the key "serial_numbers" to fill with the API response chunks
    coverage_summary = {}
    coverage_summary["serial_numbers"] = []

    # Loop over a list with all serial numbers with a step incrementation of MAX_SR_NO
    for index in range(0, len(list(serial_dict.keys())), MAX_SR_NO):

        # Part 1: Get the total number of pages for the serial_chunk list
        # Re-try the Cisco support API call with a backoff again in case of an error
        for _ in range(RETRY_ATTEMPTS):
            # Create a chunk list with the maximum allowed elements specified by MAX_SR_NO
            serial_chunk = list(serial_dict.keys())[index : index + MAX_SR_NO]

            # Call the Cisco support API for the serial_chunk list to get the total number of pages
            try:
                response = sni.getCoverageSummaryBySerialNumbers(sr_no=serial_chunk, page_index=1)
            except requests.exceptions.JSONDecodeError:
                continue

            # If the pagination details are present
            # Break out of the range() loop if ErrorResponse is not present in the API response
            if "pagination_response_record" in response:
                # Get the total number of pages to create API calls for all pages
                num_pages = response["pagination_response_record"]["last_index"]
                break

            # SLEEP and continue with next range() loop attempt
            time.sleep(SLEEP)
            SLEEP = SLEEP * SLEEP_MULTIPLIER

        # Ending for loop as iterable exhausted
        else:
            print_task_name(text=task_text)
            print(task_error(text=task_text, changed="False"))
            print("'Get SNI data' -> CISCOAPIResult <Success: False>\n")
            for key, value in response["ErrorResponse"]["APIError"][0].items():
                print(f"-> {key}: {value}")
            print(
                "\n\U0001f4a5 "
                f"ALERT: GET CISCO SUPPORT API DATA FAILED AFTER {RETRY_ATTEMPTS} RETRY ATTEMPTS! "
                "\U0001f4a5\n"
                "\033[1m\u001b[31m-> Analyse the error message and identify the root cause\033[0m\n\n"
            )
            sys.exit(1)

        # Part 2: Get the API data for each page of the serial_chunk list
        # Call the Cisco support API for each page of the serial_chunk list
        for page in range(1, num_pages + 1):
            # Re-try the Cisco support API call with a backoff again in case of an error
            for _ in range(RETRY_ATTEMPTS):
                # Call the Cisco support API for the serial_chunk list
                try:
                    response = sni.getCoverageSummaryBySerialNumbers(sr_no=serial_chunk, page_index=page)
                except requests.exceptions.JSONDecodeError:
                    continue

                # If the pagination details are present
                # Break out of the range() loop if ErrorResponse is not present in the API response
                if "pagination_response_record" in response:
                    # Update the owner_coverage_status dict
                    for item in response["serial_numbers"]:
                        coverage_summary["serial_numbers"].append(item)
                    break

                # SLEEP and continue with next range() loop attempt
                time.sleep(SLEEP)
                SLEEP = SLEEP * SLEEP_MULTIPLIER

            # Ending for loop as iterable exhausted
            else:
                print_task_name(text=task_text)
                print(task_error(text=task_text, changed="False"))
                print("'Get SNI data' -> CISCOAPIResult <Success: False>\n")
                for key, value in response["ErrorResponse"]["APIError"][0].items():
                    print(f"-> {key}: {value}")
                print(
                    "\n\U0001f4a5 "
                    f"ALERT: GET CISCO SUPPORT API DATA FAILED AFTER {RETRY_ATTEMPTS} RETRY ATTEMPTS! "
                    "\U0001f4a5\n"
                    "\033[1m\u001b[31m-> Analyse the error message and identify the root cause\033[0m\n\n"
                )
                sys.exit(1)

    # Add all records to the serial_dict dictionary
    for record in coverage_summary["serial_numbers"]:
        # sr_no = record["sr_no"]
        serial_dict[record["sr_no"]]["SNIgetCoverageSummaryBySerialNumbers"] = record

    return serial_dict


def print_sni_coverage_summary_by_serial_numbers(serial_dict, verbose=False):
    """
    This function prints the result of get_sni_coverage_summary_by_serial_numbers() in Nornir style to stdout.
    """
    task_text = "CISCO-API get coverage summary data by serial number"
    print_task_name(text=task_text)

    for sr_no, items in serial_dict.items():
        record = items["SNIgetCoverageSummaryBySerialNumbers"]
        print(task_host(host=f"HOST: {items['host']} / SN: {sr_no}", changed="False"))
        if "ErrorResponse" in record:
            print(task_error(text=task_text, changed="False"))
            print("'Get SNI data' -> CISCOAPIResult <Success: False>")
            error_response = record["ErrorResponse"]["APIError"]
            print(f"\n-> {error_response['ErrorDescription']} ({error_response['SuggestedAction']})\n")
        else:
            print(task_info(text=task_text, changed="False"))
            print("'Get SNI data' -> CISCOAPIResult <Success: True>")
            print(f"\n-> Orderable pid: {record['orderable_pid_list'][0]['orderable_pid']}")
            print(f"-> Customer name: {record['contract_site_customer_name']}")
            print(f"-> Customer address: {record['contract_site_address1']}")
            print(f"-> Customer city: {record['contract_site_city']}")
            print(f"-> Customer province: {record['contract_site_state_province']}")
            print(f"-> Customer country: {record['contract_site_country']}")
            print(f"-> Is covered by service contract: {record['is_covered']}")
            print(f"-> Covered product line end date: {record['covered_product_line_end_date']}")
            print(f"-> Service contract number: {record['service_contract_number']}")
            print(f"-> Service contract description: {record['service_line_descr']}")
            print(f"-> Warranty end date: {record['warranty_end_date']}")
            print(f"-> Warranty type: {record['warranty_type']}\n")

        if verbose:
            print(json.dumps(record, indent=4))


def get_eox_by_serial_numbers(serial_dict, api_client_creds):
    """
    This function takes the serial_dict which contains all serial numbers and the Cisco support API creds to
    run get the end of life data by serial number with the cisco-support library. The result of each serial
    will be added with a new key to the dict. The function returns the updated serials dict. The format of
    the serials_dict need to be as below.
    "<serial>": {
        "host": "<hostname>",
        ...
    },
    """
    # pylint: disable=invalid-name,too-many-locals,too-many-branches

    # Backoff SLEEP and attempt values
    RETRY_ATTEMPTS = 20
    SLEEP = 1
    SLEEP_MULTIPLIER = 1
    # Maximum serial number API parameter value
    MAX_SR_NO = 20

    task_text = "CISCO-API get EoX data by serial number"

    eox = EoX(*api_client_creds)

    # Create a dictionary with the key "serial_numbers" to fill with the API response chunks
    end_of_life = {}
    end_of_life["EOXRecord"] = []

    # Loop over a list with all serial numbers with a step incrementation of MAX_SR_NO
    for index in range(0, len(list(serial_dict.keys())), MAX_SR_NO):

        # Part 1: Get the total number of pages for the serial_chunk list
        # Re-try the Cisco support API call with a backoff again in case of an error
        for _ in range(RETRY_ATTEMPTS):
            # Create a chunk list with the maximum allowed elements specified by MAX_SR_NO
            serial_chunk = list(serial_dict.keys())[index : index + MAX_SR_NO]

            # Call the Cisco support API for the serial_chunk list to get the total number of pages
            try:
                response = eox.getBySerialNumbers(serialNumber=serial_chunk, pageIndex=1)
            except requests.exceptions.JSONDecodeError:
                continue

            # If the pagination details are present
            # Break out of the range() loop if ErrorResponse is not present in the API response
            if "PaginationResponseRecord" in response:
                # Get the total number of pages to create API calls for all pages
                num_pages = response["PaginationResponseRecord"]["LastIndex"]
                break

            # SLEEP and continue with next range() loop attempt
            time.sleep(SLEEP)
            SLEEP = SLEEP * SLEEP_MULTIPLIER

        # Ending for loop as iterable exhausted
        else:
            print_task_name(text=task_text)
            print(task_error(text=task_text, changed="False"))
            print("'Get EoX data' -> CISCOAPIResult <Success: False>\n")
            if "ErrorResponse" in response:
                for key, value in response["ErrorResponse"]["APIError"][0].items():
                    print(f"-> {key}: {value}")
            else:
                print("-> The EoX API returned NULL. Could be a bug in the API.")
            print(
                "\n\U0001f4a5 "
                f"ALERT: GET CISCO SUPPORT API DATA FAILED AFTER {RETRY_ATTEMPTS} RETRY ATTEMPTS! "
                "\U0001f4a5\n"
                "\033[1m\u001b[31m-> Analyse the error message and identify the root cause\033[0m\n\n"
            )
            sys.exit(1)

        # Part 2: Get the API data for each page of the serial_chunk list
        # Call the Cisco support API for each page of the serial_chunk list
        for page in range(1, num_pages + 1):
            # Re-try the Cisco support API call with a backoff again in case of an error
            for _ in range(RETRY_ATTEMPTS):
                # Call the Cisco support API for the serial_chunk list
                try:
                    response = eox.getBySerialNumbers(serialNumber=serial_chunk, pageIndex=page)
                except requests.exceptions.JSONDecodeError:
                    continue

                # If the pagination details are present
                # Break out of the range() loop if ErrorResponse is not present in the API response
                if "PaginationResponseRecord" in response:
                    # Update the owner_coverage_status dict
                    for item in response["EOXRecord"]:
                        end_of_life["EOXRecord"].append(item)
                    break

                # SLEEP and continue with next range() loop attempt
                time.sleep(SLEEP)
                SLEEP = SLEEP * SLEEP_MULTIPLIER

            # Ending for loop as iterable exhausted
            else:
                print_task_name(text=task_text)
                print(task_error(text=task_text, changed="False"))
                print("'Get EoX data' -> CISCOAPIResult <Success: False>\n")
                if "ErrorResponse" in response:
                    for key, value in response["ErrorResponse"]["APIError"][0].items():
                        print(f"-> {key}: {value}")
                else:
                    print("-> The EoX API returned NULL. Could be a bug in the API.")
                print(
                    f"\n\U0001f4a5 "
                    f"ALERT: GET CISCO SUPPORT API DATA FAILED AFTER {RETRY_ATTEMPTS} RETRY ATTEMPTS! "
                    "\U0001f4a5\n"
                    "\033[1m\u001b[31m-> Analyse the error message and identify the root cause\033[0m\n\n"
                )
                sys.exit(1)

    for record in end_of_life["EOXRecord"]:
        # The response value of "EOXInputValue" can be a single serial number or a comma separated string of
        # serial numbers as the API response can collect multiple same EoX response together
        for sr_no in record["EOXInputValue"].split(","):
            serial_dict[sr_no]["EOXgetBySerialNumbers"] = record

    return serial_dict


def print_eox_by_serial_numbers(serial_dict, verbose=False):
    """
    This function prints the result of get_eox_by_serial_numbers() in Nornir style to stdout.
    """
    task_text = "CISCO-API get EoX data by serial number"
    print_task_name(text=task_text)

    for sr_no, items in serial_dict.items():
        record = items["EOXgetBySerialNumbers"]
        print(task_host(host=f"HOST: {items['host']} / SN: {sr_no}", changed="False"))
        if "EOXError" in record:
            if "No product IDs were found" in record["EOXError"]["ErrorDescription"]:
                print(task_error(text=task_text, changed="False"))
                print("'Get EoX data' -> CISCOAPIResult <Success: False>")
                print(f"\n-> {record['EOXError']['ErrorDescription']} (Serial number does not exist)\n")
            elif "EOX information does not exist" in record["EOXError"]["ErrorDescription"]:
                print(task_info(text=task_text, changed="False"))
                print("'Get EoX data' -> CISCOAPIResult <Success: True>")
                print(f"\n-> {record['EOXError']['ErrorDescription']}\n")
        else:
            print(task_info(text=task_text, changed="False"))
            print(
                f"'Get EoX data (Update timestamp {record['UpdatedTimeStamp']['value']})' "
                + "-> CISCOAPIResult <Success: True>"
            )
            print(f"\n-> EoL product ID: {record['EOLProductID']}")
            print(f"-> Product ID description: {record['ProductIDDescription']}")
            print(f"-> EoL announcement date: {record['EOXExternalAnnouncementDate']['value']}")
            print(f"-> End of sale date: {record['EndOfSaleDate']['value']}")
            print(f"-> End of maintenance release: {record['EndOfSWMaintenanceReleases']['value']}")
            print(f"-> End of vulnerability support: {record['EndOfSecurityVulSupportDate']['value']}")
            print(f"-> Last day of support: {record['LastDateOfSupport']['value']}\n")

        if verbose:
            print(json.dumps(record, indent=4))
