import sys
import os

my_list = ['C:\\PythonProject2\\.venv\\Scripts\\pade.exe', 'C:\\Users\\mrsli\\AppData\\Local\\Programs\\Python\\Python38\\python38.zip', 'C:\\Users\\mrsli\\AppData\\Local\\Programs\\Python\\Python38\\DLLs', 'C:\\Users\\mrsli\\AppData\\Local\\Programs\\Python\\Python38\\lib', 'C:\\Users\\mrsli\\AppData\\Local\\Programs\\Python\\Python38', 'C:\\PythonProject2\\.venv', 'C:\\PythonProject2\\.venv\\lib\\site-packages',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\terminaltables-3.1.0-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\flask-1.1.1-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\flask_migrate-2.5.2-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\flask_sqlalchemy-2.4.1-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\flask_wtf-0.14.2-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\flask_login-0.4.1-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\flask_bootstrap-3.3.7.1-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\flask_script-2.0.6-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\click-7.0-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\itsdangerous-1.1.0-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\jinja2-2.10.3-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\markupsafe-1.1.1-py3.8-win-amd64.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\werkzeug-0.16.0-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\alchimia-0.8.1-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\sqlalchemy-1.3.10-py3.8-win-amd64.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\requests-2.22.0-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\twisted-19.7.0-py3.8-win-amd64.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\alembic-1.14.0-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\wtforms-3.2.1-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\visitor-0.1.3-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\dominate-2.9.1-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\certifi-2024.12.14-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\urllib3-1.25.11-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\idna-2.8-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\chardet-3.0.4-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\attrs-24.3.0-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\pyhamcrest-2.1.0-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\hyperlink-21.0.0-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\automat-24.8.1-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\incremental-24.7.2-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\constantly-23.10.4-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\zope.interface-7.2-py3.8-win-amd64.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\importlib_resources-6.4.5-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\importlib_metadata-8.5.0-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\typing_extensions-4.12.2-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\mako-1.3.8-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\tomli-2.2.1-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\zipp-3.21.0-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\pade\\core', 'C:\\Users\\mrsli\\AppData\\Local\\Programs\\Python\\Python38\\python38.zip', 'C:\\Users\\mrsli\\AppData\\Local\\Programs\\Python\\Python38\\DLLs', 'C:\\Users\\mrsli\\AppData\\Local\\Programs\\Python\\Python38\\lib', 'C:\\Users\\mrsli\\AppData\\Local\\Programs\\Python\\Python38', 'C:\\Users\\mrsli\\AppData\\Local\\Programs\\Python\\Python38\\lib\\site-packages']
my_path = sys.path
for i in my_list:
    if i not in my_path:
        sys.path.append(os.path.abspath(i))

from pade.misc.utility import start_loop
from pade.acl.aid import AID
import json
from classes.manager import Manager
from classes.details import Product
from classes.worker import Worker
from classes.parts import Part


if __name__ == '__main__':
    agents = list()
    #port = int(sys.argv[1])
    port = 2000
    with open('C:\\PythonProject2\\files\\server1.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open('C:\\PythonProject2\\files\\client.json', 'r', encoding='utf-8') as f:
        data2 = json.load(f)

    workers = data['worker']
    parts = data['part']
    details = data['detail']
    clients = sorted(data2, key=lambda x: x['deadline'])

    for i in range(len(workers)):
        workers[i]['wait_time'] = 0
        workers[i]['full_time'] = workers[i]['busy']
        workers[i]['inters'] = []

    part_list = []

    for num, i in enumerate(workers):
        name = f'worker{port}@localhost:{port}'
        agent = Worker(AID(name=name), i['name'], i['qualification'], i['busy'], i['machines'], i['probability'])
        part_list.append(name)
        agents.append(agent)
        workers[num]['num'] = port
        port += 1

    for num, i in enumerate(parts):
        agent = Part(AID(name=f'part{port}@localhost:{port}'), i['name'], i['time'], i['equipment'], workers)
        agents.append(agent)
        parts[num]['num'] = port
        port += 1

    for num, i in enumerate(details):
        agent = Product(AID(name=f'product{port}@localhost:{port}'), i['name'], i['time'], i['parts'], parts, workers)
        agents.append(agent)
        details[num]['num'] = port
        port += 1

    agent = Manager(AID(name=f'manager{port}@localhost:{port}'), workers, parts, details, clients)
    agents.append(agent)

    start_loop(agents)
