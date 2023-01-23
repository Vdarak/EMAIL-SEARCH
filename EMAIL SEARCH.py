import imaplib
import email

def get_weekly_mails(username, password):
    # Connect to the email server
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)
    mail.select("inbox")

    # Search for recent congratulations emails
    result, data = mail.search(None, "ALL")
    ids = data[0].split()
    ids = ids[-10:]

    # Fetch the subject of the emails
    for i in ids:
        result, data = mail.fetch(i, "(RFC822)")
        for response in data:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                subject = msg["Subject"]
                if "security" in subject.lower():
                    print(subject)
                else : print ("given word not found in subject")

get_weekly_mails("2017.vedant.darak@ves.ac.in", "qhcnkdsehdcdzlrq")
