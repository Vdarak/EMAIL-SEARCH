import imaplib
import email
# I used the word weekly instead of congratulations.
# However when you run this code you can change the word to your desired choice.
# you can use your own gmail id & password (line 29)
# if an error comes due to 2 factor authentication login accounts then you might need to use an app password which can be generated in gmail settings

def get_weekly_mails(username, password):
    # Connect to the email server
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)
    mail.select("inbox")

    # Searching for last 10 emails
    result, data = mail.search(None, "ALL")
    ids = data[0].split()
    ids = ids[-10:]

    # Fetching the subject of the emails
    for i in ids:
        result, data = mail.fetch(i, "(RFC822)")
        for response in data:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                subject = msg["Subject"]
                if "weekly" in subject.lower():
                    print(subject)
                else : print ("given word not found in subject")

get_weekly_mails("username", "password")
