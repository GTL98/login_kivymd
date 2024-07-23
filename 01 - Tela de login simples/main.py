# --- Importar as bibliotecas --- #
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

# --- Configurar a dimesão da janela do App --- #
Window.size = (450, 500)


class Login(MDApp):
    """Classe responsável por criar o App."""
    def builder(self) -> None:
        """Função responsável por construir o App."""
        # --- Ler o arquivo .kv --- #
        pagina_login = Builder.load_file('login.kv')
        return pagina_login

    def verificacao(self, email: str, senha: str) -> None:
        """
        Função resposável por verificar o e-mail e a senha.
        :param email: E-mail recebido.
        :param senha: Senha recebida.
        """
        if email == 'gui@ufpr.br' and senha == '123':
            print('Logado com sucesso!')
        else:
            print('E-mail não cadastrado')


if __name__ == '__main__':
    Login().run()
