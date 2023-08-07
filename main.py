
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
