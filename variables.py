import os

url = "https://loginfs.ntu.edu.sg/adfs/ls/?SAMLRequest=lVJda8IwFP0r4b73U4UabMVNZILDYuse9hbbW81oE5ebyn7%2BalWmL8IghIScc8%2B952Qy%2FWlqdkJDUqsYAtcHhqrQpVT7GLb5wolgmkxINHV45LPWHtQGv1skyzqiIn55iaE1imtBkrgSDRK3Bc9m7yseuj4%2FGm11oWtgMyI0tpN61YraBk2G5iQL3G5WMRysPRL3PGXbGoVRbndwsWxd2nuiU3bOWl6%2FZdka2LzrQiph%2B85v5FrvparogVtW5NXkAVtoU2A%2FRAyVqAmBLecxiKEfRZUYDqrBAMdfYVChX45EcRAhBrthB6JUEMkT%2FtGIWlwqskLZGEI%2FDBw%2FcEI%2F9wN%2BXiN3HESfwNLr6C9SXSx95tPuAiL%2Bluepk66zHNjHLZoOANcgeK9u7hN4XljcbIfkfyZPvHvB5Hp9%2FAjJLw%3D%3D&SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&Signature=Yh8bl8Evof4333f%2FgUkeH20tt%2FDN0vuBlI3K5ojVVFPD7gigSlBqrsBEoPbX7NpSRoByM8BmXrleR5eH00ziRmlpB20gD2dJcNocX1tlRPufCKITt7cFCd%2Boib5Br31QllHVrcToW8fqWG%2BK4PwHi0zg8GiOtQqNZ3wg734Cj0L0epBdmyGgX5S5YYvNzrG03RnYF%2FRK9xJrKyxatRqC051POgo5GyLYXz4XZSqPIWtBL4SHjwzzHnYZu%2Bl%2Bi%2FlUEfhw8pUH3iS5oFsKoUjuGsq1A59UuE0u9NDwz9apfBeoVaEmAiLuWPLs%2Fr9nRWJtlRQiHVeJ5hGadRK%2FF3qCvg%3D%3D"
if not os.path.exists("Downloads"):
    os.mkdir("Downloads")
downloadDir =  os.path.join(os.getcwd(), "Downloads") # Directory
ntuLearn = 'https://ntulearn.ntu.edu.sg'
chromedriver = r'C:\Users\shyma\Desktop\Github\Projects\Blackboard\chromedriver.exe' # Location of chromedriver.exe (Google and download it if you do not have it)
downloadSleepTime = 1 # No built-in function in selenium to wait for download to finish. If there are potential big downloads, increase this before os attempts to move it to appropriate location


# Input your module name and page itemLink. See the following for example:
startFolder = ['BE2601', 'AB3601']
startLink = ['https://ntulearn.ntu.edu.sg/webapps/blackboard/content/listContent.jsp?course_id=_327806_1&content_id=_2342882_1&mode=reset',
             'https://ntulearn.ntu.edu.sg/webapps/blackboard/content/listContent.jsp?course_id=_327744_1&content_id=_2339923_1&mode=reset']
