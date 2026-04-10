import flet as ft

from models.user import User 
from repositories.user_repo import create_user, get_all_user, delete_user, get_user


def main (page: ft.Page):
    page.title = "Usuários"
    page.window.width = 400
    page.window.height = 700


    def clear_fields():
        for f in fields:
            f.value = ''
        page.update()


    def check (e):
        fields_value = all([name.value, last_name.value, email.value])
        btn_adicionar.disabled = not (fields_value)
        if fields_value:
            lbl_status.value = "Tudo certo"
            lbl_status.bgcolor = "blue"


        page.update()


    def save_user(e):
        new_user = User(name.value, last_name.value, email.value)
        try:
            create_user(new_user)
            lbl_status.value = f"{new_user.name} adicionado com sucesso"
            lbl_status.bgcolor = 'green'
            clear_fields()
        except:
            lbl_status.value = 'ERRO'
            clear_fields()
        
    
    lbl_content = ft.Text('Gerenciamento de usuários',
                    text_align='center',
                    size=24)
    
    #imputs
    name = ft.TextField(label="Nome", on_change=check)
    last_name = ft.TextField(label="Sobrenome", on_change=check)
    email = ft.TextField(label="Email", on_change=check)
    fields = [name, last_name, email]
    
    btn_adicionar = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=save_user, disabled=False)

    lbl_status = ft.Text("Todos os campos são obrigatórios", bgcolor="red")

    page.add(lbl_content)
    page.add(
        ft.Column(fields)
    )
    if name.value or last_name.value or email.value:
        lbl_status.value = "Tudo certo para salvar"
        lbl_status.bgcolor = "green"
        btn_adicionar.visible = True
    
    page.add(ft.Row())
    page.add(lbl_status)
    page.add(ft.Row())
    page.add(ft.Row())
    page.add(btn_adicionar)


ft.app(target=main)