import instaloader

L = instaloader.Instaloader()

#kait.drawsthings
# Replace this with login we need
#L.login(USER, PASSWORD) 
#L.interative_login(USER)
#L.load_session_from_file(USER)

# Currently Hardcoded to Kaits profile - Change to list eventually
profile = instaloader.Profile.from_username(L.context, "kait.drawsthings")

# Get whatever info from posts in a recent timeframe
# Maybe just go since the last call? 24hours?
#profile.get_posts()

for post in profile.get_posts():
    L.download_post(post, "kait.drawsthings")

# Store data
#profile.storeData()

# Filter Data
#profile.FilterData()

