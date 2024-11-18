from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout
import re

from plyer import filechooser

# KV layout definition
kv = '''
# Login screen layout
<MaterialTextInput>:
    name: "login"
    FloatLayout:
        MDTextField:
            id: username_input
            hint_text: "Email"
            font_size: "20dp"
            icon_right: "email"
            size_hint_x: .85
            pos_hint: {"center_x": .5, "center_y": .65}
            mode: "line"
            helper_text: "Enter a valid email"
            helper_text_mode: "on_focus"
            error: False  # To control error highlighting

        MDTextField:
            id: password_input
            hint_text: "Password"
            font_size: "20dp"
            icon_right: "eye-off"
            size_hint_x: .85
            pos_hint: {"center_x": .5, "center_y": .5}
            mode: "line"
            password: True
            hint_text_color: (1, 1, 1, 1)
            helper_text: "Password required"
            helper_text_mode: "on_focus"
            error: False  # To control error highlighting

        # Checkbox to toggle password visibility
        BoxLayout:
            spacing: dp(5)
            size_hint: .85, None
            pos_hint: {"center_x": .5, "center_y": .38}
            height: "30dp"
            MDCheckbox:
                id: my_checkbox
                size_hint: None, None
                size: dp(30), dp(30)
                on_press:
                    password_input.password = not password_input.password
            MDLabel:
                text: "Show password"
                size_hint_y: None
                height: dp(30)
                theme_text_color: "Secondary"

        # Sign in and Sign up buttons
        BoxLayout:
            orientation: "horizontal"
            size_hint: .85, None
            height: "50dp"
            pos_hint: {"center_x": .5, "center_y": .3}
            spacing: dp(10)

            MDFlatButton:
                text: "SIGN IN"
                font_size: "22dp"
                on_release:
                    app.validation1()
                    app.password()
                    app.switch_to_dashboard()
                md_bg_color: 0.1, 0.7, 0.3, 1
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                size_hint: 0.45, None
                height: dp(50)

            MDFlatButton:
                text: "SIGN UP"
                font_size: "22dp"
                on_release:
                    app.switch_to_registred()  # Ensure proper indentation
                md_bg_color: 0.7, 0.3, 0.1, 1
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                size_hint: 0.45, None
                height: dp(50)

# Dashboard screen layout
<Dashboard>:
    name: "dashboard"
    FloatLayout:
        

        BoxLayout:
            orientation: "horizontal"
            size_hint: None, None
            size: "45dp", "50dp"
            pos_hint: {"right": 1, "top": 1}
            spacing: dp(25)

            Image:
                id: profile_picture
                source: "images/settings1.png"
                size_hint: None, None
                size: "35dp", "55dp"
                pos_hint: {"right":1, "top": 1}
                allow_stretch: True
                radius: [60]

        BoxLayout:
            orientation: "horizontal"
            size_hint: None, None
            size: "110dp", "40dp"
            pos_hint: {"right": 1, "top": 1}
            spacing: dp(25)

            Image:
                id: profile_picture
                source: "images/withdraw.png"
                size_hint: None, None
                size: "35dp", "55dp"
                pos_hint: {"right":1, "top": 1}
                allow_stretch: True
                radius: [60]
                on_touch_down: app.switch_to_withdraw(*args)

        BoxLayout:
            orientation: "horizontal"
            size_hint: None, None
            size: "175dp", "40dp"
            pos_hint: {"right": 1, "top": 1}
            spacing: dp(25)

            Image:
                id: profile_picture
                source: "images/image.jpg"
                size_hint: None, None
                size: "35dp", "55dp"
                pos_hint: {"right":1, "top": 1}
                allow_stretch: True
                radius: [60]
                on_touch_down:app.switch_to_Wallet(*args)

        BoxLayout:
            orientation: "vertical"
            size_hint: None, None
            size: "65dp", "75dp"
            pos_hint: {"right": 1, "top": 1}

            MDLabel:
                text: "settings"
                size_hint_y: None
                height: dp(20)
                pos_hint: {"center_x": 0.65, "top": 1}
                theme_text_color: "Custom"
                text_color: 1.0, 0.929, 0.153
        BoxLayout:
            orientation: "vertical"
            size_hint: None, None
            size: "145dp", "75dp"
            pos_hint: {"right": 1, "top": 1}

            MDLabel:
                text: "withdraw"
                size_hint_y: None
                height: dp(20)
                pos_hint: {"center_x": 0.65, "top": 1}
                theme_text_color: "Custom"
                text_color: 0, 0, 1, 1

        BoxLayout:
            orientation: "vertical"
            size_hint: None, None
            size: "207dp", "75dp"
            pos_hint: {"right": 1, "top": 1}

            MDLabel:
                text: "wallet"
                size_hint_y: None
                height: dp(20)
                pos_hint: {"center_x": 0.65, "top": 1}
                theme_text_color: "Custom"
                text_color: 0.8980, 0.2941, 0.1333, 1

        Image:
            id: profile_image
            source: "images/profile.png"
            size_hint: None, None
            size: "40dp", "55dp"
            pos_hint: {"left": 1,"top":1}
            allow_stretch: True
            radius: [60]
            on_touch_down: app.on_image_touch_up(*args)

        MDLabel:
            text: "profile"
            size_hint_y: None
            pos_hint: {"center_x": .5, "center_y": .9}
            height: dp(30)
            theme_text_color: "Custom"
            text_color: 1, 0.0784, 0.5765, 1

        MDRaisedButton:
            text: "PHENOMENAL"
            size_hint: None, None
            size: "150dp", "100dp"
           
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            md_bg_color:0.5, 0.0, 0.5
            text_color:1.0, 0.8431, 0.0
            font_size: "24sp"

        BoxLayout:
            orientation: "horizontal"
            size_hint: None, None
            size: "150dp", "40dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.3}
            spacing: dp(4)

            MDRaisedButton:
                text: "Invest"
                size_hint: None, None
                size: "100dp", "50dp"
                md_bg_color: 0.2, 0.6, 1, 1
                on_release:app.switch_to_invest()

            MDRaisedButton:
                text: "Referral"
                size_hint: None, None
                size: "100dp", "50dp"
                md_bg_color: 0.8, 0.3, 0.3, 1
              

        MDRaisedButton:
            text: "ENTER TO THE GAME"
            size_hint: None, None
            size: "100dp", "50dp"
            md_bg_color:0.0, 0.392, 0.0
            
            pos_hint: {"center_x": 0.5, "center_y": 0.1}
            text_color: 1.0, 1.0, 1.0

# Registered screen layout
<registred>:
    name: "registred"
    FloatLayout:
        MDTextField:
            id: Dashboard_email_input
            hint_text: "Email"
            font_size: "20dp"
            icon_right: "email"
            size_hint_x: .85
            pos_hint: {"center_x": .5, "center_y": .85}
            mode: "line"
            helper_text: "Enter a valid email"
            helper_text_mode: "on_focus"
            error: False

        MDTextField:
            id: Dashboard_firstname_input
            hint_text: "First Name"
            font_size: "20dp"
            icon_right: "account"
            size_hint_x: .85
            pos_hint: {"center_x": .5, "center_y": .71}
            mode: "line"
            helper_text: "Enter a valid first name"
            helper_text_mode: "on_focus"
            error: False

        MDTextField:
            id: Dashboard_lastname_input
            hint_text: "Last Name"
            font_size: "20dp"
            icon_right: "account"
            size_hint_x: .85
            pos_hint: {"center_x": .5, "center_y": .57}
            mode: "line"
            helper_text: "Enter a valid last name"
            helper_text_mode: "on_focus"
            error: False

        MDTextField:
            id: Dashboard_username_input
            hint_text: "Username"
            font_size: "20dp"
            icon_right: "account"
            size_hint_x: .85
            pos_hint: {"center_x": .5, "center_y": .43}
            mode: "line"
            helper_text: "Enter a valid username"
            helper_text_mode: "on_focus"
            error: False

        MDTextField:
            id: Dashboard_password_input
            hint_text: "Password"
            font_size: "20dp"
            icon_right: "eye-off"
            size_hint_x: .85
            pos_hint: {"center_x": .5, "center_y": .29}
            mode: "line"
            password: True
            hint_text_color: (1, 1, 1, 1)
            helper_text: "Password required"
            helper_text_mode: "on_focus"
            error: False

        # Checkbox to toggle password visibility
        BoxLayout:
            spacing: dp(5)
            size_hint: .85, None
            pos_hint: {"center_x": .5, "center_y": .18}
            height: "30dp"
            MDCheckbox:
                id: my_checkbox
                size_hint: None, None
                size: dp(30), dp(30)
                on_press:
                    password_input.password = not password_input.password
            MDLabel:
                text: "Show password"
                size_hint_y: None
                height: dp(30)
                theme_text_color: "Secondary"

        # Sign up and Sign in buttons
        BoxLayout:
            orientation: "horizontal"
            size_hint: .85, None
            height: "50dp"
            pos_hint: {"center_x": .5, "center_y": .09}
            spacing: dp(10)

            MDFlatButton:
                text: "SIGN UP"
                font_size: "22dp"
                on_release:
                    app.validation()
                    
                    
                md_bg_color: 0.1, 0.7, 0.3, 1
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                size_hint: 0.45, None
                height: dp(50)
<Wallet>:
    name: "wallet"
    FloatLayout:

        # Profile Image
        Image:
            id: profile_picture
            source: "images/image.jpg"
            size_hint: None, None
            size: "200dp", "75dp"
            pos_hint: {"center_x": .5, "center_y": .8}
            allow_stretch: True

        # Wallet Title
        BoxLayout:
            orientation: "horizontal"
            size_hint: None, None
            size: "85dp", "20dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.7}
            

            MDLabel:
                text: "wallet"
                font_size: "30dp"
                pos_hint: {"center_x": 0.5, "center_y": .7}
                theme_text_color: "Custom"
                text_color: 1, 0.0784, 0.5765, 1    

        # Amount Input Field
        MDTextField:
            id: wallet_amount
            hint_text: "Amount"
            font_size: "20dp"
            icon_right: "currency-usd"  # Currency USD icon on the right
            size_hint_x: .75
            pos_hint: {"center_x": .5, "center_y": .5}
            mode: "fill"
            readonly: True  # Make the field readonly (no user input)
            text: "100.00"  # You can set a default value if needed
        MDRaisedButton:
            text: "Back"
            size_hint: None, None  # Disable automatic scaling, set fixed size
            size: "75dp", "30dp"  # Define the fixed size for the button
            md_bg_color: 0.0, 0.0, 0.0  # Background color: Black
            text_color: 1.0, 1.0, 1.0  # Text color: White
            pos_hint: {"x": 0, "top": 1}  # Position the button at the top-left corner
            on_release: app.switch_to_dashboard1()  # Call the method when the button is pressed
    

            
<Withdraw>:
    name: "withdraw"
    FloatLayout:

        # Profile Image
        Image:
            id: profile_picture
            source: "images/withdraw.png"
            size_hint: None, None
            size: "200dp", "75dp"
            pos_hint: {"center_x": .5, "center_y": .8}
            allow_stretch: True
            
            # Wallet Title
        BoxLayout:
            orientation: "horizontal"
            size_hint: None, None
            size: "85dp", "20dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.7}
            

            MDLabel:
                text: "withdraw"
                font_size: "20dp"
                pos_hint: {"center_x": 0.5, "center_y": .7}
                theme_text_color: "Custom"
                text_color: 1, 0.0784, 0.5765, 1    

        # Amount Input Field
        MDTextField:
            id: withdraw_amount
            hint_text: "amount to withdraw"
            font_size: "20dp"
            icon_right: "currency-usd"  # Changed to a valid icon
            size_hint_x: .75
            pos_hint: {"center_x": .5, "center_y": .6}
            mode: "round"
            helper_text: "Enter a valid amount"
            helper_text_mode: "on_focus"
            error: False
        MDTextField:
            id: withdraw_account_number
            hint_text: "Bank account number"
            font_size: "20dp"
           
            size_hint_x: .75
            pos_hint: {"center_x": .5, "center_y": .5}
            mode: "round"
            helper_text: "Enter a valid amount"
            helper_text_mode: "on_focus"
            error: False
        MDTextField:
            id: withdraw_name
            hint_text: "account holder name"
            font_size: "20dp"
           
            size_hint_x: .75
            pos_hint: {"center_x": .5, "center_y": .4}
            mode: "round"
            helper_text: "Enter a valid Name"
            helper_text_mode: "on_focus"
            error: False
        MDLabel:
            text: 'Account Type'
            theme_text_color: "Secondary"
            size_hint_y: None
            height: "48dp"
        MDRaisedButton:
            text: "SUBMIT"
            size_hint: None, None
            size: "100dp", "50dp"
            md_bg_color:0.0, 0.0, 1.0
            on_press: app.on_referral_button_press
            pos_hint: {"center_x": 0.5, "center_y": 0.3}
            text_color: 1.0, 1.0, 1.0
        MDRaisedButton:
            text: "Back"
            size_hint: None, None  # Disable automatic scaling, set fixed size
            size: "75dp", "30dp"  # Define the fixed size for the button
            md_bg_color: 0.0, 0.0, 0.0  # Background color: Black
            text_color: 1.0, 1.0, 1.0  # Text color: White
            pos_hint: {"x": 0, "top": 1}  # Position the button at the top-left corner
            on_release: app.switch_to_dashboard1()  # Call the method when the button is pressed

<invest>:
    name: "invest"
    FloatLayout:

        # Profile Image
        Image:
            id: profile_picture
            source: "images/invest-removebg-preview.png"
            size_hint: None, None
            size: "250dp", "80dp"
            pos_hint: {"center_x": .5, "center_y": .8}
            allow_stretch: True
        MDTextField:
            id: Invest_amount_input
            hint_text: "Enter your amount"
            font_size: "20dp"
           
            size_hint_x: .75
            pos_hint: {"center_x": .5, "center_y": .6}
            mode: "fill"
            input_filter: "float" 
            
        MDRaisedButton:
            text: "invest"
            size_hint: None, None
            size: "100dp", "50dp"
            md_bg_color:0.5, 0.0, 0.5
            on_press: app.on_referral_button_press
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            text_color: 1.0, 1.0, 1.0       
            
        MDRaisedButton:
            text: "Back"
            size_hint: None, None  # Disable automatic scaling, set fixed size
            size: "75dp", "30dp"  # Define the fixed size for the button
            md_bg_color: 0.0, 0.0, 0.0  # Background color: Black
            text_color: 1.0, 1.0, 1.0  # Text color: White
            pos_hint: {"x": 0, "top": 1}  # Position the button at the top-left corner
            on_release: app.switch_to_dashboard1()  # Call the method when the button is pressed

           
           
            
        
        
        
            


            


'''


