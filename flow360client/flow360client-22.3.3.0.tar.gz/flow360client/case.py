import collections
import json
import os
import time

from botocore.exceptions import ClientError
from requests import HTTPError

from . import mesh
from .authentication import refreshToken
from .casehelper import updateTotalForceHeaderToV2, updateSurfForceHeaderToV2, validateSurfaceNames
from .config import Config
from .httputils import flow360ApiPost, flow360ApiDelete, flow360ApiGet
from .s3utils import S3TransferType
from .validation import validateJSON

auth = Config.auth
keys = Config.user

def validateCaseJSON(config, meshId, solverVersion):
    return validateJSON('case', config, meshId=meshId, solverVersion=solverVersion)

@refreshToken
def SubmitCase(name, tags, meshId, priority, config, parentId,
        validate, **kwargs):
    if validate:
        solverVersion = mesh.GetMeshInfo(meshId)['solverVersion']
        validateCaseJSON(config, meshId, solverVersion)
    body = {
        "name": name,
        "tags": tags,
        "meshId": meshId,
        "priority": priority,
        "runtimeParams": config,
        "parentId": parentId
    }
    for key, value in kwargs.items():
        body[key] = value

    url = f'volumemeshes/{meshId}/case'

    resp = flow360ApiPost(url, data=body)
    return resp


@refreshToken
def DeleteCase(caseId):
    url = f'case/{caseId}'
    resp = flow360ApiDelete(url)
    return resp


@refreshToken
def GetCaseInfo(caseId):
    url = f'case/{caseId}'

    resp = flow360ApiGet(url)
    runtime = flow360ApiGet(f'case/{caseId}/runtimeParams')
    runtimeContent = None
    try:
        runtimeContent = json.loads(runtime['content'])
    except Exception as e:
        print('invalid runtimeParams or not exist:' + runtime['content'])
        return None

    resp['runtimeParams'] = runtimeContent
    return resp


@refreshToken
def ListCases(name=None, status=None, meshId=None, include_deleted=False):
    if meshId is None:
        url = "cases"
    else:
        url = f'volumemeshes/{meshId}/cases'

    resp = flow360ApiGet(url)
    if not include_deleted:
        resp = list(filter(lambda i: i['caseStatus'] != 'deleted', resp))
    return resp


@refreshToken
def GetCaseResidual(caseId):
    try:
        resp = flow360ApiGet(f'case/{caseId}/result/nonlinear_residual_v2')
        return resp
    except HTTPError as e:
        resp = flow360ApiGet(f'case/{caseId}/result/nonlinear_residual')
        return resp
    except:
        raise RuntimeError('Error in getting case residual.')


@refreshToken
def GetCaseTotalForces(caseId):
    try:
        resp = flow360ApiGet(f'case/{caseId}/result/total_forces_v2')
        return resp
    except HTTPError as e:
        resp = flow360ApiGet(f'case/{caseId}/result/total_forces')
        resp = updateTotalForceHeaderToV2(caseId, resp)
        return resp
    except:
        raise RuntimeError('Error in getting case total force.')


@refreshToken
def GetCaseLinearResidual(caseId):
    try:
        resp = flow360ApiGet(f'case/{caseId}/result/linear_residual_v2')
        return resp
    except:
        raise HTTPError('There is no linear residual available')


# refreshToken
def GetCaseMinMaxState(caseId):
    try:
        resp = flow360ApiGet(f'case/{caseId}/result/minmax_state_v2')
        return resp
    except:
        raise HTTPError('There is no minmax state available')


# refreshToken
def GetCaseCFL(caseId):
    try:
        resp = flow360ApiGet(f'case/{caseId}/result/cfl_v2')
        return resp
    except:
        raise HTTPError('There is no minmax state available')


@refreshToken
# caseId: case uuid to retrieve case
# surfaces: the list of surface names, if None, forces on all surfaces will be returned
def GetCaseSurfaceForcesByNames(caseId, targetSurfNames=None):
    caseInfo = GetCaseInfo(caseId)
    meshInfo = mesh.GetMeshInfo(caseInfo['caseMeshId'])
    caseBnds = caseInfo['runtimeParams']['boundaries']
    orderedPatchNames = meshInfo['boundaries']

    validateSurfaceNames(caseBnds, targetSurfNames)
    resp = dict()
    try:
        resp = flow360ApiGet(f'case/{caseId}/result/surface_forces_v2')
    except HTTPError as e:
        resp = flow360ApiGet(f'case/{caseId}/result/surface_forces')
        resp = updateSurfForceHeaderToV2(caseBnds, orderedPatchNames, resp)
    except:
        raise RuntimeError('Error in getting case surface force.')

    stepKeys = []
    forceKeys = []
    surfaceNamesCsv = []
    surfaceForces = collections.defaultdict(dict)
    for key in resp.keys():
        if key in ['steps', 'physical_step', 'pseudo_step']:
            stepKeys.append(key)
        else:
            dividerIndex = key.rfind('_')
            forceKeys.append(key[dividerIndex + 1:])
            surfaceNamesCsv.append(key[:dividerIndex])

    for surfName in surfaceNamesCsv:
        if targetSurfNames != None and surfName not in targetSurfNames:
            continue
        for key in stepKeys:
            surfaceForces[surfName][key] = resp[key]
        for key in forceKeys:
            surfaceForces[surfName][key] = resp[surfName + '_' + key]
    return surfaceForces


