import datetime
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
import os
import boto3
import jwt
from jinja2 import Template

from hadata.user import MongoUser
from hareqres.jwtbearer import JWT_SECRET, JWT_ALGORITHM
from hareqres.jwtbearer import encode_jwt
from hareqres.user import User
from hautils.logger import logger


def email_token(receiver):
    """
    The email_token function takes a receiver email address as an argument and returns a token.
    The token is created by encoding the receiver email address in a JWT payload, which expires after 48 hours.

    :param receiver: Send the email to the user
    :return: A token that is a jwt
    :doc-author: Trelent
    """
    logger.info("email token called with %s" % (receiver,))
    payload = {
        "email": receiver,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=2)
    }
    logger.info("token creation %s" % (payload,))
    token = encode_jwt(payload)
    logger.info("token created %s" % (token,))
    return token


def send_registration_confirmation(user):
    token = email_token(user.email)
    app_url = os.getenv("APP_URL", "http://localhost:3000")
    template_data = json.dumps({"first_name": user.first_name, "last_name": user.last_name, "hostname": app_url, "token": token})

    ses = boto3.client("ses", region_name="ap-southeast-1", aws_access_key_id="AKIA5CLBR5JUXW7XTYXC",
                       aws_secret_access_key="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")
    ses.send_templated_email(
        Source="HiAcuity Support <support@hiacuity.com>",
        Template="Registration",
        ConfigurationSetName="hiacuity",
        Destination={"ToAddresses": [user.email]},
        SourceArn='arn:aws:ses:ap-southeast-1:898389633641:identity/hiacuity.com',
        TemplateData=template_data
    )


async def send_assessment_invitation(user: MongoUser):
    ses = boto3.client("ses", region_name="ap-southeast-1", aws_access_key_id="AKIA5CLBR5JUXW7XTYXC",
                       aws_secret_access_key="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")
    token = email_token(user.email)
    app_url = os.getenv("APP_URL", "http://localhost:3000")
    template_data = json.dumps({"first_name": user.first_name, "company_name": "Hiacuity", "password": user.clear_password, "hostname": app_url,
     "token": token, "email": user.email, "last_name": user.last_name})
    ses.send_templated_email(
        Source="HiAcuity Support <support@hiacuity.com>",
        Template="Invitation",
        ConfigurationSetName="hiacuity",
        Destination={"ToAddresses": [user.email]},
        SourceArn='arn:aws:ses:ap-southeast-1:898389633641:identity/hiacuity.com',
        TemplateData=template_data
    )


async def verify_token(token: str):
    """
    The verify_token function takes a token as an argument and returns the user object associated with that token.
    The function uses the jwt library to decode the token, then loads it into a json object. The json object is then
    used to query MongoDB for the user's document, which is returned.

    :param token:str: Pass the token that is being verified
    :return: A dictionary of the user's information
    :doc-author: Trelent
    """
    payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    user = json.loads(MongoUser.objects(email=payload.get("email")).to_json())
    selected_user = user[0]
    return selected_user
