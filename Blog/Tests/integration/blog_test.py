from unittest import TestCase, main
import sys
sys.path.append("C:\\Users\\EX002236\\Desktop\\Auto testing\\Blog")
from blog import Blog


class BlogTest(TestCase):
    def test_create_post_in_blog(self):
        b = Blog("Název", "autor")
        b.create_post("Titulek", "Obsah")

        self.assertEqual(b.posts[0].title, "Titulek")
        self.assertEqual(b.posts[0].content, "Obsah")


    def test_json(self):
        b = Blog("Název", "autor")
        b.create_post("Test Post", "Test Content")

        expected = {
            "title": "Název",
            "author": "autor",
            "posts": [
                {
                    "title": "Test Post",
                    "content": "Test Content",
                }
            ]
        }

        self.assertDictEqual(expected, b.json())

    def test_json_no_posts(self):
        b = Blog("Název", "autor")
        expected = {
            "title": "Název",
            "author": "autor",
            "posts": []
        }

        self.assertDictEqual(expected, b.json())


if __name__ == "__main__":
    main()
