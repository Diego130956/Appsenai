from logging import disable
from urllib import response

import flet
from flet import ThemeMode, Text, View, AppBar, Colors, Button, FloatingActionButton, Icons, TextField, ListView, Card, \
     Icon, ListTile, PopupMenuButton, PopupMenuItem, Container, Column, Row, CrossAxisAlignment, FontWeight




import asyncio

import flet
import item
from flet import ThemeMode, View, Colors, ListView, Icons, ListTile, Image, Column, Text, \
    Pagelet, NavigationBar, NavigationBarDestination, ScrollMode, FontWeight, Card, Row, Colors
from flet.controls.material import card

from src.api_endpoint_cadastro import cadastro_cep


def main(page: flet.Page):
    # Configurações
    page.title = "Cadastro"
    page.theme_mode = ThemeMode.LIGHT  # ou ThemeMode.Light
    page.window.width = 400
    page.window.height = 700

    # Funções
    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )




            # TODO: Montar a lista de personagens do seu jeito, capricha ein



    def salvar_dados():
        cep = input_ce.value
        numero = input_numero.value
        tem_erro = False
        if cep:
            input_ce.error = None
        else:
            input_ce.error = "Campo obrigatorio"

        if numero:
            input_numero.error = None

        else:
            input_numero.error = "Campo obrigatorio"


            input_ce.value = ""
            input_numero.value = ""

        if not tem_erro:
            endereco = cadastro_cep(cep)
            text_cidade.value = endereco["localidade"]
            text_uf.value = endereco["uf"]
            text_logradouro.value = endereco["logradouro"]
            text_bairro.value = endereco["bairro"]


    # Gerenciar as telas(routes)
    def route_change():

        # montar a priemeira lista

        page.views.clear()

        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title=Text("Cadastro", weight=FontWeight.BOLD),
                        bgcolor=Colors.ORANGE
                    ),
                    input_ce,
                    input_numero,
                    text_cidade,
                    text_uf,
                    text_logradouro,
                    text_bairro,
                    btn_salvar,
                ],
                padding=0
            )
        )

    # Voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes
    list_view = ListView(height=500)


    input_ce = TextField(label="CEP", hint_text="Digite o CEP")
    input_numero = TextField(label="Numero", hint_text="Digite o numero da casa")
    btn_salvar = Button("Salvar", width=400, on_click=lambda: salvar_dados())
    text_cidade = TextField(label="Cidade",disabled=True)
    text_uf = TextField(label="UF",disabled=True)
    text_logradouro = TextField(label="Logradouro",disabled=True)
    text_bairro = TextField(label="Bairro",disabled=True)
    # dados = response.json()

    list_view = ListView(height=500)

    #  eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)










