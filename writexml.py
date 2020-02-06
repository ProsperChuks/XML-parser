import xml.etree.ElementTree as ET

tree = ET.ElementTree()
data = ET.Element('data')
items = ET.SubElement(data, 'items')
item1 = ET.SubElement(items, 'item')
item2 = ET.SubElement(items, 'item')
item1.set('name','item1')
item2.set('name','item2')
item1.text = 'item1abc'
item2.text = 'item2abc'

mydata = ET.tostring(data)
tree._setroot(data)
tree.write("write.xml", "Windows 1252")
