from ncclient import manager
from jinja2 import Template

# Render our Jinja template
interface_template = Template(open('interface.xml').read())
interface_rendered = interface_template.render(
  INTERFACE_INDEX='2', 
  IP_ADDRESS='10.10.0.21', 
  SUBNET_MASK='255.255.255.0'
)

# Execute the edit-config RPC
result = m.edit_config(target='running', config=interface_rendered)
print(result)
