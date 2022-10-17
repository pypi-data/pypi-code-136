from datetime import date

from marstuff.bases import Object
from marstuff.utils import convert, Extras, List


class Manifest(Object):
    def __init__(self, id=None, name=None, landing_date=None, launch_date=None, status=None, photos=None, max_sol=None, max_date=None, total_photos=None, **extras):
        self.id = convert(id, int)
        self.name = convert(name, str)
        self.landing_date = convert(landing_date, date)
        self.launch_date = convert(launch_date, date)
        self.status = convert(status, str)
        self.photos = convert(photos, List[ManifestPhoto])
        self.max_sol = convert(max_sol, int)
        self.max_date = convert(max_date, date)
        self.total_photos = convert(total_photos, int)
        self.extras: dict = convert(extras, Extras)


from marstuff.objects.photo import ManifestPhoto