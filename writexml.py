
import xml.etree.ElementTree as et

# Instance of ElementTree
tree = et.ElementTree()

# Root Element Tag
root = et.Element("root")


# child Element Tag of root
a = et.Element("a")
b = et.Element("b")

# Text to be stored in the a element
a.text = "five"
b.text = "Mira"


try:
    # Adds the element tag to root
    root.append(a)
    root.append(b)
except Exception as err:
    print(f"append() argument must be an Element. cause:{err}")

try:
    tree._setroot(root)
    tree.write("write.xml")
except Exception as e:
    print(f"cannot write to xml file. cause:{e}")
