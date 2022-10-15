import boto3
from botocore.exceptions import ClientError

from hautils.logger import logger
from hautils.web import exception_log


def send_email(recipient, subject, body, body_text):
    """
    The send_email function accepts four parameters:
        1. recipient - the email address of the person you are sending to
        2. subject - the subject line of your email message
        3. body_text - a plain text version of your email message (optional)
        4. body_html - an HTML version of your email message (optional)

       The function sends an HTML or plain text email depending on what parameters are provided.

    :param recipient: Specify the email address to which you want to send the notification
    :param subject: Specify the subject of the email
    :param body: Construct the body of the email
    :param body_text: Populate the email body for recipients with non-html email clients
    :return: The following:
    :doc-author: Trelent
    """
    # Replace sender@example.com with your "From" address.
    # This address must be verified with Amazon SES.
    SENDER = "HiAcuity <noreply@hiacuity.com>"

    # Replace recipient@example.com with a "To" address. If your account
    # is still in the sandbox, this address must be verified.
    RECIPIENT = recipient

    # Specify a configuration set. If you do not want to use a configuration
    # set, comment the following variable, and the
    # ConfigurationSetName=CONFIGURATION_SET argument below.
    CONFIGURATION_SET = "ConfigSet"

    # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
    AWS_REGION = "ap-southeast-1"

    # The subject line for the email.
    SUBJECT = subject

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = body_text

    # The HTML body of the email.
    BODY_HTML = body

    # The character encoding for the email.
    CHARSET = "UTF-8"

    # Create a new SES resource and specify a region.
    client = boto3.client('ses',region_name=AWS_REGION)

    # Try to send the email.
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
            # If you are not using a configuration set, comment or delete the
            # following line
            ConfigurationSetName=CONFIGURATION_SET,
        )
    # Display an error if something goes wrong.
    except ClientError as e:
        exception_log(e)
    else:
        logger.info("email sent to %s " % (RECIPIENT,))