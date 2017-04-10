# Accepts csv file, reads it, creates JSON output and prints it to a file
import csv, json, time, os.path
from sys import argv
import os.path
#Below Script accepts path of csv from terminal
script , inputcsv = argv

#Check if the file extension is csv
#A simplified version of cjp_1.py for the if condition below
if inputcsv.endswith('.csv') == True:
    #Open the file below
    infile = open( inputcsv, 'r' )
    #Read the file using csvreader functionality
    reader = csv.DictReader(infile)
    output = json.dumps( [ row for row in reader ] )
    #Use this to create a new file everytime with a datestamp
    #Replace .js below with .txt if you want the output in notepad
    outfile = time.strftime("%Y%m%d-%H%M%S") + '.js'
    # You can directly create a file in Python at a file location as shown below
    print 'The name of your file is ', outfile
    # print  outfile
    JSONFILE = open(outfile,'w')
    JSONFILE.write(output)
    JSONFILE.close()
else:
    print 'Hey!!This is not a CSV!!!'
    quit()
