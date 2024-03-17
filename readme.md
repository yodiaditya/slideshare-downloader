# Slideshare Downloader

Download Slideshare without login and converted into pdf with high-resolution automatically.

## Environment
This code tested on macOS Big Sur and Python 3.10. The requirement needed are

**Chromium Driver**

- Download Chromium Driver [here](https://googlechromelabs.github.io/chrome-for-testing/) match with your environment (OS, Arch and Chrome Version)
- Extract then copy to any binary path you want. ie: `/opt/local/bin/chromedriver`
- Check permission is readable by everyone


## Installation

```
git clone https://github.com/yodiaditya/slideshare-downloader.git
cd slideshare-downloader
python -m venv venv
source venv/bin/activate
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
