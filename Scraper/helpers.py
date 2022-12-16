import re

pattern = "(books)+.*(open)+|(open)+.*(books)+|(opening)+.*(books)+|(books)+.*(opening)+"

# Short little helper to clean up code in the download_profiles step
def post_filter_helper(post):
    # First have to check if the pattern is even there and to reject matches that return None
    if post.caption != None:
        match_object = (re.search(pattern, post.caption.lower()))
        if match_object != None:
            return match_object.group()