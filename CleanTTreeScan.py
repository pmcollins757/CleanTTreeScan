from sys import argv
from subprocess import call

#Arguments: Name of Scan file to be cleaned.
fName = argv[1]

#Open the file
fid = open(fName)
#Open the temp file
ftmp = open('ztemp.txt', "w")
#Read the lines of the file into a list.
fList = fid.readlines()
fLength = len(fList) - 1

#Split each line into individual items in a nested list of lists
#First create an empty list
splitlist = []
#In the following 'for' loop for every line in the range 
#from the fourth line until the second to last line it 
#splits the string that is each line at the white 
#space and then appends that onto the list "splitlist".
for i in xrange(3,fLength):
    splitlist.append(fList[i].split())
    #Join the strings together, getting rid of the normal formatting associated with python printing lists of strings.
    tmp = "\t".join(splitlist[i -3][3:-1:2])
    #Add the line to the text file
    print>>ftmp, tmp

# close the file, just for safety
fid.close()
call(['mv', 'ztemp.txt', fName])
