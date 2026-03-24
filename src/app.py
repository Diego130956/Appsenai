from turtle import width

import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, ElevatedButton, Container, \
    TextButton, Colors, FontWeight
from datetime import datetime


def main(page: flet.Page):
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.LIGHT
    page.window.width = 400
    page.window.height = 700

    def salvar_nome():
        text.value = f'Bom Dia {input_nome.value} {input_sobrenome.value}'

    def verificar_parimpar():
        numero1 = int(input_numero.value)
        if numero1 % 2 == 0:
            text_parimapr.value = f'O {numero1} é par'
        else:
            text_parimapr.value = f'O {numero1} é impar'

    def calcular_idade():
        numero = input_idade.value
        idade = datetime.now().year - int(numero)
        if idade >= 18:
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
    btn_verificar = ElevatedButton("Verificar", on_click=verificar_parimpar)
    btn_calcular = TextButton("Calcular", on_click=calcular_idade)

    page.add(

                Container(
                    Column(
                        [
                            Text("Atividade 01", weight=FontWeight.BOLD),
                            input_nome,
                            input_sobrenome,
                            btn_salvar,
                            text,



                        ],

                        horizontal_alignment=CrossAxisAlignment.CENTER



                    ),
                    bgcolor=Colors.BLUE_300,
                    padding=15,
                    width = 400,
                    border_radius=10

                ),
                Container(
                    Column(
                        [
                            Text("Atividade 02", weight=FontWeight.BOLD),

                            input_numero,
                            btn_verificar,
                            text_parimapr

                        ],

                        horizontal_alignment=CrossAxisAlignment.CENTER

                    ),
                    bgcolor=Colors.RED_300,
                    padding=15,
                    width=400,
                    border_radius = 10

                ),
                Container(
                    Column(
                        [
                            Text("Atividade 03", weight=FontWeight.BOLD),

                            input_idade,
                            btn_calcular,
                            text_idade

                        ],

                        horizontal_alignment=CrossAxisAlignment.CENTER

                    ),
                    bgcolor=Colors.PURPLE_300,
                    padding=15,
                    width=400,
                    border_radius=10

                )



    )


flet.run(main)


# input_idade,
#                             btn_calcular,
#                             text_idade,