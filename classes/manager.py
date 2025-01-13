import sys
import os

my_list = ['C:\\PythonProject2\\.venv\\Scripts\\pade.exe', 'C:\\Users\\mrsli\\AppData\\Local\\Programs\\Python\\Python38\\python38.zip', 'C:\\Users\\mrsli\\AppData\\Local\\Programs\\Python\\Python38\\DLLs', 'C:\\Users\\mrsli\\AppData\\Local\\Programs\\Python\\Python38\\lib', 'C:\\Users\\mrsli\\AppData\\Local\\Programs\\Python\\Python38', 'C:\\PythonProject2\\.venv', 'C:\\PythonProject2\\.venv\\lib\\site-packages',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\terminaltables-3.1.0-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\flask-1.1.1-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\flask_migrate-2.5.2-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\flask_sqlalchemy-2.4.1-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\flask_wtf-0.14.2-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\flask_login-0.4.1-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\flask_bootstrap-3.3.7.1-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\flask_script-2.0.6-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\click-7.0-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\itsdangerous-1.1.0-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\jinja2-2.10.3-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\markupsafe-1.1.1-py3.8-win-amd64.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\werkzeug-0.16.0-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\alchimia-0.8.1-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\sqlalchemy-1.3.10-py3.8-win-amd64.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\requests-2.22.0-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\twisted-19.7.0-py3.8-win-amd64.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\alembic-1.14.0-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\wtforms-3.2.1-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\visitor-0.1.3-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\dominate-2.9.1-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\certifi-2024.12.14-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\urllib3-1.25.11-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\idna-2.8-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\chardet-3.0.4-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\attrs-24.3.0-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\pyhamcrest-2.1.0-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\hyperlink-21.0.0-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\automat-24.8.1-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\incremental-24.7.2-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\constantly-23.10.4-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\zope.interface-7.2-py3.8-win-amd64.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\importlib_resources-6.4.5-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\importlib_metadata-8.5.0-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\typing_extensions-4.12.2-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\mako-1.3.8-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\tomli-2.2.1-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\zipp-3.21.0-py3.8.egg', 'C:\\PythonProject2\\.venv\\lib\\site-packages\\pade\\core', 'C:\\Users\\mrsli\\AppData\\Local\\Programs\\Python\\Python38\\python38.zip', 'C:\\Users\\mrsli\\AppData\\Local\\Programs\\Python\\Python38\\DLLs', 'C:\\Users\\mrsli\\AppData\\Local\\Programs\\Python\\Python38\\lib', 'C:\\Users\\mrsli\\AppData\\Local\\Programs\\Python\\Python38',
           'C:\\Users\\mrsli\\AppData\\Local\\Programs\\Python\\Python38\\lib\\site-packages', 'C:\\PythonProject2\\classes', 'C:\\PythonProject2\\files']
my_path = sys.path
for i in my_list:
    if i not in my_path:
        sys.path.append(os.path.abspath(i))

from pade.misc.utility import display_message, start_loop, call_later
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID


