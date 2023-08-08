
#fhand = open('biblekjv.txt')
#for linesAll in fhand:
#    print(linesAll)
#example of reading a file for each line in file print out to terminal this file too big do NOT RUN

#counting the lines in the file 'Line Count: 31103'
fhand = open('biblekjv.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count: ', count)


#Reading the WHOLE file by character
#fhand = open('biblekjv.txt')
#inp = fhand.read()
#print(len(inp))
#print(inp[0:20])....prints only first 20 characters...first 20 char

fhand = open('biblekjv.txt')
for line in fhand:
    if line.startswith('Jud') :
        print(line)

#the above script looks for all lines in text file that start with chars J-U-D

#above code revised to remove newline whitespace
fhand = open('biblekjv.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('Am') :
        print(line)

#same code as above but optimized
fhand = open('biblekjv.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('Am') :
        continue
    print(line)

#we can look for a line anywhere in our string
fhand = open('biblekjv.txt')
for line in fhand:
    line = line.rstrip()
    if not 'christ' in line:
        continue
    print(line)

#
#fname = input('Enter the file name: ')
#fhand = open(fname)
#count = 0
#for line in fhand:
#    if line.startswith('Subject:') :
#        count = count + 1
#print('There were', count, 'subject lines in', fname)
#the commented out code above allows users to input bad data, see revised code below
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File Cannot Be Opened: ', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print('There were ', count, ' subject lines in ', fname)
#enter a file name at prompt


#chapter 8 python4everyone looking inside lists
#a collection allows us to put many values in a single variable
#a collection is good because we can carry many values around in one package

friends = [ 'Jesus', 'God', 'Judas' ]
cargo = ['shoes', 'robe', 'wisdom' ]
