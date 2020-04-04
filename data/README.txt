The data folder contains the solvent descriptor data from the solvent selection paper (Amar et al. DOI: 10.1039/c9sc01844a) 
- 'solvents_results_YA_v14.csv': is the original raw file
- 'all_solvents_UDM.csv': contains mol descriptors for all solvents, prepared to be converted to UDM (e.g. changing column
   names, removing spaces etc.)
- 'all_solvents.xml': The UDM file created from the csv file above
- 'solvents_results_UDM.csv': contains mol descriptors + conv. and d.e. for the solvents that they did experiments with
- 'solvents_results.xml': The UDM file created from the csv file above
- 'all_SMILES_CAS.csv': contains just the SMILES and CAS numbers of all solvents. This avoids having to generate the 
   SMILES strings every time you want to work with the data
- 'udm_6_0_0.xsd': The UDM Schema, available at https://www.pistoiaalliance.org/projects/udm/
- 'predicted_best_solvent.xml': The UDM file containing SMILES string and CAS number for the predicted optimal solvent to test
