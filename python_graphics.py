try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

class Rect(object):
    def __init__(self, x1, y1, x2, y2, color):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.color = color

class Text(object):
    def __init__(self, x1, y1, text, color, font):
        self.x1 = x1
        self.y1 = y1
        self.text = text
        self.color = color
        self.font = font

class Window(object):
    def __init__(self, width, height, title = "Python Graphics", background="Black"):
        
        self.__root = tk.Tk()
        self.__root.resizable(width=False, height=False)
        self.__root.geometry('{}x{}'.format(width, height))
        self.__root.bind("<Key>", self.__get_key)
        self.__win = tk.Canvas(self.__root, width=width, height = height, background=background)
        self.__win.pack()
        self.__root.title(title)
        self.__last_key = []
        self.__objects = []

    def __get_key(self, event):
        """ Records any key events that occur """
        self.__last_key.append(event.keysym)

    def get_last_key(self):
        """ Returns the last key pressed.  None if no keys have been pressed since the last call. """
        if len(self.__last_key) > 0:
            return self.__last_key.pop(0)
        else:
            return None

    def draw_screen(self):
        """ Draws any objects you've sent to the screen """
        self.__win.delete(tk.ALL)

        for item in self.__objects:
            if isinstance(item, Rect):
                self.__win.create_rectangle(item.x1, item.y1, item.x2, item.y2, fill=item.color)
            elif isinstance(item, Text):
                self.__win.create_text(item.x1, item.y1, text=item.text, fill=item.color, font=item.font)

        self.__win.update()
        self.__objects.clear()

    def draw_rect(self, x1, y1, x2, y2, fill):
        """ Draws a square at the given location """
        self.__objects.append(Rect(x1, y1, x2, y2, fill))

    def draw_text(self, x1, y1, text, color, font=("Consolas", 8)):
        """ Draws text onto the screen """
        self.__objects.append(Text(x1, y1, text, color, font))
