from unittest import TestCase, main
import sys
sys.path.append("C:\\Users\\EX002236\\Desktop\\Auto testing\\Blog")
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog("Název", "autor")

        self.assertEqual("Název", b.title)
        self.assertEqual("autor", b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog("Název", "autor")
        b2 = Blog("Název2", "autor2")

        self.assertEqual(b.__repr__(), "Název by autor (0 posts)")
        self.assertEqual(b2.__repr__(), "Název2 by autor2 (0 posts)")

    def test_repr_multiple_posts(self):
        b = Blog("Název", "autor")
        b.posts = ["test"]

        b2 = Blog("Název2", "autor2")
        b2.posts = ["test1", "test2"]

        self.assertEqual(b.__repr__(), "Název by autor (1 post)")
        self.assertEqual(b2.__repr__(), "Název2 by autor2 (2 posts)")

if __name__ == "__main__":
    main()
