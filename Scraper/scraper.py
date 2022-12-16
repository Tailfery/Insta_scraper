import instaloader
import helpers

L = instaloader.Instaloader()


#kait.drawsthings
# Replace this with login we need
#L.login(USER, PASSWORD) 
#L.interative_login(USER)
#L.load_session_from_file(USER)

# List of usernames to download
string_list = ["wraith________", "moss.meadows"]
profile_list = []


# Currently Hardcoded to Kaits profile - Change to list eventually
for profile in string_list:
    profile_list.append(instaloader.Profile.from_username(L.context, profile))


# Download the profile and filter using regular expressions for the phrases books open, opening books, etc. 
# Can clean this up later for a better regular expression but try this for now
# Filter out closed for instances where it mentions both closed books but opening at a later date

L.download_profiles(profiles=profile_list,
post_filter=lambda post: not "closed" in helpers.post_filter_helper(post))


# for post in profile.get_posts():
#    L.download_post(post, "kait.drawsthings")

# Store data
#profile.storeData()

# Filter Data
#profile.FilterData()

