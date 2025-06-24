import glob

def quickAssign(*, infile, outfile, upSeq, downSeq, guideLength, guideDirectory, rc = True):
    with open(infile) as infile, open(outfile, 'w') as outfile:
        data = readInGuides(guideDirectory)
        for line in infile:
            currDict = data
            position = line.find(upSeq)
            if position != -1:
                guideStart = position + len(upSeq)
                if line[guideStart + guideLength:guideStart + guideLength + len(downSeq)] == downSeq:
                    sequence = line[guideStart:guideStart + guideLength]
                    if rc:
                        sequence = reverseComplement(sequence)
                    for character in sequence:
                        if character not in currDict:
                            currDict[character] = {}
                        currDict = currDict[character]
                    if len(currDict) != 0:
                        currDict['final'][3] += 1
                    else:
                        currDict['final'] = [sequence, 'unknown', 'unknown', 1]
        outfile.write('sequence\tgene_ID\tUID\toccurrences\n')
        for value in list(NestedDictValues(data)):
            outfile.write('\t'.join(value[:-1]) + '\t' + str(value[3])  + '\n')





#from https://stackoverflow.com/questions/23981553/get-all-values-from-nested-dictionaries-in-python
def NestedDictValues(d):
  for v in d.values():
    if isinstance(v, dict):
      yield from NestedDictValues(v)
    else:
      yield v

def readInGuides(directory):
    guideDict = {}
    for infile in glob.glob(directory + '/*.csv'):
        with open(infile) as file:
            header = file.readline()
            for line in file:
                data = line[:-1].split(',')
                sequence = data[2]
                gene_ID = data[0]
                UID = data[1]
                currDict = guideDict
                for character in sequence:
                    if character not in currDict:
                        currDict[character] = {}
                    currDict = currDict[character]
                currDict['final'] = [sequence, gene_ID, UID, 0]
    return guideDict



def reverseComplement(sequence):
    sequenceList = [character for character in sequence]
    revSeq = ''
    while len(sequenceList) > 0:
        character = sequenceList.pop()
        if character == 'A':
            revSeq += 'T'
        elif character == 'T':
            revSeq += 'A'
        elif character == 'G':
            revSeq += 'C'
        elif character == 'C':
            revSeq += 'G'
        else:
            revSeq += 'N'
    return revSeq

'''

        '''
