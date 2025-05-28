import re


def extract_hashtags(text):
    return re.findall(r"(?<!\w)(#\w+\b)", text, re.IGNORECASE)


print(extract_hashtags("Here's #fun and #exciting123 and #cool! and #Wow about#face"))
