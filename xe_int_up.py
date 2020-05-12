import requests
import sys
import json
HOST = 'ios-xe-mgmt-latest.cisco.com'
# HOST = 'ios-xe-mgmt.cisco.com'
PORT = 9443
USER = 'developer'
# USER = 'root'
PASS = 'C1sco12345'
# PASS = 'D_Vay!_10&'


requests.packages.urllib3.disable_warnings()

def main():
    # payload = '{"ietf-interfaces:interface": {"name": "GigabitEthernet2", "description": "Configured by RESTCONF", "type": "iana-if-type:ethernetCsmacd", "enabled": false}}'
    payload = '{"ietf-interfaces:interface": {"name": "GigabitEthernet2", "description": "Configured by RESTCONF", "type": "iana-if-type:ethernetCsmacd", "enabled": true}}'
    url = "https://{h}:{p}/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet2".format(h=HOST, p=PORT)
    headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json'
    }
    response = requests.put(url, auth=(USER, PASS),headers=headers, verify=False, data = payload)
                
    print(response.text)

    url = "https://{h}:{p}/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet2".format(h=HOST, p=PORT)
    headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json'
    }
    response = requests.get(url, auth=(USER, PASS),headers=headers, verify=False, data = payload)

    # print (response.json())
    jsonResponse = response.json()
    for key, value in jsonResponse.items():
        print(f'Interface Name: {jsonResponse["ietf-interfaces:interface"]["name"]}')
        print(f'Interface Description: {jsonResponse["ietf-interfaces:interface"]["description"]}')
        print(f'Interface Status: {jsonResponse["ietf-interfaces:interface"]["enabled"]}')
    
    

if __name__ == '__main__':
    sys.exit(main())