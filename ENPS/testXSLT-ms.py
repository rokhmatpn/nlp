
def process_with_msxslt(xsltfname, xmlfname, targetfname):
    import win32com.client.dynamic
    xslt = win32com.client.dynamic.Dispatch("Msxml2.DOMDocument.4.0")
    xslt.async = 0
    xslt.load(xsltfname)
    xml = win32com.client.dynamic.Dispatch("Msxml2.DOMDocument.4.0")
    xml.async = 0
    xml.load(xmlfname)
    output = xml.transformNode(xslt)
    open(targetfname, 'wb').write(output)
	
process_with_msxslt("C:\Users\rokhmat.pn\Documents\TFS-2018\Integrated%20Newsroom%20Management%20System\scripts\ENPS\fromINR.xslt", "INR_20190512_5183.xml", "result.xml")
