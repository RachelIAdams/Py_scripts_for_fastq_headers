import sys

## Files get imported in command line ###

filename_in = sys.argv[1]
filename_out = sys.argv[2]

fasta_oldnames = open(filename_in, "rU") #opens the input file
fasta_newnames = open(filename_out,"w") #file to be written to


prefix = '@sample=' #how you want each line to start

for line in fasta_oldnames: #read each line of the input file at a time
    if line.startswith('@M0'): # if line starts with carrot, do the following:
        splitline = line.split(':') # split up the line by colons
        sample_name = splitline[9].strip() # their label is the 10th cut of the split; strip the space
        # print sample_name
        descriptor1 = splitline[5] # the first descriptor is the 6th cut
        # descriptor 1
        descriptor2prep = splitline[6] # the second descriptor is part of the 7th cut
        descriptor2 = descriptor2prep.split(' ')[0] # to get the second descriptor, need to split the 7th cut of the original strip by space, the get the first cut of that split
        # print third
        print >>fasta_newnames, '%s%s;_%s:%s' % (prefix, sample_name, descriptor1, descriptor2) #put the different parts together and print that as the new sequence header to the file
    
    else: #if line didn't start with carrot (ie. the sequences) just print that line and strip the space
        print >>fasta_newnames, line.strip()




