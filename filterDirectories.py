from tableColumnIndex import *

def filterDirectory(patchList):
    with open("optionalDirectoryList.txt") as f:
        optionalDirectoryList=[line.rstrip('\n') for line in f]
        print(optionalDirectoryList)
    mandatoryPatchList=[]
    optionalPatchList=[]
    for patch in patchList:
        patchNeeded=True
        for directory in optionalDirectoryList:
            if directory in patch[dataIndex][patchIndex] or directory in patch[dataIndex][seriesIndex]:
                patchNeeded=False
                break
        if patchNeeded:
            mandatoryPatchList.append(patch)
        else:
            optionalPatchList.append(patch)
            print(patch)

    return mandatoryPatchList, optionalPatchList
