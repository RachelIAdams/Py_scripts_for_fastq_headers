
import sys
import os

#os.chdir('/Users/rachel/Desktop/play/play_directory')
in_directory = sys.argv[1]
os.chdir(in_directory)

filenames=os.listdir('.')

#print filenames

for i in filenames:
    if '.fastq' not in i:
        continue
    file_in=open(i, "rU")
    name = i
    parts = name.split('.')
    newname = parts[0] + "_newname." + parts[1]
    file_out=open(newname,"w")
    sample_name_a=parts[0]
    sample_name_b=sample_name_a.split('_')[0]
#sample_name_c=sample_name_b.split('-',2)
    print sample_name_b
    for line in file_in:
        if line.startswith('@M0'):
            splitline = line.split(':')
            print >>file_out, '%s:%s:%s:%s:%s:%s:%s:%s:%s:%s' % (splitline[0], splitline[1], splitline[2],splitline[3], splitline[4],splitline[5],splitline[6],splitline[7],splitline[8],sample_name_b)
        else:
            print >>file_out, line.strip()
