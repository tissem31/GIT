###Redistribute BGP on EIGRP and vice-versa
from ncclient import manager
from jinja2 import Template

m = manager.connect(host='10.10.0.20', port=830, username='admin',
                    password='123', hostkey_verify='False', look_for_keys='False')
                    
# Render our Jinja template
eigrp_template = Template(open('eigrp.xml').read())
eigrp_rendered = eigrp_template.render(
  AS_eigrp='200',
  AS_bgp='64512',
  VRF_NAME_2='TWO',
  BW='1500', Delay='100', RELIABILITY='255', LOAD='1', MTU='1500',
  NET_ADD='10.255.20.0',
  WILD_CARD_MASK='0.0.0.3',

)

# Execute the edit-config RPC
result = m.edit_config(target='running', config=eigrp_rendered)
print(result)