class MaterialTextInput(Screen):
    """Login screen logic"""
    pass

class Dashboard(Screen):
    """Dashboard screen logic"""
    pass

class registred(Screen):
    """Registered screen logic"""
    pass
class Wallet(Screen):
    """wallet screen logic"""
    pass
class Withdraw(Screen):
    """withdraw screen logic"""
    pass
class Invest(Screen):
    """invest screen logic"""
    pass



class Kishore(MDApp):
    def build(self):
        """Build and return the ScreenManager with all screens"""
        self.theme_cls.theme_style = "Dark"  # Set the theme style
        
        # Create ScreenManager
        sm = ScreenManager()

        # Add screens to the manager
        sm.add_widget(MaterialTextInput(name="login"))
        sm.add_widget(Dashboard(name="dashboard"))
        sm.add_widget(registred(name="registred"))
        sm.add_widget(Wallet(name="wallet"))
        sm.add_widget(Withdraw(name="withdraw"))
        sm.add_widget(Invest(name="invest"))
        return sm  # Return ScreenManager as root

    def validation(self):
        email1 = self.root.get_screen("registred").ids.Dashboard_email_input.text
        email_regex1 = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(email_regex1, email1):
            self.root.get_screen("registred").ids.Dashboard_email_input.helper_text = ""
            self.root.get_screen("registred").ids.Dashboard_email_input.error = False
            self.root.current = "login"  # Switch to the login screen
            # Clear fields on login screen
            self.clear_login_fields()
            print("Valid email")
            return True
        else:
            self.root.get_screen("registred").ids.Dashboard_email_input.helper_text = "Invalid email"
            self.root.get_screen("registred").ids.Dashboard_email_input.error = True
            print("Invalid email")
            return False

    def validation1(self):
        email = self.root.get_screen("login").ids.username_input.text
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(email_regex, email):
            self.root.get_screen("login").ids.username_input.helper_text = ""
            self.root.get_screen("login").ids.username_input.error = False
            print("Valid email")
            return True
        else:
            self.root.get_screen("login").ids.username_input.helper_text = "Invalid email"
            self.root.get_screen("login").ids.username_input.error = True
            print("Invalid email")
            return False    

    def password(self):
        password = self.root.get_screen("login").ids.password_input.text
        if password == "":
            self.root.get_screen("login").ids.password_input.helper_text = "Invalid Password"
            self.root.get_screen("login").ids.password_input.error = True
            print("Invalid password")
            return False
        else:
            self.root.get_screen("login").ids.password_input.helper_text = ""
            self.root.get_screen("login").ids.password_input.error = False
            print("Valid password")
            return True

    def switch_to_dashboard(self):
        email = self.root.get_screen("login").ids.username_input.text
        password = self.root.get_screen("login").ids.password_input.text
        if email == "anv12@gmail.com" and password == "ram123":
            self.root.current = "dashboard"  # Switch to dashboard screen
            print("Login successful")
        else:
            print("Invalid credentials")
    def switch_to_dashboard1(self):
        self.root.current = "dashboard"
    def switch_to_registred(self):
        self.root.current = "registred"  # Switch to the registered screen

    def clear_login_fields(self):
        # Reset login screen fields
        self.root.get_screen("login").ids.username_input.text = ""
        self.root.get_screen("login").ids.password_input.text = ""
        self.root.get_screen("login").ids.username_input.helper_text = ""
        self.root.get_screen("login").ids.username_input.error = False
        self.root.get_screen("login").ids.password_input.helper_text = ""
        self.root.get_screen("login").ids.password_input.error = False
    def on_image_touch_up(self, instance, touch):
        
      if instance.collide_point(*touch.pos):
        self.select_image()


    def select_image(self):
        # Use Plyer to open the file chooser
        filechooser.open_file(filters=["*.png", "*.jpg", "*.jpeg", "*.bmp", "*.gif"],
        on_selection=self.update_image
          )
        

    def update_image(self, selection):
    # This function is called when a file is selected
        if selection:
            # Make sure we use the correct 'id' reference for the Image widget
            self.root.get_screen("dashboard").ids.profile_image.source = selection[0]  # Update the image source
            print(f"Image updated to: {selection[0]}")
        else:
            print("No image selected!")
    def switch_to_Wallet(self,instance, touch):
        if instance.collide_point(*touch.pos):  # Checks if the touch occurred within the bounds of the image
            self.root.current = "wallet"  # Switch to the wallet screen
            print("Switched to Wallet Screen")
    def switch_to_withdraw(self,instance, touch):
        if instance.collide_point(*touch.pos):  # Checks if the touch occurred within the bounds of the image
            self.root.current = "withdraw"  # Switch to the wallet screen
            print("Switched to Withdraw Screen")   
    def switch_to_invest(self):
       # Checks if the touch occurred within the bounds of the image
            self.root.current = "invest"  # Switch to the wallet screen
            print("Switched to invest Screen")        
    Builder.load_string(kv)

if __name__ == "__main__":
 Kishore().run()
