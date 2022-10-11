import json
from batchx import bx as bx_api


class BxImage:
    def __init__(self, image_coords: str):
        bx_api.connect()
        self.image_coords = image_coords
        self.load()
        return

    def load(self):
        image_service = bx_api.ImageService()
        req = image_service.GetImageRequest(image=self.image_coords)

        self.GetImageResponse = image_service.GetImage(req)
        return

    def _fields_to_dict(self, pb):
        if hasattr(pb, "ListFields"):
            return {k.name: self._fields_to_dict(f) for (k, f) in pb.ListFields()}
        else:
            return pb

    @property
    def response_dict(self):
        if not hasattr(self, "_response_dict"):
            self._response_dict = self._fields_to_dict(self.GetImageResponse)
        return self._response_dict

    @property
    def image_dict(self):
        return self.response_dict.get("image")

    @property
    def manifest_dict(self):
        if not hasattr(self, "_manifest_dict"):
            self._manifest_dict = json.loads(self.image_dict.get("manifest"))
        return self._manifest_dict

    @property
    def environment(self):
        return self.image_dict.get("environment")

    @property
    def name(self):
        return self.image_dict.get("name")

    @property
    def canonical_name(self):
        n = self.name.replace("/", "-")

        if n.startswith("bioinformatics-"):
            n = n.split("bioinformatics-")[1]

        if n.startswith("pipelines-"):
            n = n.split("pipelines-")[1]

        return n

    @property
    def version(self):
        return self.image_dict.get("version")

    @property
    def description(self):
        return self.image_dict.get("description")

    @property
    def title(self):
        return self.description

    @property
    def url(self):
        return "https://platform.batchx.io/{e}/tools/{n}/{v}".format(
            e=self.environment, n=self.name.replace("/", "%2F"), v=self.version
        )

    @property
    def urls(self):
        return dict(
            base=self.url,
            docs="{u}/documentation".format(u=self.url),
            input="{u}/input".format(u=self.url),
            output="{u}/output".format(u=self.url),
        )
