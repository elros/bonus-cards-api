import os

os.environ['BONUSES_API_SETTINGS'] = os.path.join(os.path.dirname(__file__), 'settings.py')


from bonuses.app import app
app.run()
