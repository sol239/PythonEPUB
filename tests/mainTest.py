import unittest
import os

from epub_handler import Ebook

test_tittle_sample_fail: str = "Title for sampleX.epub did not match the expected value"
test_author_sample_fail: str = "Author for sampleX.epub did not match the expected value"
test_cover_path_sample_fail: str = "Cover path for sampleX.epub did not match the expected value"

def get_sample_path(epub_file_name: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    subdir_path = os.path.join(current_dir, '..', 'demo', 'epub samples')
    return os.path.abspath(os.path.join(subdir_path, epub_file_name))

class TestEbookClass(unittest.TestCase):


    def test_title_sample1(self):
        ebook_1 = Ebook(get_sample_path("sample1.epub"))
        ebook_1.delete_archive()
        self.assertEqual(
            ebook_1.title,
            "Twenty Thousand Leagues Under the Seas: An Underwater Tour of the World",
            "Title for sample1.epub did not match the expected value"
        )

    def test_title_sample2(self):
        ebook_2 = Ebook(get_sample_path("sample2.epub"))
        ebook_2.delete_archive()
        self.assertEqual(
            ebook_2.title,
            "White Fang",
            "Title for sample2.epub did not match the expected value"
        )

    def test_author_sample1(self):
        ebook_1 = Ebook(get_sample_path("sample1.epub"))
        ebook_1.delete_archive()
        self.assertEqual(
            ebook_1.author,
            "Jules Verne",
            test_tittle_sample_fail
        )

    def test_author_sample2(self):
        ebook_2 = Ebook(get_sample_path("sample2.epub"))
        ebook_2.delete_archive()
        self.assertEqual(
            ebook_2.author,
            "Jack London",
            test_author_sample_fail
        )

    def test_cover_path_sample1(self):
        ebook_1 = Ebook(get_sample_path("sample1.epub"))
        # ebook_1.delete_archive()
        self.assertEqual(
            os.path.normpath(ebook_1.cover_image_path),
            get_sample_path(os.path.join(os.getcwd(), "temp", "OEBPS","3388843439980103376_cover.jpg")),
            test_cover_path_sample_fail
        )

    def test_cover_path_sample2(self):
        ebook_2 = Ebook(get_sample_path("sample2.epub"))
        # ebook_2.delete_archive()
        self.assertEqual(
            os.path.normpath(ebook_2.cover_image_path),
            get_sample_path(os.path.join(os.getcwd(), "temp", "OEBPS","5405372351310475893_cover.jpg")),
            test_cover_path_sample_fail
        )

if __name__ == '__main__':
    unittest.main(verbosity=2)