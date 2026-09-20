from abc import ABC, abstractmethod
from GameSignUpInfo import GameSignUpInfo

class SessionSheetWriterBase(ABC):
    """Interface for file writers."""

    @property
    @abstractmethod
    def name(self):
        """This property will be supplied by the inheriting classes
        individually.
        """
        pass

    @abstractmethod
    def write(self, session: GameSignUpInfo, target_folder : str) -> None:
        """Writes session info to file"""