import unittest

import app

class TestApp(unittest.TestCase):
    """Class for unit testing app

    :param unittest: [description]
    :type unittest: [type]
    """

    def test_display_iss_location(self):
        res = app.display_iss_location()
        self.assertEqual(res, True)

    def test_display_iss_pass_times(self):
        res = app.display_iss_pass_times(latitude=43, longitude=-122)
        self.assertEqual(res, True)

    def test_display_people_in_space(self):
        res = app.display_people_in_space()
        self.assertEqual(res, True)


if __name__ == "__main__":
    unittest.main()
