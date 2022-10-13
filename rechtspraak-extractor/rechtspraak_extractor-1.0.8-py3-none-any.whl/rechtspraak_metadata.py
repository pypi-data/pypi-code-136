# This file is used for getting the metadata of the ECLIs obtained using rechspraak_api file. This file takes all the
# CSV file created by rechspraak_api, picks up ECLIs and links column, and using an API gets the metadata and saves it
# in another CSV file with metadata suffix.
# This happens in async manner.

from bs4 import BeautifulSoup
import os, urllib, multiprocessing
from concurrent.futures import ThreadPoolExecutor

from rechtspraak_extractor.rechtspraak_functions import *

# Define base url
RECHTSPRAAK_METADATA_API_BASE_URL = "https://uitspraken.rechtspraak.nl/InzienDocument?id="

# Define empty lists where we'll store our data temporarily
ecli_df = []
uitspraak_df = []
rechtspraak_df = pd.DataFrame(columns=['ecli_id', 'uitspraak'])

# Define global lists if user wants in-memory data
global_ecli_df = []
global_uitspraak_df = []

threads = []
max_workers = ''


def get_cores():
    # max_workers is the number of concurrent processes supported by your CPU multiplied by 5.
    # You can change it as per the computing power.
    # Different python versions treat this differently. This is written as per python 3.6.
    n_cores = multiprocessing.cpu_count()

    global max_workers
    max_workers = n_cores * 5
    # If the main process is computationally intensive: Set to the number of logical CPU cores minus one.

    print(f"Maximum " + str(max_workers) + " threads supported by your machine.")


def extract_data_from_html(filename):
    soup = BeautifulSoup(open(filename), "html.parser")
    return soup


def get_data_from_api(ecli_id):
    url = RECHTSPRAAK_METADATA_API_BASE_URL + ecli_id
    response_code = check_api(url)
    global ecli_df
    global uitspraak_df
    try:
        if response_code == 200:
            try:
                # Create HTML file
                html_file = ecli_id + ".html"
                urllib.request.urlretrieve(url, html_file)

                # Extract data frp, HTML
                html_object = extract_data_from_html(html_file)

                soup = BeautifulSoup(str(html_object), features='lxml')

                # Get the data
                uitspraak_info = soup.find_all("div", {"class": "uitspraak-info"})
                section = soup.find_all("div", {"class": "section"})

                uitspraak = ''
                uitspraak = BeautifulSoup(str(uitspraak_info), features='lxml').get_text()
                uitspraak = uitspraak + BeautifulSoup(str(section), features='lxml').get_text()

                ecli_df.append(ecli_id)
                uitspraak_df.append(uitspraak)

                uitspraak = ''

                # BS4 creates an HTML file to get the data. Remove the file after use
                if os.path.exists(html_file):
                    os.remove(html_file)

            except urllib.error.URLError as e:
                print(e)
            except urllib.error.HTTPError as e:
                print(e)
            except Exception as e:
                print(e)
        else:
            ecli_df.append(ecli_id)
            uitspraak_df.append("API returned with error code: " + str(response_code))
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


def get_rechtspraak_metadata(save_file='n'):
    print("Rechtspraak metadata API")
    print("Reading CSV files...")
    csv_files = read_csv('data', "metadata")

    if len(csv_files) > 0:
        if save_file == 'n':
            global_df = pd.DataFrame(columns=['ecli_id', 'uitspraak'])

        start_time = time.time()        # Get start time

        get_cores()  # Get number of cores supported by the CPU

        for f in csv_files:
            # Check if file already exists
            if save_file == 'y':
                file_check = Path("data/" + f.split('/')[-1][:len(f.split('/')[-1]) - 4] + "_metadata.csv")
                if file_check.is_file():
                    print("Metadata for " + f.split('/')[-1][:len(f.split('/')[-1]) - 4] + ".csv already exists.")
                    continue

            df = pd.read_csv(f)
            no_of_rows = df.shape[0]
            print("Getting metadata of " + str(no_of_rows) + " ECLIs from " +
                  f.split('/')[-1][:len(f.split('/')[-1]) - 4] + ".csv")
            print("Working. Please wait...")

            # Get all ECLIs in a list
            ecli_list = list(df.loc[:, 'id'])

            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                for ecli in ecli_list:
                    threads.append(executor.submit(get_data_from_api, ecli))
                # for task in as_completed(threads):
                #     print(task.result())

            executor.shutdown()     # Shutdown the executor

            if save_file == 'y':           # Save file as CSV if selected
                # Save CSV file
                global ecli_df
                global uitspraak_df
                print("Creating CSV file...")
                rechtspraak_df['ecli_id'] = ecli_df
                rechtspraak_df['uitspraak'] = uitspraak_df

                # Create director if not exists
                Path('data').mkdir(parents=True, exist_ok=True)

                rechtspraak_df.to_csv("data/" +
                                      f.split('/')[-1][:len(f.split('/')[-1]) - 4] + "_metadata.csv", index=False)
                print("CSV file " + f.split('/')[-1][:len(f.split('/')[-1]) - 4] + "_metadata.csv" +
                      " successfully created.\n")
            else:
                global global_ecli_df, global_uitspraak_df
                global_ecli_df.extend(ecli_df)
                global_uitspraak_df.extend(uitspraak_df)

            # Clear the lists for the next file
            ecli_df = []
            uitspraak_df = []

        # Get total execution time
        get_exe_time(start_time)
        # print("Total execution time (seconds): %s" % (round(time.time() - start_time, 2)))

        if save_file == 'n':
            global_df['ecli_id'] = global_ecli_df
            global_df['uitspraak'] = global_uitspraak_df
            print(f"Data is stored in 'global_df'")
            print(global_df.head())
