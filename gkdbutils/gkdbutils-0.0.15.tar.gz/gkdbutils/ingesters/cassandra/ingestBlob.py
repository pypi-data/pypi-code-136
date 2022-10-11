"""Insert binary data (blob) into Cassandra.

Usage:
  %s <configFile> <inputFiles>... [--table=<table>] [--types=<types>] [--blobcolumn=<blobcolumn>]
  %s (-h | --help)
  %s --version

Options:
  -h --help                  Show this screen.
  --version                  Show version.
  --table=<table>            Target table name.
  --types=<types>            Python column types in the same order as the column headers.
  --blobcolumn=<blobcolumn>  Blob column.

"""
import sys
__doc__ = __doc__ % (sys.argv[0], sys.argv[0], sys.argv[0])
from docopt import docopt
from gkutils.commonutils import Struct, readGenericDataFile, cleanOptions, splitList
import csv
from cassandra.cluster import Cluster
from collections import OrderedDict

def nullValue(value, nullValue = '\\N'):
   returnValue = nullValue

   if value and value.strip():
      returnValue = value.strip()

   return returnValue

def nullValueNULL(value):
   returnValue = None

   if value and not isinstance(value, int) and value.strip() and value != 'NULL':
      returnValue = value.strip()

   return returnValue

def boolToInteger(value):
    returnValue = value
    if value == 'true':
        returnValue = 1
    if value == 'false':
        returnValue = 0
    return returnValue

  
def getFileBlob(filename):

    blobData = None
    with open(filename, 'rb') as fp:
        blobData = bytearray(fp.read())

    return blobData

# row is a dict
def executeLoad(options, session, data, bundlesize = 1):

    rowsUpdated = 0

    if len(data) == 0:
        return rowsUpdated

    if options.types is None:
        return rowsUpdated

    types = options.types.split(',')

    keys = list(data[0].keys())


    if len(keys) != len(types):
        print("Keys & Types mismatch")
        return rowsUpdated

    typesDict = OrderedDict()

    i = 0
    for k in keys:
        typesDict[k] = types[i]
        i += 1

    if options.blobcolumn is not None and options.blobcolumn in keys:
        keys.append(options.blobcolumn + 'image')

    print(keys)
    print(types)

    formatSpecifier = ','.join(['%s' for i in keys])

    chunks = int(1.0 * len(data) / bundlesize + 0.5)
    if chunks == 0:
        subList = [data]
    else:
        bins, subList = splitList(data, bins = chunks, preserveOrder = True)


    for dataChunk in subList:
        try:
            sql = "insert into %s " % options.table
            # Force all keys to be lowercase and devoid of hyphens
            sql += "(%s)" % ','.join(['%s' % k.lower().replace('-','') for k in keys])

            sql += " values "
            sql += ',\n'.join(['('+formatSpecifier+')' for x in range(len(dataChunk))])
            sql += ';'

            values = []
            for row in dataChunk:

                if options.blobcolumn is not None and options.blobcolumn in keys:
                    try:
                        blobData = getFileBlob(row[options.blobcolumn])
                        row[options.blobcolumn + 'image'] = blobData
                    except KeyError as e:
                        pass

                for key in keys:
                    print(key)
                    if key == options.blobcolumn + 'image':
                        print("PUKE")
                        value = row[key]
                        values.append(value)
                    else:
                        value = nullValueNULL(boolToInteger(row[key]))
                        if value is not None:
                            value = eval(typesDict[key])(value)
                        values.append(value)

            print(sql)
            session.execute(sql, tuple(values))


        except Exception as e:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(e).__name__, e.args)
            print(message)
            #print "Error %d: %s" % (e.args[0], e.args[1])

    return



def ingestData(options, inputFiles):

    #if not options.skiphtm:
    #    generateHtmNameBulk = which('generate_htmname_bulk')
    #    if generateHtmNameBulk is None:
    #        sys.stderr.write("Can't find the generate_htmname_bulk executable, so cannot continue.\n")
    #        exit(1)

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

    cluster = Cluster(db['hostname'])
    session = cluster.connect()
    session.set_keyspace(db['keyspace']) 

    for file in inputFiles:
        data = readGenericDataFile(file, delimiter=',')
        executeLoad(options, session, data)

    cluster.shutdown()

def main(argv = None):
    opts = docopt(__doc__, version='0.1')
    opts = cleanOptions(opts)

    # Use utils.Struct to convert the dict into an object for compatibility with old optparse code.
    options = Struct(**opts)

    # Could pass the inputFiles as part of the options struct, but this gives us the ability to
    # split the files into chunks if necessary for multiprocessing.

    ingestData(options, options.inputFiles)

if __name__ == '__main__':
    main()
