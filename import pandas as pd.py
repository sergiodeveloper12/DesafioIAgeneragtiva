import pandas as pd
import xml.etree.ElementTree as ET


csv_file = 'C:\Users\5689147\OneDrive - ASSAI Atacadista\Documentos\projeto.csv'
data = pd.read_csv(csv_file)


data['coluna1'] = data['coluna1'].str.strip()
data['coluna2'] = data['coluna2'].str.strip()


root = ET.Element('data')

for index, row in data.iterrows():
    item = ET.SubElement(root, 'item')
    ET.SubElement(item, 'coluna1').text = str(row['coluna1'])
    ET.SubElement(item, 'coluna2').text = str(row['coluna2'])

xml_output = 'C://Users/5689147/Meus%20Documentos//transformed_data.xml'
tree = ET.ElementTree(root)
tree.write(xml_output, encoding='utf-8', xml_declaration=True)







