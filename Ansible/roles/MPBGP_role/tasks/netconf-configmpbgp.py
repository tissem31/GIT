from ncclient import manager
from jinja2 import Template

m = manager.connect(host='10.10.0.20', port=830, username='admin',
                    password='123', hostkey_verify='False', look_for_keys='False')
                    
# Render our Jinja template
mpbgp_template = Template(open('mpbgp.xml').read())
mpbgp_rendered = mpbgp_template.render(
  ADD_LOOPBACK='10.255.255.12',
  AS='64512',
  INT_LOOPBACK='Loopback0',
  COMMUNITY='extended'

)

# Execute the edit-config RPC
result = m.edit_config(target='running', config=mpbgp_rendered)
print(result)