class Manager(Agent):
    def __init__(self, aid, workers, parts, products, clients):
        super(Manager, self).__init__(aid=aid, debug=False)

        self.workers = workers
        self.parts = parts
        self.products = products
        self.clients = clients

        # Список для хранения порядка обрабатываемой информации
        self.time_data = []
        self.all_num = 0


    def on_start(self):
        super(Manager, self).on_start()
        display_message(self.aid.localname, 'Менеджер проснулся...')

        self.clear_output()

        call_later(10.0, self.sending_message)


    def sending_message(self):
        for client in self.clients:
            message = ACLMessage(ACLMessage.REQUEST)
            message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
            message.set_performative('accept-proposal')
            message.set_sender(self.aid)
            message.receivers = []
            for ii in self.products:
                dt_res= 'product' + str(ii['num'])
                message.add_receiver(AID(dt_res))
            print(client['name'], client['order'])
            dt_cont = client['order'] + ' ' + client['name']
            message.set_content(dt_cont)
            display_message(self.aid.localname, f'Менеджер отправил сообщение {message.content} всем продуктам')
            self.send(message)


    def react(self, message):
        super(Manager, self).react(message)
        # CRINGE ALERT ALERT!!! получает информацию от продукта
        if 'product' in message.sender.name and message.performative == 'inform-iff':
            msg_cont = message.content.split()
            worker_name = msg_cont[0] + ' ' + msg_cont[1]
            product_name = msg_cont[2]
            client_name = msg_cont[3]
            score = msg_cont[4]
            busy_old = float(msg_cont[5])
            busy_new = float(msg_cont[6])
            full_time = float(msg_cont[7])
            wait_time = float(msg_cont[8])

            # сохраняем инфу о рабочем ОТ ПРОДУКТА
            time = int(str(message.datetime.second) + str(message.datetime.microsecond).zfill(6))
            self.time_data.append({'time': time,
                                   'worker': worker_name,
                                   'part': None,
                                   'product': product_name,
                                   'client': client_name,
                                   'busy_old': busy_old,
                                   'busy_new':busy_new,
                                  'full_time': full_time,
                                   'wait_time': wait_time})

            self.all_num += 1

            # Проверка - если собрал 12 продуктов (т.е. все) - то начинает запись в файл (всю инфу мы уже собрали)
            if self.all_num == len(self.clients):
                new_time = sorted(self.time_data, key=lambda x: x['time'])

                # КРАСИВАЯ (ТАБЛИЧНАЯ ЗАПИСЬ В ФАЙЛ)
                # Группируем данные по клиентам
                client_data = {}
                for entry in new_time:
                    client_name = entry["client"]
                    if client_name not in client_data:
                        client_data[client_name] = []
                    client_data[client_name].append(entry)

                with open('worker2.txt', 'w', encoding='utf-8') as f:
                    for client in client_data:
                        f.write(f"\nДанные для {client}:\n")
                        f.write(
                            f"{'Работник':<20} {'Действие':<30} {'Деталь':<15} {'Продукт':<15} {'Время':<19} {'Занятость':<10}\n")

                        for entry in client_data[client]:
                            time = entry["time"]
                            worker_name = entry["worker"]
                            action = 'Собрал деталь' if entry['part'] else 'Собрал продукт'
                            part = entry["part"] if entry["part"] else ""
                            product_name = entry["product"]

                            # Нужно, чтобы вывести время рабочего в красивом формате
                            h_old = int(entry['busy_old'] )
                            h_new = int(entry['busy_new'])
                            m_old = str(int((entry['busy_old'] - h_old) * 60)).zfill(2)
                            m_new = str(int((entry['busy_new'] - h_new) * 60)).zfill(2)

                            busy_new = entry["busy_new"]

                            f.write(
                                f"{worker_name:<20} {action:<30} {part:<15} {product_name:<15} {str(h_old).zfill(2)}:{m_old}-{str(h_new).zfill(2)}:{m_new:<10} {busy_new:<10}\n")


                with open('new_workers.txt', 'a') as f:
                    for w in new_time:
                        full_time = w['full_time']  # сколько может работать рабочий ВСЕГО
                        wait_time = w['wait_time']  # сколько "прождал" рабочий, пока не соберутся все детали (пока не использовал)
                        time = w['time']            # системное время
                        worker_name = w['worker']   # имя рабочего
                        part = w['part']            # имя части
                        product_name = w['product'] # имя продукта
                        client_name = w['client']   # имя клиента
                        busy_old = w['busy_old']    # старое время рабочего (до начала обработки детали/продукта)
                        busy_new = w['busy_new']    # новое время рабочего (до начала обработки детали/продукта)

                        # Нужно, чтобы вывести время рабочего в красивом формате
                        h_old = int(busy_old)
                        h_new = int(busy_new)
                        m_old = str(int((busy_old - h_old)*60)).zfill(2)
                        m_new = str(int((busy_new - h_new) * 60)).zfill(2)

                        # если собирал часть - пишем ее, если не собирал - не пишем ее
                        if part is None:
                            f.write(
                                f'{worker_name} Начал собирать продукт {product_name} ДЛЯ клиента {client_name}. {str(h_old).zfill(2)}:{m_old}-{str(h_new).zfill(2)}:{m_new}. {busy_new}\n')
                        else:
                            f.write(f'{worker_name} Начал собирать деталь {part} ДЛЯ продукта {product_name} для клиента {client_name}. {str(h_old).zfill(2)}:{m_old}-{str(h_new).zfill(2)}:{m_new}. {busy_new}\n')

        # CRINGE ALERT ALERT!!!
        if 'part' in message.sender.name and message.performative == 'inform-iff':
            msg_cont = message.content.split()
            worker_name = msg_cont[0] + ' ' + msg_cont[1]
            part_name = msg_cont[2]
            product_name = msg_cont[3]
            client_name = msg_cont[4]
            score = msg_cont[5]
            busy_old = float(msg_cont[6])
            busy_new = float(msg_cont[7])
            full_time = float(msg_cont[8])
            wait_time = float(msg_cont[9])

            # сохраняем инфу о рабочем ОТ ЧАСТИ
            time = int(str(message.datetime.second) + str(message.datetime.microsecond).zfill(6))
            self.time_data.append({'time': time,
                                   'worker': worker_name,
                                   'part': part_name,
                                   'product': product_name,
                                   'client': client_name,
                                   'busy_old': busy_old,
                                   'busy_new':busy_new,
                                   'full_time': full_time,
                                   'wait_time': wait_time})


    def clear_output(self):
        # Отчищаем содержимое файла перед запуском всех приколов
        with open('new_workers.txt', 'w'):
            pass

