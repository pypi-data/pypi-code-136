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
instantie_df = []
datum_uitspraak_df = []
datum_publicatie_df = []
zaaknummer_df = []
rechtsgebieden_df = []
bijzondere_kenmerken_df = []
inhoudsindicatie_df = []
vindplaatsen_df = []
rsm_df = pd.DataFrame(columns=['ecli_id', 'uitspraak', 'instantie', 'datum_uitspraak', 'datum_publicatie',
                               'zaaknummer', 'rechtsgebieden', 'bijzondere_kenmerken', 'inhoudsindicatie',
                               'vindplaatsen'])

# gl_df = pd.DataFrame(columns=['ecli_id', 'uitspraak', 'instantie', 'datum_uitspraak', 'datum_publicatie',
#                               'zaaknummer', 'rechtsgebieden', 'bijzondere_kenmerken', 'inhoudsindicatie',
#                               'vindplaatsen'])

# Define global lists if user wants in-memory data
# gl_ecli_df = []
# gl_uitspraak_df = []
# gl_instantie_df = []
# gl_datum_uitspraak_df = []
# gl_datum_publicatie_df = []
# gl_zaaknummer_df = []
# gl_rechtsgebieden_df = []
# gl_bijzondere_kenmerken_df = []
# gl_inhoudsindicatie_df = []
# gl_vindplaatsen_df = []

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
    global ecli_df, uitspraak_df, instantie_df, datum_uitspraak_df, datum_publicatie_df, zaaknummer_df, \
        rechtsgebieden_df, bijzondere_kenmerken_df, inhoudsindicatie_df, vindplaatsen_df
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

                # We're using temporary variable "temp" to get the other metadata information such as instantie,
                # datum uitspraak, datum publicatie, zaaknummer, rechtsgebieden, bijzondere kenmerken,
                # inhoudsindicatie, and vindplaatsen
                temp = soup.find_all("dl", {"class": "dl-horizontal"})
                instantie = BeautifulSoup(str(temp[0]('dd')[0]), features='lxml').get_text().strip()
                datum_uitspraak = BeautifulSoup(str(temp[0]('dd')[1]), features='lxml').get_text().strip()
                datum_publicatie = BeautifulSoup(str(temp[0]('dd')[2]), features='lxml').get_text().strip()
                zaaknummer = BeautifulSoup(str(temp[0]('dd')[3]), features='lxml').get_text().strip()
                rechtsgebieden = BeautifulSoup(str(temp[0]('dd')[4]), features='lxml').get_text().strip()
                bijzondere_kenmerken = BeautifulSoup(str(temp[0]('dd')[5]), features='lxml').get_text().strip()
                inhoudsindicatie = BeautifulSoup(str(temp[0]('dd')[6]), features='lxml').get_text().strip()
                vindplaatsen = BeautifulSoup(str(temp[0]('dd')[7]), features='lxml').get_text().strip()

                uitspraak = BeautifulSoup(str(uitspraak_info), features='lxml').get_text()
                uitspraak = uitspraak + BeautifulSoup(str(section), features='lxml').get_text()

                ecli_df.append(ecli_id)
                uitspraak_df.append(uitspraak)
                instantie_df.append(instantie)
                datum_uitspraak_df.append(datum_uitspraak)
                datum_publicatie_df.append(datum_publicatie)
                zaaknummer_df.append(zaaknummer)
                rechtsgebieden_df.append(rechtsgebieden)
                bijzondere_kenmerken_df.append(bijzondere_kenmerken)
                inhoudsindicatie_df.append(inhoudsindicatie)
                vindplaatsen_df.append(vindplaatsen)

                del uitspraak, instantie, datum_uitspraak, datum_publicatie, zaaknummer, rechtsgebieden, \
                    bijzondere_kenmerken, inhoudsindicatie, vindplaatsen

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

            global ecli_df, uitspraak_df, instantie_df, datum_uitspraak_df, datum_publicatie_df, zaaknummer_df, \
                rechtsgebieden_df, bijzondere_kenmerken_df, inhoudsindicatie_df, vindplaatsen_df

            if save_file == 'y':           # Save file as CSV if selected
                # Save CSV file
                print("Creating CSV file...")
                rsm_df['ecli_id'] = ecli_df
                rsm_df['uitspraak'] = uitspraak_df
                rsm_df['instantie'] = instantie_df
                rsm_df['datum_uitspraak'] = datum_uitspraak_df
                rsm_df['datum_publicatie'] = datum_publicatie_df
                rsm_df['zaaknummer'] = zaaknummer_df
                rsm_df['rechtsgebieden'] = rechtsgebieden_df
                rsm_df['bijzondere_kenmerken'] = bijzondere_kenmerken_df
                rsm_df['inhoudsindicatie'] = inhoudsindicatie_df
                rsm_df['vindplaatsen'] = vindplaatsen_df

                # Create director if not exists
                Path('data').mkdir(parents=True, exist_ok=True)

                rsm_df.to_csv("data/" +
                                      f.split('/')[-1][:len(f.split('/')[-1]) - 4] + "_metadata.csv", index=False)
                print("CSV file " + f.split('/')[-1][:len(f.split('/')[-1]) - 4] + "_metadata.csv" +
                      " successfully created.\n")
            else:
                rsm_df['ecli_id'].append(ecli_df)
                rsm_df['uitspraak'].append(uitspraak_df)
                rsm_df['instantie'].append(instantie_df)
                rsm_df['datum_uitspraak'].append(datum_uitspraak_df)
                rsm_df['datum_publicatie'].append(datum_publicatie_df)
                rsm_df['zaaknummer'].append(zaaknummer_df)
                rsm_df['rechtsgebieden'].append(rechtsgebieden_df)
                rsm_df['bijzondere_kenmerken'].append(bijzondere_kenmerken_df)
                rsm_df['inhoudsindicatie'].append(inhoudsindicatie_df)
                rsm_df['vindplaatsen'].append(vindplaatsen_df)
                # global gl_ecli_df, gl_uitspraak_df, gl_instantie_df, gl_datum_uitspraak_df, gl_datum_publicatie_df, \
                #     gl_zaaknummer_df, gl_rechtsgebieden_df, gl_bijzondere_kenmerken_df, gl_inhoudsindicatie_df, \
                #     gl_vindplaatsen_df
                #
                # gl_ecli_df.extend(ecli_df)
                # gl_uitspraak_df.extend(uitspraak_df)
                # gl_instantie_df.extend(instantie_df)
                # gl_datum_uitspraak_df.extend(datum_uitspraak_df)
                # gl_datum_publicatie_df.extend(datum_publicatie_df)
                # gl_zaaknummer_df.extend(zaaknummer_df)
                # gl_rechtsgebieden_df.extend(rechtsgebieden_df)
                # gl_bijzondere_kenmerken_df.extend(bijzondere_kenmerken_df)
                # gl_inhoudsindicatie_df.extend(inhoudsindicatie_df)
                # gl_vindplaatsen_df.extend(vindplaatsen_df)

            # Clear the lists for the next file
            ecli_df = []
            uitspraak_df = []
            instantie_df = []
            datum_uitspraak_df = []
            datum_publicatie_df = []
            zaaknummer_df = []
            rechtsgebieden_df = []
            bijzondere_kenmerken_df = []
            inhoudsindicatie_df = []
            vindplaatsen_df = []

        # Get total execution time
        get_exe_time(start_time)
        # print("Total execution time (seconds): %s" % (round(time.time() - start_time, 2)))

        if save_file == 'n':
            # gl_df['ecli_id'] = gl_ecli_df
            # gl_df['uitspraak'] = gl_uitspraak_df
            # gl_df['instantie'] = gl_instantie_df
            # gl_df['datum_uitspraak'] = gl_datum_uitspraak_df
            # gl_df['datum_publicatie'] = gl_datum_publicatie_df
            # gl_df['zaaknummer'] = gl_zaaknummer_df
            # gl_df['rechtsgebieden'] = gl_rechtsgebieden_df
            # gl_df['bijzondere_kenmerken'] = gl_bijzondere_kenmerken_df
            # gl_df['inhoudsindicatie'] = gl_inhoudsindicatie_df
            # gl_df['vindplaatsen'] = gl_vindplaatsen_df
            # print(gl_df.head())
            # gl_ecli_df = []
            # gl_uitspraak_df = []
            # gl_instantie_df = []
            # gl_datum_uitspraak_df = []
            # gl_datum_publicatie_df = []
            # gl_zaaknummer_df = []
            # gl_rechtsgebieden_df = []
            # gl_bijzondere_kenmerken_df = []
            # gl_inhoudsindicatie_df = []
            # gl_vindplaatsen_df = []
            return rsm_df
