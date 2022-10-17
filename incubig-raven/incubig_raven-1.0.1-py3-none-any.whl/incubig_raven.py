from email import message
from azure.communication.email import EmailClient, EmailContent, EmailMessage, EmailAttachment, EmailRecipients, EmailAddress
from azure.core.credentials import AzureKeyCredential
from decouple import config
import logging
import base64

def send_raven(**kwargs):
#Connecting with client
    try:
        credential = AzureKeyCredential(config("RAVEN_KEY"))
        endpoint = config("RAVEN_ENDPOINT")
        client = EmailClient(endpoint, credential)
    except:
        client = EmailClient(kwargs["endpoint"], kwargs["credential"])

    content = EmailContent(
        subject=kwargs["email_content"]["subject"],
        plain_text=kwargs["email_content"]["body"],
        html= kwargs["email_content"]["html"],
    )

    if (("cc" in kwargs["email_recipients"]) and ("bcc" in kwargs["email_recipients"])):
        recipients = EmailRecipients(
            to=[
                EmailAddress(email=recipient["email"], display_name=recipient["name"]) for recipient in kwargs["email_recipients"]["to"]
            ],
            cc=[
                EmailAddress(email=recipient["email"], display_name=recipient["name"]) for recipient in kwargs["email_recipients"]["cc"]
            ],
            bcc=[
                EmailAddress(email=recipient["email"], display_name=recipient["name"]) for recipient in kwargs["email_recipients"]["bcc"]
            ],
        )
    elif ("cc" in kwargs["email_recipients"]):
        recipients = EmailRecipients(
            to=[
                EmailAddress(email=recipient["email"], display_name=recipient["name"]) for recipient in kwargs["email_recipients"]["to"]
            ],
            cc=[
                EmailAddress(email=recipient["email"], display_name=recipient["name"]) for recipient in kwargs["email_recipients"]["cc"]
            ],
        )
    else:
        recipients = EmailRecipients(
            to=[
                EmailAddress(email=recipient["email"], display_name=recipient["name"]) for recipient in kwargs["email_recipients"]["to"]
            ]
        )

    if "attachment" in kwargs:
        file_bytes_b64 = base64.b64encode(bytes(kwargs["attachment"]["data"], 'utf-8'))

        attachment = EmailAttachment(
            name=kwargs["attachment"]["name"],
            attachment_type="."+kwargs["attachment"]["type"],
            content_bytes_base64=file_bytes_b64.decode()
        )
        message = EmailMessage(sender="solutions@incubig.email", content=content, recipients=recipients,attachments=[attachment])
    else:
        message = EmailMessage(sender="solutions@incubig.email", content=content, recipients=recipients)
    
    response = client.send(message)

    return response.message_id

def raven_status(**kwargs):
    try:
        credential = AzureKeyCredential(config("RAVEN_KEY"))
        endpoint = config("RAVEN_ENDPOINT")
        client = EmailClient(endpoint, credential)
    except:
        client = EmailClient(kwargs["endpoint"], kwargs["credential"])

    message_id = kwargs["message_id"]
    return client.get_send_status(message_id)
