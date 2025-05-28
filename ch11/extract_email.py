import re


def extract_email_parts(text):
    emails = re.findall(r"([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})", text)
    return emails


result = extract_email_parts(
    "Reach me at felipe.dev@vtex.com or hello@openai.org andres.felipe-m23@gmail.com"
)
test = """
Contact us at support@example.com, jane.doe@sub.mail-server.org,
or help@weird-domain123.co.uk! Don't write to fake@.com or invalid@server.
"""

print(result)
print(extract_email_parts(test))
