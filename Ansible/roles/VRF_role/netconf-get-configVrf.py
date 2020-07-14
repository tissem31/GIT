from ncclient import manager
from jinja2 import Template

m = manager.connect(host='10.10.0.20', port=830, username='admin',
                    password='123', hostkey_verify='False', look_for_keys='False')
                    
# Render our Jinja template
vrf_template = Template(open('vrf.xml').read())
vrf_rendered = vrf_template.render(
  VRF_NAME='B',
  AS_RD='10.254.254.10:1', 
  RD_Exp='10.254.254.20:1',
  RD_Imp='10.254.254.10:1'
)

# Execute the edit-config RPC
result = m.edit_config(target='running', config=vrf_rendered)
print(result)