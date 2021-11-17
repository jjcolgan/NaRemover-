# lefse is not working in microbiome analyst. Writing a program to first identify reads
# that do not have a taxonomic classification at any level from taxonomy table, output a new taxonomy table without those reads, then take the ASVs without
# taxonomic classification and remove them from the asv table.
#reading in taxonomy file to list of lines
input = open('C:/Users/jjcol/OneDrive/Desktop/CeliacResearchProject/Bodke Microbiome Analyst/TaxaTableNewControls.txt','r')
lines = input.readlines()
input.close()
#preparing outputfile
output = open('C:/Users/jjcol/OneDrive/Desktop/CeliacResearchProject/Bodke Microbiome Analyst/TaxaTableNewDataNoNA.txt', 'w')
#Removes all asvs without an phylum or lower classification, noTA is used to count asvs without a taxonomic assignment, noO is used to count ASVs with only a phylum level assignment
# ASVs only a phylum level assignment are written to a fasta file and will be blasted. 
ASVs = []
noTA = 0
noO =0
for line in lines:
    words = line.split("\t")
    if words[2] == "NA":
            if words[1] == 'NA':
                noTA+= 1
                ASVs.append(words[0])
            else:
                noO +=1
                output.write(line)
    else:
        output.write(line)
output.close()
print("done removing NAs from taxonomy file")
output=open('C:/Users/jjcol/OneDrive/Desktop/CeliacResearchProject/Bodke Microbiome Analyst/unassignedBacteria.fa', 'w')

#creating fasta file of seqs without taxonomic assignment below phylum 
for asv in ASVs:
    output.write('>'+asv + '\n'+asv + '\n')  
#reading in ASV table, if line starts with an asv from the list, do not write it to output.
input = open('C:/Users/jjcol/OneDrive/Desktop/CeliacResearchProject/Bodke Microbiome Analyst/ASVTableNewData (1).txt','r')
lines = input.readlines()
output = open('C:/Users/jjcol/OneDrive/Desktop/CeliacResearchProject/Bodke Microbiome Analyst/ASVTableNoNA.txt','w')
counter =0
debug =0
for line in lines:
    toAdd = True
    word = line.split("\t")
    for asv in ASVs:
        counter = 0 
        if word[0] == asv:
            counter += 1
            toAdd =False
            ASVs.pop(counter)
            break
    if toAdd == True:
        output.write(line)
numOriginal=len(lines)-1
output.close()
output =open('C:/Users/jjcol/OneDrive/Desktop/CeliacResearchProject/noNAStats.txt','w')
output.write('Of ' + str(numOriginal) + ' asvs ' + str(noTA+noO) + ' were removed. Of those removed ' +str(noTA)
             + ' had no taxonomic assignment and ' + str(noO) + ' had only phylum classification. ' + str(numOriginal - (noTA+noO)) + ' asvs remain.')
output.close()
