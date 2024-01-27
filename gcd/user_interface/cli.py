from gcd.data_access.google_git.known_paths import GoogleProjects
from gcd.user_interface.argument_parser import GcdArgumentParser
from gcd.business_logic.commit_finder import CommitFinder

def main():
    parser = GcdArgumentParser()
    arguments = parser.parse_args();
    commit_finder = CommitFinder(GoogleProjects.Chromium)
    result = commit_finder.find_issue_from_tag(arguments.issue, arguments.tag)
    print(f"found: {result}")

if "__main__" == __name__:
    main()
