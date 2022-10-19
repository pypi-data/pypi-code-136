import shutil
import zipfile
from pathlib import Path

import requests


class GithubDownloader:

    @staticmethod
    def download_github_archive(url: str, file_path: Path) -> None:
        """
        Download git archive
        :param url:
        :param file_path:
        """
        response = requests.get(url)
        with open(file_path, 'wb') as f:
            f.write(response.content)

    @staticmethod
    def unzip_file(zip_file_path: Path, folder_path: Path) -> None:
        """
        Unzip file
        :param zip_file_path:
        :param folder_path:
        """
        with zipfile.ZipFile(zip_file_path) as existing_zip:
            existing_zip.extractall(folder_path)

    @staticmethod
    def get_unzip_folder_path(zip_path: Path) -> Path:
        """
        Get unzip folder path
        :param zip_path:
        :return: unzip folder path
        """
        return zip_path.parent.glob(f"{zip_path.stem}-*").__next__()

    @staticmethod
    def download_github_archive_and_unzip(url: str, file_path: Path, folder_path: Path) -> Path:
        """
        Download git archive and unzip
        :param url:
        :param file_path:
        :param folder_path:
        :return: unzip folder path
        """
        GithubDownloader.download_github_archive(url, file_path)
        GithubDownloader.unzip_file(file_path, folder_path)
        return GithubDownloader.get_unzip_folder_path(file_path)

    @staticmethod
    def download_github_archive_and_unzip_to_folder(url: str, folder_path: Path) -> None:
        """
        Download git archive and unzip to folder
        :param url:
        :param folder_path:
        """
        GithubDownloader.download_github_archive_and_unzip(url, folder_path / 'archive.zip', folder_path)

    @staticmethod
    def download_github_archive_and_unzip_to_file(url: str, project_name: str) -> Path:
        """
        Download git archive and unzip to file
        :param url:
        :param project_name:
        :return: unzip folder path
        """
        url = f'{url}/archive/master.zip'
        file_path = Path(f'project/{project_name}.zip')
        file_path.parent.mkdir(parents=True, exist_ok=True)
        return GithubDownloader.download_github_archive_and_unzip(url, file_path, file_path.parent)

    @staticmethod
    def rename_project(folder_path: Path, project_name: str) -> Path:
        """
        Rename project. If project directory is exists, delete it.
        :param folder_path:
        :param project_name:
        return project folder path
        """
        project_path = folder_path.parent / project_name
        if project_path.exists():
            shutil.rmtree(project_path)
        folder_path.rename(project_path)
        return project_path
