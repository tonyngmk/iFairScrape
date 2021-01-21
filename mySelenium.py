import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import os, re, time
from variables import *

# Selenium
def loginToHome():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {
        "download.default_directory": downloadDir, #Change default directory for downloads
        "download.prompt_for_download": False, # Auto download files
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
    })
    driver = webdriver.Chrome(executable_path = chromedriver, chrome_options=options)  # Or Chrome(), or Ie(), or Opera()
    driver.get(url)
    # Login page
    username = driver.find_element_by_id("userNameInput")
    password = driver.find_element_by_id("passwordInput")
    username.send_keys(os.environ['bbUser'])
    password.send_keys(os.environ['bbPass'])
    driver.find_element_by_id("submitButton").click()

    # Error Prompt
    driver.get("https://ntulearn.ntu.edu.sg/auth-saml/saml/redirectToLearn")
    element = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath('//*[@id="agree_button"]'))
    driver.find_element_by_xpath('//*[@id="agree_button"]').click()
    return driver

# def recursiveFolder(folderLink, driver):
#     # getting the request from url
#     global contentFolderText, contentFolderLink, itemText, itemLink, lamsText, lamsLink, misc
#     driver.get(folderLink[1])
#     # converting the text
#     # s = BeautifulSoup(r.text,"html.parser")
#     elem = driver.find_element_by_xpath("//*")
#     html = elem.get_attribute("outerHTML")
#     soup = BeautifulSoup(html, 'html.parser')
#     folders = soup.find('div',{'class':'container clearfix'}).find("ul", {"id":"content_listContainer"}).findAll("li", {"class":"clearfix liItem read"})
#     for folder in folders:
#         if folder.find("img").get("alt") == "Item":
#             name = folder.find("a").text.replace(u'\xa0', u'')
#             link = ntuLearn + folder.find("a").get('href')
#             itemText.append(name)
#             itemLink.append(link)
#             driver.get(link) # Download
#             time.sleep(1) # No built-in function in selenium to wait for download to finish
#             filename = max([downloadDir + "\\" + f for f in os.listdir(downloadDir)],key=os.path.getctime) # Downloaded file name can be different from item name
#             if not os.path.exists(os.path.join(os.path.join(os.getcwd(), folderLink[0]), name)):
#                 os.rename(filename, os.path.join(os.path.join(os.getcwd(), folderLink[0]), name)) # Shift downloaded file
#         elif folder.find("img").get("alt") == "Content Folder":
#             currentName = folderLink[0] + "\\" + folder.find("a").text.replace(u'\xa0', u'')
#             currentName = re.sub(r'[^\w\s\\-]', '', currentName)
#             if not os.path.exists(currentName):
#                  os.makedirs(currentName)
#             currentLink = ntuLearn + folder.find("a").get('href')
#             contentFolderText.append(currentName)
#             contentFolderLink.append(currentLink)
#             recursiveFolder((currentName, currentLink))
