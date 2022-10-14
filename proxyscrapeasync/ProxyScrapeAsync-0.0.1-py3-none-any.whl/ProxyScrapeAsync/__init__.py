import aiohttp
import json

from typing import Any

url = "https://api.proxyscrape.com/v2"

class proxyinfo:
  """Simple Class For Proxy Info"""
  def __init__(
    self,
    response
  ):
    """Simple Function For Proxy Info"""
    self.response = response
    self.proxy_count = self.response.get("proxy_count")
    self.last_updated = self.response.get("last_updated")
    self.organizations = self.response.get("organizations")
    self.ports = self.response.get("ports")
    self.countries = self.response.get("countries")

async def get_proxies(**params: Any):
  """Gets Proxies and returns, accepts any parameters."""
  async with aiohttp.ClientSession() as session:
    async with session.request(
      method="GET",
      url=f"{url}",
      params=params
    ) as data:
        response = await data.text()
        
        return response


async def get_proxyinfo():
  """Gets Proxy Info and Returns in a Simple Format."""
  async with aiohttp.ClientSession() as session:
    async with session.request(
      method="GET",
      url=f"{url}?request=proxyinfo"
    ) as data:
      response = await data.text()
      response = json.loads(response)
      return proxyinfo(response=response)
      
"""
```py
import asyncio
import ProxyScrapeAsync as API

async def test():
  proxies = await API.get_proxies(
    request="displayproxies",
    protocol="http",
    timeout="10000",
    country="all",
    ssl="all"
  )
  print(proxies)
  info = await API.get_proxyinfo()
  print(info.last_updated)
  print(info.proxy_count, "proxies")
  
asyncio.run(test())
```
"""