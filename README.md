# genesym_to_name
First steps in Python using the NCBI API to translate GeneSymbols to Names and fetch 
aliases.

By default the genes.py expects a text file with one gene symbol per line in a file named 
list.txt. Other input file names can be specified wiht -i filename. It the calls functions 
from getgenes.py to fetch all EntrezIDs per Symbol. By default it only searches for human 
genes. Then it writes a tab-delimited text file containing GeneSymbol, Nomenclature, 
Aliases, EntrezID as output.csv. By default it omits IDs where no nomenclature can be found.

