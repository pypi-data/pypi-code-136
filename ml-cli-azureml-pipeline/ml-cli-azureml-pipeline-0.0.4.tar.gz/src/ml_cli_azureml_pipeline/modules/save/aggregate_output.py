from pathlib import Path
import json
import numpy as np


def build_agregation(dir_path:str):
    flist = [p for p in Path(dir_path).iterdir() if p.is_file()]

    http600 = []
    http500 = []
    http400 = []
    ticks = []
    number_http200OK = 0
    number_http200OKO = 0

    number_retry = 0

    for file_path in flist:
        if not str(file_path).endswith(".json"):
            continue
        with open(file_path, encoding='utf8') as f:
            data = json.load(f)
            number_retry = number_retry + data["TryNumber"]
            status_code = data["StatusCode"]
            ticks.append(data["TicksAt"]/10000000)
            if status_code >= 600:
                p = Path(data["FileDirectory"])
                http500.append(p.stem)
            elif status_code >= 500:
                p = Path(data["FileDirectory"])
                http500.append(p.stem)
            elif status_code >= 400:
                p = Path(data["FileDirectory"])
                http400.append(p.stem)
            elif status_code == 200:
                p = Path(data["FileDirectory"])
                http400.append(p.stem)
                body = json.loads(data["Body"])

                number_ancien_permis_recto = 0
                number_nouveau_permis_recto = 0
                number_nouveau_permis_verso = 0
                for analysis in body["analysis"]:
                    for element in analysis["elements"]:
                        if element["document_type"] == "ancien_permis_recto":
                            number_ancien_permis_recto = number_ancien_permis_recto + 1
                        elif element["document_type"] == "nouveau_permis_recto":
                            number_nouveau_permis_recto = number_nouveau_permis_recto + 1
                        elif element["document_type"] == "nouveau_permis_verso":
                            number_nouveau_permis_verso = number_nouveau_permis_verso + 1

                if number_nouveau_permis_recto > 1 or \
                        number_nouveau_permis_recto > 1 or \
                        number_nouveau_permis_verso > 1:
                    number_http200OKO = number_http200OKO + 1
                elif (
                        number_nouveau_permis_recto > 0 or
                        number_nouveau_permis_recto > 0) and \
                        number_nouveau_permis_verso > 0:
                    number_http200OKO = number_http200OKO + 1
                else:
                    number_http200OK = number_http200OK + 1

    startAt = np.min(ticks)
    endAt = np.max(ticks)

    result = {
        "total": len(flist),
        "number200_OK": number_http200OK,
        "number200_KO": number_http200OKO,
        "number200": number_http200OK+number_http200OKO,
        "number500": len(http500),
        "number600": len(http600),
        "number400": len(http400),
        "http600": http600,
        "http500": http500,
        "http400": http400,
        "elapsed_time_seconds": int(endAt-startAt)
    }
    return result

def create_summary(dir_path:str, output_file_path:str):
    result = build_agregation(dir_path)
    print(result)
    with open(output_file_path, "w") as out_file:
        json.dump(result, out_file, indent=6)


