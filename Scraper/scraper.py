import instaloader
import re

L = instaloader.Instaloader()


#kait.drawsthings
# Replace this with login we need
#L.login(USER, PASSWORD) 
#L.interative_login(USER)
#L.load_session_from_file(USER)

# Currently Hardcoded to Kaits profile - Change to list eventually
profile = instaloader.Profile.from_username(L.context, "kait.drawsthings")

# Download the profile and filter using regular expressions for the phrases books open, opening books, etc. 
# Can clean this up later for a better regular expression but try this for now

L.download_profiles(profile.get_posts(), 
post_filter=lambda post: re.search("(books)+.*(open)+|(open)+.*(books)+|(opening)+.*(books)+|(books)+.*(opening)+", post.caption.lower()),
max_count=1)

for post in profile.get_posts():
    L.download_post(post, "kait.drawsthings")

# Store data
#profile.storeData()

# Filter Data
#profile.FilterData()

