from score_checker import Scorer

filename = "0_example"
extention = ".txt"
f = open(filename+extention, "r")
landscap = []
potraits = []
mainarray = []

# read file and seperate the records
for line in f.readlines()[1:]:
    temparray = line.strip().split(" ")
    mainarray.append(temparray)
    if temparray[0] == "L":
        landscap.append(temparray)
    else:
        potraits.append(temparray)

def findIntersect(a,b):
    tempa = a[2:]
    tempb = b[2:]
    length = len(list(set(tempa) & set(tempb)))
    return length

# find match records
def findmatchrecords(inputarray):
    indexarray = []
    tempindex = []
    for i in range(0, len(inputarray)):
        print(i)
        iArray = inputarray[i]
        maxlength = 0
        if (len(inputarray) - 1) == i:
            break
        startindex = i + 1
        index = startindex
        for j in range(startindex, len(inputarray)):
            jArray = inputarray[j]
            length = findIntersect(iArray, jArray)
            if maxlength < length:
                maxlength = length
                index = j
            last = len(inputarray) - 1
            if last == j and index not in tempindex:
                tempindex.append(index)
        if i not in tempindex:
            tempindex.append(i)



    print(len(tempindex))
    for i in range(0,len(tempindex),2):
        indexarray.append([inputarray[tempindex[i]], inputarray[tempindex[i+1]]])
    return indexarray

potraits1 = findmatchrecords(potraits)
landscap1 = findmatchrecords(landscap)

filename1 = filename + "_output" + extention
with open(filename1, 'w') as the_file:
    templen = sum(len(x) for x in landscap1)
    len = len(potraits1) + templen
    the_file.write(str(len)+"\n")
    indexs = []
    for obj in potraits1:
        index0 = str(mainarray.index(obj[0]))
        index1 = str(mainarray.index(obj[1]))
        temp = index0 + " " + index1 + "\n"
        the_file.write(temp)

    for obj in landscap1:
        for temp in obj:
            index0 = str(mainarray.index(temp))
            temp1 = index0 + "\n"
            the_file.write(temp1)

    the_file.flush()

    score = Scorer(filename+extention, filename1)
    score.exhibition_walk()
    print("Final score = %s" % score.score)











