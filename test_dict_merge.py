import collections
from collections import OrderedDict
from pprint import pprint

def merge_list_by_key(original_list, updated_list, key, ignore_when_null=None):
    ignore_when_null = [] if ignore_when_null is None else ignore_when_null

    if not original_list:
        return updated_list

    items_map = collections.OrderedDict([(i[key], i.copy()) for i in original_list])

    merged_items = collections.OrderedDict()
    
    for item in updated_list:
        item_key = item[key]
        if item_key in items_map:
            for ignored_key in ignore_when_null:
                if ignored_key in item and item[ignored_key] is None:
                    item.pop(ignored_key)
            merged_items[item_key] = items_map[item_key]
            merged_items[item_key].update(item)
        else:
            merged_items[item_key] = item

    return list(merged_items.values())


def dict_merge(rtn_dct, merge_dct):
    for k, v in merge_dct.items():
        if not rtn_dct.get(k):
            rtn_dct[k] = v
        elif isinstance(rtn_dct[k], dict) and isinstance(merge_dct[k], collections.Mapping):
            rtn_dct[k] = dict_merge(rtn_dct[k], merge_dct[k])
        elif isinstance(rtn_dct[k], list) and isinstance(merge_dct[k], list):
			rtn_dct[k] = merge_dct[k]
        else:
            rtn_dct[k] = v
    return rtn_dct



d1 = {
    "type": "ServerProfileV12",
    "uri": "/rest/server-profiles/0e4dd073-5fcc-48ec-85ef-8642e305eb46",
    "name": "temp171",
    "description": "",
    "firmware": {
        "firmwareBaselineUri": "null",
        "manageFirmware": False,
        "forceInstallFirmware": False,
        "firmwareInstallType": "null",
        "firmwareScheduleDateTime": "",
        "firmwareActivationType": "null",
        "reapplyState": "NotApplying",
        "consistencyState": "Unknown"
    },
    "connectionSettings": {
        "reapplyState": "NotApplying",
        "connections": [
            {
                "id": 1,
                "name": "m1",
                "functionType": "FibreChannel",
                "networkUri": "/rest/fc-networks/88af62dd-07cd-41cf-a9f6-2df7fa6896aa",
                "portId": "Mezz 3:1-b",
                "requestedVFs": "null",
                "allocatedVFs": "null",
                "interconnectUri": "/rest/interconnects/69d651e2-23c9-4eda-b5f4-e61c54997d44",
                "macType": "Virtual",
                "wwpnType": "Virtual",
                "mac": "9A:C4:A3:A0:00:0D",
                "wwnn": "10:00:BE:F5:9D:00:00:03",
                "wwpn": "10:00:BE:F5:9D:00:00:02",
                "requestedMbps": "2500",
                "allocatedMbps": 2500,
                "maximumMbps": 20000,
                "ipv4": "null",
                "boot": {
                    "priority": "NotBootable"
                },
                "state": "Deployed",
                "status": "OK",
                "managed": True,
                "networkName": "null",
                "lagName": "null",
                "interconnectPort": 11,
                "isolatedTrunk": False,
                "privateVlanPortType": "None"
            },
            {
                "id": 2,
                "name": "m2",
                "functionType": "FibreChannel",
                "networkUri": "/rest/fc-networks/88af62dd-07cd-41cf-a9f6-2df7fa6896aa",
                "portId": "Mezz 3:1-b",
                "requestedVFs": "null",
                "allocatedVFs": "null",
                "interconnectUri": "/rest/interconnects/69d651e2-23c9-4eda-b5f4-e61c54997d44",
                "macType": "Virtual",
                "wwpnType": "Virtual",
                "mac": "9A:C4:A3:A0:00:0D",
                "wwnn": "10:00:BE:F5:9D:00:00:03",
                "wwpn": "10:00:BE:F5:9D:00:00:02",
                "requestedMbps": "2500",
                "allocatedMbps": 2500,
                "maximumMbps": 20000,
                "ipv4": "null",
                "boot": {
                    "priority": "NotBootable"
                },
                "state": "Deployed",
                "status": "OK",
                "managed": True,
                "networkName": "null",
                "lagName": "null",
                "interconnectPort": 11,
                "isolatedTrunk": False,
                "privateVlanPortType": "None"
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "USB",
            "HardDisk",
            "PXE"
        ]
    },	
    "osDeploymentSettings": {
        "osDeploymentPlanUri": "null",
        "osVolumeUri": "null",
        "forceOsDeployment": False,
        "osCustomAttributes": [],
        "reapplyState": "NotApplying",
        "deployMethod": "null",
        "deploymentPortId": "null",
        "deploymentMac": "null"
    },
    "scopesUri": "/rest/scopes/resources/rest/server-profiles/0e4dd073-5fcc-48ec-85ef-8642e305eb46",
    "serviceManager": "null",
    "eTag": "1592408185956/28",
    "refreshState": "NotRefreshing"
}

d2 = {
    "type": "ServerProfileV12",
    "name": "temp171",
	"newName": "temp_venkat",
    "description": "",
    "affinity": "Bay",
    "firmware": {
        "firmwareBaselineUri": "null",
        "manageFirmware": False,
        "forceInstallFirmware": False,
        "firmwareInstallType": "null",
        "firmwareScheduleDateTime": "",
        "firmwareActivationType": "null",
    },
    "connectionSettings": {
    "connections": [
            {
                "id": 1,
                "name": "m1",
                "functionType": "FibreChannel",
                "networkUri": "/rest/fc-networks/88af62dd-07cd-41cf-a9f6-2df7fa6896aa",
                "portId": "Auto",
                "requestedMbps": "2500"
			}
	    ],
    },
    "boot": {
        "manageBoot": True
    }
}

merged_dict = dict_merge(d1, d2)

#existing_connections = d1['connectionSettings']['connections']
#params_connections = d2['connectionSettings']['connections']
#merged_dict['connectionSettings']['connections'] = merge_list_by_key(existing_connections, params_connections, key='id')

pprint(merged_dict)