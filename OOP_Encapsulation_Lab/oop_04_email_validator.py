import re


class EmailValidator:
    def __init__(self, min_length: int, mails: [], domains: []) -> None:
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return True if len(name) >= self.min_length else False

    def __is_mail_valid(self, mail):
        return any(True if m == mail else False for m in self.mails)

    def __is_domain_valid(self, domain):
        return any(True if d == domain else False for d in self.domains)

    def validate(self, email: str):
        name = re.findall(r"([a-zA-Z\d]+)@", email)[0]
        mail = re.findall(r"@([a-zA-Z\d]+)", email)[0]
        domain = re.findall(r"\.([a-zA-Z\d]+)", email)[0]

        return all((self.__is_name_valid(name), self.__is_mail_valid(mail), self.__is_domain_valid(domain)))


# mails = ["gmail", "softuni"]
# domains = ["com", "bg"]
# email_validator = EmailValidator(6, mails, domains)
# print(email_validator.validate("pe77er@gmail.com"))
# print(email_validator.validate("georgios@gmail.net"))
# print(email_validator.validate("stamatito@abv.net"))
# print(email_validator.validate("abv@softuni.bg"))
import unittest


class Tests(unittest.TestCase):
    def test_init(self):
        ev = EmailValidator(5, ["me"], ["you", "he"])
        self.assertEqual(ev.min_length, 5)
        self.assertEqual(ev.mails, ["me"])
        self.assertEqual(ev.domains, ["you", "he"])

    def test_private_validate_name(self):
        ev = EmailValidator(5, ["me"], ["you", "he"])
        self.assertEqual(ev._EmailValidator__is_name_valid("abc"), False)
        self.assertEqual(ev._EmailValidator__is_name_valid("abcdef"), True)

    def test_private_validate_mail(self):
        ev = EmailValidator(5, ["me"], ["you", "he"])
        self.assertEqual(ev._EmailValidator__is_mail_valid("me"), True)
        self.assertEqual(ev._EmailValidator__is_mail_valid("you"), False)

    def test_private_validate_domain(self):
        ev = EmailValidator(5, ["me"], ["you", "he"])
        self.assertEqual(ev._EmailValidator__is_domain_valid("he"), True)
        self.assertEqual(ev._EmailValidator__is_domain_valid("she"), False)

    def test_validate(self):
        ev = EmailValidator(5, ["me"], ["you", "he"])
        self.assertEqual(ev.validate("itsme@me.you"), True)
        self.assertEqual(ev.validate("me@me.you"), False)
        self.assertEqual(ev.validate("itsme@me.she"), False)
        self.assertEqual(ev.validate("itsme@you.he"), False)


if __name__ == "__main__":
    unittest.main()
