import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import os, re, time, shutil
from variables import *
from mySelenium import loginToHome

driver = loginToHome()

# Recursively look for folders, downloading items
def recursiveFolder(folderLink):
    # getting the request from url
    driver.get(folderLink[1])
    # converting the text
    # s = BeautifulSoup(r.text,"html.parser")
    elem = driver.find_element_by_xpath("//*")
    html = elem.get_attribute("outerHTML")
    soup = BeautifulSoup(html, 'html.parser')
    folders = soup.find('div',{'class':'container clearfix'}).find("ul", {"id":"content_listContainer"}).findAll("li", {"class":"clearfix liItem read"})
    for folder in folders:
        if folder.find("img").get("alt") == "Item" or folder.find("img").get("alt") == "File":
            name = folder.find("a").text.replace(u'\xa0', u'')
            link = mainSite + folder.find("a").get('href')
            itemText.append(name)
            itemLink.append(link)
            driver.get(link) # Download
            time.sleep(downloadSleepTime) # No built-in function in selenium to wait for download to finish
            filename = max([downloadDir + "\\" + f for f in os.listdir(downloadDir)],key=os.path.getctime) # Downloaded file name can be different from item name
            nameWithoutDir = re.findall(r"^.+\\([^\/]+)$", filename)[0]
            if not os.path.exists(os.path.join(os.path.join(os.getcwd(), folderLink[0]), nameWithoutDir)):
                os.rename(filename, os.path.join(os.path.join(os.getcwd(), folderLink[0]), nameWithoutDir)) # Shift downloaded file
        elif folder.find("img").get("alt") == "Content Folder":
            currentName = folderLink[0] + "\\" + folder.find("a").text.replace(u'\xa0', u'')
            currentName = re.sub(r'[^\w\s\\-]', '', currentName)
            if not os.path.exists(currentName):
                 os.makedirs(currentName)
            currentLink = mainSite + folder.find("a").get('href')
            contentFolderText.append(currentName)
            contentFolderLink.append(currentLink)
            recursiveFolder((currentName, currentLink))

contentFolderText, contentFolderLink, itemText, itemLink, lamsText, lamsLink, misc = [[] for i in range(7)]
[contentFolderText.append(i) for i in startFolder] # Directory
[contentFolderLink.append(i) for i in startLink] # First site
contentFolderTextLink = [(k, v) for k, v in zip(contentFolderText, contentFolderLink)]
[recursiveFolder((k,v)) for k, v in contentFolderTextLink]

# Clears downloads folder after process is complete
shutil.rmtree(downloadDir)
#
# files = glob.glob(downloadDir)
# for f in files:
#     os.remove(f)
print("Process is completed.")
