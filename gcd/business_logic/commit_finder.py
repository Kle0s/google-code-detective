import re
from gcd.data_access.google_git.known_paths import GoogleProjects, GOOGLE_SOURCE
from gcd.data_access.google_git.url_builder import GitUrlBuilder
from gcd.data_access.commit import Commit
from gcd.data_access.page_fetcher import PageFetcher
from gcd.data_access.google_git.json_handler import GoogleGitJsonHandler

class CommitFinder:
    __format: str
    __project: str
    __url_builder = GitUrlBuilder(GOOGLE_SOURCE)
    __fetcher = PageFetcher()

    def __init__(self, project: GoogleProjects, format: str = "json") -> None:
        self.__format = format.upper()
        self.__project = project

    def __is_bugfix(self, commit: Commit, issue: int) -> bool:
        results = re.findall("^[Bb][Uu][Gg]\s*[:=]\s*.*?(\d+)$", commit.message, re.IGNORECASE | re.MULTILINE)
        return str(issue) in results

    def __get_commit(self, url: str) -> Commit:
        content = self.__fetcher.fetch(url)
        json_content = content[4:]
        return GoogleGitJsonHandler(json_content).get_commit()

    def find_issue_from_tag(self, issue: int, tag: str) -> str:
        url = self.__url_builder.get_tag_url(self.__project, tag, self.__format)

        while True:
            commit = self.__get_commit(url)

            if (self.__is_bugfix(commit, issue)):
                return commit.commit_hash
            
            url = self.__url_builder.get_commit_url(self.__project, commit.parent_hash, self.__format)
