import asyncio
from cProfile import label

import flet
import item

from flet import ThemeMode, Text, View, AppBar, Colors, Button, FloatingActionButton, Icons, TextField, ListView, Card, \
     Icon, ListTile, PopupMenuButton, PopupMenuItem, Container, Column, Row, CrossAxisAlignment, FontWeight


class Elevador:
    def __init__(self, preco, marca, material, quantidade_carga):
        self.preco = preco
        self.marca = marca
        self.material=material
        self.quantidade_carga=quantidade_carga



def main(page: flet.Page):
    # Configurações
    page.title = "Elevador"
    page.theme_mode = ThemeMode.LIGHT  # ou ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700
    lista_dados = []

    # Funções
    # Função de navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def ver_detalhes(elevador):
        text_preco.value = elevador.preco
        text_marca.value = elevador.marca
        text_quantidade_carga.value = elevador.quantidade_carga
        text_material.value = elevador.material

        navegar("/detalhes")


    def montar_lista_padrao():
        list_view.controls.clear()

        for item in lista_dados:
            list_view.controls.append(
                ListTile(
                    leading=Icon(Icons.ELEVATOR_SHARP, color=Colors.BLUE),
                    title=item.marca,
                    subtitle=item.preco,
                    trailing=PopupMenuButton(
                        icon=Icons.MORE_VERT,
                        items=[
                            PopupMenuItem("Ver Detalhes", icon=Icons.REMOVE_RED_EYE, on_click=lambda _, elevador=item: ver_detalhes(elevador)),
                            PopupMenuItem("Excluir", icon=Icons.DELETE, on_click=lambda: excluir(item)),

                        ]
                    ),
                )
            )

    def excluir(item):
        lista_dados.remove(item)
        montar_lista_padrao()

    def salvar_dados():
        preco = input_preco.value.strip()
        marca = input_marca.value.strip()
        material = input_material.value.strip()
        quantidade_carga = input_quantidade_peso.value.strip()
        tem_erro = False

        if  preco:
            input_preco.error = None
        else:
            input_preco.error = "Campo obrigatorio"


        if marca:
            input_marca.error = None

        else:
            tem_erro = True
            input_marca.error = "Campo obrigatorio"

        if quantidade_carga:
            input_quantidade_peso.error = None
        else:
            input_quantidade_peso.error= "Campo obrigatorio"

        if material:
            input_material.error = None

        else:
            input_material.error = "Campo obrigatorio"


        if not tem_erro:
            #montar objeto
            elevador = Elevador(
                preco=preco,
                marca=marca,
                quantidade_carga=quantidade_carga,
                material=material,

            )
            lista_dados.append(elevador)

            input_preco.value = ""

            input_marca.value = ""

            input_material.value =""
            input_quantidade_peso.value =""


        montar_lista_padrao()

    # Função de gerenciar as telas (routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title="Elevador",
                        bgcolor=Colors.BLUE_GREY_400
                    ),
                list_view,
            ],
            floating_action_button=FloatingActionButton(
                icon=Icons.ADD,
                on_click=lambda: navegar("/form_cadastro"),

            )
        )
        )

        if page.route == "/form_cadastro":
            page.views.append(
                View(
                    route="/form_cadastro",
                    controls=[
                        flet.AppBar(
                            title="Lista de elevador",
                        ),
                        input_marca,
                        input_preco,
                        input_material,
                        input_quantidade_peso,
                        btn_salvar

                    ]
                )
            )

        elif page.route == "/detalhes":
            page.views.append(
                View(
                    route="/detalhes",
                    controls=[
                        flet.AppBar(
                        title="Detalhes:",
                        bgcolor=Colors.AMBER_200,
                        ),
                        Container(
                            Column([
                                text_marca,
                                Row([
                                    Icon(Icons.ARROW_RIGHT_ROUNDED, size=40),
                                    text_preco
                                ]),
                                Row([
                                    Icon(Icons.ARROW_RIGHT_ROUNDED, size=40),
                                    text_material
                                ]),
                                Row([
                                    Icon(Icons.ARROW_RIGHT_ROUNDED, size=40),
                                    text_quantidade_carga
                                ]),

                            ],
                                horizontal_alignment=CrossAxisAlignment.CENTER
                            ),
                        ),



                    ]
                )
            )

    # Função de voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes
    input_preco = TextField(label="Preço", hint_text="Digite o Preço" )
    input_material = TextField(label="Material", hint_text="Digite o material")
    input_marca = TextField(label="Marca", hint_text="Digite a Marca")
    input_quantidade_peso = TextField(label="Quantidade de Peso", hint_text="Digite a Quantidade de Peso máximo")
    text_preco = Text()
    text_marca = Text(weight=FontWeight.BOLD, size=24)
    text_quantidade_carga = Text()
    text_material = Text()



    # input_sexo = Dropdown(
    #     width=300,
    #     label="Sexo",
    #     editable=True,
    #     options=[
    #         DropdownOption("Feminino"),
    #         DropdownOption("Masculino"),
    #
    #     ],
    # )

    btn_salvar = Button("Salvar", width=400, on_click=lambda: salvar_dados())

    list_view = ListView(height=500)


    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)
