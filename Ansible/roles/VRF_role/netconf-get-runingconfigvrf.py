# Import the required dependencies
from ncclient import manager

m = manager.connect(host='10.10.0.15', port=830, username='admin',
                    password='123', hostkey_verify='False', look_for_keys='False' )

# Create a configuration filter
vrf_filter = '''
  <filter>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <ip>
          <vrf>
				<VRFName>ONE</VRFName>
          <vrf>
          <ConfigVrf-Configuration></ConfigVrf-Configuration>
      </native>
      <ip>
  </filter>
'''

# Execute the get-config RPC
result = m.get_config('running', vrf_filter)
print(result)