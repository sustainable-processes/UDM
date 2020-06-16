UDM 6.0.0, 18 February 2020
====================================

Introduction
------------

This package contains the UDM XML schema definition version 6.0.0 released by
Pistoia Alliance, sample data sets annd applications that operate on the UDM
file format.

For more information please see:
1. http://www.pistoiaalliance.org/projects/udm/
2. https://github.com/PistoiaAlliance/UDM


Licences for data sets
----------------------

Both SPRESI and Reaxys data sets are covered by the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 licence.


Schema
------

UDM_License.pdf                    -- Copy of the UDM license accepted
                                      when downloading this UDM package.
udm_6_0_0.xsd                      -- The UDM 6.0.0 XML schema.
udm_6_0_0_*.xsd                    -- Controlled vocabularies used by
                                      UDM 6.0.0
Previous/udm_pa_4_0_0.xsd          -- The UDM 4.0.0 XML schema.
Previous/udm_5_0_1.xsd             -- The UDM 5.0.1 XML schema.


Data sets
---------

data/SPRESI/spresi-10k.xml         -- 10,000 reactions from the SPRESI
                                      database; first 100 include atom-atom
                                      mappings and reaction centre
                                      information (converted from RD file).
                                      Courtesy of Hans Kraut / InfoChem.

data/SPRESI/spresi-100.rdf         -- First 100 reactions from the SPRESI
                                      dataset in the original RD file format.
                                      Courtesy of Hans Kraut / InfoChem.

data/SPRESI/legalcode.txt          -- Licence conditions for the SPRESI
                                      datasets.

data/Reaxys/reaxys-reactions.xml   -- Original 1000 reactions from Reaxys
                                      (UDM 3.6.0.112).
                                      Courtesy of Markus Fisher / Elsevier.

data/Reaxys/reaxys-reactions-5.xml -- 1000 reactions from Reaxys converted
                                      to UDM 5.0.1 (Brooklyn).

data/Reaxys/reaxys-reactions-6.xml -- 1000 reactions from Reaxys converted
                                      to UDM 6.0.0.

data/Reaxys/legalcode.txt          -- Licence conditions for the Reaxys
                                      datasets.


Documentation
-------------

ChangeLog.pdf                      -- Description of changes introduced
                                      in version 4.0.0, 5.0.1 and 6.0.0.

Glossary.pdf                       -- Glossary of key UDM terms.


Code
----

spresi2udm                         -- Python 3 code used for conversion of
                                      SPRESI RD file to UDM 6.0.0.
