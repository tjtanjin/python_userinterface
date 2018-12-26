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
        """
        Verify if the correct login credentials have been provided.
        Args:
            None
        """
        #Note that it is bad practice to hardcode username/password, this is used for rough idea only
        if self.ids["username"].text == "username" and self.ids["password"].text == "password":
            self.ids["successlogin_message"].opacity = 1
            Clock.schedule_once(self.hidemessage, 1.5)
            self.manager.current = "user_page"
        else:
            self.ids["errorlogin_message"].opacity = 1
            Clock.schedule_once(self.hidemessage, 1.5)

    def hidemessage(self, placeholder):
        """
        Toggles message on and off.
        Args:
            placeholder: -
        """
        self.ids["successlogin_message"].opacity = 0
        self.ids["errorlogin_message"].opacity = 0
    
    def quit(self):
        """
        Exits upon clicking the quit button.
        Args:
            None
        """
        sys.exit()

class UserPage(Screen):
    def logout(self):
        """
        Logout back to main login page.
        Args:
            None
        """
        self.manager.current = "login_page"

class ScreenManagement(ScreenManager):
    pass

kv_file = Builder.load_file('trial.kv')

class TrialApp(App):
    def builder(self):
        return kv_file

if __name__ == '__main__':
    TrialApp().run()