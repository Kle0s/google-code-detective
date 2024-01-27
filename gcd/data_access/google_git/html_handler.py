from lxml.html import HtmlElement, fromstring
from gcd.data_access.commit import Commit
from gcd.data_access.google_git.handler import GoogleGitHandler


class GoogleGitHtmlHandler(GoogleGitHandler):
    __document: HtmlElement

    def __init__(self, html_content: str) -> None:
        self.__document = fromstring(html_content)

    def get_commit(self) -> Commit:
        return Commit(
            self.__get_commit_hash(),
            self.__get_parent_hash(),
            self.__get_message()
        )

    def __get_node_content(self, xpath: str) -> str:
        nodes = self.__document.xpath(xpath)
        if (0 == len(nodes)):
            raise Exception(f"xpath not found ('{xpath}')")
        return nodes[0].text_content()

    def __get_commit_hash(self) -> str:
        return self.__get_node_content("/html/body/div/div/div[2]/table/tr[1]/td[1]")

    def __get_parent_hash(self) -> str:
        return self.__get_node_content("/html/body/div/div/div[2]/table/tr[5]/td/a")

    def __get_message(self) -> str:
        return self.__get_node_content("/html/body/div/div/pre")


if __name__ == "__main__":
    import requests
    response = requests.get("https://chromium.googlesource.com/v8/v8.git/+/e0f2a195d87c9a06685121e0e783efd92d030df3")
    print(GoogleGitHtmlHandler(response.content).get_commit())
