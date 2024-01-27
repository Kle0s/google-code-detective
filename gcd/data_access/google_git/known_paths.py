from enum import Enum


# Chromium open source project path
GOOGLE_SOURCE = f"https://chromium.googlesource.com"

class GitPaths(Enum):
    Source = "src"
    Tags = "tags"
    Refs = "refs"

    def __str__(self) -> str:
        return self.value

# Chromium projects
class GoogleProjects(Enum):
    Chromium = "chromium"

    def __str__(self) -> str:
        return self.value
    
