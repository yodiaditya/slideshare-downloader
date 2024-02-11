#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys, os
import img2pdf
import re
import requests

from time import localtime, strftime
from os import listdir, walk
from os.path import isfile, join

try: from urllib.request import urlopen #python3
except ImportError: from urllib2 import urlopen #python2
try: from bs4 import BeautifulSoup #python3
except ImportError: from BeautifulSoup import BeautifulSoup #python2
try: input = raw_input #python2
except NameError: pass #python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time 

CURRENT = os.path.dirname(__file__)

options = Options()

# options.headless = True
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome("/snap/bin/chromium.chromedriver", options=options)

def download_images(url):
    # html = requests.get(url).content
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # modify this depend on your internet connection and the size of the slides
    time.sleep(5)

    # Get the page source after interactions
    page_source = driver.page_source.encode('utf-8')

    soup = BeautifulSoup(page_source, 'html.parser')
    title = '_'.join(( '/tmp/pdf_images', strftime("%Y/%m/%d_%H:%M:%S", localtime()) ))  #soup.title.string
    images = soup.findAll('source', {'data-testid':'slide-image-source'})

    print(images)

    driver.quit()

    i = 1

    for image in images:
        image_url = image.get('srcset').split('w, ')[-1].split(' ')[0]

        # command = "wget '%s' -P '%s' --no-check-certificate" % (image_url, title)
        # os.system(command)
        r = requests.get(image_url)

        if not os.path.exists(title):
            os.makedirs(title)
    
        filename = str(i) + ".jpg"
        i += 1
    
        with open(title + "/"+ filename, 'wb') as f:
            f.write(r.content)

    convert_pdf(title)

def convert_pdf(img_dir_name):
    f = []
    for (dirpath, dirnames, filenames) in walk(join(CURRENT, img_dir_name)):
        f.extend(filenames)
        break
    f = ["%s/%s" % (img_dir_name, x) for x in f]
    
    def atoi(text):
        return int(text) if text.isdigit() else text

    def natural_keys(text):
        '''
        alist.sort(key=natural_keys) sorts in human order
        http://nedbatchelder.com/blog/200712/human_sorting.html
        (See Toothy's implementation in the comments)
        '''
        return [ atoi(c) for c in re.split('(\d+)', text) ]

    f.sort(key=natural_keys)
    
    print(f)

    pdf_bytes = img2pdf.convert(f, dpi=300, x=None, y=None)
    doc = open(pdf_f, 'wb')
    doc.write(pdf_bytes)
    doc.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = " ".join(sys.argv[1:])
    else:
        url = input('Slideshare URL: ').strip()
    if (url.startswith("'") and url.endswith("'")) or (url.startswith('"') and url.endswith('"')):
        url = url[1:-1]
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    pdf_f = re.sub('[^0-9a-zA-Z]+', '_', url.split("/")[-1]) #get url basename and replace non-alpha with '_'
    if pdf_f.strip() == '':
        print("Something wrong to get filename from URL, fallback to result.pdf")
        pdf_f = "result.pdf"
    else:
        pdf_f+=".pdf"

    download_images(url)


