#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import img2pdf

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
        command = 'wget %s -P %s' % (image_url, title)
        os.system(command)

    convert_pdf(title)

def convert_pdf(url):
    f = []
    for (dirpath, dirnames, filenames) in walk(join(CURRENT, url)):
        f.extend(filenames)
        break
    f = ["%s/%s" % (url, x) for x in f]
    print f

    pdf_bytes = img2pdf.convert(f, dpi=300, x=None, y=None)
    doc = open('result.pdf', 'wb')
    doc.write(pdf_bytes)
    doc.close()

if __name__ == "__main__":
    url = raw_input('Slideshare URL : ')
    download_images(url)