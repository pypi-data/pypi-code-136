from azure.storage.blob import BlobClient


def list_blob_content(url: str, encoding: str = 'UTF-8', logging_enable: bool = True) -> 'list[str]':
    """
    Read all content of a blob and convert to list, splitting at line breaks.
    
    Args:
        url (str): Blob full URL localization in Azure Storage Blob.
        encoding (str): Encoding format for text downloading. Defaults to ``UTF-8``.
        logging_enable (bool): To enable the logger or not when downloading blob content. Defaults to ``True``.
        
    Returns:
        Blob content as a list of strings.
    
    """
    with BlobClient.from_blob_url(blob_url=url, logging_enable=logging_enable) as blob_client:
        return blob_client.download_blob().content_as_text(encoding=encoding).splitlines()
