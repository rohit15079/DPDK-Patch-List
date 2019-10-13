from tableColumnIndex import *

def filterDelegate(patchList):
    with open("delegateList.txt") as f:
        delegateList=[line.rstrip('\n') for line in f]
        print(delegateList)
    mandatoryPatchList=[]
    optionalPatchList=[]
    for listEntry in patchList:
        if listEntry[dataIndex][delegateIndex] in delegateList:
            optionalPatchList.append(listEntry)
        else:
            mandatoryPatchList.append(listEntry)
    return mandatoryPatchList, optionalPatchList
