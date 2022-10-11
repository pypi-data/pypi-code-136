"""Read inserted data from Cassandra based on randomly selected objects from input list.

Usage:
  %s <configFile> <filename> [--table=<table>] [--number=<number>] [--nprocesses=<nprocesses>] [--loglocation=<loglocation>] [--logprefix=<logprefix>]
  %s (-h | --help)
  %s --version

Options:
  -h --help                             Show this screen.
  --version                             Show version.
  --table=<table>                       Table name [default: candidates].
  --number=<number>                     Number of random objects we want to pick from the list [default: 5].
  --nprocesses=<nprocesses>             Number of processes to use by default to get/write the results [default: 1]
  --loglocation=<loglocation>           Log file location [default: /tmp/].
  --logprefix=<logprefix>               Log prefix [default: lcSearch].

"""
import sys
__doc__ = __doc__ % (sys.argv[0], sys.argv[0], sys.argv[0])
from docopt import docopt
from gkutils.commonutils import Struct, readGenericDataFile, cleanOptions, splitList, parallelProcess
import csv
from cassandra.cluster import Cluster
from collections import OrderedDict, defaultdict

from cassandra import ConsistencyLevel
from cassandra.query import dict_factory, SimpleStatement
import random
from datetime import datetime
import os

# OK - so it looks like if you want to test stuff, they all have to be inside the test_ function.

def getLCByObject(options, session, objectList):
    lightcurves = {}
    for row in objectList:
        # Turn off paging by default. Default page size is 5000.
        simple_statement = SimpleStatement("select * from candidates where objectId = %s;", consistency_level=ConsistencyLevel.ONE, fetch_size=None)
        # Can only iterate once through the output data. Store in a list.
        outputData = list(session.execute(simple_statement, (row['objectId'],)))
        lightcurves[row['objectId']] = outputData

#    for k,v in lightcurves.items():
#        print(k, v)
    return lightcurves
            


def worker(num, db, objectListFragment, dateAndTime, firstPass, miscParameters):
    """thread worker function"""
    # Redefine the output to be a log file.
    options = miscParameters[0]

    pid = os.getpid()
    sys.stdout = open('%s%s_%s_%d_%d.log' % (options.loglocation, options.logprefix, dateAndTime, pid, num), "w")
    cluster = Cluster(db['hostname'])
    session = cluster.connect()
    session.row_factory = dict_factory
    session.set_keyspace(db['keyspace'])


    # This is in the worker function
    lightcurves = getLCByObject(options, session, objectListFragment)

    print("Process complete.")
    cluster.shutdown()
    print("Connection Closed - exiting")

    return 0


def test_me():

    # Setup the test - read the test data from the input file. Connect to the database.
    def setup(options):
        inputData = readGenericDataFile(options.filename)
        return inputData

    # Exercise the code - insert the test data
    def run(options, inputData):
        import yaml
        with open(options.configFile) as yaml_file:
            config = yaml.safe_load(yaml_file)

        username = config['cassandra']['local']['username']
        password = config['cassandra']['local']['password']
        keyspace = config['cassandra']['local']['keyspace']
        hostname = config['cassandra']['local']['hostname']

        db = {'username': username,
              'password': password,
              'keyspace': keyspace,
              'hostname': hostname}


        # Get n lightcurves. Consider doing this in parallel for a proper test.
        # As an initial test, run it single threaded.

        # We have the inputData, get a random subset.
        subset = inputData
        if len(inputData) > int(options.number):
            subset = random.sample(inputData, int(options.number))


        if int(options.nprocesses) > 1 and len(subset) > 1:
            # Do it in parallel!
            currentDate = datetime.now().strftime("%Y:%m:%d:%H:%M:%S")
            (year, month, day, hour, min, sec) = currentDate.split(':')
            dateAndTime = "%s%s%s_%s%s%s" % (year, month, day, hour, min, sec)
            nProcessors, listChunks = splitList(subset, bins = int(options.nprocesses), preserveOrder=True)

            print("%s Parallel Processing..." % (datetime.now().strftime("%Y:%m:%d:%H:%M:%S")))
            parallelProcess(db, dateAndTime, nProcessors, listChunks, worker, miscParameters = [options], drainQueues = False)
            print("%s Done Parallel Processing" % (datetime.now().strftime("%Y:%m:%d:%H:%M:%S")))
        else:
            cluster = Cluster(db['hostname'])
            session = cluster.connect()
            session.row_factory = dict_factory
            session.set_keyspace(db['keyspace'])

            lightcurves = getLCByObject(options, session, subset)
