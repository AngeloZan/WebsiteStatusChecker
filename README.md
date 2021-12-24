# WebsiteStatusChecker
 A simple bot using python to check a website status

## Setup
I have basically two more files (not commited) in the root directory: *my_sites.json* and *.env*. They look like this:

### my_site.json
```
[
    "https://...",
    "https://...",
    "https://..."
]
```

i.e. just an array containing all of my websites url's.


### .env
```
SENDER=...
SENDER_PWD=...
SMTP_SERVER=...
EMAIL_USE_TLS=True
SMTP_PORT=...
RECEIVER=...
```


This file stores all the sensiteve data.

**SENDER** is the email address that is going to send status update messages to **RECEIVER**.
**SENDER_PWD** is the password for sender address.
