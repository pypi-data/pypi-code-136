import logging

import pandas as pd
import pymsteams
from pymsteams import TeamsWebhookException

from notify.types import DfsInfo


class NotifyTeams:
    def __init__(self, webhook: str):
        """

        Parameters
        ----------
        webhook: str
            url for sending the teams message
        """

        self.msg = pymsteams.connectorcard(webhook)
        self.msg.color("#F0B62E")

    def add_full_dataframe(self, df: pd.DataFrame) -> None:
        """

        Parameters
        ----------

        df: pd.DataFrame
            Dataframe that will be added to the card.

        Returns
        -------
        None
            Adds a section for the table to the teams message object.

        """

        if df.shape[0] > 30:
            logging.warning(f"only first 30 records will be added.({df.shape[0]}> the limit of 30).")
            df = df.head(n=30)

        section = pymsteams.cardsection()
        md_table = df.to_markdown(index=False)
        section.text(md_table)
        self.msg.addSection(section)

    def create_dataframe_report(self, dfs: DfsInfo) -> None:
        """

        Parameters
        ----------

        dfs: dict
            Dataframes containing {name, df} as key value pairs

        Returns
        -------
        None
            Adds a section for the table to the teams message object.

        """
        for df_name, df_shape in dfs.items():
            section = pymsteams.cardsection()
            section.activityTitle(f"<h1><b>{df_name}</b></h1>")
            section.activityImage("https://pbs.twimg.com/profile_images/1269974132818620416/nt7fTdpB.jpg")
            section.text(f"> In totaal **{df_shape[0]}** records met **{df_shape[1]}** kolommen verwerkt")
            self.msg.addSection(section)

    def create_buttons(self, buttons: dict) -> None:
        """

        Parameters
        ----------
        buttons: dict
            dictionairy containing button_name, button_link as key, value pairs.

        Returns
        -------
        None
            Adds the button(s) to the teams message

        """

        for button_name, button_link in buttons.items():
            self.msg.addLinkButton(button_name, button_link)

    def basic_message(
        self,
        title: str,
        message: str = None,
        buttons: dict = None,
        df: pd.DataFrame = pd.DataFrame(),
        dfs: DfsInfo = None,
    ) -> None:
        """
        This function posts a message, containing a section, in a Microsoft Teams channel

        Parameters
        ----------
        dfs: dict
            Dataframes dictionary, with keys as dataframe name and value as dataframe.
        df: pd.DataFrame
            df that will be added to a card section. length of dataframe should not exceed 10.
        title: str
            Title of the message (optional)
        message: str
            Content of the message (optional)
        buttons: dict
            dictionary of button_name, button_url as key value pairs

        Returns
        -------
        None
            sends a message in a teams channel, reporting col en records as information.
        """

        self.msg.title(title)  # always required.

        if message:
            self.msg.text(message)

        if dfs:
            self.create_dataframe_report(dfs)

        if not df.empty:
            self.add_full_dataframe(df)

        if buttons:
            self.create_buttons(buttons)

        try:
            self.msg.send()
        except TeamsWebhookException:
            logging.warning("Teams notification not sent!")
