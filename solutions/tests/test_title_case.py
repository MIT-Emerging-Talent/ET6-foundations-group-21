import unittest
from title_case import title_case 

class TestStringToTitleCase(unittest.TestCase):
    def test_regular_sentence(self):
        self.assertEqual(title_case("hello world"), "Hello World")
        self.assertEqual(title_case("python is awesome"), "Python Is Awesome")

    def test_empty_string(self):
        self.assertEqual(title_case(""), "")

    def test_numeric_and_text(self):
        self.assertEqual(title_case("123abc"), "123abc")

    def test_mixed_case(self):
        self.assertEqual(title_case("HeLLo WoRLd"), "Hello World")

    def test_special_characters(self):
        self.assertEqual(title_case("hello@world"), "Hello@World")
        self.assertEqual(title_case("hello-world"), "Hello-World")
        self.assertEqual(title_case("hello.world"), "Hello.World")

    def test_single_word(self):
        self.assertEqual(title_case("python"), "Python")

if __name__ == "__main__":
    unittest.main()
