# Standardization of Ig datasets using universal numbering system and auto generating Bridged 1D maps

![alt text] (https://github.com/hackathonismb/Standardization-of-Ig-datasets-using-universal-numbering-system-and-auto-generating-Bridged-1D-maps/blob/d7c0ccbe09f7cfbba24b34cebf268ce8578a4bd6/Picture1.png)

# Table of Contents
  * [Statement of the Problem](https://github.com/hackathonismb/Standardization-of-Ig-datasets-using-universal-numbering-system-and-auto-generating-Bridged-1D-maps/#1-statement-of-the-problem)
  * [Why is it significant?](https://github.com/hackathonismb/Standardization-of-Ig-datasets-using-universal-numbering-system-and-auto-generating-Bridged-1D-maps/#2-why-is-it-significant)
  * [Objectives](https://github.com/hackathonismb/Standardization-of-Ig-datasets-using-universal-numbering-system-and-auto-generating-Bridged-1D-maps/#3-objectives)
  * [What is ProteinContactMaps?](https://github.com/hackathonismb/Standardization-of-Ig-datasets-using-universal-numbering-system-and-auto-generating-Bridged-1D-maps/#4-what-is-proteincontactmaps)
  * [How to use ProteoMap?](https://github.com/hackathonismb/Standardization-of-Ig-datasets-using-universal-numbering-system-and-auto-generating-Bridged-1D-maps/#5-how-to-use-proteomap)
  * [Team](https://github.com/hackathonismb/Standardization-of-Ig-datasets-using-universal-numbering-system-and-auto-generating-Bridged-1D-maps/#6-team)
  * [References](https://github.com/hackathonismb/Standardization-of-Ig-datasets-using-universal-numbering-system-and-auto-generating-Bridged-1D-maps/#7-references)
  * [License](https://github.com/hackathonismb/Standardization-of-Ig-datasets-using-universal-numbering-system-and-auto-generating-Bridged-1D-maps/#8-license)

## 1. Statement of the Problem

The 1D protein sequence contains information about amino acid residues, but not about essential topological information. On the other hand, 3D structure gives topological annotation and visualization of domain interactions but lacks amino acid residue information and is difficult to comprehend biological function. 1D representation maps contain both sequence information and 3D domain assembly, allowing biologists to grasp residue connections and, ultimately, function.

## 2. Why is it significant?

The immune system relies heavily on Ig domains. They detect foreign antigens, bind the receptor binding domain (RBD), and eliminate antigens from the biological system. IgV domains are especially essential because of the variable region's capacity to bind novel antigens and RBDs. Visualizing domain folds and RBD binding in 1D maps will reveal areas with insertions and/or mutations that impede the immune system from identifying pathogens. 1D maps will be used to discover novel treatment targets.

## 3. Objectives

**Visualization of 1D maps:** construct a 1D map of Ig domains that non-experts can comprehend.

**Superimpose Residue Information on 1D Map:** Use 3D annotation to produce a vector representation of residue features and include them into the 1D map. For example, bold residues indicate whether the structure is oriented in or out.

**Generate 1D maps for domains that have no preceding 3D annotation:** Employing machine learning, identify the main traits in order to construct innovative 1D maps from sequence data.

## 4. What is ProteinContactMaps?

1. iCn3D parses a structure to get a list of residue contacts.
2. The relevant sequence is retrieved and the numbering of the sequences is synchronized. This approach is required to build a correspondence in the 1D map positions in order to compare two or more sequences. When available, we utilize the Kabat reference sequence number. This need can be eased by matching the protein sequences to be compared and assigning a sequence number to match the alignment.
3. A json file with an upgraded 1D sequence is created. The goal of this stage is to collect per-residue data (i.e. number of contacts is makes with other residues; list of residues it interacts with, etc.)
4. The augmented 1D representations can be developed applying the enriched 1D representation (Logo plots, Contact maps, etc.)
5. If no template exists, a fresh 1D plot based on residue contact information must be created. Based on the information from the contact map, this technique is being constructed.
6. When a template as a modification of the previous template is available, a new 1D ProteinContactMaps can be constructed. This is an advantageous method for comparing ProteoMaps. Color coding 1D attributes acquired in the improved 1D sequence can be used to enhance ProteoMaps.

## 5. How to use ProteinContactMaps?

scripts/excel_template.py -> can be called with a parameter 1 or 0 from command line where the value 1 creates the template(s) with the color coding for the contact maps and 0 creates the standard ones.

scripts/.xlsx --> templates

data/source -> contain the .txt files which are the output of ANARCi (http://opig.stats.ox.ac.uk/webapps/newsabdab/sabpred/anarci/) for Kabat numbering normalization

.txt to .json conversion is provided by an excel macro (Chirag)

data/input_files -> folder with the json files

scripts/contacts.sh -> Contact counting is generated with the script contacts.sh starting from the contact map generated by iCn3D (refere to iCn3D for details)

data/output and data/output2 -> folder where the colorized (by number of contacts) outputs are stored.5. 


## 6. Team
* Umesh Khaniya
* Chirag Patel
* Caesar Tawfeeq
* Siddhi Jani
* Sujitkumar
* Prasanthkumar
* Philippe Youkharibache

## 7. References
1. Wang, J., Youkharibache, P., Marchler-Bauer, A., Lanczycki, C., Zhang, D., Lu, S., ... & Ge, Y. (2022). iCn3D: From Web-Based 3D Viewer to Structural Analysis Tool in Batch Mode. Frontiers in Molecular Biosciences, 102.

2. Youkharibache, P. (2021). Topological and Structural Plasticity of the single Ig fold and the double Ig fold present in CD19. Biomolecules, 11(9), 1290.

3. Youkharibache, P., Cachau, R., Madej, T., & Wang, J. (2020). Using iCn3D and the World Wide Web for structure-based collaborative research: Analyzing molecular interactions at the root of COVID-19. bioRxiv.

## 8. License 

Licensed under MIT License - Copyright (c) 2022 hackathonismb (Refer LICENSE file for more details.
