#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 11:53:27 2020

@author: dsw46
"""

#Import libraries for csv_to_udm
import pandas as pd
import xml.etree.ElementTree  as ET
from lxml.builder import ElementMaker # lxml only !
from lxml import etree
import datetime
E = ElementMaker()

#Additional libraries for validation
#https://emredjan.github.io/blog/2017/04/08/validating-xml/
from lxml import etree
from io import StringIO

def csv_to_udm(csv_file, prop_names, udm_file):
    '''
    This script will convert a CSV file to an XML UDM file. It takes 3 inputs:
    - csv_file:   The csv file name/path
    - prop_names: A list of names of the headers in your csv which you would like included in the xml file
    - udm_file:   The name of the destination file
    
    It assumes that the csv already contains a column for MW (molecular weight), 
    MF (molecular formula), NAME, and CAS columns in the CSV
    '''

    df = pd.read_csv(csv_file)

    #The first line of the header is supposed to be:
    #header = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
    #However I have to remove the encoding info to make it run

    #I also added "maxOccurs="unbounded" to the property type in the schema

    header = '''<?xml version="1.0" standalone="no"?>
<UDM DATABASE="SPRESI" SEQUENCE="1" TIMESTAMP="{}">
  <UDM_VERSION MAJOR="6" MINOR="0" REVISION="0" VERSIONTEXT="6.0.0"/>
  <MOLECULES>
'''

    #Create a timestamp
    ts = datetime.datetime.now().timestamp()
    timestamp = datetime.datetime.fromtimestamp(ts).isoformat()

    footer = '''  </MOLECULES>
  <REACTIONS>
    <REACTION ID="1">
    </REACTION>
  </REACTIONS>
</UDM>
    '''

    mol_id = 1
    with open(udm_file, 'w') as f:
        f.write(header.format(timestamp))
        for idx, row in df.iterrows():
            f.write('    <MOLECULE ID="{}">\n'.format(mol_id))
            f.write('      <MW>{}</MW>\n'.format(row.MW))
            for name in prop_names:
                f.write('      <PROPERTY name="{}">{}</PROPERTY>\n'.format(name, row[name]))
            f.write('      <MF>{}</MF>\n'.format(row.MF))
            f.write('      <NAME>{}</NAME>\n'.format(row.NAME))
            f.write('      <CAS>{}</CAS>\n'.format(row.CAS))
            f.write('    </MOLECULE>\n')
            mol_id += 1
        f.write(footer)
        
def prediction_udm_file(CAS_number, udm_file):
    '''
    This script will create a UDM file with the CAS number and SMILES string of the prediction:
    - CAS: The CAS number (a string)
    - udm_file:   The name of the destination file
    '''

    #The first line of the header is supposed to be:
    #header = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
    #However I have to remove the encoding info to make it run

    #I also added "maxOccurs="unbounded" to the property type in the schema

    header = '''<?xml version="1.0" standalone="no"?>
<UDM DATABASE="SPRESI" SEQUENCE="1" TIMESTAMP="{}">
  <UDM_VERSION MAJOR="6" MINOR="0" REVISION="0" VERSIONTEXT="6.0.0"/>
  <MOLECULES>
'''

    #Create a timestamp
    ts = datetime.datetime.now().timestamp()
    timestamp = datetime.datetime.fromtimestamp(ts).isoformat()

    footer = '''  </MOLECULES>
  <REACTIONS>
    <REACTION ID="1">
    </REACTION>
  </REACTIONS>
</UDM>
    '''
    SMILES = CAS_to_SMILES(CAS_number)
    mol_id = 1
    with open(udm_file, 'w') as f:
        f.write(header.format(timestamp))
        f.write('    <MOLECULE ID="{}">\n'.format(mol_id))
        if SMILES != 'Did not work':
            try:
                f.write('      <MOLSTRUCTURE>{}</MOLSTRUCTURE>\n'.format(SMILES))
            except AttributeError:
                pass
        f.write('      <CAS>{}</CAS>\n'.format(CAS_number))
        f.write('    </MOLECULE>\n')
        f.write(footer)
        

def UDM_verifier(xml_file, xsd_file):
    "This function checks whether an xml file complies with the" 
    "UDM schema"
    "NB: need to remove the 'encoding='utf-8' entry for the code to work"
    # open and read xml file
    with open(xml_file, 'r') as xml_file:
        xml_to_check = xml_file.read()   
        
    # open and read schema file
    with open(xsd_file, 'r') as schema_file:
        schema_to_check = schema_file.read()
        
    xmlschema_doc = etree.parse(StringIO(schema_to_check))
    xmlschema = etree.XMLSchema(xmlschema_doc)

    # parse xml
    try:
        doc = etree.parse(StringIO(xml_to_check))
        print('XML well formed, syntax ok.')

    # check for file IO error
    except IOError:
        print('Invalid File')

    # check for XML syntax errors
    except etree.XMLSyntaxError as err:
        print('XML Syntax Error, see error_syntax.log')
        with open('error_syntax.log', 'w') as error_log_file:
            error_log_file.write(str(err.error_log))
        quit()

    except:
        print('Unknown error, exiting.')
        quit()

    # validate against schema
    try:
        xmlschema.assertValid(doc)
        print('XML valid, schema validation ok.')

    except etree.DocumentInvalid as err:
        print('Schema validation error, see error_schema.log')
        with open('error_schema.log', 'w') as error_log_file:
            error_log_file.write(str(err.error_log))
        quit()

    except:
        print('Unknown error, exiting.')
        quit()    

from urllib.request import urlopen

def CAS_to_SMILES(ids):
    """This function takes in CAS ids and returns the corresponding SMILES string"""
    try:
        url = 'http://cactus.nci.nih.gov/chemical/structure/' + ids + '/smiles'
        ans = urlopen(url).read().decode('utf8')
        return ans
    except:
        return 'Did not work'
        #pass
#https://stackoverflow.com/questions/54930121/converting-molecule-name-to-smiles

def udm_to_df(udm_file):
    '''
    This script takes in a XML UDM file and produces a pandas df from it.
    
    
    '''
    tree = ET.parse(udm_file)
    root = tree.getroot()
    
    sol_columns=[]
    for i in range(len(root[1][1])):
        try:
            sol_columns.append((list(root[1][1][i].attrib.values())[0]))
        except IndexError:
            sol_columns.append((root[1][1][i].tag))

    #initialise df
    df=pd.DataFrame(columns=sol_columns)

    for i in range(len(root[1])):
        data_entries=[]
        for j in range(len(root[1][1])):
            data_entries.append(root[1][i][j].text)
        data_entries_df=pd.DataFrame([data_entries], columns=sol_columns)
        df=df.append(data_entries_df, ignore_index=True)
    return df
