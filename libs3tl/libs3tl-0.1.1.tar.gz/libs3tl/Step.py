from datetime import datetime
import inspect
import json
import redis
from jproperties import Properties
import pandas as pd
import logging
import time
import os
import sys
import traceback
import requests


class Step:

    # initializing with defaults
    def __init__(self):
        self.setStartTime()
        self.step = "St"
        self.paramsFile = 'Step.properties'
        self.logger = 'logStep'
        self.logFile = self.getRelativeFile( os.getcwd() +'\../logs/Step.log')

    # Needed for relative paths
    def getRelativeFile(self, filename):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, filename)
        return filename

    # Tasks to be done at the start of the script
    def startup(self):
        self.setTaskID()
        self.setUUID()
        self.params = self.loadParams(self.paramsFile)
        self.nextstep = self.params["nextstep"].data
        self.setTaskExecutionID()
        self.startRedisConn()
        self.setLogger(self.logger, self.logFile, logging.INFO)
        self.consensusID = self.taskID
        self.consensusExecutionID = self.taskExecutionID
        if ("consensusID" in self.params):
            self.consensusID = self.params["consensusID"].data
            self.consensusExecutionID = self.consensusID + "_" + self.startTime

    # setter for Start Time
    def setStartTime(self):
        now = datetime.utcnow()
        self.startTime = now.strftime("%Y%m%d%H%M%S")

    # setter for task Execution ID
    def setTaskExecutionID(self):
        self.taskExecutionID = self.taskID + "_" + self.startTime

    # Create  Redis connection
    def startRedisConn(self):
        self.rC = self.makeRedisConn()

    # Load parameters from file
    def loadParams(self, filename):
        configs = Properties()
        filename = self.getRelativeFile(os.getcwd() + '\../params/' + filename)
        with open(filename, 'rb') as config_file:
            configs.load(config_file)
            config_file.close()
        return configs

    # declaring Redis connection parameters
    def makeRedisConn(self):
        try:
            connection = redis.StrictRedis(host=self.params["redisHost"].data,
                                           port=self.params["redisPort"].data,
                                           password=self.params["redisPassword"].data,
                                           decode_responses=True)
            response = connection.ping()
            return connection
        except (redis.exceptions.ConnectionError, ConnectionRefusedError):
            self.getLogger().error(self.logMessageFormat(self.step, inspect.stack()[0][3], 'Error in redis connection setup'))

    # Extracting UUID from path of current working directory
    def setUUID(self):
        path = os.getcwd().replace("\\", "/").split("/")
        self.taskUUID = path[-2]

    # Reading taskID from text file
    def setTaskID(self):
        with open(self.getRelativeFile( os.getcwd() +'\../params/Identifier.txt')) as f:
            lines = f.readlines()
        self.taskID = "BATCH_MULTISOURCE_AAPL"
        f.close()

    # Storing the datahandoff in a dataframe and the converting  DF to json and printing it
    # def handOff(self, rC, taskID, step, datatohandoff):
    def handOff(self, step, datatohandoff):
        df = pd.DataFrame(eval(datatohandoff))
        self.rC.publish(self.taskID + "_" + step, df.to_json())

    # setter function to configure Logger
    def setLogger(self, logger_name, log_file, level=logging.INFO):
        self.mylogger = logging.getLogger(logger_name)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fileHandler = logging.FileHandler(log_file, mode='a')
        fileHandler.setFormatter(formatter)
        self.mylogger.setLevel(level)
        self.mylogger.addHandler(fileHandler)
        logging.Formatter.datefmt = '%Y-%m-%d %H:%M:%S'
        logging.Formatter.converter = time.gmtime

    # getter function to get logger
    def getLogger(self):
        return self.mylogger

    def logMessageFormat(self, fileName, method, message):
        try:
            if message == None or fileName == None or method == None:
                logdata = ' : ' + 'None'
                return logdata
            else:
                logdata = ' : ' + self.taskExecutionID + ' : ' + fileName + ' : ' + method + ' : ' + message
                return logdata
        except:
            print('logMessageFormat')
            return 'None except'

    def exceptionTraceback(self):
        try:
            # Get current system exception
            ex_traceback = sys.exc_info()
            # Extract unformatter stack traces as tuples
            # trace_back = traceback.extract_tb(ex_traceback)
            # Format stacktrace
            stack_trace = ''
            # stack_trace = list()
            # print(trace_back)
            # for trace in trace_back:
            #     stack_trace.append("File : %s , Line : %d, Message : %s" % (trace[0], trace[1], trace[3]))
            return str(str(ex_traceback) + ' ' + str(stack_trace))
        except Exception as error:
            print('#######exceptionTraceback#### ' + str(error))

    def connectToAPIForKey(self, url, headers, successResponse, key):
        try:
            response = self.createAndGetResponseFromURL(url, headers, successResponse)
            if response == None:
                return None
            responseData = json.loads(response.text)
            if key in responseData:
                return responseData[key]
            else:
                self.getLogger().error(self.logMessageFormat(self.step, inspect.stack()[0][3], 'Key not found' + key))
                print('Key not found' + key)
                return None
        except(BaseException) as e:
            self.getLogger().error(self.logMessageFormat(self.step, inspect.stack()[0][3], str(e)))
            print(self.exceptionTraceback())
            return None

    def createAndGetResponseFromURL(self, url, headers, successResponse):
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == successResponse:
                return response
            else:
                self.getLogger().error(self.logMessageFormat(self.step, inspect.stack()[0][3],
                                                             'response.status_code from createAndGetResponseFromURL ' + str(
                                                                 response.status_code)))
                return None
        except(BaseException) as e:
            self.getLogger().error(self.logMessageFormat(self.step, inspect.stack()[0][3], str(e)))
            print(self.exceptionTraceback())
            return None
