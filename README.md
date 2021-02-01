# Blackboard Scraper

### Description

Script made to scrape brochures from NTU's Career Fair (iFair).

Note that this repository is fairly large in size (800mb) as a result of scraped Brochures included. Do download only relevant script if required, or download brochures at **Brochures** folder for the scraped files.

*Peek at interface of Selenium:*
![Edit the system environment variables](./images/blackboard.gif )
[![iFair Scrape Demo](http://img.youtube.com/vi/NZfdPJsgTvs/0.jpg)](http://www.youtube.com/watch?v=NZfdPJsgTvs "iFairScrapeDemo")


## Table of content
1. Features
2. How to use
3. Explanation

## 1. Features
- Create folders for each company
- Download brochures and place in respective files
- Complete process from login to end

## 2. How to use

### 2.1. Clone repository

Firstly, **clone** this repository locally into your machine.

Do note again that you can download the script individually if you do not require Brochures.

### 2.2. Dependencies

Secondly, ensure that you have the **required dependencies** of selenium and bs4. It can easily be obtained through `pip install -r requirements.txt` or

```
pip install selenium
pip install beautifulsoup4
```
### 2.3. Environment variables

It is often not good practice to leave credentials in any script. This can be circumvented through using **environment variables**.
- For Windows, Go to Start -> Edit the system environment variables

![Edit the system environment variables](./images/startEnviron.png )

- Advanced -> Environment Variables...

![Environment variables](./images/startEnviron2.png )

- Under user variables, create variables **bbUser** and **bbPass** for username and password for Blackboard respectively. Alternatively, you can rename variable names under *mySelenium.py* and customize your user environment variables.

![User variables](./images/startEnviron3.png )

### 2.4. Script variables

There might be a few **variables** I believe that differ from schools to schools, despite using the same Blackboard platform. Do edit the variables inside *variables.py* accordingly:
1. `chromedriver`

The location of the file *chromedriver.exe*. The file is included in this repository, but do Google for the latest update of it if you wish.

2. `downloadSleepTime`

Selenium has no built-in function to understand whether a file has completed the download or not. Hence, the script downloads files or attachments and immediately moves them after the sleep timer interval, where a short sleep time will suffice for small files. However, do consider increasing the sleep timer if the script fails or you anticipate there are large files.

### 2.5 Run

Finally, just execute *run.py*. Files like *bs4Test.py* is optional.

## 3. Note

I am not responsible for anyone's usage or abuse of this method.

Please use this and any other scraping methods responsibly.
