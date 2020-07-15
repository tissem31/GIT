# Import the required dependencies
from ncclient import manager

m = manager.connect(host='10.10.0.15', port=830, username='admin',
                    password='123', hostkey_verify='False', look_for_keys='False')

# Create a configuration filter
ospf_filter = '''
  <filter>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
          <router>
	       <ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf"></ospf>
          </router>
      </native>
  </filter>
'''

# Execute the get-config RPC
result = m.get_config('running', ospf_filter)
print(result)