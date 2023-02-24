from radicale.auth import BaseAuth
from requests      import get
from os            import environ
from sys           import stderr
from datetime      import datetime

class Auth(BaseAuth):
    def __init__(self, configuration):
        super().__init__(configuration)

    def login(self, login, password):
        answer = None
        response = get(
            'http://supervisor/auth',
            headers = {'X-Supervisor-Token': environ.get('SUPERVISOR_TOKEN')},
            auth = (login, password)
        )
        if (response.status_code == 200 and response.json()['result'] == 'ok'):
            answer= login
        return answer
