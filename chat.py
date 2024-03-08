# Título: Hashzap
# Botão de iniciar chat
    # Clicou no botão:
        #popup / modal
            # Título: Bem vindo ao Hashzap
            # Campo: Escreva seu nome no chat
            # Botão: Entrar no chat

# Chat
# Embaixo do Chat
    # Campo de Digite sua mensagem
    # Botão de Enviar

# Flet -> Framework do Python

import flet as ft # Importar

def main(pagina): # Criar a função principal/main
    texto = ft.Text('Hashzap')

    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem):
        # Adicione a mensagem no chat
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        print('Enviar Mensagem')
        pagina.pubsub.send_all(f'{nome_usuario.value}: {campo_mensagem.value}')
        # Limpe o cmapo mensagem
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label='Digite sua mensagem', on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_mensagem, botao_enviar])
    def entrar_chat(evento):
        print('Entrar no chat')
        # Fechar popup
        popup.open = False
        # Tirar o botão iniciar chat
        pagina.remove(botao_iniciar)
        # Tirar o título Hashzap
        pagina.remove(texto)
        # Criar o chat
        pagina.add(chat)
        pagina.pubsub.send_all(f'{nome_usuario.value} entrou no chat')
        # Colocar o campo de digitar mensagem
        # Criar o botão de enviar
        pagina.add(linha_enviar)
        pagina.update()

    titulo_popup = ft.Text('Bem vindo ao Hashzap')
    nome_usuario = ft.TextField(label="Escreva o seu nome no chat")
    botao_entrar = ft.ElevatedButton('Entrar no chat', on_click=entrar_chat)
    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=titulo_popup,
        content=nome_usuario,
        actions=[botao_entrar]
    )

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open=True
        pagina.update()

    botao_iniciar = ft.ElevatedButton('Iniciar chat', on_click=abrir_popup)

    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER) # Criar o app chamando a função principal