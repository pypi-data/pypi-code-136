"""This module is a collection of classes and methods to perform the actual
posting of content to Mastodon."""
# pylint: disable=too-few-public-methods
# With two private methods it is still nice to have these in their own module
import logging
import os
import sys
from dataclasses import dataclass
from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar

import aiofiles
import aiohttp
import magic
from minimal_activitypub.client_2_server import ActivityPub
from minimal_activitypub.client_2_server import ActivityPubError
from minimal_activitypub.client_2_server import ApiError
from rich import print as rprint
from tqdm.asyncio import tqdm

from . import CLIENT_WEBSITE
from . import PROGRESS_BAR_FORMAT
from . import USER_AGENT
from .collect import LinkedMediaHelper
from .collect import MediaAttachment
from .collect import RedditHelper
from .control import BotConfig
from .control import Configuration
from .control import MastodonConfig
from .control import PromoConfig
from .control import Secret


logger = logging.getLogger("Tootbot")

MP = TypeVar("MP", bound="MastodonPublisher")

SECRETS_FILE = "mastodon.secret"  # pragma: allowlist secret


@dataclass
class MastodonPublisher:
    """Ease the publishing of content to Mastodon."""

    bot: BotConfig
    media_only: bool
    nsfw_marked: bool
    mastodon_config: MastodonConfig
    promo: PromoConfig
    instance: ActivityPub

    num_non_promo_posts: int = 0

    MAX_LEN_TOOT = 500

    @classmethod
    async def initialise(
        cls: Type[MP],
        config: Configuration,
        session: aiohttp.ClientSession,
        secrets: Secret,
    ) -> MP:
        """Initialises and returns an new MastodonPublisher class."""
        try:
            instance = ActivityPub(
                instance=config.mastodon_config.domain,
                access_token=secrets.client_secret.strip(),
                session=session,
            )
            await instance.determine_instance_type()

            user_info = await instance.verify_credentials()

            logger.debug(
                "Successfully authenticated on %s as @%s",
                config.mastodon_config.domain,
                user_info["username"],
            )

        except (ActivityPubError, ApiError) as error:
            logger.error("Error while logging into Mastodon: %s", error)
            logger.error("Tootbot cannot continue, now shutting down")
            sys.exit(1)

        return cls(
            instance=instance,
            mastodon_config=config.mastodon_config,
            bot=config.bot,
            media_only=config.media.media_only,
            nsfw_marked=config.reddit.nsfw_marked,
            promo=config.promo,
        )

    @staticmethod
    async def get_secrets(mastodon_domain: str, config_dir: str) -> Secret:
        """Checks that Mastodon API secrets are available. If not collects
        neccesarry info from user input the create and store APi secrets for
        Mastodon API secrets.

        Arguments:
            mastodon_domain: domain name for Mastodon instance used for tooting. This
            is read from config.ini file, where it must be configured
            :config_dir: direcotry containing all the configuration files
        """

        mastodon_secrets = Secret(  # nosec B106
            client_id=None,
            client_secret="undefined",  # pragma: allowlist secret
        )

        secrets_file = f"{config_dir}/{SECRETS_FILE}"
        # Log into Mastodon if enabled in settings
        if not os.path.exists(secrets_file):
            # If the secret file doesn't exist,
            # it means the setup process hasn't happened yet
            rprint("Mastodon API keys not found. (See wiki for help).")
            user_name = input("[ .. ] Enter email address for Mastodon account: ")
            password = input("[ .. ] Enter password for Mastodon account: ")
            rprint("Generating login key for Mastodon...")
            try:
                async with aiohttp.ClientSession() as session:
                    access_token = await ActivityPub.get_auth_token(
                        instance_url=mastodon_domain,
                        username=user_name,
                        password=password,
                        session=session,
                        user_agent=USER_AGENT,
                        client_website=CLIENT_WEBSITE,
                    )

                    mastodon = ActivityPub(
                        instance=mastodon_domain,
                        access_token=access_token,
                        session=session,
                    )
                    await mastodon.determine_instance_type()
                    user_info = await mastodon.verify_credentials()
                mastodon_username = user_info["username"]
                rprint(
                    f"Successfully authenticated on "
                    f"{mastodon_domain} as @{mastodon_username}"
                )
                async with aiofiles.open(file=secrets_file, mode="w") as file:
                    await file.write(access_token)
                    await file.write("\n")
                    await file.write(mastodon.instance)
                    mastodon_secrets.client_secret = access_token
                rprint(
                    f"Mastodon login information now stored in " f"{secrets_file} file"
                )

            except (ActivityPubError, ApiError) as error:
                logger.error("Error while logging into Mastodon: %s", error)
                logger.error("Tootbot cannot continue, now shutting down")
                sys.exit(1)

        else:
            async with aiofiles.open(
                file=secrets_file,
                mode="r",
            ) as file:
                mastodon_secrets.client_secret = await file.readline()

        return mastodon_secrets

    async def make_post(
        self: MP,
        posts: Dict[Any, Any],
        reddit_helper: RedditHelper,
        media_helper: LinkedMediaHelper,
    ) -> None:
        """Makes a post on mastodon from a selection of reddit submissions.

        Arguments:
            posts: A dictionary of subreddit specific hashtags and PRAW Submission
                   objects
            reddit_helper: Helper class to work with Reddit
            media_helper: Helper class to retrieve media linked to from a reddit
            Submission.
        """
        break_to_mainloop = False
        for additional_hashtags, source_posts in posts.items():
            if break_to_mainloop:
                break

            for post in source_posts:

                # Find out if we have any attachments to include with toot.
                logger.debug(
                    "Getting attachments for post %s",
                    source_posts[post].id,
                )
                attachments = MediaAttachment(source_posts[post], media_helper)
                await attachments.get_media_files()
                await self._remove_posted_earlier(attachments)

                # Make sure the post contains media,
                # if MEDIA_POSTS_ONLY in config is set to True
                if self.media_only and len(attachments.media_paths) == 0:
                    logger.warning(
                        "Skipping %s, non-media posts disabled or "
                        "media file not found",
                        source_posts[post].id,
                    )
                    # Log the post anyway
                    await self.bot.post_recorder.log_post(
                        reddit_id=source_posts[post].id
                    )
                    continue

                try:
                    # Generate promo message if needed
                    promo_message = None
                    if self.num_non_promo_posts >= self.promo.every > 0:
                        promo_message = self.promo.message
                        self.num_non_promo_posts = -1

                    # Generate post caption
                    caption = reddit_helper.get_caption(
                        source_posts[post],
                        MastodonPublisher.MAX_LEN_TOOT,
                        add_hash_tags=additional_hashtags,
                        promo_message=promo_message,
                    )

                    # Upload media files if available
                    media_ids = await self._post_attachments(attachments)

                    # Determine if spoiler is necessary
                    spoiler = None
                    if source_posts[post].over_18 and self.nsfw_marked:
                        spoiler = "NSFW"

                    # Post to Mastodon
                    toot = await self.instance.post_status(
                        status=caption,
                        media_ids=media_ids,
                        visibility=self.mastodon_config.post_visibility,
                        sensitive=self.mastodon_config.media_always_sensitive,
                        spoiler_text=spoiler,
                    )
                    rprint(f'Posted to Mastodon: "{caption}" (at {toot["url"]})')

                    # Log the toot
                    await self.bot.post_recorder.log_post(
                        reddit_id=source_posts[post].id,
                        shared_url=source_posts[post].url,
                    )

                    self.num_non_promo_posts += 1
                    self.mastodon_config.number_of_errors = 0

                except ActivityPubError as error:
                    logger.error("Error while posting toot: %s", error)
                    # Log the post anyway, so we don't get into a loop of the
                    # same error
                    await self.bot.post_recorder.log_post(
                        reddit_id=source_posts[post].id
                    )
                    self.mastodon_config.number_of_errors += 1

                # Clean up media file
                attachments.destroy()

                # Return control to main loop
                break_to_mainloop = True
                break

    async def _post_attachments(self: MP, attachments: MediaAttachment) -> List[str]:
        """_post_attachments post any media in attachments.media_paths list.

        Arguments:
            attachments: object with a list of paths to media to be posted on Mastodon

        Returns:
            media_ids: List of dicts returned by mastodon.media_post
        """
        media_ids: List[str] = []
        if len(attachments.media_paths) == 0:
            return media_ids

        title = "Uploading attachments"
        for checksum, media_path in tqdm(
            attachments.media_paths.items(),
            desc=f"{title:.<60}",
            total=len(attachments.media_paths),
            unit="attachment",
            ncols=120,
            bar_format=PROGRESS_BAR_FORMAT,
        ):
            try:
                mime_type = magic.from_file(media_path, mime=True)
                logger.debug(
                    "Media %s (%s) with checksum: %s",
                    media_path,
                    mime_type,
                    checksum,
                )
                async with aiofiles.open(file=media_path, mode="rb") as upload:
                    media = await self.instance.post_media(
                        file=upload,
                        mime_type=mime_type,
                    )
                logger.debug(
                    "MastodonPublisher._post_attachments - uploaded: %s", media_path
                )
                logger.debug("MastodonPublisher._post_attachments - result: %s", media)

                # Log the media upload
                await self.bot.post_recorder.log_post(check_sum=checksum)
                media_ids.append(media.get("id"))
            except (ActivityPubError, TypeError) as error:
                logger.debug(
                    "Error when uploading media %s (%s): %s",
                    media_path,
                    mime_type,
                    error,
                )

        logger.debug("MastodonPublisher._post_attachments - media_ids: %s", media_ids)
        return media_ids

    async def _remove_posted_earlier(self: MP, attachments: MediaAttachment) -> None:
        """_remove_posted_earlier checks che checksum of all proposed
        attachments and removes any from the list that have already been posted
        earlier.

        Arguments:
            attachments: object with list of paths to media files proposed to be
            posted on Mastodon
        """
        # Build a list of checksums for files that have already been posted earlier
        checksums = []
        for checksum in attachments.media_paths:
            logger.debug(
                "Media attachment (path, checksum): %s, %s",
                attachments.media_paths[checksum],
                checksum,
            )
            if attachments.media_paths[checksum] is None:
                checksums.append(checksum)
            # Check for duplicate of attachment sha256
            elif await self.bot.post_recorder.duplicate_check(checksum):
                logger.debug("Media with checksum %s has already been posted", checksum)
                checksums.append(checksum)
        # Remove all empty or previously posted images
        for checksum in checksums:
            attachments.destroy_one_attachment(checksum)
