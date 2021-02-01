import os

if not os.path.exists("Downloads"):
    os.mkdir("Downloads")
downloadDir =  os.path.join(os.getcwd(), "Downloads") # Directory
mainSite = 'https://ntulearn.ntu.edu.sg'
chromedriver = r'C:\Users\shyma\Desktop\Github\Projects\Blackboard\chromedriver.exe' # Location of chromedriver.exe (Google and download it if you do not have it)
downloadSleepTime = 1 # No built-in function in selenium to wait for download to finish. If there are potential big downloads, increase this before os attempts to move it to appropriate location

# Input your module name and page itemLink. See the following for example:
# startFolder = ['BE2601', 'AB3601']
# startLink = ['https://ntulearn.ntu.edu.sg/webapps/blackboard/content/listContent.jsp?course_id=_327806_1&content_id=_2342882_1&mode=reset',
#              'https://ntulearn.ntu.edu.sg/webapps/blackboard/content/listContent.jsp?course_id=_327744_1&content_id=_2339923_1&mode=reset']
