import tkinter as tk
import unittest
from unittest.mock import patch

from calc.calculator import add  # 仮の関数
from tk_test_app.test_app import App  # 仮のモジュールとクラス


class TestCalclator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)


class TestApp(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = App(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_initial_label_text(self):
        self.assertEqual(self.app.label.cget("text"), "Hello, World!")

    def test_button_click(self):
        with patch.object(self.app, 'on_click') as mock_on_click:
            self.app.button.invoke()
            self.root.update_idletasks()  # イベントループを強制的に更新
            mock_on_click.assert_called_once()

    def test_label_text_after_click(self):
        self.app.on_click()
        self.assertEqual(self.app.label.cget("text"), "Button Clicked!")

if __name__ == "__main__":
    unittest.main()