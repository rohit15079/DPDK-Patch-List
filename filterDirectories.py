from tableColumnIndex import *

def filterDirectory(patchList):
    with open("optionalDirectoryList.txt") as f:
        optionalDirectoryList=[line.rstrip('\n') for line in f]
        print(optionalDirectoryList)
    mandatoryPatchList=[]
    optionalPatchList=[]
    for patch in patchList:
        for directory in optionalDirectoryList:
            if directory in patch[dataIndex][patchIndex]:
                print(patch[dataIndex][patchIndex])
                print(directory)
                optionalPatchList.append(patch)
            else:
                mandatoryPatchList.append(patch)
    return mandatoryPatchList, optionalPatchList
