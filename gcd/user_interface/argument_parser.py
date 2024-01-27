from argparse import ArgumentParser

class GcdArgumentParser(ArgumentParser):
    def __init__(self):
        super().__init__("google-code-detective")
        self.__add_arguments()

    def __add_arguments(self):
        self.add_argument("--issue", required=True, action="store", type=int, help="Chromium issue id")
        self.add_argument("--tag", required=True, action="store", type=str, help="Chromium tag (version)")
