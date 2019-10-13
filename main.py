from fetchData import fetchPatchList
from tableColumnIndex import *
from filterDelegates import filterDelegate

patchList=fetchPatchList()
mandatoryPatchList, optionalPatchList=filterDelegate(patchList)
print(mandatoryPatchList)
print(optionalPatchList)
