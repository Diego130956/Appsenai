from turtle import width

import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, ElevatedButton, TextButton
from datetime import datetime



def main(page: flet.Page):
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.LIGHT
    page.window.width = 400
    page.window.height = 700


    def salvar_nome():
        text.value = f'Bom Dia {input_nome.value} {input_sobrenome.value}'

    def verificar_parimpar():
        numero = input_numero.value
        if numero % 2 == 0:
            text_parimapr.value = f'O {numero} é par'
        else:
            text_parimapr.value = f'O {numero} é impar'

    def calcular_idade():
        numero = input_idade.value
        idade = datetime.now().year - int(numero)
        if  idade >= 18:
            text_idade.value = f'Você tem {idade} e é maior de idade'
        else:
            text_idade.value = f'Você tem {idade} e é menor de idade'





    text = Text()
    text_parimapr = Text()
    text_idade = Text()
    input_nome = TextField(label="Nome")
    input_sobrenome = TextField(label="Sobrenome")
    input_numero = TextField(label="Digite um numero", hint_text="Verifique se é par ou impar")
    input_idade = TextField(label="Digite o ano de nascimento", hint_text="EX: 2000")
    btn_salvar = OutlinedButton("Salvar", on_click=salvar_nome)
    btn_verificar = ElevatedButton("Verificar", on_click=salvar_nome)
    btn_calcular = TextButton("Calcular", on_click=calcular_idade)

    page.add(
        Column(
            [
                input_nome,
                input_sobrenome,
                btn_salvar,
                text,
                input_numero,
                btn_verificar,
                text_parimapr,
                input_idade,
                btn_calcular,
                text_idade,


            ],
            width = 400,
            horizontal_alignment = CrossAxisAlignment.CENTER
        )
    )

flet.run(main)