from urllib.parse import urljoin
from gcd.data_access.google_git.known_paths import GoogleProjects, GitPaths


class GitUrlBuilder:
    __git_storage_url: str

    def __init__(self, base_url: str) -> None:
        self.__git_storage_url = base_url
    
    def __get_query(self, format: str | None) -> str:
        return f"?format={format.upper()}" if format else ""

    def get_commit_url(self, project: GoogleProjects, commit: str, format: str = None) -> str:
        query = self.__get_query(format)
        return urljoin(self.__git_storage_url, f"/{project}/{GitPaths.Source}/+/{commit}{query}")

    def get_tag_url(self, project: GoogleProjects, tag: str, format: str = None) -> str:
        query = self.__get_query(format)
        return urljoin(self.__git_storage_url, f"/{project}/{GitPaths.Source}/+/{GitPaths.Refs}/{GitPaths.Tags}/{tag}{query}")
