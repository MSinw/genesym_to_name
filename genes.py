import getgenes
import fileops
import sys
import collections

#checks if -i is given and tries to get an input file name
try:   
    if sys.argv[1] == "-i":
        try: 
            infile =  sys.argv[2]
        except:
            print("Use -i infilename to specify infile")
            sys.exit(1)
#if no arg is given defaults to list.txt
except:
    print("Defaulting to list.txt as input.")
    infile = "list.txt"


#fetch the symbols
symbols = fileops.sym_per_line(file = infile)
#count tthe symbols
num_sym = len(symbols)
#sort the symbol list alphabetically
symbols.sort()
print(str(num_sym)+" loaded")
idlist = []
for sym in symbols:
    print("Get IDs of Symbol: "+sym)
    idlist.extend(getgenes.getIDList(sym))
print("Fetching names")
names = getgenes.getNames(idlist)
#orders the dictionary alphabetically
names_od = collections.OrderedDict(sorted(names.items()))
print("Writing file")
lines = fileops.writefile(names_od)
#if there are more lines written the symbols there should be multiple IDs per symbol
print("Querried "+str(num_sym)+" gene symbols.")
print("Written "+str(lines)+" lines to output.")
