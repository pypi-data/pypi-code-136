import asyncio
import base64
import logging
import time
from datetime import datetime, timedelta

import aiohttp

start_time = time.time()

# Setup logging
logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    level=logging.INFO,
    datefmt="%d-%m-%Y %H:%M:%S",
)
logger = logging.getLogger("piecowatt")
logger.info(f"{__name__} is starting...")


class Ecowatt:
    def __init__(self, id_client: str, id_secret: str):
        self.id_client = id_client
        self.id_secret = id_secret
        self.token = None
        self.token_expires_at = None
        self.signals = None
        self.error = ""
        self.error_reason = ""

    def set_token(self, token: str, expires_at: str) -> dict:
        self.token = token
        self.token_expires_at = expires_at
        logger.debug(
            f"Token is set to {{'token': '{self.token}', 'expires_at': '{self.token_expires_at}'}}"
        )
        return {"token": self.token, "expires_at": self.token_expires_at}

    async def _generate_token(self) -> dict:
        to_encode = self.id_client + ":" + self.id_secret
        id_encoded = base64.b64encode(to_encode.encode()).decode()
        logger.debug(f"Oauth2 Credential converted to base64: {id_encoded}")
        api_url = "https://digital.iservices.rte-france.com/token/oauth/"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {id_encoded}",
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(api_url, headers=headers, ssl=False) as response:
                if response.ok:
                    r = await response.json()
                    self.token = r["access_token"]
                    expires_in = r["expires_in"]
                    expires_at = datetime.now() + timedelta(seconds=expires_in)
                    self.token_expires_at = expires_at.strftime("%Y-%m-%d %H:%M:%S")
                    logger.debug(
                        f"New token generated: {self.token}. "
                        f"Expiring in {round(expires_in / 60)} minutes."
                    )
                    return {"token": self.token, "expires_at": self.token_expires_at}
                elif response.status == 400:
                    r = await response.json()
                    logger.error(
                        "Client application authentication failed: "
                        "Make sure your 'id_client / id_secret' are correct"
                    )
                    logger.debug(
                        f"'generate token' failed: {response.status}"
                        f" - {r['error']} - {r['error_description']}"
                    )
                    self.token = None
                    self.error = "Client application authentication failed"
                    self.error_reason = (
                        "Make sure your 'id_client / id_secret' are correct"
                    )
                    return {}
                else:
                    r = await response.json()
                    logger.error(
                        f"'generate token' failed: {response.status}"
                        f" - {r['error']} - {r['error_description']}"
                    )
                    self.error = (
                        f"generate token failed: {response.status}" f" - {r['error']}"
                    )
                    self.error_reason = r["error_description"]
                    self.token = None
                    return {}

    async def get_token(self) -> dict:
        if self.token:  # token exist = generated in the past
            expires_at = self.token_expires_at
            time_remaining = (
                datetime.strptime(expires_at, "%Y-%m-%d %H:%M:%S") - datetime.now()
            )
            if time_remaining.total_seconds() < 60:
                logger.debug(
                    f"'Get token': {self.token} is expired. Retrieving a new one ..."
                )
                return await self._generate_token()
            else:
                logger.debug(
                    f"Valid bearer token found: {self.token}."
                    f" Expiring in {round(time_remaining.seconds / 60, 1)} minutes."
                )
                return self.token
        else:  # no token found or never generated before. Case for first time for exemple
            logger.debug("'Get token': No token found. Retrieving a new one ...")
            return await self._generate_token()

    async def get_signals(self) -> dict:
        if await self.get_token():
            api_url = (
                "https://digital.iservices.rte-france.com/open_api/ecowatt/v4/signals"
            )
            headers = {
                "Content-type": "application/json",
                "Authorization": "Bearer " + self.token,
            }
            async with aiohttp.ClientSession() as session:
                async with session.get(api_url, headers=headers, ssl=False) as response:
                    if response.ok:
                        res_json = await response.json()
                        self.signals = {
                            key: value for key, value in enumerate(res_json["signals"])
                        }
                        return self.signals
                    elif response.status == 401:
                        logging.error(
                            f"{api_url} endpoint returned: {await response.reason}. "
                            f"Bad token or expired token."
                        )
                        logging.debug(response.headers)
                        self.error = (
                            f"{api_url} endpoint returned: {await response.reason}"
                        )
                        self.error_reason = "Bad token or expired token."
                        return {"error": self.error, "error_reason": self.error_reason}
                    elif response.status == 429:
                        logger.warning(
                            f"Too many requests on Ecowatts /signals API. "
                            f"Please retry in {response.headers['Retry-After']} seconds."
                        )
                        self.error = "Too many requests on Ecowatts /signals API."
                        self.error_reason = f"Please retry in {response.headers['Retry-After']} seconds."
                        return {"error": self.error, "error_reason": self.error_reason}
                    else:
                        self.error = response.status
                        self.error_reason = response.reason
                        return {"error": self.error, "error_reason": self.error_reason}
        else:
            logger.debug("'Get Signals' failed: No token could be found or generated")
            return {"error": self.error, "error_reason": self.error_reason}


async def main():
    id_client = "REPLACE WITH CORRECT VALUE"
    id_secret = "REPLACE WITH CORRECT VALUE"
    ecowatt = Ecowatt(id_client, id_secret)
    signals = await ecowatt.get_signals()
    if not signals.get("error"):
        for key, signal in signals.items():
            print(f"{signal['jour'][0:10]}: {signal['message']} ({signal['dvalue']})")
    else:
        print(f"{ecowatt.error} {ecowatt.error_reason}")


if __name__ == "__main__":
    asyncio.run(main())
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
