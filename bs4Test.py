from bs4 import BeautifulSoup
import os, re

url = r"C:\Users\shyma\Desktop\Github\Projects\Blackboard\stratMag.html"
contentFolderTextLink = [(k, v) for k, v in zip(["Opening Course Brief"], [url])]
soup = BeautifulSoup(open(url, encoding="utf-8"), "html.parser")
folders = soup.find('div',{'class':'container clearfix'}).find("ul", {"id":"content_listContainer"}).findAll("li", {"class":"clearfix liItem read"})
contentFolderText, contentFolderLink, itemText, itemLink, fileText, fileLink, lamsText, lamsLink, misc = [[] for i in range(9)]

prevFolderName = "Module Files"

for folder in folders:
    if folder.find("img").get("alt") == "Content Folder":
        presentFolderName = folder.find("a").text.replace(u'\xa0', u'')
        afterFolderName = os.path.join(prevFolderName, presentFolderName)
        contentFolderText.append(afterFolderName)
        contentFolderLink.append(folder.find("a").get('href'))
    elif folder.find("img").get("alt") == "Item":
        itemText.append(folder.find("a").text.replace(u'\xa0', u''))
        itemLink.append(folder.find("a").get('href'))
    elif folder.find("img").get("alt")== "File":
        fileText.append(folder.find("a").text.replace(u'\xa0', u''))
        fileLink.append(folder.find("a").get('href'))
    elif folder.find("img").get("alt") == "LAMS Lesson":
        lamsText.append(folder.find("a").text.replace(u'\xa0', u''))
        lamsLink.append(folder.find("a").get('href'))
    else:
        misc.append(folder)

contentFolderTextLink = [(k, v) for k, v in zip(contentFolderText, contentFolderLink)]
itemTextLink = [(k, v) for k, v in zip(itemText, itemLink)]
fileTextLink = [(k, v) for k, v in zip(fileText, fileLink)]
lamsTextLink = [(k, v) for k, v in zip(lamsText, lamsLink)]

print(fileTextLink)
print(misc)



# Content Folder, LAMS Lesson, Item

# # Make folder if not exist
# dir = 'Module Files'
# sourceName = [os.path.join('Module Files', i) for i in folderText]
# sourceName = [re.sub(r'[^\w\s\\-]', '', i) for i in sourceName]
# for folder in sourceName:
#     if not os.path.exists(folder):
#          os.makedirs(folder)
