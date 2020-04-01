import lxml.etree as ET

dom = ET.parse("INR_20190512_5183.xml")
xslt = ET.parse("fromINR.xslt")
transform = ET.XSLT(xslt)
newdom = transform(dom)

output = ET.tostring(newdom, pretty_print=True)
print output
open("result.xml", 'wb').write(output)
