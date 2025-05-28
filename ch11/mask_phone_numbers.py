import re


def mask_phone_number(text):
    pattern = r"(\(?\b\d{3}\)?[-\s]\d{3}[-\s]\d{2})(\d{2}\b)"
    masked_version = re.sub(
        pattern, lambda m: re.sub(r"\d", "*", m.group(1)) + m.group(2), text
    )
    print(masked_version)


text = "Call me at 321-555-1234"  # Match
text2 = "Call me at 3221-555-1234"  # Not match
text3 = "Call me at 322-5556-1234"  # Not match
text4 = "Call me at 321-555-12345"  # Not match
text5 = "Call me at 321-555-1234 or 321-555-1234"  # Match
text6 = "Call me at 321-555-1234 or (123) 456-7890"  # Match
text6 = "Call me at 321-555-1234 or (1.23) 456-7890"  # Not Match

mask_phone_number(text)
mask_phone_number(text2)
mask_phone_number(text3)
mask_phone_number(text4)
mask_phone_number(text5)
mask_phone_number(text6)
