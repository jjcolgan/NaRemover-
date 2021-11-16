# lefse is not working in microbiome analyst. Writing a program to first identify reads
# that do not have a taxonomic classification at any level from taxonomy table, output a new taxonomy table without those reads, then take the ASVs without
# taxonomic classification and remove them from the asv table.

#reading in taxonomy file to list of lines 
input = open('C:/Users/jjcol/OneDrive/Desktop/CeliacResearchProject/Bodke Microbiome Analyst/taxaTableNewControls.txt','r')

lines = input.readlines()

input.close()

#preparing outputfile 
output = open('C:/Users/jjcol/OneDrive/Desktop/CeliacResearchProject/Bodke Microbiome Analyst/TaxaTableNewDataNoNA.txt', 'w')

#if the second word, should be phylum classification is NA, read is useless. Write all reads with non NA phylum to output. A lsit of NA ASVs will be complied from this as well.
ASVs = []
for line in lines:
    words = line.split("\t")
    if words[1] != "NA":
            output.write(line )
            ASVs.append(words[0])             
output.close()
#reading in ASV table, if line starts with an asv from the list, do not write it to output.

input = open('C:/Users/jjcol/OneDrive/Desktop/CeliacResearchProject/Bodke Microbiome Analyst/ASVTableNewData (1).txt','r')
lines = input.readlines()
output = open('C:/Users/jjcol/OneDrive/Desktop/CeliacResearchProject/Bodke Microbiome Analyst/ASVTableNoNA.txt','w')
for line in lines:
    for asv in ASVs:
        if line.startswith(asv) == False:
            output.write(line)
            break
output.close()
              
            
              
    
              
              
        
