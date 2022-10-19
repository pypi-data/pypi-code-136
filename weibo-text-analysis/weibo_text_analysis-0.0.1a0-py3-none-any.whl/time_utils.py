import time

def convert_to_standard_time(s):
    s=s.replace("+0800","")
    return time.strftime("%Y-%m-%d %H:%M:%S", time.strptime(s, "%a %b %d %H:%M:%S %Y"))

if __name__=="__main__":
    time_str="Fri Oct 07 07:00:09 +0800 2022"
    print(convert_to_standard_time(time_str))