from urllib.request import urlopen
from collections import defaultdict
import json

#fetches all ids per symbol from the geneDB at NCBI, db and org can be overwritten to query other DBs or other organisms than human
def getIDList(symbol,  db = "gene",  org = "human",  outform = "json"):
    url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db="+db+"&term="+symbol+"[sym]+AND+"+org+"[Organism]&retmode="+outform
    ensearch = urlopen(url).read().decode('utf-8')
    enjson = json.loads(ensearch)
    return enjson['esearchresult']['idlist']

#expecting a list of ids, querys by default the geneDB at NCBI
def getNames(idlist,  db = "gene",  outform ="json"):
    if not isinstance(idlist,  list):
            raise TypeError("Expecting a list of IDs")
    ids = ""
    #convert the list into a comma-separated string, needed for the query
    for id_n in idlist:
        ids = ids+","+id_n
    url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=gene&id="+ids+"&retmode="+outform
    enfetch = urlopen(url).read().decode('utf-8')
    enjson = json.loads(enfetch)
    names = defaultdict(list)         
    #loops throgh every id in the result data
    for id in idlist:
        #genename/symbol tuple
        name = enjson["result"][id]["name"]
        #nomenclaturename tuple
        nomname = ("Nomenclature Name",  enjson["result"][id]["nomenclaturename"])
        #uid tuple
        entrezid = ("uid",  id)
        #aliases tuple
        aliases = ("Aliases",  enjson["result"][id]["otheraliases"])
        #put all the tuples into a list
        data = [entrezid,  nomname,  aliases]
        #append the data to a dictionary with the genename/symbol as key
        names[name].append(data)
    return names
