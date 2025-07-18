from abc import ABC, abstractmethod

class Login(ABC):
    @abstractmethod
    def add_user(self, name: str, password: str) -> str:
        """
        Registers a new user.
        Returns:
            0 if successful, or a negative error code:
            -1: invalid screen name (must be 4-10 chars)
            -2: invalid password (must be 2-10 chars)
            -3: screen name already taken
        """
        pass

    @abstractmethod
    def login(self, name: str, password: str) -> str:
        """
        Logs in a user.
        Returns:
            0 if successful, or a negative error code:
            -1: screen name not found
            -2: invalid password
            -3: user already logged in
        """
        pass
