#using ELement Tree
from xml.etree import ElementTree as ET

#passing in the name of the xml file as a parameter
xmlfile = ET.parse("file.xml")
root = xmlfile.getroot()

# looping through the xml file
for child in root:
    print(child.tag, child.attrib)

# getting a text from a tag
# fname - specifies the name of the xml tag
print(root.find('fname').text)

# tag method to print out tag names
# attrib method to print out attribute names and properties
