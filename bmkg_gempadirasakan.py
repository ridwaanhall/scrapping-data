import requests
from xml.etree import ElementTree

url = "https://data.bmkg.go.id/DataMKG/TEWS/gempadirasakan.xml"
response = requests.get(url)

if response.status_code == 200:
    xml_data = response.content
    root = ElementTree.fromstring(xml_data)

    print("GEMPA DIRASAKAN")
    for i, gempa in enumerate(root.findall("gempa")):
        number = str(i + 1).zfill(2)
        print(f"Gempa {number} :")
        print(f"Tanggal    : {gempa.find('Tanggal').text}")
        print(f"Jam        : {gempa.find('Jam').text}")
        print(f"Coordinate : {gempa.find('./point/coordinates').text}")
        print(f"Kedalaman  : {gempa.find('Kedalaman').text}")
        print(f"Magnitude  : {gempa.find('Magnitude').text}")
        print(f"Wilayah    : {gempa.find('Wilayah').text}")
        print(f"Dirasakan  : {gempa.find('Dirasakan').text}")
        print()
else:
    print("Error fetching data")
