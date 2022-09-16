from abc import ABC, abstractmethod


class IntefaceHandler(ABC):
    @abstractmethod
    def will_handle(self) -> bool:
        pass

    @abstractmethod
    def handle(self):
        pass
