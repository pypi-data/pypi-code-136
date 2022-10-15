# Filename:       | meraki_api_library_v1.py
# Author:         | Marco Caspers
# Version:        | 9.0.0
# Description:
#
# Version 8.0.3, rewrite for Macal.
#
# Version 9.0.0, detached from MacalLibrary class for Macal version 3.5 which supports external libraries.
# Use this file in conjunction with meraki.mcl
#
# Rewrite to remove dependancy on meraki_api_interface.py
#
# Version 9.1.0, Macal 4.0.3 release


import meraki
from meraki.exceptions import APIError
from utilities import *
from datetime import datetime
import time

import macal


Dapi = None
LastErrorMessage = ''

LAST_REQUEST = datetime.now()
EXEC_DELAY = 0.21
DEFAULT_REQUEST_COUNT = 1
API_CALL_THROTTLE_DELAY = 3
API_CALL_THROTTLE_PORT_STATUS_DELAY = 6


def exec_throttle(p_requestcount=DEFAULT_REQUEST_COUNT):
	"""Execution Throttler
		This is used to delay the execution of network requests so that the limit for the total number of requests is not exceded.
		Exceeding the limit of requests per second will result in fatal error, bad request responses by the API."""
	global LAST_REQUEST
	timeElapsed = (datetime.now() - LAST_REQUEST).total_seconds()
	if (timeElapsed < (EXEC_DELAY * p_requestcount)):
		time.sleep(EXEC_DELAY * p_requestcount - timeElapsed)
	LAST_REQUEST = datetime.now()


