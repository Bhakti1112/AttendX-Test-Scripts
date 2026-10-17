import unittest


def login(username, password):
    """Sample login validation for AttendX."""
    if username == "student1" and password == "pass123":
        return True
    return False


class TestLogin(unittest.TestCase):

    def test_valid_login(self):
        self.assertTrue(login("student1", "pass123"))

    def test_invalid_password(self):
        self.assertFalse(login("student1", "wrongpass"))

    def test_invalid_username(self):
        self.assertFalse(login("unknown", "pass123"))

    def test_empty_username(self):
        self.assertFalse(login("", "pass123"))


if __name__ == "__main__":
    unittest.main()