'''
IOS XRv 9000 host	     SSH port	NETCONF port	XR bash port	gRPC port	username	password
sandbox-iosxr-1.cisco.com	22	         830	       57722	       57777	  admin	    C1sco12345
'''
from ncclient import manager

with manager.connect(
host="sandbox-iosxr-1.cisco.com", 
port="830",
timeout=30,
username="admin", 
password="C1sco12345", 
hostkey_verify=False,
look_for_keys=False,
allow_agent=False) as iosx:
    for cape in iosx.server_capabilities:
        print(cape)

    
