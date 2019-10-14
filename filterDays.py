from tableColumnIndex import *
from patchDateIndex import *
from datetime import date

def filterDay(patchList, startDate, endDate):
    startDate=[int(n) for n in startDate.split('-')]
    print(startDate)
    print(int(startDate[year]))
    print(int(startDate[month]))
    print(int(startDate[day]))
    startDate=date(startDate[year], startDate[month], startDate[day])
    endDate=[int(n) for n in endDate.split('-')]
    endDate=date(endDate[year], endDate[month], endDate[day])
    requiredPatchList=[]
    for patch in patchList:
        if patch[dataIndex][dateIndex]=="Date":
            requiredPatchList.append(patch)
            continue
        patchDate=[int(n) for n in patch[dataIndex][dateIndex].split('-')]
        patchDate=date(patchDate[year], patchDate[month], patchDate[day])
        if patchDate>startDate:
            continue
        elif startDate>=patchDate and patchDate>=endDate:
            requiredPatchList.append(patch)
        else:
            break
    return requiredPatchList
