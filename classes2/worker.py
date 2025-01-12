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
import random

class Worker(Agent):
    def __init__(self, aid, name=None, qualification=None, busy=None, machines = None, probability = None):
        super(Worker, self).__init__(aid=aid, debug=False)


        self.name = name
        self.qualification = qualification
        self.busy = busy
        self.machines = machines
        self.probability = probability


        self.coefficient = None




    def on_start(self):
        super(Worker, self).on_start()
        display_message(self.aid.localname, f'Рабочий {self.name} создан')

        # Задаем коэфф. Эффективности сотрудника
        coef_dict = {'High': 1, 'Medium': 0.8, 'Low': 0.5}
        self.coefficient = coef_dict[self.qualification]


    def react(self, message):
        super(Worker, self).react(message)

        # может ли рабочий выполнить задачу + score ИЗ ЧАСТИ
        if 'part' in message.sender.name and message.performative == 'query-if':
            msg_cont = message.content.split()
            part_name = msg_cont[0]
            part_time = float(msg_cont[1])
            prod_name = msg_cont[2]
            client_name = msg_cont[3]
            part_equipt = msg_cont[4].split(',')

            return_num = 0
            flag = 0
            for ii in part_equipt:
                if ii in self.machines:
                    flag = 1

            if flag == 0:
                return_num = -2
            else:
                if random.random() < self.probability:
                    print(f'СЛУЧАЙНОСТЬ!!! РАБОЧИЙ ВЫКИНУТ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                    return_num = 0
                else:
                    return_num += (part_time / self.coefficient) + (2.5 / 40 * self.busy)

                print(f'Рабочий {self.name} начал собирать деталь {part_name} для продукта {prod_name} для клиента {client_name}. Его счет {return_num}')
            self.send_answer_to_part(message, str(return_num), part_name, prod_name, client_name)


        # может ли рабочий выполнить задачу + score ИЗ ПРОДУКТА
        if 'product' in message.sender.name and message.performative == 'query-if':
            print('начал проверять')
            msg_cont = message.content.split()
            part_name = msg_cont[0]
            part_time = float(msg_cont[1])
            client_name = msg_cont[2]

            return_num2 = (part_time / self.coefficient) + (2.5 / 40 * self.busy)
            self.send_answer_to_product(message, str(return_num2))


        # обновляет время рабочего ИЗ ПРОДУКТА
        if 'product' in message.sender.name and message.performative == 'accept-proposal':
            msg_cont = message.content.split()
            prod_name = msg_cont[0]
            part_time = float(msg_cont[1])
            client_name = msg_cont[2]

            return_num2 = (part_time / self.coefficient) + (2.5 / 40 * self.busy)
            self.send_to_calendar_2(prod_name, client_name, str(return_num2))



        # обновляет время рабочего ИЗ ЧАСТИ
        if 'part' in message.sender.name and message.performative == 'accept-proposal':
            msg_cont = message.content.split()
            part_name = msg_cont[0]
            part_time = float(msg_cont[1])
            prod_name = msg_cont[2]
            client_name = msg_cont[3]
            score = float(msg_cont[4])
            score_2 = float(msg_cont[5])

            self.busy = self.busy - part_time




            self.send_to_calendar(part_name, prod_name, client_name, str(score_2), str(self.busy))
            print(f'Рабочий {self.name} начал собирать деталь {part_name} для продукта {prod_name} для клиента {client_name}. Его счет {str(score_2)}. Время {self.busy}' )



    # Отправляет сообщение со своим score + часть + продукт + клиент ДЛЯ ЧАСТИ
    def send_answer_to_part(self, message_old, score, part_name, prod_name, client_name):
        message = ACLMessage(ACLMessage.REQUEST)
        message.set_sender(self.aid)
        message.set_performative('proxy')
        message.add_receiver(AID(message_old.sender.localname))
        message.set_content(f'{score} {part_name} {prod_name} {client_name}')

        self.send(message)


    def send_answer_to_product(self, message_old, score):
        message = ACLMessage(ACLMessage.REQUEST)
        message.set_sender(self.aid)
        message.set_performative('proxy')
        message.add_receiver(AID(message_old.sender.localname))
        message.set_content(score)
        self.send(message)


    # Типа как должно обновляться время
    def update_time(self, new_time):
        self.busy = new_time


    # Отправляет информацию менеджеру для внесения в календарь
    def send_to_calendar(self, part, prod, client, score, busy):
        message = ACLMessage(ACLMessage.INFORM)
        message.set_performative('inform-if')
        message.set_sender(self.aid)
        message.add_receiver('manager')
        message.set_datetime_now()
        message.set_content(f'{self.name} Начал собирать деталь {part} для продукта {prod} для клиента {client}. Счет {score}. Время {busy}')
        self.send(message)


    def send_to_calendar_2(self, prod, client, score):
        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        message = ACLMessage(ACLMessage.INFORM)
        message.set_performative('inform-iff')
        message.set_sender(self.aid)
        message.add_receiver('manager')
        message.set_datetime_now()
        message.set_content(
            f'{self.name} Начал собирать продукт {prod} для клиента {client}. Счет {score}')
        self.send(message)
