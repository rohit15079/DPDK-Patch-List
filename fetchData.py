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
        pageDataRaw=requests.get(webUrl+patchListUrl+pageUrl+str(currentPage))
        pageData=BeautifulSoup(pageDataRaw.text, "html.parser")
        table=pageData.find("table")

        if currentPage==1:
            tableHead=table.find("thead").find("tr").find_all("th")
            patchListHead=[]
            patchListHyperlinksHead=[]

            for element in tableHead:
                hyperlink=element.find('a')
                patchListHyperlinksHead.append('')
                patchListHead.append(element.text.strip())

            patchList.append(patchListHead)
            patchListHyperlinks.append(patchListHyperlinksHead)

        tableBody=table.find("tbody")
        tableRows=tableBody.find_all("tr")

        for row in tableRows:
            rowData = row.find_all("td")
            patchListRowEntry=[]
            patchListHyperlinksRowEntry=[]

            for element in rowData:
                hyperlink=element.find('a')
                if str(hyperlink)=="None":
                    patchListHyperlinksRowEntry.append('')
                elif hyperlink.attrs["href"][0]=='?':
                    patchListHyperlinksRowEntry.append(webUrl+patchListUrl+hyperlink.attrs["href"])
                else:
                    patchListHyperlinksRowEntry.append(webUrl+hyperlink.attrs["href"])

                patchListRowEntry.append(element.text.strip())

            patchList.append(patchListRowEntry)
            patchListHyperlinks.append(patchListHyperlinksRowEntry)

        if str(pageData.find(attrs={"class":"next"}))=="None":
            nextPageExists=False

    return patchList, patchListHyperlinks
