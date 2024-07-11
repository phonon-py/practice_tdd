import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sample App")

        self.label = tk.Label(root, text="Hello, World!")
        self.label.pack()

        self.button = tk.Button(root, text="Click Me", command=self.on_click)
        self.button.pack()

    def on_click(self):
        self.label.config(text="Button Clicked!")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()