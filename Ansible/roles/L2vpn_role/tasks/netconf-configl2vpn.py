from ncclient import manager
from jinja2 import Template

m = manager.connect(host='10.10.0.20', port=830, username='admin',
                    password='123', hostkey_verify='False', look_for_keys='False')
                    
# Render our Jinja template
l2vpnE2E_template = Template(open('l2vpn.xml').read())
l2vpnE2E_rendered = l2vpnE2E_template.render(
  INT='3',
  IP_ADD='10.255.255.14',
  VCID='34',
  ENCAPSULATION='mpls',
  PSEUDOWIRE='ETH-to-ETH'

)

# Execute the edit-config RPC
result = m.edit_config(target='running', config=l2vpnE2E_rendered)
print(result)