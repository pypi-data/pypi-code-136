import json
import os
import time

from .authentication import refreshToken
from .config import Config
from .httputils import flow360ApiPost, flow360ApiGet, flow360ApiDelete
from .s3utils import S3TransferType
from .errorHandling import deprecated 
from .validation import validateJSON

auth = Config.auth
keys = Config.user

@refreshToken
def AddMeshWithJson(name, mesh_json, tags, fmat, endianness, solver_version=None):
    return AddMeshBase(name, mesh_json, tags, fmat, endianness, solver_version)


@refreshToken
def AddMesh(name, noSlipWalls, tags, fmat, endianness, solver_version=None):
    return AddMeshBase(name, {
        "boundaries":
            {
                "noSlipWalls": noSlipWalls
            }
    }, tags, fmat, endianness, solver_version)

def AddMeshBase(name, meshParams, tags, fmat, endianness, solver_version):
    '''
       AddMesh(name, noSlipWalls, tags, fmat, endianness, version)
       returns the raw HTTP response
       {
           'meshId' : 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
           'addTime' : '2019:01:01:01:01:01.000000'
       }
       The returned meshId is need to subsequently call UploadMesh
       Example:
           resp = AddMesh('foo', [1], [], 'aflr3', 'big')
           UploadMesh(resp['meshId'], 'mesh.lb8.ugrid')
       '''

    body = {
        "meshName": name,
        "meshTags": tags,
        "meshFormat": fmat,
        "meshEndianness": endianness,
        "meshParams": json.dumps(meshParams)
    }

    if solver_version:
        body['solverVersion'] = solver_version

    resp = flow360ApiPost("volumemeshes", data=body)
    return resp

def validateVolumeMeshJSON(config, solverVersion=None):
        return validateJSON('volumemesh', config, solverVersion=solverVersion)

@refreshToken
def GenerateMeshFromSurface(name, config, surfaceMeshId, tags, solver_version,
        validate):
    if validate:
        validateVolumeMeshJSON(json.dumps(config), solver_version)
    body = {
        "name": name,
        "tags": tags,
        "surfaceMeshId": surfaceMeshId,
        "config": json.dumps(config),
        "format": 'cgns'
    }

    if solver_version:
        body['solverVersion'] = solver_version

    resp = flow360ApiPost("volumemeshes", data=body)
    return resp


@refreshToken
def DeleteMesh(meshId):
    resp = flow360ApiDelete(f"volumemeshes/{meshId}")
    return resp


@refreshToken
def GetMeshInfo(meshId):
    url = f"volumemeshes/{meshId}"
    resp = flow360ApiGet(url)
    meshParams = None 
    try:
        meshParams = json.loads(resp['meshParams'])
    except Exception as e:
        print('invalid meshParams or not exist:' + str(resp['meshParams']))
        pass
    resp['meshParams'] = meshParams
    return resp

@refreshToken
def CompleteVolumeMeshUpload(meshInfo, fileName):
    url = f"volumemeshes/{meshInfo['id']}/completeUpload?fileName={fileName}"
    resp = flow360ApiPost(url, meshInfo)
    return resp


@refreshToken
def ListMeshes(include_deleted=False):
    resp = flow360ApiGet("volumemeshes")
    if not include_deleted:
        resp = list(filter(lambda i: i['meshStatus'] != 'deleted', resp))
    return resp


@refreshToken
def UploadMesh(meshId, meshFile):
    '''
    UploadMesh(meshId, meshFile)
    '''

    meshInfo = GetMeshInfo(meshId)
    print(meshInfo)
    compression = ''
    if meshFile.endswith('.gz'):
        compression += 'gz'
    elif meshFile.endswith('.bz2'):
        compression += 'bz2'

    fileName = GetMeshFileName(meshInfo['meshName'], meshInfo['meshFormat'],
                               meshInfo['meshEndianness'], compression)

    S3TransferType.VolumeMesh.upload_file(meshId, fileName, meshFile)

    CompleteVolumeMeshUpload(meshInfo, fileName)

def DownloadVolumeFile(id, src, target):
    S3TransferType.VolumeMesh.download_file(id, src, target)

@refreshToken
@deprecated("DownloadMeshGenerationConfigJson()")
def DownloadMeshConfigJson(id, fileName=None):
    if fileName is None:
        fileName = 'config.json'
    DownloadVolumeFile(id, 'config.json', fileName)

@refreshToken
def DownloadMeshGenerationConfigJson(id, fileName=None):
    if fileName is None:
        fileName = 'volumeMeshGenerationConfig.json'
    DownloadVolumeFile(id, 'config.json', fileName)

def DownloadMeshProc(meshId, fileName=None):
    logFileName = 'logs/flow360_volume_mesh.user.log'
    if fileName is None:
        fileName = os.path.basename(logFileName)
    DownloadVolumeFile(meshId, src=logFileName, target=fileName)

def DownloadMeshingLogs(id, fileName=None):
    DownloadMeshProc(id, fileName)

def GetMeshFileName(meshName, meshFormat, endianness, compression):
    if meshFormat == 'aflr3':
        if endianness == 'big':
            name = 'mesh.b8.ugrid'
        elif endianness == 'little':
            name = 'mesh.lb8.ugrid'
        else:
            raise RuntimeError("unknown endianness: {}".format(endianness))
    else:
        name = meshName
        if not name.endswith('.' + meshFormat):
            name += '.' + meshFormat

    if compression is not None and len(compression) > 0:
        name += '.' + compression
    return name

def DownloadVolumeMesh(id, target=None, targetDir=None):
    meshInfo = GetMeshInfo(id)
    src = GetMeshFileName(meshInfo['meshName'], meshInfo['meshFormat'],
                               meshInfo['meshEndianness'], meshInfo['meshCompression'])
    if target is None:
        meshName = os.path.basename(src)
        if targetDir is None:
            target = os.path.join(os.getcwd(), meshName)
        else:
            target = os.path.join(targetDir, meshName)

    DownloadVolumeFile(id, src, target)

def WaitOnMesh(meshId, timeout=86400, sleepSeconds=10):
    startTime = time.time()
    while time.time() - startTime < timeout:
        try:
            info = GetMeshInfo(meshId)
            if info['meshStatus'] in ['deleted', 'error', 'preerror', 'unknownError', 'processed']:
                return info['meshStatus']
        except Exception as e:
            print('Warning : {0}'.format(str(e)))

        time.sleep(sleepSeconds)


def getFileCompression(name):
    if name.endswith("tar.gz"):
        return 'tar.gz'
    elif name.endswith(".gz"):
        return 'gz'
    elif name.endswith("bz2"):
        return 'bz2'
    else:
        return None

