from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.core.window import Window

# Tema de fondo
Window.clearcolor = (0.95, 0.97, 1, 1)  # color azul muy claro

# Variables globales
registered_username = ""
registered_password = ""

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=12, padding=20)

        # Logo
        try:
            layout.add_widget(Image(source="logo.png", size_hint=(1, 0.4)))
        except:
            pass  # Evita errores si falta la imagen

        # Título
        layout.add_widget(Label(text='Inicia sesión o regístrate', font_size=22, bold=True, color=(0.2, 0.3, 0.4, 1)))

        # Usuario
        layout.add_widget(Label(text='Usuario:', font_size=16, color=(0.2, 0.2, 0.2, 1)))
        self.username_input = TextInput(multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.username_input)

        # Contraseña
        layout.add_widget(Label(text='Contraseña:', font_size=16, color=(0.2, 0.2, 0.2, 1)))
        self.password_input = TextInput(password=True, multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.password_input)

        # Botón de Registro
        self.register_btn = Button(text='Registrarse', background_color=(0.1, 0.5, 1, 1),
                                   font_size=16, size_hint_y=None, height=45)
        self.register_btn.bind(on_press=self.register)
        layout.add_widget(self.register_btn)

        # Botón de Inicio de Sesión
        self.login_btn = Button(text='Iniciar Sesión', background_color=(0.1, 0.4, 1, 1),
                                font_size=16, size_hint_y=None, height=45)
        self.login_btn.bind(on_press=self.login)
        layout.add_widget(self.login_btn)

        self.add_widget(layout)

    def register(self, instance):
        global registered_username, registered_password
        username = self.username_input.text.strip()
        password = self.password_input.text.strip()

        if not username or not password:
            self.show_popup("Error", "Por favor, completa todos los campos.")
        else:
            registered_username = username
            registered_password = password
            self.show_popup("Registro exitoso", "Ahora puedes iniciar sesión.")

    def login(self, instance):
        username = self.username_input.text.strip()
        password = self.password_input.text.strip()

        if username == registered_username and password == registered_password:
            self.manager.current = "welcome"
            self.manager.get_screen("welcome").welcome_label.text = f"🎉 Bienvenido, {username}!"
        else:
            self.show_popup("Error", "Usuario o contraseña incorrectos.")

    def show_popup(self, title, message):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text=message, font_size=16))
        close_btn = Button(text='Cerrar', size_hint=(1, 0.5))
        content.add_widget(close_btn)
        popup = Popup(title=title, content=content, size_hint=(0.8, 0.4))
        close_btn.bind(on_press=popup.dismiss)
        popup.open()

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        self.welcome_label = Label(text="Bienvenido", font_size=22, color=(0, 0, 0, 1))
        layout.add_widget(self.welcome_label)
        self.add_widget(layout)

class MainApp(App):
    def build(self):
        sm = ScreenManager()

        login_screen = LoginScreen(name="login")
        welcome_screen = WelcomeScreen(name="welcome")

        sm.add_widget(login_screen)
        sm.add_widget(welcome_screen)

        return sm

if __name__ == "__main__":
    MainApp().run()
