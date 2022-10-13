# This file is used to get all the Rechtspraak ECLIs from an API.
# It takes two required arguments and one optional argument
# 1. max - Maximum number of ECLIs to retrieve
# 2. starting-date (yyyy-mm-dd) - Start date of ECLI publication
# 3. ending-date (yyyy-mm-dd) - It's an optional parameter. If not given, current date will be automatically chosen
# File is stored in data/Rechtspraak folder

import json, xmltodict, argparse, os
from datetime import date, datetime
from pathlib import Path

# sys.path.append(dirname(dirname(dirname(dirname(abspath(__file__))))))

from test_rechtspraak_functions import *
# from storage_handler import DIR_DATA_RECHTSPRAAK


# Get env variable
RECHTSPRAAK_API_BASE_URL = os.getenv('RECHTSPRAAK_API_BASE_URL')


def get_data_from_url(url):
    res = requests.get(url)
    res.raw.decode_content = True

    # Convert the XML data to JSON format
    xpars = xmltodict.parse(res.text)
    json_string = json.dumps(xpars)
    json_object = json.loads(json_string)

    # Get the JSON object from a specific branch
    json_object = json_object['feed']['entry']

    return json_object


def save_csv(json_object, file_name):
    # Define the dataframe to enter the data
    df = pd.DataFrame(columns=['id', 'title', 'summary', 'updated', 'link'])
    ecli_id = []
    title = []
    summary = []
    updated = []
    link = []

    # Iterate over the object and fill the lists
    for i in json_object:
        ecli_id.append(i['id'])
        title.append(i['title']['#text'])
        if '#text' in i['summary']:
            summary.append(i['summary']['#text'])
        else:
            summary.append("No summary available")
        updated.append(i['updated'])
        link.append(i['link']['@href'])

    # Save the lists to dataframe
    df['id'] = ecli_id
    df['title'] = title
    df['summary'] = summary
    df['updated'] = updated
    df['link'] = link

    # Create director if not exists
    Path('data').mkdir(parents=True, exist_ok=True)

    # Save CSV file
    file_path = os.path.join('data', file_name + '.csv')
    df.to_csv(file_path, index=False)


def get_rechtspraak(max=10000, sd=None, en=None):
    print("Rechtspraak dump downloader API")

    # Arguements to pass to API
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--max', help='Maximum number of ECLIs to retrieve', type=int, required=True)
    parser.add_argument('-sd', '--starting-date', help='Starting date', required=True)
    parser.add_argument('-ed', '--ending-date', help='Ending date', required=False)
    parser.add_argument("-mp", "--memory-profile", required=False, choices=["y", "n"], default="n",
                        help="Display memory consumption?")
    args = parser.parse_args()

    amount = args.max
    starting_date = args.starting_date

    # If the end date is not entered, the current date is taken
    today = date.today()
    ending_date = today.strftime("%Y-%m-%d")
    if args.ending_date:
        ending_date = args.ending_date

    # Used to calculate total execution time
    start_time = time.time()

    # Build the URL after getting all the arguments
    url = RECHTSPRAAK_API_BASE_URL + 'max=' + str(amount) + '&date=' + starting_date + '&date=' + ending_date

    print("Checking the API")
    # Check the working of API
    response_code = check_api(url)
    if response_code == 200:
        print("API is working fine!")
        print("Getting " + str(amount) + " documents from " + starting_date + " till " + ending_date)

        json_object = get_data_from_url(url)

        if json_object:
            # Get current time
            current_time = datetime.now().strftime("%H:%M:%S")

            # Build file name
            file_name = 'Rechtspraak_' + starting_date + '_' + ending_date + '_' + current_time

            save_csv(json_object, file_name)
            print(f"Data saved to CSV file successfully.")
            get_exe_time(start_time)
            # print(f"Total execution time: %s" % round((time.time() - start_time), 3))
    else:
        print(f"URL returned with a {response_code} error code")
