import urllib2
from bs4 import BeautifulSoup

def extractMData(webpage):
    soup = BeautifulSoup(webpage, "html.parser")
    divBlock = soup.findAll("div", {"class":"block"})
    info = divBlock[3]
    getLeft = info.findAll("div", {"class":"info_left"})
    getRight = info.findAll("div", {"class":"info_right"})
    # print soup.title
    # print divBlock[3]
    # print getLeft
    # print getRight
    for i in range(0,len(getLeft)):
        textLeft = getLeft[i].get_text()
        textRight = getRight[i].get_text()
        print textLeft + ": " + textRight
    print ""

# Open webpage
webpage = urllib2.urlopen("http://inadaybooks.com/justiceleague/")

# print BeautifulSoup(webpage)

# Convert to BeautifulSoup
soup = BeautifulSoup(webpage, "html.parser")
## print soup.title
## print soup.body

# Get the contents container div
divContainer = soup.find("div", {"id":"container"})
## print divContainer

divBlock = divContainer.findAll("div", {"class":"block"})
## print divBlock[3]

divSep = divBlock[3].findAll("div", {"class":"separator"})
## print divSep

members = divSep[3].findAll("a")
## print members

# # Loop through members
# for member in members:
#     # Strip <a> tags
#     # print member.get_text()
#     print member.get("title")
#     # print member.get("href")

# Actually Web Crawling
for member in members:
    # Strip <a> tags
    hrefMike = member.get("href")
    # Create URL to open
    urlMike = "http://inadaybooks.com/justiceleague/"+hrefMike
    # Open URL
    pageMike = urllib2.urlopen(urlMike)

    extractMData(pageMike)



