#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import img2pdf
import re

from os import listdir, walk
from os.path import isfile, join

import urllib2
from BeautifulSoup import BeautifulSoup

CURRENT = os.path.dirname(__file__)

def download_images(url):
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html)
    title = 'pdf_images' #soup.title.string
    images = soup.findAll('img', {'class':'slide_image'})

    for image in images:
        image_url = image.get('data-full').split('?')[0]
        command = 'wget %s -P %s --no-check-certificate' % (image_url, title)
        os.system(command)

    convert_pdf(title)

def convert_pdf(url):
    f = []
    for (dirpath, dirnames, filenames) in walk(join(CURRENT, url)):
        f.extend(filenames)
        break
    f = ["%s/%s" % (url, x) for x in f]
    
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
    
    print f

    pdf_bytes = img2pdf.convert(f, dpi=300, x=None, y=None)
    doc = open('result.pdf', 'wb')
    doc.write(pdf_bytes)
    doc.close()

if __name__ == "__main__":
    url = raw_input('Slideshare URL: ').strip()
    if (url.startswith("'") and url.endswith("'")) or (url.startswith('"') and url.endswith('"')):
        url = url[1:-1]
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    download_images(url)
