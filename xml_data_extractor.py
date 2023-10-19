import xml.etree.ElementTree as ET

# NOTE: Insert the path of your XML file in the variable 'path'
path = ""

tree = ET.parse('your_xml_file.xml')  # Replace 'your_xml_file.xml' with your XML file path
root = tree.getroot()