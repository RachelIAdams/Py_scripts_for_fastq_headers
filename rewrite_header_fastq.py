import sys

## Files get imported in command line ###

filename_in = sys.argv[1]
filename_out = sys.argv[2]
barcode_map = sys.argv[3]

fastq_oldnames = open(filename_in, "rU") #opens the input file
fastq_newnames = open(filename_out,"w") #file to be written to


handle = open(barcode_map, "rU") #reads in barcode map and makes it a pythonic dictionary
map = {}
for line in handle:
    k, v = line.strip().split('\t')
    map[k.strip()] = v.strip()

handle.close()


prefix = '@barcodelabel=' #how you want each line to start

for line in fastq_oldnames: #read each line of the input file at a time
    if line.startswith('@M0'): # if line starts with a particular character, do the following:
        splitline = line.split(':') # split up the line by colons; there should be 10
        #their_label = splitline[9].strip() # their label is the 10th cut of the split; strip the space
        their_labelprep = splitline[9].strip()
        their_label = their_labelprep.split(' ')[1]
        sample_name=map[their_label] #look up their label in the barcode map
        # print sample_name
        descriptor0 = splitline[4] # the first descriptor is the 5th cut
        descriptor1 = splitline[5] # the second descriptor is the 6th cut
        descriptor2prep = splitline[6] # the third descriptor is part of the 7th cut
        descriptor2 = descriptor2prep.split(' ')[0] # to get the second descriptor, need to split the 7th cut of the original strip by space, the get the first cut of that split
        print >>fastq_newnames, '%s%s;_%s:%s:%s' % (prefix, sample_name, descriptor0,descriptor1, descriptor2) #put the different parts together and print that as the new sequence header to the file

    else: #if line didn't start with carrot (ie. the three other lines) just print that line and strip the space
        print >>fastq_newnames, line.strip()



