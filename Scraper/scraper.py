import instaloader
import helpers
import glob
import os

# Create an instaloader object to work wtih
L = instaloader.Instaloader()

# List of usernames to download
string_list = ["wraith________", "moss.meadows"]
profile_list = []
post_timestamps = {}

# Iterate through the list of usernames and create profiles to download later
for profile in string_list:
    profile_list.append(instaloader.Profile.from_username(L.context, profile))

# Grab the current timestamps since last downloaded to compare if updated after the download
for username in string_list:
    post_timestamps[username] = instaloader.LatestStamps('./latest-stamps.ini').get_last_post_timestamp(username)

# Download the profile and filter using regular expressions for the phrases books open, opening books, etc. 
# Filter out closed for instances where it mentions both closed books but opening at a later date
# With the latest_stamps option it only downloads most recent posts since last download
L.download_profiles(profiles=profile_list,
post_filter=lambda post: not "closed" in helpers.post_filter_helper(post),
latest_stamps=instaloader.LatestStamps('./latest-stamps.ini'))

#Check if post timestamp is equal to current one in the ini file and if its not then send the post
# to the discord bot. Currently this is a messy way of doing it and the plan is to get rid of all files
# after it posts to discord so it only needs to fetch the single .txt file in the folder.
for username in string_list:
    if post_timestamps[username] != instaloader.LatestStamps('./latest-stamps.ini').get_last_post_timestamp(username):
        file_list = glob.glob('I:/Documents/Coding_Projects/Insta_scraper/Scraper/' + username +'/*.txt')
        recent_file = min(file_list, key=os.path.getctime)
        file = open(recent_file, 'r', encoding="utf8")
        caption = file.read()
        file.close()
        helpers.discord_notify(caption, username)