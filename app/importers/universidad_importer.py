import xml.etree.ElementTree as ET

def parse_universidades(xml_path: str):
    tree = ET.parse(xml_path, parser=ET.XMLParser(encoding="windows-1252"))
    root = tree.getroot()
    return [{
        "id": int(elem.find("universidad").text),
        "nombre": elem.find("nombre").text.strip()
    } for elem in root.findall("_expxml")]

#Archivo "Universidades_importer.py" eliminado porque no cumplía con DRY. El código era el mismo que éste. 