import xml.etree.ElementTree as ET


xml_data = """
<user>
    <first_name>John</first_name>
    <last_name>Doe</last_name>
    <email>john.doe@example.com</email>
</user>
"""

root = ET.fromstring(xml_data )

print(root.find('first_name').text )