import json
import os
import time

from .authentication import refreshToken
from .config import Config
from .httputils import FileDoesNotExist
from .httputils import flow360ApiPost, flow360ApiGet, flow360ApiDelete
from .s3utils import S3TransferType
from .validation import validateJSON

auth = Config.auth
keys = Config.user

def validateSurfaceMeshJSON(config, solverVersion=None):
        return validateJSON('surfacemesh', config, solverVersion=solverVersion)

@refreshToken
def AddSurfaceMesh(name, tags, solver_version, format):
    body = {
        "name": name,
        "tags": tags,
        "format": format
    }

    if solver_version:
        body['solverVersion'] = solver_version

    resp = flow360ApiPost("surfacemeshes", data=body)
    return resp

@refreshToken
def GenerateSurfaceMeshFromGeometry(name, config, tags, solver_version, 
        validate):
    if validate:
        validateSurfaceMeshJSON(json.dumps(config), solver_version)
    body = {
        "name": name,
        "tags": tags,
        "config": json.dumps(config),
    }

    if solver_version:
        body['solverVersion'] = solver_version

    resp = flow360ApiPost("surfacemeshes", data=body)
    return resp


@refreshToken
def DeleteSurfaceMesh(surfaceMeshId):
    resp = flow360ApiDelete(f"surfacemeshes/{surfaceMeshId}")
    return resp


@refreshToken
def GetSurfaceMeshInfo(surfaceMeshId):
    url = f"surfacemeshes/{surfaceMeshId}"
    resp = flow360ApiGet(url)
    return resp


@refreshToken
def CompleteSurfaceMeshUpload(meshId, fileName):
    url = f"surfacemeshes/{meshId}/completeUpload?fileName={fileName}"
    resp = flow360ApiPost(url)
    return resp


@refreshToken
def ListSurfaceMeshes(include_deleted=False):
    resp = flow360ApiGet("surfacemeshes")
    if not include_deleted:
        resp = list(filter(lambda i: i['status'] != 'deleted', resp))
    return resp


@refreshToken
def UploadGeometry(surfaceMeshId, geoFile):
    '''
    Upload for files other than surface mesh
    '''

    if not os.path.exists(geoFile):
        print('mesh file {0} does not Exist!'.format(geoFile))
        raise FileDoesNotExist(geoFile)

    fileName = 'geometry.csm'
    S3TransferType.SurfaceMesh.upload_file(surfaceMeshId, fileName, geoFile)
    CompleteSurfaceMeshUpload(surfaceMeshId, fileName)


@refreshToken
def UploadSurfaceMesh(surfaceMeshId, meshFile):
    '''
    Upload surface mesh
    '''

    def getMeshName(meshFile, meshFormat):

        name = "surfaceMesh." + meshFormat

        if meshFile.endswith('.gz'):
            name += '.gz'
        elif meshFile.endswith('.bz2'):
            name += '.bz2'
        return name

    meshInfo = GetSurfaceMeshInfo(surfaceMeshId)
    print(meshInfo)
    fileName = getMeshName(meshFile, meshInfo['format'])

    if not os.path.exists(meshFile):
        print('mesh file {0} does not Exist!'.format(meshFile))
        raise FileDoesNotExist(meshFile)

    S3TransferType.SurfaceMesh.upload_file(surfaceMeshId, fileName, meshFile)
    CompleteSurfaceMeshUpload(meshInfo['id'], fileName)


def DownloadSurfaceFile(id, filename):
    S3TransferType.SurfaceMesh.download_file(id, filename, os.path.join(id, filename))


def DownloadLogs(id):
    DownloadSurfaceFile(id, 'logs/flow360_surface_mesh.user.log')


def WaitOnMesh(meshId, timeout=86400, sleepSeconds=10):
    startTime = time.time()
    while time.time() - startTime < timeout:
        try:
            info = GetSurfaceMeshInfo(meshId)
            if info['status'] in ['deleted', 'error', 'preerror', 'unknownError', 'processed']:
                return info['meshStatus']
        except Exception as e:
            print('Warning : {0}'.format(str(e)))

        time.sleep(sleepSeconds)

