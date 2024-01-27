from abc import abstractmethod, ABC
from gcd.data_access.commit import Commit


class GoogleGitHandler(ABC):
    @abstractmethod
    def get_commit(self) -> Commit:
        pass
