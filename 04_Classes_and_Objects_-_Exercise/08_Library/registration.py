class Registration:
    def __init__(self):
        pass

    @staticmethod
    def add_user(user: 'class User', library: 'class Library'):
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"

        library.user_records.append(user)

    @staticmethod
    def remove_user(user: 'class User', library: 'class Library'):
        if user in library.user_records:
            library.user_records.remove(user)
        else:
            return f"We could not find such user to remove!"

    @staticmethod
    def change_username(user_id: int, new_username: str, library: 'class Library'):
        try:
            user = next(filter(lambda u: u.user_id == user_id, library.user_records))
        except StopIteration:
            return f"There is no user with id = {user_id}!"

        if user.username == new_username:
            return f"Please check again the provided username - it should be different than the username used so far!"

        try:
            library.rented_books[new_username] = library.rented_books.pop(user.username)
        except KeyError:
            pass

        user.username = new_username
        return f"Username successfully changed to: {new_username} for user id: {user_id}"
