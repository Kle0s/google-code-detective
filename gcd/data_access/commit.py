from dataclasses import dataclass


@dataclass
class Commit:
    commit_hash: str
    parent_hash: str
    message: str
