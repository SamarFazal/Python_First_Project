
import xml.dom.minidom
import xml.etree.ElementTree as ET

def main():
    # use the parse() function to load and parse an XML file
    doc = xml.dom.minidom.parse("test.xml");

    # print out the document node and the name of the first child tag
    print (doc.nodeName)
    print (doc.firstChild.tagName)
    # get a list of XML tags from the document and print each one
    channels = doc.getElementsByTagName("channel")
    print (channels)
    for channel in channels:
        links= channel.getElementsByTagName("link")
        for lt in links:
            t=lt.getAttribute("link")
            print(t)
        #print (skill.getAttribute("description"))
        #print (skill.getAttributeNode("description"))

    
    
    '''tree1 = ET.parse("test.xml")
    root = tree1.getroot()
    attributes = root.attrib
    print(attributes)
    print(list(root))
    owner = attributes.get("item")
    print(owner)'''
    


if __name__ == "__main__":
    main();