
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
