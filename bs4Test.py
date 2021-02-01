from bs4 import BeautifulSoup
import os, re


# Creating folders
# url = r"C:\Users\shyma\Desktop\Github\Projects\iFair\iFair.html"
# soup = BeautifulSoup(open(url, encoding="utf-8"), "html.parser")
# folders = soup.find('div',{'class':'row white center booths-listing'}).findAll('div', {"class":"col-5l col-4m col-6s left booth"})
# for folder in folders:
#     folderName = folder.find('h3').text
#     folderName = re.sub(r'[^\w\s\\-]', '', folderName)
#     # if not os.path.exists(os.path.join  (os.path.join(os.getcwd(), "Downloads"), folderName)):
#     #     os.rename(filename, os.path.join(os.path.join(os.getcwd(), folderLink[0]), nameWithoutDir)) # Shift downloaded file
#     if not os.path.exists(os.path.join("Downloads", folderName)):
#          os.makedirs(os.path.join("Downloads", folderName))
#     folderUrl = folder.find("a").get('href')
#     print(folderUrl)

# Finding brochuresPath
url = r"C:\Users\shyma\Desktop\Github\Projects\iFair\Brochures.html"
soup = BeautifulSoup(open(url, encoding="utf-8"), "html.parser")
brochures = soup.find('div',{'class':'tabbed-content selected cf'}).findAll('li')
for brochure in brochures:
    itemUrl = brochure.find("a").get('href')
    itemUrl = re.findall(r"\.(.*)", itemUrl)[0]
    itemUrl = "https://ifair.ntu.edu.sg/" + itemUrl
    print(itemUrl)
    print(brochure.find('a').get('title'))
