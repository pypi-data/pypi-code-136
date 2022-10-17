from azure.communication.email import EmailClient, EmailContent, EmailMessage, EmailAttachment, EmailRecipients, EmailAddress
from azure.core.credentials import AzureKeyCredential
from decouple import config
import logging
import base64

def send_raven(email_recipients, email_content, *attachment):
#Connecting with client
    try:
        credential = AzureKeyCredential(config("RAVEN_KEY"))
        endpoint = config("RAVEN_ENDPOINT")
        client = EmailClient(endpoint, credential)
    except:
        logging.error("No credentials found")
        logging.warning("Please provide raven endpoint")
        endpoint = input()
        logging.warning("Please provide raven key")
        endpoint = input()
        client = EmailClient(endpoint, credential)

    content = EmailContent(
        subject=email_content["subject"],
        plain_text=email_content["body"],
        html= email_content["html"],
    )

    if (("cc" in email_recipients) and ("bcc" in email_recipients)):
        recipients = EmailRecipients(
            to=[
                EmailAddress(email=recipient["email"], display_name=recipient["name"]) for recipient in email_recipients["to"]
            ],
            cc=[
                EmailAddress(email=recipient["email"], display_name=recipient["name"]) for recipient in email_recipients["cc"]
            ],
            bcc=[
                EmailAddress(email=recipient["email"], display_name=recipient["name"]) for recipient in email_recipients["bcc"]
            ],
        )
    elif ("cc" in email_recipients):
        recipients = EmailRecipients(
            to=[
                EmailAddress(email=recipient["email"], display_name=recipient["name"]) for recipient in email_recipients["to"]
            ],
            cc=[
                EmailAddress(email=recipient["email"], display_name=recipient["name"]) for recipient in email_recipients["cc"]
            ],
        )
    else:
        recipients = EmailRecipients(
            to=[
                EmailAddress(email=recipient["email"], display_name=recipient["name"]) for recipient in email_recipients["to"]
            ]
        )

    if attachment:
        file_bytes_b64 = base64.b64encode(bytes(attachment["data"], 'utf-8'))

        attachment = EmailAttachment(
            name=attachment["name"],
            attachment_type="."+attachment["type"],
            content_bytes_base64=file_bytes_b64.decode()
        )
        message = EmailMessage(sender="solutions@incubig.email", content=content, recipients=recipients,attachments=[attachment])
    else:
        message = EmailMessage(sender="solutions@incubig.email", content=content, recipients=recipients)
    
    response = client.send(message)

    return client.get_send_status(response.message_id)
