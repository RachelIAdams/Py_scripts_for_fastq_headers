
import sys

## Files get imported in command line ###

filename_in = sys.argv[1]
filename_out = sys.argv[2]

fastq_oldnames = open(filename_in, "rU") #opens the input file
list_of_ids_txt = open(filename_out,"w") #file to be written to

list_of_ids=[]

for line in fastq_oldnames: #read each line of the input file at a time
    if line.startswith('@M'): # if line starts with certain character', do the following:
        splitline = line.split(':') # split up the line by colons; there should be 10
        their_label = splitline[9].strip() # their label is the 10th cut of the split; strip the space
        list_of_ids.append(their_label)
    else: pass

print >>list_of_ids_txt, "\n".join(set(list_of_ids))


