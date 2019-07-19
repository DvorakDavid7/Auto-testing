from unittest import TestCase, main
from unittest.mock import patch
import sys
sys.path.append("C:\\Users\\EX002236\\Desktop\\Auto testing\\Blog")
import app
from blog import Blog
from post import Post


class AppTest(TestCase):
    def test_menu_print(self):
        with patch("builtins.input", return_value = "q") as mocked_print:
            with patch("builtins.print"): # patch funkce print v proceduře print_blogs()
                app.menu()
                mocked_print.assert_called_with(app.MENU_TEXT)


    def test_menu_calls_print_blogs(self):
        with patch("app.print_blogs") as mocked_print:
            # abych nemusel zadávat input nahradím input() falešnou funkcí (mock)
            with patch("builtins.input", return_value = "q"):
                app.menu()
                mocked_print.assert_called()


    def test_print_blogs(self):
        blog = Blog("Test", "Test Author")
        app.blogs = {"Test": blog}
        # všechny funkce print v tomto bloku jsou mock
        with patch("builtins.print") as mocked_print:
            app.print_blogs()
            # pokud je výstupem argument test projde
            mocked_print.assert_called_with("- Test by Test Author (0 posts)")


    def test_ask_create_blog(self):
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ("Test", "Autor")
            # "Test" pro první volání "Autor" pro druhé volání
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get("Test"))
            # metoda get() vrací hodnotu pro zadaný klíč



    def test_ask_read_blog(self):
        blog = Blog("Test", "Test Author")
        app.blogs = {"Test": blog}
        with patch("builtins.input", return_value = "Test") as mocked_input:
            with patch("app.print_posts") as mocked_print_posts:
                app.ask_read_blog()
                mocked_print_posts.assert_called_with(blog)


    def test_print_posts(self):
        blog = Blog("Test", "Test Author")
        blog.create_post("Test Post", "Test content")
        app.blogs = {"Test": blog}
        with patch("app.print_post") as mocked_print_post:
            app.print_posts(blog)
            mocked_print_post.assert_called_with(blog.posts[0])


    def test_print_post(self):
        post = Post("Titulek", "Obsah")
        expected = "Titulek: Obsah"
        with patch("builtins.print") as mocked_print:
            app.print_post(post)
            mocked_print.assert_called_with(expected)



main()
