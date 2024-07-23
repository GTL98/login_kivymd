# --- Importar as bibliotecas --- #
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

# --- Configurar a dimensão da janela do App --- #
Window.size = (350, 600)


class Login(MDApp):
    """Classe responsável por criar o App."""
    def build(self):
        """Função responsável por construir o App."""
        # --- Carregar o arquivo .kv --- #
        pagina_login = Builder.load_file('login.kv')
        return pagina_login


if __name__ == '__main__':
    Login().run()
