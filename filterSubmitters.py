from tableColumnIndex import *

def filterSubmitter(patchList):
    with open("submitterList.txt") as f:
        submitterList=[line.rstrip('\n') for line in f]
        print(submitterList)
    mandatoryPatchList=[]
    optionalPatchList=[]
    for listEntry in patchList:
        if listEntry[dataIndex][submitterIndex] in submitterList:
            optionalPatchList.append(listEntry)
        else:
            mandatoryPatchList.append(listEntry)
    return mandatoryPatchList, optionalPatchList
