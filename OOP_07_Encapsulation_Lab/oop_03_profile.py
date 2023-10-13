import re


class Profile:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username: str) -> None:
        """
        Length - 5 to 15 characters (inclusive)

        """
        start_range = 5
        end_range = 15
        if len(username) not in range(start_range, end_range + 1):
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = username

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str) -> None:
        """
        - at least 8 characters long;
        - at least one upper case letter
        - at least one digit.

        """
        if not re.fullmatch(r"[A-Za-z\d]{8,}", password):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = password

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
