
import xml.etree.ElementTree as et

# Instance of ElementTree
tree = et.ElementTree()

# Root Element Tag
root = et.Element("root")
f = et.Element("f").text = "&nbsp;"
root.append(f)

# child Element Tag of root
a = et.Element("a")
b = et.Element("b")
# Text to be stored in the a element
a.text = "five"
b.text = "Mira"

# Adds the element tag to root
root.append(a)
root.append(b)

tree._setroot(root)
tree.write("write.xml")
