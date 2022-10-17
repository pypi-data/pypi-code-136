import logging
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from urllib import request

import pandas as pd

from notify.utils import check_environment_variables, dataframe_to_html


class NotifyMail:
    def __init__(
        self,
        to: str,
        subject: str,
        message: str,
        cc: str = None,
        bcc: str = None,
        files: dict = None,
        df: pd.DataFrame = pd.DataFrame(),
        server: str = "smtp.office365.com",
        port: int = 587,
        user_tls: bool = True,
    ):
        """
        This function sends an e-mail from Microsoft Exchange server

        Parameters
        ----------
        to: str
            the e-mail adress to send email to
        subject: str
            subject of the message
        message:
            HTML or plain text content of the message
        cc: str
            e-mail address to add as cc
        bcc: str
            e-mail address to add as bcc
        files: str, list
            Path(s) to file(s) to add as attachment
        df: pd.DataFrame
            dataframe that needs to be added to the HTML message.
        """

        self.to = to
        self.cc = cc
        self.bcc = bcc
        self.subject = subject
        self.message = message
        self.files = [files] if isinstance(files, str) else files

        check_environment_variables(["EMAIL_USER", "EMAIL_PW"])
        self.username = os.environ.get("EMAIL_USER")
        self.pw = os.environ.get("EMAIL_PW")
        self.df = df

        self.server = server
        self.port = port
        self.use_tls = user_tls

    def send_email(self) -> None:
        """
        This function sends an e-mail from Microsoft Exchange server

        Returns
        -------
        None
        """
        msg = MIMEMultipart()
        msg["From"] = self.username
        msg["To"] = self.to
        msg["Cc"] = self.cc
        msg["Bcc"] = self.bcc
        msg["Date"] = formatdate(localtime=True)
        msg["Subject"] = self.subject

        if self.df.shape[0] in range(1, 31):
            html_table = dataframe_to_html(df=self.df)
        elif self.df.shape[0] > 30:
            logging.warning(f"Only first 30 records will be added. ({self.df.shape[0]} > the limit of 30).")
            html_table = dataframe_to_html(df=self.df.head(n=30))
        else:
            html_table = ""  # no data in dataframe (0 records)

        self.message += html_table
        msg.attach(MIMEText(self.message, "html"))

        # attach files if these are given else ignore
        if self.files:
            # There might be a more safe way to check if a string is an url, but for our purposes, this suffices.
            is_url = list(self.files.values())[0].startswith(("http", "www"))
            for name, path in self.files.items():
                part = MIMEBase("application", "octet-stream")
                if is_url:
                    with request.urlopen(path) as download:
                        part.set_payload(download.read())
                else:
                    with open(path, "rb") as file:
                        part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename={name}")
                msg.attach(part)

        smtp = smtplib.SMTP(self.server, self.port)
        if self.use_tls:
            smtp.starttls()

        smtp.login(self.username, self.pw)
        smtp.send_message(msg=msg)
        smtp.quit()