# input: caseId: case uuid to retrieve case
# input: surfComboDict: dict "surfComboName" -> {"surfaces":[<list of boundary patch names or ids>]}
# output: {"nameSpecifier1":{"steps":[],"CL":[],...}, "nameSpecifier2":{"steps":[],"CL":[],...}}
@refreshToken
def GetCaseSummationOfSurfacesForces(caseId, surfComboDict):
    forcesCombo = dict()
    for surfaceCombo, component in surfComboDict.items():
        forcesCombo[surfaceCombo] = dict()
        forcesOnPatches = GetCaseSurfaceForcesByNames(caseId, component["surfaces"])

        forceTable = forcesOnPatches[list(forcesOnPatches.keys())[0]]
        for forceType, forceData in forceTable.items():
            if forceType in ["steps", "physical_step", "pseudo_step"]:
                forcesCombo[surfaceCombo][forceType] = forceData
            else:
                forcesCombo[surfaceCombo][forceType] = [0.0] * len(forceData)

        for patchName, forceTable in forcesOnPatches.items():
            for forceType, forceData in forceTable.items():
                if forceType not in ["steps", "physical_step", "pseudo_step"]:
                    for i in range(len(forceData)):
                        forcesCombo[surfaceCombo][forceType][i] += forceData[i]
    return forcesCombo


@refreshToken
# input: caseId: case uuid to retrieve case
# input: surfComboList: list of dict [{"surfaceName":"surfCombo1","surfaceIds":[1,3,5]},{},...]. The surfaceIds are 1-based (for .ugrid).
def GetCaseSurfaceForces(caseId, surfComboList):
    surfComboDict = dict()
    for surfCombo in surfComboList:
        surfIdsStr = [str(surfId) for surfId in surfCombo['surfaceIds']]
        surfComboDict[surfCombo['surfaceName']] = {"surfaces": surfIdsStr}
    forcesCombo = GetCaseSummationOfSurfacesForces(caseId, surfComboDict)
    return forcesCombo

@refreshToken
def DownloadFile(caseId, src, target=None):
    # default: target  = cwd/src's name
    if target is None:
        target = os.path.basename(src)
    if src is None:
        raise RuntimeError('src fileName must not be None!')
    try:
        S3TransferType.Case.download_file(caseId, src, target)
    except ClientError as e:
        if src.endswith('.csv'):
            S3TransferType.Case.download_file(caseId, \
                    src.replace(".csv", "_v2.csv"), target)
        else:
            raise RuntimeError('Error in download file {:s}'.format(src))

@refreshToken
def DownloadResultsFile(caseId, src, target=None):
    DownloadFile(caseId, src='results/'+src, target=target)

@refreshToken
def DownloadVolumetricResults(caseId, fileName=None):
    volumeFileName = "volumes.tar.gz"
    if fileName is None:
        fileName = volumeFileName
    if fileName[-7:] != '.tar.gz':
        raise RuntimeError('fileName must have extension .tar.gz!')
    DownloadResultsFile(caseId, src=volumeFileName, target=fileName)

@refreshToken
def DownloadSurfaceResults(caseId, fileName=None):
    surfaceFileName = "surfaces.tar.gz"
    if fileName is None:
        fileName = surfaceFileName
    if fileName is not None and fileName[-7:] != '.tar.gz':
        raise RuntimeError('fileName must have extension .tar.gz!')
    DownloadResultsFile(caseId, src=surfaceFileName, target=fileName)

@refreshToken
def DownloadSolverOut(caseId, fileName=None):
    logFileName = 'flow360_case.user.log'
    if fileName is None:
        fileName = logFileName
    DownloadFile(caseId, src='logs/'+logFileName, target=fileName)

def WaitOnCase(caseId, timeout=86400, sleepSeconds=10):
    startTime = time.time()
    while time.time() - startTime < timeout:
        try:
            info = GetCaseInfo(caseId)
            if info['caseStatus'] in ['deleted', 'error', 'preerror', 'unknownError', 'diverged', 'completed']:
                return info['caseStatus']
        except Exception as e:
            print('Warning : {0}'.format(str(e)))

        time.sleep(sleepSeconds)
