from fetchData import fetchPatchList
from tableColumnIndex import *
from filterDelegates import filterDelegate
from filterSubmitters import filterSubmitter
from filterDirectories import filterDirectory
from filterDays import filterDay

patchList=fetchPatchList()
startDate="2019-10-14"
endDate="2019-10-14"
patchList=filterDay(patchList, startDate, endDate)
optionalPatchList=[]
mandatoryPatchList, optionalPatches=filterDelegate(patchList)
for patch in optionalPatches:
    optionalPatchList.append(patch)
mandatoryPatchList, optionalPatches=filterSubmitter(mandatoryPatchList)
for patch in optionalPatches:
    optionalPatchList.append(patch)
mandatoryPatchList, optionalPatches=filterDirectory(mandatoryPatchList)
for patch in optionalPatches:
    optionalPatchList.append(patch)
print(mandatoryPatchList)
