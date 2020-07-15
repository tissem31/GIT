###Redistribute BGP on OSPF and vice-versa
from ncclient import manager
from jinja2 import Template

m = manager.connect(host='10.10.0.20', port=830, username='admin',
                    password='123', hostkey_verify='False', look_for_keys='False')
                    
# Render our Jinja template
ospf_template = Template(open('ospf.xml').read())
ospf_rendered = ospf_template.render(
  NET_ADD='10.255.10.0', 
  WILD_CARD_MASK='0.0.0.3', 
  AREA_NUMBER='10',
  AS='64512',
  VRF_NAME_1='ONE',
  PROCESS_ID='2',

)

# Execute the edit-config RPC
result = m.edit_config(target='running', config=ospf_rendered)
print(result)

