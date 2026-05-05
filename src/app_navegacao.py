from turtle import width

import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, ElevatedButton, Container, \
    TextButton, Colors, FontWeight
from datetime import datetime


def main(page: flet.Page):
    page.title = "Exemplo de Navegacao"
    page.theme_mode = ThemeMode.LIGHT
    page.window.width = 400
    page.window.height = 700




flet.run(main)