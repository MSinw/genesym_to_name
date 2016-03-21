from csv import writer

#reads textfile with one genesymbol  per line and returns a sortet list with uniques symbols
def sym_per_line(file = 'list.txt'):
    with open(file, 'r',  encoding='utf-8') as infile:
        symbols_all = infile.read()
        #splits the file in a list
        symbols = symbols_all.split()
        #makes the entries unique
        symbols = list(set(symbols))
    return(symbols)

#writes the querid data into output.csv, expects a dictionary as input, filter = 0 will write Symbols without a nomenclature to the file
def writefile(data,  filename = "output.csv",  filter = 1):    
    with open(filename, 'w', newline='') as csvfile:
        genenames = writer(csvfile,  delimiter = '\t')
        genenames.writerow(['Symbol', 'Name',  'Alias',  'EntrezID'])
        lines_written = 0
        #loop through every  key in the input dictionary
        for k,  v in data.items():
            #loops through every entry inside the key, e.g. sometimes there are multiple IDs
            for details in v:
                #check if only symbols with nomenclature should be writen to the file
                if filter and details[1][1] != "":
                    #in the json data retrieved from NCBI there are a lot of , in the nomenclature name, thereofre we delete them
                    genenames.writerow([k, details[1][1].replace(',',''), details[2][1],  details[0][1] ])
                    lines_written += 1
                elif not filter:
                    genenames.writerow([k, details[1][1].replace(',',''), details[2][1],  details[0][1] ])
                    lines_written += 1
        return lines_written
