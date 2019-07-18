from unittest import TestCase, main
from unittest.mock import patch
import sys
sys.path.append("C:\\Users\\EX002236\\Desktop\\Auto testing\\Blog")
import app
from blog import Blog


class AppTest(TestCase):
    def test_menu_print(self):
        with patch("builtins.input") as mocked_print:
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



main()
