from abc import ABC, abstractmethod

class AbstractUserAuth(ABC):
    @abstractmethod
    def register(self, username, password):
        pass

    @abstractmethod
    def login(self, username, password):
        pass

class AbstractEventManager(ABC):
    @abstractmethod
    def view_events(self, status_filter=None):
        pass

    @abstractmethod
    def update_status(self, event_id, status):
        pass

    @abstractmethod
    def delete_event(self, event_id):
        pass

    @abstractmethod
    def add_event(self, name, time):
        pass

