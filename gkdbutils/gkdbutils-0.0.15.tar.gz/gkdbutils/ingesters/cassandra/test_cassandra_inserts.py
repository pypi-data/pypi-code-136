from gkutils.commonutils import readGenericDataFile

from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster
from cassandra.query import dict_factory
from cassandra.query import SimpleStatement

from ingestGenericDatabaseTable import executeLoad
from numpy import array
from numpy.testing import assert_array_almost_equal
from numpy.testing import assert_array_equal


# OK - so it looks like if you want to test stuff, they all have to be inside the test_ function.

def test_me():
    class EmptyClass:
        pass

    # Setup the test - read the test data from the input file. Connect to the database.
    def setup(options):
        inputData = readGenericDataFile(options.filename, delimiter = options.delimiter)
        return inputData

    # Exercise the code - insert the test data
    def run(options, inputData):
        db = {'hostname': options.hostname, 'keyspace': options.keyspace}
        cluster = Cluster(db['hostname'])
        session = cluster.connect()
        session.set_keyspace(db['keyspace']) 

        executeLoad(session, options.table, inputData, types = options.types.split(','))

        cluster.shutdown()

    # Verify the test - read the test data from the database
    def verify(options, inputData):
        db = {'hostname': options.hostname, 'keyspace': options.keyspace}
        cluster = Cluster(db['hostname'])
        session = cluster.connect()
        session.row_factory = dict_factory
        session.set_keyspace(db['keyspace']) 

        # Turn off paging by default. Default page size is 5000.
        simple_statement = SimpleStatement("select * from test_noncandidates;", consistency_level=ConsistencyLevel.ONE, fetch_size=None)
        # Can only iterate once through the output data. Store in a list.
        outputData = list(session.execute(simple_statement))

        sortedinputData = sorted(inputData, key=lambda d: (d['objectId'], d['jd'])) 
        sortedoutputData = sorted(outputData, key=lambda d: (d['objectid'], d['jd'])) 

        inputArrayFid = array([int(x['fid']) for x in sortedinputData])
        outputArrayFid = array([x['fid'] for x in sortedoutputData])

        inputArrayObjectId = array([x['objectId'] for x in sortedinputData])
        outputArrayObjectId = array([x['objectid'] for x in sortedoutputData])

        inputArrayJd = array([float(x['jd']) for x in sortedinputData])
        outputArrayJd = array([x['jd'] for x in sortedoutputData])

        inputArrayDiffmaglim = array([float(x['diffmaglim']) for x in sortedinputData])
        outputArrayDiffmaglim = array([x['diffmaglim'] for x in sortedoutputData])

        assert_array_equal(inputArrayFid, outputArrayFid)
        assert_array_equal(inputArrayObjectId, outputArrayObjectId)
        assert_array_almost_equal(inputArrayJd, outputArrayJd)
        assert_array_almost_equal(inputArrayDiffmaglim, outputArrayDiffmaglim)

        # Yeah, I need to setup the verification. Let's get the thing executing first.
        # Executes from the command line, but will not execute in pytest.

        cluster.shutdown()


    # Cleanup - truncate the test table. Disconnect from the database.
    def cleanup(options):
        db = {'hostname': options.hostname, 'keyspace': options.keyspace}
        cluster = Cluster(db['hostname'])
        session = cluster.connect()
        session.set_keyspace(db['keyspace']) 

        session.execute("truncate table test_noncandidates;")

        cluster.shutdown()



    options = EmptyClass()
    options.hostname = ['localhost']
    options.keyspace = 'test01'
    #options.filename = '/Users/kws/lasair/cassandra/load-old-data/noncandidates/test_100_rows.csv'
    options.filename = '/Users/kws/lasair/cassandra/load-old-data/noncandidates/test_10000_rows.csv'
    options.table = 'test_noncandidates'
    options.delimiter = ','
    # The test is reading a CSV file with no schema types. So add the types.
    options.types = 'str,float,float,int,int,float,float,float,int'

    testData = setup(options)
    run(options, testData)
    verify(options, testData)
    cleanup(options)

if __name__ == '__main__':
    test_me()

