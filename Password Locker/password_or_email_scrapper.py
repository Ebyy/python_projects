import re, pyperclip

# Create regex for phone numbers
phoneRegex = re.compile(r"""
# 415-555-0000, 555-2345, (234) 762-0000, 333-7280 ext 12345, ext. 26354, x74363
(        
((\d\d\d)|(\(\d\d\d\)))?        # area code (optional)
(\s|-)              # first seperator
 \d\d\d             # first 3 digits
-                   # seperator
\d\d\d\d            # last 4 digits
(((ext(\.)?\s) |x)       # extension word part(optional)
(\d{2,5}))?               # extension number-part (optional)
)
""", re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r"""
# some.+_thing@(\d{2,5})?.com

[a-zA-Z0-9_.+]+            # name part
@            # @ symbol
[a-zA-Z0-9_.+]+            # domain name part
""", re.VERBOSE)
# Get text of the clipboard
text = pyperclip.paste()

# Extract email and text from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []

for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)

pyperclip.copy(results)
print("Phone numbers and email addresses have been copied to clipboard!")