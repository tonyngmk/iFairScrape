import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import os, re, time, shutil
from variables import *
from mySelenium import loginToHome
import urllib

driver = loginToHome()
for hallNo in range(1, 17):
    driver.get(f"https://ifair.ntu.edu.sg/hall/pg/{hallNo}")
    elem = driver.find_element_by_xpath("//*")
    html = elem.get_attribute("outerHTML")
    soup = BeautifulSoup(html, 'html.parser')
    folders = soup.find('div',{'class':'row white center booths-listing'}).findAll('div', {"class":"col-5l col-4m col-6s left booth"})
    for folder in folders:
        folderName = folder.find('h3').text
        folderName = re.sub(r'[^\w\s\\-]', '', folderName)
        folderName = folderName.strip()
        # if not os.path.exists(os.path.join  (os.path.join(os.getcwd(), "Downloads"), folderName)):
        #     os.rename(filename, os.path.join(os.path.join(os.getcwd(), folderLink[0]), nameWithoutDir)) # Shift downloaded file
        if not os.path.exists(os.path.join("Brochures", folderName)):
             os.makedirs(os.path.join("Brochures", folderName))
        folderUrl = folder.find("a").get('href')
        folderUrl = re.findall(r"\.(.*)", folderUrl)[0]
        folderUrl = "https://ifair.ntu.edu.sg/" + folderUrl
        driver.get(folderUrl)
        brochuresPath = '//*[@id="exhibitor-brochures"]'
        element = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(brochuresPath))
        driver.execute_script("arguments[0].click();", element)
        # Downloading brochures
        time.sleep(1) # Wait for JS to execute
        elem2 = driver.find_element_by_xpath("//*")
        html2 = elem2.get_attribute("outerHTML")
        # soup2 = BeautifulSoup(html2, 'html.parser')
        # html2 = driver.execute_script("return document.documentElement.innerHTML;")
        html2 = html2.replace(u'\u2715', u'')
        soup2 = BeautifulSoup(html2, 'html.parser')
        brochures = soup2.find('div',{'class':'tabbed-content selected cf'}).findAll('li')
        for brochure in brochures:
            try:
                itemName = brochure.find("a").get('title')
                itemName = re.sub(r'[^\w\s\\\.-]', '', itemName)
                itemUrl = brochure.find("a").get('href')
                itemUrl = re.findall(r"\.(.*)", itemUrl)[0]
                itemUrl = "https://ifair.ntu.edu.sg/" + itemUrl
                if itemName.endswith(".pdf"):
                    driver.get(itemUrl)
                    time.sleep(downloadSleepTime) # No built-in function in selenium to wait for download to finish
                    filename = max([downloadDir + "\\" + f for f in os.listdir(downloadDir)],key=os.path.getctime) # Downloaded file name can be different from item name
                    if not os.path.exists(os.path.join(os.path.join(os.path.join(os.getcwd(), "Brochures"), folderName), itemName)):
                        try:
                            os.rename(filename, os.path.join(os.path.join(os.path.join(os.getcwd(), "Brochures"), folderName), itemName)) # Shift downloaded file
                            print("File moved:\n", filename, "to\n", os.path.join(os.path.join(os.path.join(os.getcwd(), "Brochures"), folderName), itemName))
                        except (FileNotFoundError, PermissionError): # Download has not completed
                            time.sleep(5)
                            filename = max([downloadDir + "\\" + f for f in os.listdir(downloadDir)],key=os.path.getctime) # Downloaded file name can be different from item name
                            os.rename(filename, os.path.join(os.path.join(os.path.join(os.getcwd(), "Brochures"), folderName), itemName)) # Shift downloaded file
                            print("File moved:\n", filename, "to\n", os.path.join(os.path.join(os.path.join(os.getcwd(), "Brochures"), folderName), itemName))

            except AttributeError: # Currently, there are no brochures available.
                pass

# Clears downloads folder after process is complete
shutil.rmtree(downloadDir)
#
# files = glob.glob(downloadDir)
# for f in files:
#     os.remove(f)
print("Process is completed.")