def FnInitDashboardApi(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""Implementation of FnInitDashboardapi function"""
	global Dapi
	global LastErrorMessage
	macal.ValidateFunctionArguments(func, scope, filename)
	var = scope.GetVariable("api_key")
	api_key = var.GetValue()
	try:
		Dapi = meraki.DashboardAPI(api_key, suppress_logging = True)
		scope.SetReturnValue(True)
		return
	except APIError as error:
		LastErrorMessage = f"{error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Unhandled Exception: {ex}'
	scope.SetReturnValue(False)



def GetApiVersion(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	macal.ValidateFunctionArguments(func, scope, filename)
	if Dapi:
		scope.SetReturnValue(Dapi._session._version)
		return
	scope.SetReturnValue(False)



def GetLastErrorMessage(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""Implementation of GetLastErrorMessage function, just returns the last error message to the scripting engine."""
	global LastErrorMessage
	macal.ValidateFunctionArguments(func, scope, filename)
	scope.SetReturnValue(LastErrorMessage)



def GetOrganizations(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""get_app_Organizations()
		input
			Dapi 		- Dashboard API
		
		The API returns a list of organizations.

        https://developer.cisco.com/meraki/api-v1/#!get-organizations
	"""	
	global LastErrorMessage
	macal.ValidateFunctionArguments(func, scope, filename)
	exec_throttle(API_CALL_THROTTLE_DELAY)
	try:
		result = Dapi.organizations.getOrganizations()
		scope.SetReturnValue(result)
		return
	except APIError as error:
		if "errors" in error.response:
			emsg = ""
			for msg in error.response["errors"]:
				emsg = f"{emsg}\n{msg}"
			LastErrorMessage = emsg
		LastErrorMessage = error.response
	except Exception as ex:
		LastErrorMessage = f"Unhandled exception: {ex}"
	scope.SetReturnValue(False)



def GetOrganization(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""get_app_Organizations()
		input
			Dapi 		- Dashboard API
			org_id      - Organization ID
		
		The API returns the information of the organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization
	"""	
	global LastErrorMessage
	macal.ValidateFunctionArguments(func, scope, filename)
	var = scope.GetVariable("org_id")
	org_id = var.GetValue()
	exec_throttle(API_CALL_THROTTLE_DELAY)
	try:
		result = Dapi.organizations.getOrganization(org_id)
		scope.SetReturnValue(result)
		return
	except APIError as error:
		if "errors" in error.response:
			emsg = ""
			for msg in error.response["errors"]:
				emsg = f"{emsg}\n{msg}"
			LastErrorMessage = emsg
		LastErrorMessage = error.response
	except Exception as ex:
		LastErrorMessage = f"Unhandled exception: {ex}"
	scope.SetReturnValue(False)



def GetInventory(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""get_org_Inventory(Dapi, org_id)
		
		Input:
	   		Dapi   - Dashboard API
	   		org_id - Organization ID

	   	Output:
	   		list of organizations inventory
	   		https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-devices"""
	global Dapi
	global LastErrorMessage
	macal.ValidateFunctionArguments(func, scope, filename)
	var = scope.GetVariable("org_id")
	org_id = var.GetValue()
	exec_throttle(API_CALL_THROTTLE_DELAY)
	try:
		result = Dapi.organizations.getOrganizationInventoryDevices(org_id, total_pages = -1)
		scope.SetReturnValue(result)
		return
	except APIError as error:
		LastErrorMessage = f"{error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Unhandled Exception: {ex}'
	scope.SetReturnValue(False)
	



def GetDevices(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""get_org_Devices(Dapi, org_id)
		
		Input:
	   		Dapi   - Dashboard API
	   		org_id - Organization ID

	   	Output:
	   		list of organizations devices
	   		https://developer.cisco.com/meraki/api-v1/#!get-organization-devices"""
	global Dapi
	global LastErrorMessage
	macal.ValidateFunctionArguments(func, scope, filename)
	var = scope.GetVariable("org_id")
	org_id = var.GetValue()
	exec_throttle(API_CALL_THROTTLE_DELAY)
	try:
		result = Dapi.organizations.getOrganizationDevices(org_id, total_pages = -1)
		scope.SetReturnValue(result)
		return
	except APIError as error:
		LastErrorMessage = f"{error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Unhandled Exception: {ex}'
	scope.SetReturnValue(False)



def GetDevice(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""get_dev_Device(Dapi, serial)
		
		Input:
	   		Dapi      - Dashboard API
	   		serial    - Device serial number

	   	Output:
	   		Get a device from the list of devices.
	   		https://developer.cisco.com/meraki/api-v1/#!get-device"""
	global Dapi
	global LastErrorMessage
	macal.ValidateFunctionArguments(func, scope, filename)
	var = scope.GetVariable("serial")
	serial = var.GetValue()
	exec_throttle(API_CALL_THROTTLE_DELAY)
	try:
		result = Dapi.devices.getDevice(serial)
		scope.SetReturnValue(result)
		return
	except APIError as error:
		LastErrorMessage = f"{error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Unhandled Exception: {ex}'
	scope.SetReturnValue(False)



def GetDevicesStatuses(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""get_org_DevicesStatuses(Dapi, org_id)
		
		Input:
	   		Dapi   - Dashboard API
	   		org_id - Organization ID

	   	Output:
	   		list of statuses of organizations devices
	   		https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-statuses"""
	global Dapi
	global LastErrorMessage
	macal.ValidateFunctionArguments(func, scope, filename)
	var = scope.GetVariable("org_id")
	org_id = var.GetValue()
	exec_throttle(API_CALL_THROTTLE_DELAY)
	try:
		result = Dapi.organizations.getOrganizationDevicesStatuses(org_id, total_pages = -1)
		scope.SetReturnValue(result)
		return
	except APIError as error:
		LastErrorMessage = f"{error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Unhandled Exception: {ex}'
	scope.SetReturnValue(False)
	
def GetDevicesLatency(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""get_org_DevicesUplinksLossAndLatency(Dapi, org_id)
		
		Input:
	   		Dapi   - Dashboard API
	   		org_id - Organization ID

	   	Output:
	   		list of Uplink, packet loss and latency data for organizations devices
	   		https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-uplinks-loss-and-latency"""
	global Dapi
	global LastErrorMessage
	macal.ValidateFunctionArguments(func, scope, filename)
	var = scope.GetVariable("org_id")
	org_id = var.GetValue()
	exec_throttle(API_CALL_THROTTLE_DELAY)
	try:
		result = Dapi.organizations.getOrganizationDevicesUplinksLossAndLatency(org_id, total_pages = -1)
		scope.SetReturnValue(result)
		return
	except APIError as error:
		LastErrorMessage = f"{error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Unhandled Exception: {ex}'
	scope.SetReturnValue(False)


def GetDevicesLatencyEx(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""get_org_DevicesUplinksLossAndLatency(Dapi, org_id)
		
		Input:
	   		Dapi   - Dashboard API
	   		org_id - Organization ID

	   	Output:
	   		list of Uplink, packet loss and latency data for organizations devices
	   		This is the enhanced version that calculates the averages this is to reduce the clunk in the macal script.
	   		https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-uplinks-loss-and-latency"""
	global Dapi
	global LastErrorMessage
	macal.ValidateFunctionArguments(func, scope, filename)
	var = scope.GetVariable("org_id")
	org_id = var.GetValue()	
	exec_throttle(API_CALL_THROTTLE_DELAY)
	#try:
	result = Dapi.organizations.getOrganizationDevicesUplinksLossAndLatency(org_id, total_pages = -1)
	#{'networkId': 'N_645140646620848439', 'serial': 'Q2JN-94W8-MN69', 'uplink': 'wan2', 'ip': '8.8.8.8', 'timeSeries': [{'ts': '2022-09-05T13:10:37Z', 'lossPercent': 0.0, 'latencyMs': 3.1}, {'ts': '2022-09-05T13:11:37Z', 'lossPercent': 0.0, 'latencyMs': 3.0}, {'ts': '2022-09-05T13:12:36Z', 'lossPercent': 0.0, 'latencyMs': 2.9}, {'ts': '2022-09-05T13:13:37Z', 'lossPercent': 0.0, 'latencyMs': 3.1}, {'ts': '2022-09-05T13:14:37Z', 'lossPercent': 0.0, 'latencyMs': 3.2}]}
	ret = []
	for item in result:
		rec = {}
		rec['networkId'] = item['networkId']
		rec['serial'] = item['serial']
		rec['uplink'] = item['uplink']
		rec['ip'] = item['ip']
		rec['lossPercent'] = 0.0
		rec['latencyMs'] = 0.0
		rec['timeSeries'] = item['timeSeries']
		countLoss    = len(item['timeSeries'])
		countLatency = len(item['timeSeries'])
		for ts in item['timeSeries']:
			if ts['lossPercent'] is None:
				countLoss -= 1
			else:
				rec['lossPercent'] += ts['lossPercent']
			if ts['latencyMs'] is None:
				countLatency -= 1
			else:
				rec['latencyMs'] += ts['latencyMs']
		if countLoss > 0:
			rec['lossPercent'] = rec['lossPercent'] / countLoss
		if countLatency > 0:
			rec['latencyMs'] = rec['latencyMs'] / countLatency
		ret.append(rec)
	scope.SetReturnValue(ret)
	return
	#except APIError as error:
	#	LastErrorMessage = f"{error.operation}: {error.status}, {error.message}, {error.reason}"
	#except Exception as ex:
	#	LastErrorMessage = f'Unhandled Exception: {ex}'
	scope.SetReturnValue(False)



def GetDeviceManagementInterface(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""
		get_devices_managementInterface(Dapi, serial)

		Input:
			Dapi   - Dashboard API
	   		serial - Serial number of the device.

		Output:
			Return the management interface settings for a device
			https://developer.cisco.com/meraki/api-v1/#!get-device-management-interface

	"""
	global Dapi
	global LastErrorMessage
	macal.ValidateFunctionArguments(func, scope, filename)
	var = scope.GetVariable("serial")
	serial = var.GetValue()
	exec_throttle(API_CALL_THROTTLE_DELAY)
	try:
		result = Dapi.devices.getDeviceManagementInterface(serial)
		scope.SetReturnValue(result)
		return
	except APIError as error:
		LastErrorMessage = f"{error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Unhandled Exception: {ex}'
	scope.SetReturnValue(False)



def GetConfigTemplates(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""get_org_ConfigTemplates(Dapi, org_id)
		
		Input:
	   		Dapi   - Dashboard API
	   		org_id - Organization ID

	   	Output:
	   		list of configuration templates of this organization
	   		https://developer.cisco.com/meraki/api-v1/#!get-organization-config-templates"""
	global Dapi
	global LastErrorMessage
	macal.ValidateFunctionArguments(func, scope, filename)
	var = scope.GetVariable("org_id")
	org_id = var.GetValue()
	exec_throttle(API_CALL_THROTTLE_DELAY)
	try:
		result = Dapi.organizations.getOrganizationConfigTemplates(org_id)
		scope.SetReturnValue(result)
		return
	except APIError as error:
		LastErrorMessage = f"{error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Unhandled Exception: {ex}'
	scope.SetReturnValue(False)



def GetNetworks(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""get_org_Networks(Dapi, org_id)
		Input:
	   		Dapi   - Dashboard API
	   		org_id - Organization ID

	   	Output:
	   		list of networks in the organization
	   		https://developer.cisco.com/meraki/api-v1/#!get-organization-networks"""
	global Dapi
	global LastErrorMessage
	macal.ValidateFunctionArguments(func, scope, filename)
	var = scope.GetVariable("org_id")
	org_id = var.GetValue()
	exec_throttle(API_CALL_THROTTLE_DELAY)
	try:
		result = Dapi.organizations.getOrganizationNetworks(org_id)
		scope.SetReturnValue(result)
		return
	except APIError as error:
		LastErrorMessage = f"{error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Unhandled Exception: {ex}'
	scope.SetReturnValue(False)



def GetNetwork(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""get_org_Network(Dapi, network_id)
		Input:
	   		Dapi   - Dashboard API
	   		network_id - Network ID

	   	Output:
	   		Get a single network
	   		https://developer.cisco.com/meraki/api-v1/#!get-network"""
	global Dapi
	global LastErrorMessage
	macal.ValidateFunctionArguments(func, scope, filename)
	var = scope.GetVariable("network_id")
	network_id = var.GetValue()
	exec_throttle(API_CALL_THROTTLE_DELAY)
	try:
		result = Dapi.networks.getNetwork(network_id)
		scope.SetReturnValue(result)
		return
	except APIError as error:
		LastErrorMessage = f"{error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Unhandled Exception: {ex}'
	scope.SetReturnValue(False)



def GetApplianceUplinkStatuses(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""get_app_UplinkStatuses(Dapi, org_id)
		Input:
	   		Dapi   - Dashboard API
	   		org_id - Organization ID
		Output:
		List the uplink status of every Meraki MX and Z series appliances in the organization
        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-uplink-statuses"""
	global Dapi
	global LastErrorMessage
	macal.ValidateFunctionArguments(func, scope, filename)
	var = scope.GetVariable("org_id")
	org_id = var.GetValue()
	exec_throttle(API_CALL_THROTTLE_DELAY)
	try:
		result = Dapi.appliance.getOrganizationApplianceUplinkStatuses(org_id, total_pages = -1)
		scope.SetReturnValue(result)
		return
	except APIError as error:
		LastErrorMessage = f"{error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Unhandled Exception: {ex}'
	scope.SetReturnValue(False)



def GetLicenseOverview(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""get_org_LicensesOverview(Dapi, org_id)
		
		Input:
	   		Dapi       - Dashboard API
	   		org_id     - Organization ID

		Output:
			LicensesOverview for the organization.
			https://developer.cisco.com/meraki/api-v1/#!get-organization-licenses-overview"""
	global Dapi
	global LastErrorMessage
	macal.ValidateFunctionArguments(func, scope, filename)
	var = scope.GetVariable("org_id")
	org_id = var.GetValue()
	exec_throttle(API_CALL_THROTTLE_DELAY)
	try:
		result = Dapi.organizations.getOrganizationLicensesOverview(org_id)
		scope.SetReturnValue(result)
		return
	except APIError as error:
		LastErrorMessage = f"{error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Unhandled Exception: {ex}'
	scope.SetReturnValue(False)



def GetAppPerformance(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""get_app_Performance(Dapi, serial)
		Input:
	   		Dapi   - Dashboard API
	   		serial - Device Serial Number
		Output:
		Return the performance score for a single device. Only primary MX devices supported. If no data is available, a 204 error code is returned.
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-performance"""
	global Dapi
	global LastErrorMessage
	macal.ValidateFunctionArguments(func, scope, filename)
	var = scope.GetVariable("serial")
	serial = var.GetValue()
	exec_throttle(API_CALL_THROTTLE_DELAY)
	try:
		result = Dapi.appliance.getDeviceAppliancePerformance(serial)
		scope.SetReturnValue(result)
		return
	except APIError as error:
		if error.status == 400:
			LastErrorMessage = f'{error.operation}: {error.status}, {serial} {error.message["errors"][0]}'
		elif error.status != 404:
			LastErrorMessage = f"{error.operation}: {error.status}, {error.message}, {error.reason}"
		LastErrorMessage = f"Unknown error for {serial}: {error.status}, {error.response}"
	except Exception as ex:
		LastErrorMessage = f'Unhandled Exception: {ex}'
	scope.SetReturnValue(False)



def GetNetworkTraffic(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""get_app_NetworkTraffic(Dapi, network_id, T_timepsan=7200)
		
		Input:
	   		Dapi       - Dashboard API
	   		network_id - Network ID
	   		timespan   - Timespan in which to measure data, default 2 hours.

		Output:
			The traffic analysis data for this network.
            https://documentation.meraki.com/MR/Monitoring_and_Reporting/Hostname_Visibility
            ->Traffic Analysis with Hostname Visibility must be enabled on the network.
	        https://developer.cisco.com/meraki/api-v1/#!get-network-traffic"""
	global Dapi
	global LastErrorMessage
	macal.ValidateFunctionArguments(func, scope, filename)
	vni = scope.GetVariable("networkId")
	network_id = vni.GetValue()
	vts = scope.GetVariable("timespan")
	T_timespan = vts.GetValue()
	print("@ This function is obsolete please use get_app_NetworkApplianceUplinkUsageHistory")
	exec_throttle(API_CALL_THROTTLE_DELAY)
	result = None
	try:
		result = Dapi.networks.getNetworkTraffic(network_id, timespan = T_timespan)
		scope.SetReturnValue(result)
		return
	except APIError as error:
		if error.status == 400:
			if "errors" in error.message:
				if (len(error.message["errors"]) > 0):
					if (error.message["errors"][0] == ERROR_TRAFFIC_AND_VISIBILITY):
						LastErrorMessage = f"{ERROR_TRAFFIC_AND_VISIBILITY} (NetworkID: {network_id}"
			else:
				LastErrorMessage = f"{error.operation}: {error.status}, {error.message}, {error.reason}"
		elif error.status == 404:
			LastErrorMessage = ERROR_NOT_FOUND_TRAFFIC.format(network_id)
		else:
			LastErrorMessage = f"{error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Unhandled Exception: {ex}'
	scope.SetReturnValue(False)



def GetNetworkEvents(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""get_net_NetworkEvents()
		input:
			Dapi 		 - Dashboard API
			network_id   - Network ID
			product_Type - Product Type of the appliance
							  Valid types are wireless, appliance, switch, systemsManager, camera, and cellularGateway

			start_After  - The date/time from where to start collecting the data
							use -1 if you want to list all the events, regardless of the start date/time

		output:
			Gets a list of all network events that happened after the given date/time, for the specified product type, on the given network_id.
			https://developer.cisco.com/meraki/api-v1/#!get-network-events"""
	global Dapi
	global LastErrorMessage
	macal.ValidateFunctionArguments(func, scope, filename)
	vni = scope.GetVariable("networkId")
	network_id = vni.GetValue()
	vpt = scope.GetVariable("product_Type")
	product_Type = vpt.GetValue()
	vsa = scope.GetVariable("start_After")
	start_After = vsa.GetValue()
	exec_throttle(API_CALL_THROTTLE_DELAY)
	try:
		if (start_After == -1):
			result = Dapi.networks.getNetworkEvents(network_id, productType = product_Type, total_pages = 10)
		else:
			result = Dapi.networks.getNetworkEvents(network_id, productType = product_Type, startingAfter = start_After)
		scope.SetReturnValue(result)
		return
	except APIError as error:
		LastErrorMessage = f"{error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Unhandled Exception: {ex}'
	scope.SetReturnValue(False)



def GetOrgSecurityEvents(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""get_app_OrganizationSecurityEvents()
		input
			Dapi 		- Dashboard API
			org_id 		- Organization ID
			time_span 	- Timespan over which to collect the data.
							Default is 5 minutes (300 seconds),
							Use -1 to list all data.
		
		List the security events for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-security-events
	"""
	global Dapi
	global LastErrorMessage
	macal.ValidateFunctionArguments(func, scope, filename)
	var = scope.GetVariable("org_id")
	org_id = var.GetValue()
	vts = scope.GetVariable("time_span")
	time_span = vts.GetValue()
	exec_throttle(API_CALL_THROTTLE_DELAY)
	try:
		if (time_span == -1):
			result = Dapi.appliance.getOrganizationApplianceSecurityEvents(org_id, total_pages = -1)
		else:
			result = Dapi.appliance.getOrganizationApplianceSecurityEvents(org_id, timespan = time_span)
		scope.SetReturnValue(result)
		return
	except APIError as error:
		LastErrorMessage = f"{error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Unhandled Exception: {ex}'
	scope.SetReturnValue(False)



def GetSwitchPortStatuses(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""get_switch_DeviceSwitchPortsStatuses(Dapi, org_id)
		
		Input:
	   		Dapi     - Dashboard API
	   		serial   - Serial of the device
	   		timespan - timespan in seconds (300 = 5m default.)

	   	Output:
	   		list of statuses for ports for a specific switch.
	   		https://developer.cisco.com/meraki/api-v1/#!get-device-switch-ports-statuses"""
	global Dapi
	global LastErrorMessage
	macal.ValidateFunctionArguments(func, scope, filename)
	var = scope.GetVariable("serial")
	serial = var.GetValue()
	vts = scope.GetVariable("time_span")
	time_span = vts.GetValue()
	exec_throttle(API_CALL_THROTTLE_PORT_STATUS_DELAY)
	try:
		result = Dapi.switch.getDeviceSwitchPortsStatuses(serial=serial, timespan = time_span)
		scope.SetReturnValue(result)
		return
	except APIError as error:
		LastErrorMessage = f"{error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Unhandled Exception: {ex}'
	scope.SetReturnValue(False)



def GetSwitchPortStatusT0(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""get_switch_DeviceSwitchPortsStatuses(Dapi, org_id)
		
		Input:
	   		Dapi     - Dashboard API
	   		serial   - Serial of the device
	   		t0 - The beginning of the timespan for the data. The maximum lookback period is 31 days from today.

	   	Output:
	   		list of statuses for ports for a specific switch.
	   		https://developer.cisco.com/meraki/api-v1/#!get-device-switch-ports-statuses"""
	global Dapi
	global LastErrorMessage
	macal.ValidateFunctionArguments(func, scope, filename)
	var = scope.GetVariable("serial")
	serial = var.GetValue()
	vt0 = scope.GetVariable("t0")
	t0 = vt0.GetValue()
	exec_throttle(API_CALL_THROTTLE_DELAY)
	try:
		result = Dapi.switch.getDeviceSwitchPortsStatuses(serial=serial, t0=t0)
		scope.SetReturnValue(result)
		return
	except APIError as error:
		LastErrorMessage = f"{error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Unhandled Exception: {ex}'
	scope.SetReturnValue(False)



def GetApplianceUplinkUsageHistory(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""
		getNetworkApplianceUplinksUsageHistory.

		by default timespan   is 10 minutes.
		by default resolution is 1 minute.

		so by default a query returns 10 results per interface.

		The dimension is bytes.

		https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-uplinks-usage-history
	"""
	global Dapi
	global LastErrorMessage
	macal.ValidateFunctionArguments(func, scope, filename)
	var = scope.GetVariable("networkId")
	network_id = var.GetValue()
	exec_throttle(API_CALL_THROTTLE_DELAY)
	try:
		upl = Dapi.appliance.getNetworkApplianceUplinksUsageHistory(network_id)
		nr = upl[0]['byInterface']
		for i, pt in enumerate(upl):
			if i > 0:
				inf = pt['byInterface']
				for f, intf in enumerate(inf):
					if nr[f]["sent"] is None:
						nr[f]["sent"] = 0
					if nr[f]["received"] is None:
						nr[f]["received"] = 0
					if intf is not None:
						if intf["sent"] is not None:
							nr[f]['sent'] += intf["sent"]
						if intf["received"] is not None:
							nr[f]['received'] += intf["received"]
		# Recalculate to bytes per second.
		for f in nr:
			f["sent"] = f["sent"] / 600
			f["received"] = f["received"] / 600
		scope.SetReturnValue(nr)
		return
	except APIError as error:
		LastErrorMessage = f"{error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Unhandled Exception: {ex}'
	scope.SetReturnValue(False)



def GetApplianceTrafficShapingUplinkBandwidth(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""
    		**Returns the uplink bandwidth settings for your MX network.**
    		https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-uplink-bandwidth
    		- networkId (string): (required)
    """
	global Dapi
	global LastErrorMessage
	macal.ValidateFunctionArguments(func, scope, filename)
	var = scope.GetVariable("networkId")
	network_id = var.GetValue()
	exec_throttle(API_CALL_THROTTLE_DELAY)
	try:
		result = Dapi.appliance.getNetworkApplianceTrafficShapingUplinkBandwidth(network_id)
		scope.SetReturnValue(result)
		return
	except APIError as error:
		LastErrorMessage = f"{error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Unhandled Exception: {ex}'
	scope.SetReturnValue(False)



def GetWirelessStatus(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""https://developer.cisco.com/meraki/api/#!get-network-device-wireless-status"""
	global Dapi
	global LastErrorMessage
	macal.ValidateFunctionArguments(func, scope, filename)
	var = scope.GetVariable("serial")
	serial = var.GetValue()
	exec_throttle(API_CALL_THROTTLE_DELAY)
	try:
		result = Dapi.wireless.getDeviceWirelessStatus(serial)
		scope.SetReturnValue(result)
		return
	except APIError as error:
		LastErrorMessage = f"{error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Unhandled Exception: {ex}'
	scope.SetReturnValue(False)



def Output(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""Implementation of Output function. output => (params args)"""
	macal.ValidateFunctionArguments(func, scope, filename)
	params = params[0].get_value()
	if len(params) != 2:
		raise Exception(f"Output requires 2 arguments got ({len(params)}).")
	v = params[1].get_value()
	if (v is not None and v != '' and v != {} and v != [] and v != macal.NIL):
		print(params[0].get_value())
		print(v)



def OutputOnCondition(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""Implementation of OutputOnCondition function"""
	macal.ValidateFunctionArguments(func, scope, filename)
	params = params[0].get_value()
	if params[0].get_value() is False: return
	if len(params) != 3:
		raise Exception(f"OutputOnCondition requires 3 arguments got ({len(params)}).")
	params = params[1:]
	v = params[1].get_value()
	if (v is not None and v != '' and v != {} and v != [] and v != macal.NIL):
		print(params[0].get_value())
		print(v)



def Header(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""Implementation of Header function"""
	macal.ValidateFunctionArguments(func, scope, filename)
	print("<<<mrk_srv_devices>>>")
	params = params[0].get_value()
	v = params[1].get_value()
	if (params[0].get_value() == True):
		print(f"[{v}_demo]")
	else:
		print(f"[{v}]")
	model = params[2].get_value()
	serial = params[3].get_value()
	template = params[4].get_value()
	if model is None or model == macal.NIL: model = ""
	if serial is None or serial == macal.NIL: serial = ""
	if template is None or template == macal.NIL: template = ""
	print(f"{model} - {serial} - {template}")



def ProductInfo(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""Implementation of Header function"""
	macal.ValidateFunctionArguments(func, scope, filename)
	print("<<<mrk_dev_product_info>>>")
	params = params[0].get_value()
	model = params[0].get_value()
	serial = params[1].get_value()
	template = params[2].get_value()
	if model is None or model == macal.NIL: model = ""
	if serial is None or serial == macal.NIL: serial = ""
	if template is None or template == macal.NIL: template = ""
	print(f"{model} - {serial} - {template}")



def DeviceHeader(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""Implementation of DeviceHeader function"""
	macal.ValidateFunctionArguments(func, scope, filename)
	params = params[0].get_value()
	v = params[1].get_value()
	if params[0].get_value() == True:
		print(f"<<<<{v}_demo>>>>")
	else:
		print(f"<<<<{v}>>>>")



def ReadFilters(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""Implementation of DeviceHeader function"""
	macal.ValidateFunctionArguments(func, scope, filename)
	var = scope.GetVariable("customer")
	customer = var.GetValue()
	if not customer:
		return None
	# Valid types are wireless, appliance, switch, systemsManager, camera, and cellularGateway
	filters = {}
	filters_base = customer["network_event_filters"][0]
	filename  = getframeinfo(currentframe()).filename   # get the filename/path where this script is located.
	filepath  = dirname(filename)			        # get the path of this file.

	if "switch" in filters_base:
		filename =  f"""{filepath}{filters_base["switch"]}"""
		filters["switch"] = loadJson(filename)
	if "wireless" in filters_base:
		filename =  f"""{filepath}{filters_base["wireless"]}"""
		filters["wireless"] = loadJson(filename)
	if "appliance" in filters_base:
		filename =  f"""{filepath}{filters_base["appliance"]}"""
		filters["appliance"] = loadJson(filename)
	if "systemsManager" in filters_base:
		filename =  f"""{filepath}{filters_base["systemsManager"]}"""
		filters["systemsManager"] = loadJson(filename)
	if "camera" in filters_base:
		filename =  f"""{filepath}{filters_base["camera"]}"""
		filters["camera"] = loadJson(filename)
	if "cellularGateway" in filters_base:
		filename =  f"""{filepath}{filters_base["cellularGateway"]}"""
		filters["cellularGateway"] = loadJson(filename)
	scope.SetReturnValue(filters)



def FlattenRecord(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""Implementation of FlattenRecord function"""
	macal.ValidateFunctionArguments(func, scope, filename)
	var = scope.GetVariable("rec")
	rec = var.GetValue()
	result = ""
	for (key, value) in rec.items():
		result = "{},'{}','{}'".format(result, key, value)
	result = result[1:]
	scope.SetReturnValue(result)



def FlattenTuple(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""Implementation of FlattenTuple function"""
	macal.ValidateFunctionArguments(func, scope, filename)
	var = scope.GetVariable("tup")
	tup = var.GetValue()
	result = []
	for item in tup:
		if isinstance(item, str):
			result.append(f"'{item}'")
		else:
			result.append(item)
	scope.SetReturnValue(result)


def GetSensorReadingsHistory(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
	"""https://developer.cisco.com/meraki/api-v1/#!get-organization-sensor-readings-history"""
	global Dapi
	global LastErrorMessage
	macal.ValidateFunctionArguments(func, scope, filename)
	var = scope.GetVariable("org_id")
	org_id = var.GetValue()
	exec_throttle(API_CALL_THROTTLE_DELAY)
	try:
		result = Dapi.sensor.getOrganizationSensorReadingsHistory(org_id)
		scope.SetReturnValue(result)
		return
	except APIError as error:
		LastErrorMessage = f"{error.operation}: {error.status}, {error.message}, {error.reason}"
	except Exception as ex:
		LastErrorMessage = f'Unhandled Exception: {ex}'
	scope.SetReturnValue(False)
