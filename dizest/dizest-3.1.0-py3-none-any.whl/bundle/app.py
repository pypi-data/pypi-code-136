import sys
import os
import season
import multiprocessing as mp
import psutil

PATH_WEBSRC = os.path.dirname(__file__)
def run_ctrl():
    app = season.app(path=PATH_WEBSRC, bundle=True)
    os.environ['WERKZEUG_RUN_MAIN'] = 'true'
    app.run()

run_ctrl()