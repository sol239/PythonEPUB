import unittest

from ebook import Ebook


class TestEbookCase(unittest.TestCase):
    def test_title(self):

        # assign
        ebook = Ebook("C:/Users/david_dyn8g78/Downloads/Endymion - Dan Simmons.epub")

        self.assertEqual(ebook.title, "Endymion")  # add assertion here


if __name__ == '__main__':
    unittest.main()
