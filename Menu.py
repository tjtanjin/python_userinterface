import kivy, sys
kivy.require('1.10.1')
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty

class LoginPage(Screen):
    def verify_credentials(self):
        if self.ids["username"].text == "username" and self.ids["password"].text == "password":
            self.manager.current = "user_page"
        else:
            self.ids["errorlogin_message"].opacity = 1
            Clock.schedule_once(self.displayerror, 2)

    def displayerror(self, instance):
            self.ids["errorlogin_message"].opacity = 0
    
    def quit(self):
        sys.exit()

class UserPage(Screen):
    def logout(self):
        self.manager.current = "login_page"
    pass

class ScreenManagement(ScreenManager):
    pass

kv_file = Builder.load_file('trial.kv')

class TrialApp(App):
    def builder(self):
        return kv_file

if __name__ == '__main__':
    TrialApp().run()