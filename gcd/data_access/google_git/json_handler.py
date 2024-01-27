from simplejson import loads
from typing import Any
from gcd.data_access.commit import Commit
from gcd.data_access.google_git.handler import GoogleGitHandler


class GoogleGitJsonHandler(GoogleGitHandler):
    __json: Any

    def __init__(self, json_content: str) -> None:
        self.__json = loads(json_content)
    
    def get_commit(self) -> Commit:
        return Commit(
            self.__get_commit_hash(),
            self.__get_parent_hash(),
            self.__get_message()
        )
    
    def __get_commit_hash(self) -> str:
        return self.__json["commit"]
    
    def __get_parent_hash(self) -> str:
        return self.__json["parents"][0]
    
    def __get_message(self) -> str:
        return self.__json["message"]


if __name__ == "__main__":
    import requests
    response = requests.get("https://chromium.googlesource.com/v8/v8.git/+/e0f2a195d87c9a06685121e0e783efd92d030df3?format=JSON")
    print(GoogleGitJsonHandler(response.content[4:]).get_commit())

