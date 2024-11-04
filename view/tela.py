from abc import ABC, abstractmethod
from os import path
from tkinter import Tk, Label, Entry, Button, Frame


class Tela(ABC):
    def __init__(self: object, master: Tk) -> None:
        self.elementos: set = set().add(master)
        self.master = master
        self.html()
        self.css()

    @abstractmethod
    def html(self: object, master: Tk) -> None:
        pass

    def get_style(self: object) -> None:
        style_sheet_path = path.realpath(path.dirname(__file__))
        if style_sheet_path.find('/') != -1:
            style_sheet_path = str(
                style_sheet_path[:style_sheet_path.find('/')] +
                'model/style_sheet.txt')
        else:
            style_sheet_path = str(
                    style_sheet_path[:style_sheet_path.find('\\')] +
                    'model\\style_sheet.txt')
        with open(style_sheet_path, 'r') as style_sheet:
            self.parametros = {
                style[:style.find(':')]:
                style[style.find(':') + 1:style.rfind('\n')]
                for style in style_sheet.readlines()
            }

    def css(self: object) -> None:
        self.get_style()
        FG = self.parametros.get('fg-color')
        BG = self.parametros.get('bg-color')
        FONT = (self.parametros.get('font-family'),
                self.parametros.get('font-size'),
                self.parametros.get('font-extra'))
        for elemento in self.elementos:
            tipo = type(elemento)
            if tipo is Label:
                elemento.config(bg=BG, fg=FG, font=FONT)
            elif tipo is Entry:
                elemento.config(bg=BG, fg=FG, font=FONT, insertbackground=FG)
            elif tipo is Button:
                elemento.config(bg=BG, fg=FG, font=FONT,
                                activebackground=FG,
                                activeforeground=BG)
            elif tipo is Tk:
                elemento.title(self.titulo)
                elemento.geometry(self.geometry)
                elemento.minsize(self.minsize)
                elemento.maxsize(self.maxsize)
            elif tipo is Frame:
                elemento.config(bg=BG)
