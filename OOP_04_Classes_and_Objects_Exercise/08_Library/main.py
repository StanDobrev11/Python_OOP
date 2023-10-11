# NOT OK for JUDGE with this type of imports.
# for Judge should be "from project.library import Library"
# However, this DOESN'T work

from library import Library
from registration import Registration
from user import User

if __name__ == "__main__":
    user_1 = User(10, 'Ivan')
    user = User(12, 'Peter')

    library = Library()
    registration = Registration()
    registration.add_user(user_1, library)
    registration.add_user(user, library)
    print(registration.add_user(user, library))
    registration.remove_user(user, library)
    print(registration.remove_user(user, library))
    registration.add_user(user, library)
    print(registration.change_username(2, 'Igor', library))
    print(registration.change_username(12, 'Peter', library))
    print(registration.change_username(12, 'George', library))

    [print(f'{user_record.user_id}, {user_record.username}, {user_record.books}') for
     user_record in library.user_records]

    library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets',
                                                    'The Prisoner of Azkaban',
                                                    'The Goblet of Fire',
                                                    'The Order of the Phoenix',
                                                    'The Half-Blood Prince',
                                                    'The Deathly Hallows']})

    library.get_book('J.K.Rowling', 'The Deathly Hallows', 17, user)
    print(library.books_available)
    print(library.rented_books)
    print(user.books)
    print(library.get_book('J.K.Rowling', 'The Deathly Hallows', 10, user))
    print(library.return_book('J.K.Rowling', 'The Cursed Child', user))
    library.return_book('J.K.Rowling', 'The Deathly Hallows', user)
    print(library.books_available)
    print(library.rented_books)


    library.get_book('J.K.Rowling', 'The Deathly Hallows', 17, user)
    library.get_book('J.K.Rowling', 'The Half-Blood Prince', 10, user)
    library.get_book('J.K.Rowling', 'The Goblet of Fire', 14, user_1)
    library.get_book('J.K.Rowling', 'The Prisoner of Azkaban', 8, user_1)
    print(library.rented_books)
    print(user.books)