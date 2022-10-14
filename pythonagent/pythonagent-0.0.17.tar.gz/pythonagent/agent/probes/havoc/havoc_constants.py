import json

HAVOC_TYPES = [
    "InBoundService_Delay",
    "InBoundService_Failure",
    "OutBoundService_Delay",
    "OutBoundService_Failure",
    "MethodCall_Delay",
    "MethodCall_Failure",
    "Custom_Memory_Leak"
]

# EXPIRE_DURATION_MS = 300000  # 5 minutes
# EXPIRE_DURATION_MS = 3000  # 3 seconds
EXPIRE_DURATION_MS = 1000  # 1 seconds


SIZE_OF_OBJECTS_BYTES = 524288000  # 500 MB

# Inbound Service Delay
IB_SERV_DELAY_DICT = {
   "enable": 0,
   "havocType": 1,
   "bTName": "",
   "uRL": "/prod/path/to/resource",
   "methodFQM": "",
   "delayInSec": 10,
   "totalDurationInSec": 20,
   "threshOld": {"count": 0, "percentage": 0, "currentcount": 0},
   "protocol": "",
   "hostname": "",
   "backendName": "",
   "leaksINMB": "",
   "memoryLeaksInSec": ""
}
IB_SERV_DELAY_JSON = json.dumps(IB_SERV_DELAY_DICT)

# Inbound Service Failure
IB_SERV_FAIL_DICT = {
   "enable": 0,
   "havocType": 2,
   "bTName": "",
   "uRL": "/prod/path/to/resource",
   "methodFQM": "",
   "delayInSec": 10,
   "totalDurationInSec": 20,
   "threshOld": {"count": 0, "percentage": 0, "currentcount": 0},
   "protocol": "",
   "hostname": "",
   "backendName": "",
   "leaksINMB": "",
   "memoryLeaksInSec": ""
}
IB_SERV_FAIL_JSON = json.dumps(IB_SERV_FAIL_DICT)

# Outbound Service Delay
OB_SERV_DELAY_DICT = {
   "enable": 0,
   "havocType": 3,
   "bTName": "",
   "uRL": "",
   "methodFQM": "",
   "delayInSec": 10,
   "totalDurationInSec": 20,
   "threshOld": {"count": 0, "percentage": 0, "currentcount": 0},
   "protocol": "",
   "hostname": "sample_hostname",
   "backendName": "",
   "leaksINMB": "",
   "memoryLeaksInSec": ""
}
OB_SERV_DELAY_JSON = json.dumps(OB_SERV_DELAY_DICT)

# Outbound Service Failure
OB_SERV_FAIL_DICT = {
   "enable": 0,
   "havocType": 4,
   "bTName": "",
   "uRL": "",
   "methodFQM": "",
   "delayInSec": 0,
   "totalDurationInSec": 20,
   "threshOld": {"count": 0, "percentage": 0, "currentcount": 0},
   "protocol": "",
   "hostname": "sample_hostname",
   "backendName": "",
   "leaksINMB": "",
   "memoryLeaksInSec": ""
}
OB_SERV_FAIL_JSON = json.dumps(OB_SERV_FAIL_DICT)

# Method Call Delay
METH_CALL_DELAY_DICT = {
   "enable": 0,
   "havocType": 5,
   "bTName": "",
   "uRL": "",
   "methodFQM": "/var/task.lambda_handler",
   "delayInSec": 10,
   "totalDurationInSec": 20,
   "threshOld": {"count": 0, "percentage": 0, "currentcount": 0},
   "protocol": "",
   "hostname": "",
   "backendName": "",
   "leaksINMB": "",
   "memoryLeaksInSec": ""
}
METH_CALL_DELAY_JSON = json.dumps(METH_CALL_DELAY_DICT)

# Method Invocation Failure
METH_INV_FAIL_DICT = {
   "enable": 0,
   "havocType": 6,
   "bTName": "",
   "uRL": "",
   "methodFQM": "/var/task.lambda_handler",
   "delayInSec": "",
   "totalDurationInSec": 20,
   "threshOld": {"count": 0, "percentage": 0, "currentcount": 0},
   "protocol": "",
   "hostname": "",
   "backendName": "",
   "leaksINMB": "",
   "memoryLeaksInSec": ""
}
METH_INV_FAIL_JSON = json.dumps(METH_INV_FAIL_DICT)

# Custom Memory Leak
CUSTOM_MEMORY_LEAK_DICT = {
   "enable": 0,
   "havocType": 7,
   "bTName": "",
   "uRL": "",
   "methodFQM": "/var/task.lambda_handler",
   "delayInSec": "",
   "totalDurationInSec": 20,
   "threshOld": {"count": 0, "percentage": 0, "currentcount": 0},
   "protocol": "",
   "hostname": "",
   "backendName": "",
   "leaksINMB": 500,
   "memoryLeaksInSec": 5
}
CUSTOM_MEMORY_LEAK_JSON = json.dumps(CUSTOM_MEMORY_LEAK_DICT)


HAVOC_PROFILES_JSON = [IB_SERV_DELAY_JSON, IB_SERV_FAIL_JSON,
                       OB_SERV_DELAY_JSON, OB_SERV_FAIL_JSON,
                       METH_CALL_DELAY_JSON, METH_INV_FAIL_JSON,
                       CUSTOM_MEMORY_LEAK_JSON]
