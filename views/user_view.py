import flet as ft

from models.user import User 
from repositories.user_repo import create_user, get_all_user, delete_user, get_user


def user_view(page: ft.Page):

    def clear_fields():
        for f in fields:
            f.value = ''
        page.update()

    def check(e):
        fields_value = all([name.value, last_name.value, email.value])
        btn_adicionar.disabled = not fields_value
        if fields_value:
            lbl_status.value = "Tudo certo"
            lbl_status.color = "white"
            lbl_status.bgcolor = "green"
        else:
            lbl_status.value = "Todos os campos são obrigatórios"
            lbl_status.bgcolor = "red"
        page.update()

    def save_user(e):
        fields_value = all([name.value, last_name.value, email.value])
        try:
            new_user = User(name=name.value, last_name=last_name.value, email=email.value)
            create_user(new_user)
            lbl_status.value = f"{name.value} adicionado com sucesso"
            lbl_status.bgcolor = 'green'
            clear_fields()
        except Exception as ex:
            lbl_status.value = f'ERRO: {ex}'
            lbl_status.bgcolor = 'red'
        page.update()

    #INTERFACE
    lbl_content = ft.Text('Gerenciamento de usuários', text_align='center', size=24)
    
    name = ft.TextField(label="Nome", on_change=check)
    last_name = ft.TextField(label="Sobrenome", on_change=check)
    email = ft.TextField(label="Email", on_change=check)
    fields = [name, last_name, email]
    
    btn_adicionar = ft.FloatingActionButton(
        icon=ft.Icons.SAVE, 
        on_click=save_user, 
        disabled=True,
        bgcolor="#0D9488"
    )

    lbl_status = ft.Text("Todos os campos são obrigatórios", bgcolor="red", color="white")

    # RETORNO DA VIEW
    return ft.View(
        route="/user",
        controls=[
            ft.AppBar(
                title=ft.Text("Registrar Usuário"),
                bgcolor="#0D9488",
                color="white",
                # Botão para voltar manualmente se necessário
                leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda _: page.go("/"))
            ),
            lbl_content,
            ft.Column(fields),
            lbl_status,
            ft.Row([btn_adicionar], alignment=ft.MainAxisAlignment.END)
        ]
    )