from unittest import TestCase, main
import sys
sys.path.append("C:\\Users\\EX002236\\Desktop\\Auto testing\\Blog")
from post import Post


class PostTest(TestCase):
    def test_create_post(self):
        p = Post("Titulek", "Obsah")

        self.assertEqual("Titulek", p.title)
        self.assertEqual("Obsah", p.content)

    def test_json(self):
        p = Post("Titulek", "Obsah")
        expected = {"title": "Titulek", "content": "Obsah"}

        self.assertDictEqual(expected, p.json())


if __name__ == "__main__":
    main()
