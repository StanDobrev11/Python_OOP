import unittest

from project.team import Team


class TestTeam(unittest.TestCase):

    def setUp(self) -> None:
        self.test = Team('test')

    def test_proper_init(self):
        self.assertEqual('test', self.test.name)
        self.assertEqual({}, self.test.members)

    def test_validator_raises_exception(self):
        test_case = [chr(i) for i in range(65)]
        test_case.extend([chr(i) for i in range(123, 128)])
        for x in test_case:
            with self.assertRaises(ValueError) as ve:
                self.test.name = x
            self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_validator_valid_name(self):
        valid_alpha_symbols = [chr(i) for i in range(65, 91)]  # Uppercase letters (A-Z)
        valid_alpha_symbols.extend([chr(i) for i in range(97, 123)])  # Lowercase letters (a-z)
        for x in valid_alpha_symbols:
            self.test.name = x
            self.assertEqual(x, self.test.name)

    def test_add_member_success(self):
        actual = self.test.add_member(Ivan=15, Dragan=20, Stoyan=18)
        expected = "Successfully added: Ivan, Dragan, Stoyan"
        self.assertEqual({'Ivan': 15, 'Dragan': 20, 'Stoyan': 18}, self.test.members)
        self.assertEqual(expected, actual)

    def test_add_members_already_added(self):
        self.test.add_member(Ivan=15, Dragan=20, Stoyan=18)
        actual = self.test.add_member(Ivan=15)
        expected = "Successfully added: "
        self.assertEqual(expected, actual)
        self.assertEqual({'Ivan': 15, 'Dragan': 20, 'Stoyan': 18}, self.test.members)

    def test_remove_member_valid(self):
        self.test.add_member(Ivan=15, Dragan=20, Stoyan=18)
        actual = self.test.remove_member('Ivan')
        self.assertEqual("Member Ivan removed", actual)
        self.assertEqual({'Dragan': 20, 'Stoyan': 18}, self.test.members)

    def test_remove_not_exists(self):
        self.test.add_member(Dragan=20, Stoyan=18)
        actual = self.test.remove_member('Ivan')
        expected = "Member with name Ivan does not exist"
        self.assertEqual(expected, actual)

    def test_proper_gt_method_returns_true(self):
        self.test.add_member(Ivan=15, Dragan=20, Stoyan=18)
        test_2 = Team('testtwo')
        test_2.add_member(Petko=10, Simo=22)
        self.assertTrue(self.test > test_2)
        self.assertTrue(self.test.__gt__(test_2))

    def test_proper_gt_method_returns_false(self):
        self.test.add_member(Ivan=15)
        test_2 = Team('testtwo')
        test_2.add_member(Petko=10, Simo=22)
        self.assertFalse(self.test > test_2)

    def test_proper_add_method(self):
        self.test.add_member(Dragan=20)
        test_2 = Team('testtwo')
        test_2.add_member(Stoyan=18)
        actual = self.test + test_2
        expected = 'testtesttwo'
        self.assertEqual(expected, actual.name)
        self.assertEqual({'Dragan': 20, 'Stoyan': 18}, actual.members)
        self.assertIsInstance(actual, Team)

    def test_len_method(self):
        self.test.add_member(Ivan=15, Dragan=20, Stoyan=18)
        self.assertEqual(3, len(self.test))

    def test_str_method(self):
        self.test.add_member(Ivan=15, Dragan=20, Stoyan=18)
        expected = "Team name: test\nMember: Dragan - 20-years old\nMember: Stoyan - 18-years old\nMember: Ivan - 15-years old"
        actual = self.test.__str__()
        self.assertEqual(expected, actual)

    def test_str_not_teams(self):
        expected = "Team name: test"
        actual = self.test.__str__()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