#            for k,v in lightcurves.items():
#                print(k, v)

            cluster.shutdown()












#        lightcurves = getLCByObject(options, session, subset)
#        lightcurves = {}
#        for row in subset:
#            # Turn off paging by default. Default page size is 5000.
#            simple_statement = SimpleStatement("select * from candidates where objectId = %s;", consistency_level=ConsistencyLevel.ONE, fetch_size=None)
#            # Can only iterate once through the output data. Store in a list.
#            outputData = list(session.execute(simple_statement, (row['objectId'],)))
#            lightcurves[row['objectId']] = outputData

#        for k,v in lightcurves.items():
#            print(k, v)
            
#        cluster.shutdown()

    # Verify the test - read the test data from the database
#    def verify(options, inputData):
#        db = {'hostname': options.hostname, 'keyspace': options.keyspace}
#        cluster = Cluster(db['hostname'])
#        session = cluster.connect()
#        session.row_factory = dict_factory
#        session.set_keyspace(db['keyspace']) 
#
#        # Turn off paging by default. Default page size is 5000.
#        simple_statement = SimpleStatement("select * from test_noncandidates;", consistency_level=ConsistencyLevel.ONE, fetch_size=None)
#        # Can only iterate once through the output data. Store in a list.
#        outputData = list(session.execute(simple_statement))
#
#        sortedinputData = sorted(inputData, key=lambda d: (d['objectId'], d['jd'])) 
#        sortedoutputData = sorted(outputData, key=lambda d: (d['objectid'], d['jd'])) 
#
#        inputArrayFid = array([int(x['fid']) for x in sortedinputData])
#        outputArrayFid = array([x['fid'] for x in sortedoutputData])
#
#        inputArrayObjectId = array([x['objectId'] for x in sortedinputData])
#        outputArrayObjectId = array([x['objectid'] for x in sortedoutputData])
#
#        inputArrayJd = array([float(x['jd']) for x in sortedinputData])
#        outputArrayJd = array([x['jd'] for x in sortedoutputData])
#
#        inputArrayDiffmaglim = array([float(x['diffmaglim']) for x in sortedinputData])
#        outputArrayDiffmaglim = array([x['diffmaglim'] for x in sortedoutputData])
#
#        assert_array_equal(inputArrayFid, outputArrayFid)
#        assert_array_equal(inputArrayObjectId, outputArrayObjectId)
#        assert_array_almost_equal(inputArrayJd, outputArrayJd)
#        assert_array_almost_equal(inputArrayDiffmaglim, outputArrayDiffmaglim)
#
#        # Yeah, I need to setup the verification. Let's get the thing executing first.
#        # Executes from the command line, but will not execute in pytest.
#
#        cluster.shutdown()


#    # Cleanup - truncate the test table. Disconnect from the database.
#    def cleanup(options):
#        db = {'hostname': options.hostname, 'keyspace': options.keyspace}
#        cluster = Cluster(db['hostname'])
#        session = cluster.connect()
#        session.set_keyspace(db['keyspace']) 
#
#        session.execute("truncate table test_noncandidates;")
#
#        cluster.shutdown()


    opts = docopt(__doc__, version='0.1')
    opts = cleanOptions(opts)
    options = Struct(**opts)

    testData = setup(options)
    run(options, testData)

    #verify(options, testData)
    #cleanup(options)

if __name__ == '__main__':
    test_me()

