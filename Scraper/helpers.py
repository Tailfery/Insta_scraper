import re
from discordwebhook import Discord

# Regex pattern for searching the posts
pattern = "(books)+.*(open)+|(open)+.*(books)+|(opening)+.*(books)+|(books)+.*(opening)+"
# Discord object using the webhook given for a server
discord = Discord(url="https://discord.com/api/webhooks/1053724148054114376/qpZY98-hAEWl0qfxw1Lav2heLZP7t5xyL9WhltfsYBoJuMiDG2YuMKNSY1IYZSdz_oBw")

# Short little helper to clean up code in the download_profiles step
def post_filter_helper(post):
    # First have to check if the pattern is even there and to reject matches that return None
    if post.caption != None:
        match_object = (re.search(pattern, post.caption.lower()))
        if match_object != None:
            return match_object.group()


# For posting to Discord for notifying when books are open
def discord_notify(caption, name):
    discord.post(embeds=[
        {
            "author": {
                "name": name
            },
            "title": "Books are open!",
            "description": caption,
        }
    ]
    )
    return True