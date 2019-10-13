from fetchData import fetchPatchList
from tableColumnIndex import *
from filterDelegates import filterDelegate
from filterSubmitters import filterSubmitter

patchList=fetchPatchList()
optionalPatchList=[]
mandatoryPatchList, optionalPatches=filterDelegate(patchList)
for patch in optionalPatches:
    optionalPatchList.append(patch)
mandatoryPatchList, optionalPatches=filterSubmitter(mandatoryPatchList)
for patch in optionalPatches:
    optionalPatchList.append(patch)
print(mandatoryPatchList)
print(optionalPatchList)
