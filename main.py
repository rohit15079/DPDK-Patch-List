from fetchData import fetchPatchList
from urls import *

patchList, patchListHyperlinks=fetchPatchList()
print(patchList)
print(patchListHyperlinks)
