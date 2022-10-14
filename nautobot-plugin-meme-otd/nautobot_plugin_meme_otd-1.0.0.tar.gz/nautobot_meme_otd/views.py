"""Nautobot Meme of the day."""
from django.shortcuts import render
from nautobot.core.views.generic import View
import requests


class MemeOfTheDayView(View):
    """Meme of the day view."""

    def get(self, request):
        """Get XKCD info for template."""
        resp = requests.get("https://xkcd.com/info.0.json")

        if not resp.ok:
            content = {"title": "Unable to retrieve XKCD API data.", "url": False}
        content = {"title": resp.json()["safe_title"], "url": resp.json()["img"]}
        return render(request, "nautobot_meme_otd/meme-otd.html", content)
