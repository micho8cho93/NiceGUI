from nicegui import ui

@ui.page('/')
def welcome_page():
    with ui.card().classes('fixed-center'):
        ui.label('Welcome to my app!').classes('text-2xl')
        with ui.row():
            ui.button('Login', on_click=lambda: ui.navigate.to('/login'))
            ui.button('Sign up', on_click=lambda: ui.navigate.to('/signup'))

@ui.page('/login')
def login_page():
    with ui.card().classes('fixed-center'):
        ui.label('Welcome back!')

        ui.input(label='Username', placeholder='start typing')
        result = ui.label()

        ui.input(label='Password', placeholder='start typing',
                validation={'Input too short': lambda value: len(value) > 6}, password=True, password_toggle_button=True)
        result = ui.label()

        ui.button('Submit', on_click=lambda: ui.navigate.to('/post_login'))
        ui.button('Go Back', on_click=lambda: ui.navigate.to('/'))

@ui.page('/signup')
def signup_page():
    with ui.card().classes('fixed-center'):
        ui.label('Create an account below')

        ui.input(label='Username', placeholder='start typing')
        result = ui.label()

        ui.input(label='Password', placeholder='start typing',
                validation={'Input too short': lambda value: len(value) > 6}, password=True, password_toggle_button=True)
        result = ui.label()

        ui.button('Submit', on_click=lambda: ui.navigate.to('/'))
        ui.button('Go Back', on_click=lambda: ui.navigate.to('/'))

@ui.page('/post_login')
def post_login_page():
    with ui.card().classes('fixed-center'):
        ui.label('You are now logged in!')
        ui.button('Logout', on_click=lambda: ui.navigate.to('/welcome'))

welcome_page()

ui.run()