import xml.etree.ElementTree as ET

# Created an instance Element Tree
tree = ET.ElementTree()

# Parenting root element
root = ET.Element('data')

# Creating child elements of the root element
items = ET.SubElement(root, 'items')
item1 = ET.SubElement(items, 'item')
item2 = ET.SubElement(items, 'item')

# setting attributes for the child elements
item1.set('name','item1')
item2.set('name','item2')

# assigning texts to each child element tag
item1.text = 'item1abc'
item2.text = 'item2abc'

# _setroot() func collects an ElementTree type
# and sets it as the root parent in the XML file
tree._setroot(root)

# write() first param collects the name of the file 
# the second param decides the file's output encoding type
tree.write("write.xml", "Windows 1252")
