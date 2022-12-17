import instaloader
import helpers
import glob
import os

# Create an instaloader object to work wtih
L = instaloader.Instaloader()


# List of usernames to download
string_list = ["wraith________", "moss.meadows"]
profile_list = []

# Iterate through the list of usernames and create profiles to download later
for profile in string_list:
    profile_list.append(instaloader.Profile.from_username(L.context, profile))


# Download the profile and filter using regular expressions for the phrases books open, opening books, etc. 
# Filter out closed for instances where it mentions both closed books but opening at a later date

L.download_profiles(profiles=profile_list, fast_update=True,
post_filter=lambda post: not "closed" in helpers.post_filter_helper(post))

# Temporarily I have it grabbing the most recent .txt file but eventually should just grab
# the file if its new. It then calls up the discordwebhook module to send out the notification
for username in string_list:
    file_list = glob.glob('I:/Documents/Coding_Projects/Insta_scraper/Scraper/' + username +'/*.txt')
    recent_file = min(file_list, key=os.path.getctime)
    caption = open(recent_file, 'r', encoding="utf8").read()
    helpers.discord_notify(caption, username)
