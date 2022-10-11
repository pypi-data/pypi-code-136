from pathlib import Path
from moodle_compile.compile import importQuestions
from datetime import datetime

def main(root = Path("questions"), globPattern = {
        "exportGlob": "",
        "blackListGlob": "None",
        "IterateChildren": False
    }):
    print("============")
    print("Finale 0.1.8")
    print("============")
    print()

    print("[{}] Starting Finale".format(datetime.now().strftime("%H:%M:%S")))

    #targeted export by glob & exclusion by glob
    #export Children decides whether or not you want to export 
    #children of glob pattern category
    #make sure blackListGlob isn't accidentally blacklisting everything
    #use Null to match with nothing and "" to match with everything
    xml = importQuestions(root, globPattern)
    with open("out.xml", "w") as f:
        f.write(xml)

if __name__ == '__main__':
    main()
