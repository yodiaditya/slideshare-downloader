# Slideshare Downloader

Download Slideshare without login and converted into pdf with high-resolution automatically.

## Environment
This code tested on Ubuntu 23.04 and Python 3.10. The requirement needed are

**1. Chromium**

```sudo snap install chromium```

**2. Check Chromium.chromedriver is executable**

```/snap/bin/chromium.chromedriver```

## Installation

```
git clone https://github.com/yodiaditya/slideshare-downloader.git
pip3 install -r requirements.txt
```

## How to use

```
python slideshare2pdf.py [url]
```

This will open chromium browser and automatically scroll-down to load all the slides. 

Example:
```
python slideshare2pdf.py https://www.slideshare.net/JiangweiPan/reward-innovation-for-longterm-member-satisfaction
```

See the result: [reward_innovation_for_longterm_member_satisfaction.pdf](reward_innovation_for_longterm_member_satisfaction.pdf)

## Notes 
This is not working with ```headless=True```. You can use VM to run the browser.