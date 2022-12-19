import instaloader
import helpers
import glob
import shutil

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
# to the discord bot. After the notification is sent we delete the directory to clean up the space
for username in string_list:
    if post_timestamps[username] != instaloader.LatestStamps('./latest-stamps.ini').get_last_post_timestamp(username):
        path = 'I:/Documents/Coding_Projects/Insta_scraper/Scraper/'
        recent_file = glob.glob(path + username +'/*.txt')
        with open(recent_file.pop(), 'r', encoding="utf8") as file:
            caption = file.read()
        try:
            shutil.rmtree(path + username)
        except:
            print("chump")
        helpers.discord_notify(caption, username)