# Insta_scraper
Instagram Scraper

## Introduction:
This repository was made to search the Instagram posts of my wife's favourite tattoo artists and then notify via discord if any of them are opening their books for appointments. 

## Libraries used:

```
instaloader
discordwebhook
re
glob
shutil
```

## Meat & Bones:
This project uses the `instaloader` module to do the heavy lifting of downloading the profiles and posts of the various usernames. Once it finds a new post related to books opening it sends a discord message to let me know. I chose discord because it is on my phone and I am on it enough that I should not miss the message. 

The script was then automated used the task scheduler from Windows to run every hour.

One thing to note is that Instagram does not enjoy a large amount of calls to their server and will ban IP addresses if abused.