import urllib
from typing import Optional, Generator

from kognic.io.model.annotation.client_annotation import Annotation, PartialAnnotation
from kognic.io.resources.abstract import IOResource


class AnnotationResource(IOResource):

    def get_project_annotations(self, project: str, annotation_type: str, batch: Optional[str] = None) -> Generator[Annotation, None, None]:
        url = f"v1/annotations/projects/{project}/"
        if batch:
            url += f"batch/{batch}/"

        url += f"annotation-type/{annotation_type}/search"

        for js in self._paginate(url):
            partial_annotation = PartialAnnotation.from_json(js)
            content = self._file_client.get_json(partial_annotation.uri)
            yield partial_annotation.to_annotation(content)

    def _paginate(self, base_url: str, next_cursor_id: Optional[int] = None) -> Generator[dict, None, None]:
        next_page_url = urllib.parse.urljoin(base_url, f"?cursorId={next_cursor_id}") if next_cursor_id is not None else base_url
        page = self._client.get(next_page_url)
        for annotation in page.data:
            yield annotation
        if page.metadata.next_cursor_id is not None:
            yield from self._paginate(base_url, page.metadata.next_cursor_id)

    def get_annotation(self, input_uuid: str, annotation_type: str) -> Annotation:
        json_resp = self._client.get(f"v1/annotations/inputs/{input_uuid}/annotation-type/{annotation_type}")
        annotation = Annotation.from_json(json_resp)
        return annotation
