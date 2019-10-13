from urls import *
import requests
from bs4 import BeautifulSoup

def fetchPatchList():

    patchList=[]
    patchListHyperlinks=[]
    nextPageExists=True
    currentPage=0

    while nextPageExists:
        currentPage=currentPage+1
        print("Fetching Page "+str(currentPage)+"..........")
        pageDataRaw=requests.get(webUrl+patchListUrl+pageUrl+str(currentPage))
        print("Processing Page "+str(currentPage)+"..........")
        pageData=BeautifulSoup(pageDataRaw.text, "html.parser")
        table=pageData.find("table")

        if currentPage==1:
            tableHead=table.find("thead").find("tr").find_all("th")
            patchListHead=[]
            patchListHeadData=[]
            patchListHyperlinksHead=[]

            for element in tableHead:
                patchListHyperlinksHead.append('')
                patchListHeadData.append(element.text.strip())

            patchListHead.append(patchListHeadData)
            patchListHead.append(patchListHyperlinksHead)
            patchList.append(patchListHead)

        tableBody=table.find("tbody")
        tableRows=tableBody.find_all("tr")

        for row in tableRows:
            rowData = row.find_all("td")
            patchListRowEntry=[]
            patchListRowEntryData=[]
            patchListHyperlinksRowEntry=[]

            for element in rowData:
                hyperlink=element.find('a')
                if str(hyperlink)=="None":
                    patchListHyperlinksRowEntry.append('')
                elif hyperlink.attrs["href"][0]=='?':
                    patchListHyperlinksRowEntry.append(webUrl+patchListUrl+hyperlink.attrs["href"])
                else:
                    patchListHyperlinksRowEntry.append(webUrl+hyperlink.attrs["href"])

                patchListRowEntryData.append(element.text.strip())

            patchListRowEntry.append(patchListRowEntryData)
            patchListRowEntry.append(patchListHyperlinksRowEntry)
            patchList.append(patchListRowEntry)

        if str(pageData.find(attrs={"class":"next"}))=="None":
            nextPageExists=False

    return patchList
