import os
import sys

#convert csv files to tab delimited files

filename = sys.argv[1] #csv file to read in
infile = open(filename)
out = open(filename.replace(".csv",'.txt'), "w") #file to write to

for line in infile:
	line = line.replace(",","\s")
	out.write(line )

infile.close()
out.close()
