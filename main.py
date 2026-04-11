import flet as ft
from views.user_view import user_view

def main(page: ft.Page):
    page.title = "Wallet-Hub"
    page.theme_mode = ft.ThemeMode.LIGHT

    # 1. função de roteamento
    def route_change(route):
        print(f"Rota alterada para: {page.route}") # Log para seu terminal
        page.views.clear()
        
        # VIEW HOME
        page.views.append(
            ft.View(
                route="/",
                controls=[
                    ft.AppBar(title=ft.Text("Wallet Hub"), bgcolor="#0D9488"),
                    ft.Container(
                        content=ft.Column([
                            ft.Text("WALLET HUB", size=30, weight="bold"),
                            ft.ElevatedButton("IR PARA REGISTRO", on_click=lambda _: page.go("/user")),
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        padding=50
                    ),
                ],
            )
        )

        # VIEW USER
        if page.route == "/user":
            try:
                view_to_add = user_view(page)
                page.views.append(view_to_add)
            except Exception as e:
                print(f"Erro ao carregar user_view: {e}")

        page.update()

    # eventos
    page.on_route_change = route_change

    route_change(page.route) 

ft.app(target=main)