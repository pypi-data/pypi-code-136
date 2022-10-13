# https://www.cnblogs.com/superbaby11/p/15560994.html
from threading import Thread

def run_cmd(cmd):
    import subprocess
    return subprocess.getoutput(cmd)

def run_deno_cmd(cmd):
    from pathlib import Path
    return run_cmd(str(Path.home()) + "/.deno/bin/" + cmd)

def print_run_cmd(cmd):
    print(run_cmd(cmd))

def create_text_file(file_name, file_content):
    with open(file_name,"w") as file:
        file.write(file_content)

# https://www.jb51.net/article/232129.htm
class MyThread(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__()
        self.fun = target
        self.args = args
        self.kwargs = kwargs
    def run(self):
        self.fun(*self.args, **self.kwargs)

def thread_run_cmd(cmd):
    t = MyThread(target=run_cmd, args=(cmd,), kwargs={})
    t.start()
    t.join()
    
def thread_run_deno_cmd(cmd):
    t = MyThread(target=run_deno_cmd, args=(cmd,), kwargs={})
    t.start()
    t.join()

def get_page_content(url):
    # https://www.cnblogs.com/herbert/p/10789343.html
    # https://www.selenium.dev/documentation/webdriver/drivers/remote_webdriver/#tabs-1-1
    from selenium import webdriver
    import time
    import os
    # https://blog.csdn.net/ad72182009/article/details/116117744
    if 'http_proxy' in os.environ:
        del os.environ['http_proxy']
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        options=chrome_options)
    driver.get(url=url)
    # Wait some time for page loading
    time.sleep(4)
    found_page_source = driver.page_source
    driver.close()
    return found_page_source

def display_code(content):
    from IPython.display import Code
    return Code(data=content)

def display_iframe(url):
    from IPython.display import IFrame
    return IFrame(src = url, width = "100%", height=300)
