
from os import pipe
from intersight_auth import get_api_client

api_key_id = "5bbbec5137636d38744f9c4a/5eb193587564612d301e8b5f/6065e3347564612d32a83bd5"
api_key_file = "./intersight-key.key"

api_client = get_api_client(api_key_id, api_key_file)


print ("Connected Devices")
print ("=================")
from intersight.api import asset_api
calling_api = asset_api.AssetApi(api_client)
kwargs = dict(filter="ConnectionStatus eq 'Connected'")
# Get all device registration objects that are in connected state
api_result= calling_api.get_asset_device_registration_list(**kwargs)
for a_result in api_result.results:
    print(a_result.device_ip_address[0])

drop = input("\n Please press Enter to continue ")

print ("\n\nVirtual Machines")
print ("=================")
from intersight.api import virtualization_api
calling_api = virtualization_api.VirtualizationApi(api_client)
kwargs = dict(filter="")  #power_state eq 'PoweredOff'
# Get all device registration objects that are in connected state
api_result = calling_api.get_virtualization_vmware_virtual_machine_list(**kwargs, orderby="Name")
for a_result in api_result.results:
    print(a_result["name"])

