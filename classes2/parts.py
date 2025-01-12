import sys
import os

my_list = ['C:\\PythonProject2\\.venv\\Scripts\\pade.exe',
           'C:\\Users\\mrsli\\AppData\\Local\\Programs\\Python\\Python38\\python38.zip',
           'C:\\Users\\mrsli\\AppData\\Local\\Programs\\Python\\Python38\\DLLs',
           'C:\\Users\\mrsli\\AppData\\Local\\Programs\\Python\\Python38\\lib',
           'C:\\Users\\mrsli\\AppData\\Local\\Programs\\Python\\Python38', 'C:\\PythonProject2\\.venv',
           'C:\\PythonProject2\\.venv\\lib\\site-packages',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\terminaltables-3.1.0-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\flask-1.1.1-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\flask_migrate-2.5.2-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\flask_sqlalchemy-2.4.1-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\flask_wtf-0.14.2-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\flask_login-0.4.1-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\flask_bootstrap-3.3.7.1-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\flask_script-2.0.6-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\click-7.0-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\itsdangerous-1.1.0-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\jinja2-2.10.3-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\markupsafe-1.1.1-py3.8-win-amd64.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\werkzeug-0.16.0-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\alchimia-0.8.1-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\sqlalchemy-1.3.10-py3.8-win-amd64.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\requests-2.22.0-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\twisted-19.7.0-py3.8-win-amd64.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\alembic-1.14.0-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\wtforms-3.2.1-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\visitor-0.1.3-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\dominate-2.9.1-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\certifi-2024.12.14-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\urllib3-1.25.11-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\idna-2.8-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\chardet-3.0.4-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\attrs-24.3.0-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\pyhamcrest-2.1.0-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\hyperlink-21.0.0-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\automat-24.8.1-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\incremental-24.7.2-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\constantly-23.10.4-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\zope.interface-7.2-py3.8-win-amd64.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\importlib_resources-6.4.5-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\importlib_metadata-8.5.0-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\typing_extensions-4.12.2-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\mako-1.3.8-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\tomli-2.2.1-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\zipp-3.21.0-py3.8.egg',
           'C:\\PythonProject2\\.venv\\lib\\site-packages\\pade\\core',
           'C:\\Users\\mrsli\\AppData\\Local\\Programs\\Python\\Python38\\python38.zip',
           'C:\\Users\\mrsli\\AppData\\Local\\Programs\\Python\\Python38\\DLLs',
           'C:\\Users\\mrsli\\AppData\\Local\\Programs\\Python\\Python38\\lib',
           'C:\\Users\\mrsli\\AppData\\Local\\Programs\\Python\\Python38',
           'C:\\Users\\mrsli\\AppData\\Local\\Programs\\Python\\Python38\\lib\\site-packages',
           'C:\\PythonProject2\\classes', 'C:\\PythonProject2\\files']
my_path = sys.path
for i in my_list:
    if i not in my_path:
        sys.path.append(os.path.abspath(i))

from pade.misc.utility import display_message, start_loop, call_later, defer_to_thread, call_in_thread, call_from_thread
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from twisted.internet import protocol, reactor
import random


class Part(Agent):
    def __init__(self, aid, name=None, time=None, equipment=None, workerrr=None):
        super(Part, self).__init__(aid=aid, debug=False)
        self.name = name
        self.time = time
        self.equipment = equipment
        self.workers = workerrr

        # Чтобы отловить баг, если сообщение от рабочего не обработалось вовремя
        for ii in range(len(self.workers)):
            self.workers[ii]['score'] = -99999999

        self.count = 0

        self.coef_dict = {'High': 1, 'Medium': 0.8, 'Low': 0.5}


    def on_start(self):
        super(Part, self).on_start()
        display_message(self.aid.localname, f'Изделие {self.name} создан')


    def react(self, message):
        super(Part, self).react(message)
        if 'product' in message.sender.name:
            msg_cont = message.content.split()
            if msg_cont[0] == self.name:
                display_message(self.aid.localname, f'Я именно та деталь {msg_cont[0]} для {msg_cont[1]}')

                # отправляем сообщение календарю (список частей)
                self.send_to_calendar(msg_cont[1])

                # Ищем рабочего, который может выполнить работу (получаем список score)
                #self.call_later(8.0, self.find_worker, msg_cont[1], msg_cont[2])
                #self.find_worker(msg_cont[1], msg_cont[2])

                self.cringe(msg_cont[1], msg_cont[2], message.sender.name)

        # Получаем score от рабочих
        if 'worker' in message.sender.localname and message.performative == 'proxy':
            self.count += 1
            msg_cont = message.content.split()
            score = float(msg_cont[0])
            part_name = msg_cont[1]
            prod_name = msg_cont[2]
            client_name = msg_cont[3]
            for ii in range(len(self.workers)):
                if str(self.workers[ii]['num']) == message.sender.localname[6:]:
                    self.workers[ii]['score'] = score
                    #print(self.workers[i], self.name)

            # Если все рабочие прислали свои ответы - выбираем лучшего
            if self.count == len(self.workers):

                #отлавливаем баг со временем рабочих
                #for i in range(len(self.workers)):
                #    print(self.workers[i])

                best = max(self.workers, key=lambda x: x['score'])
                print(f'Лучший рабочий для {self.name} {best}')

                # Отправляем сообщение рабочему, чтобы тот изменил свое время
                #self.send_to_worker(prod_name, client_name, best)
                call_in_thread(self.send_to_worker, prod_name, client_name, best, best['score'])

                # Обновляем score рабочих и число присланных ответов
                for ii in range(len(self.workers)):
                    self.workers[ii]['score'] = -22222
                self.count = 0


    # CRINGE ALERT ALERT!!! Вычисляет score для всех рабочих ДЛЯ ЧАСТИ
    def cringe(self, product, client, product_aid):
        for worker in self.workers:
            return_num = 0
            flag = 0
            for ii in self.equipment:
                if ii in worker['machines']:
                    flag = 1

            if flag == 0:
                return_num = -2
            else:
                if random.random() < worker['probability']:
                    print(f'СЛУЧАЙНОСТЬ!!! РАБОЧИЙ ВЫКИНУТ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                    return_num = 0
                else:
                    return_num += (self.time / self.coef_dict[worker['qualification']]) + (2.5 / 40 * worker['busy'])
            worker['score'] = return_num

        best = max(self.workers, key=lambda x: x['score'])
        busy_old = best['busy']
        best['busy'] = round(best['busy'] - self.time, 1)

        name = best['name']
        score = best['score']
        busy_new = best['busy']
        full_time = best['full_time']
        wait_time = best['wait_time']

        print(
            f'{name} Начал собирать деталь {self.name} для продукта {product} для клиента {client}. Счет {score}. Время {busy_old}:{busy_new}')
        self.send_to_calendar2(name, self.name, product, client, str(score), str(busy_old), str(busy_new), str(full_time), str(wait_time))
        self.send_to_product(product_aid, client)


    # CRINGE ALERT ALERT!!! Отправляет сообщение в календарь о том, что рабочий начал изготавливать деталь
    def send_to_calendar2(self, name, part, prod, client, score, busy_old, busy_new, full_time, wait_time):
        message = ACLMessage(ACLMessage.INFORM)
        message.set_performative('inform-iff')
        message.set_sender(self.aid)
        message.add_receiver('manager')
        message.set_datetime_now()
        message.set_content(f'{name} {part} {prod} {client} {score} {busy_old} {busy_new} {full_time} {wait_time}')
        self.send(message)


    # CRINGE ALERT ALERT!!! Отправляет сообщение продукту о том, что часть собрана
    def send_to_product(self, product, client_name):
        message = ACLMessage(ACLMessage.INFORM)
        message.set_performative('inform-if')
        message.set_sender(self.aid)
        message.add_receiver(product)
        message.set_datetime_now()
        message.set_content(f'{client_name}')
        self.send(message)


    # Отправляет запросы всем рабочим, чтобы те прислали свой score
    def find_worker(self, product, client):

        message = ACLMessage(ACLMessage.REQUEST)
        message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
        message.set_performative('query-if')
        message.set_sender(self.aid)

        for ii in self.workers:
            pt_res = 'worker' + str(ii['num'])
            message.add_receiver(AID(pt_res))

        # Чтобы собрать все машины в одну строку
        all_equip = ''
        for ii in self.equipment:
            all_equip += ii + ','
        all_equip = all_equip[:-1]

        pt_cont = str(self.name) + ' ' + str(self.time) + ' ' + product + ' ' + client + ' ' + all_equip
        message.set_content(pt_cont)
        display_message(self.aid.localname, f'Часть {self.name} запросила время всех рабочих для {product}')
        self.send(message)


    # Отправляет определенному рабочему сообщение-запрос, чтобы тот изменил свое доступное время
    def send_to_worker(self, product, client, best, score):
        #best = max(self.workers, key=lambda worker: worker['score'])
        message = ACLMessage(ACLMessage.REQUEST)
        message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
        message.set_performative('accept-proposal')
        message.set_sender(self.aid)
        message.add_receiver(AID('worker' + str(best['num'])))

        pt_cont = str(self.name) + ' ' + str(self.time) + ' ' + product + ' ' + client + ' ' + str(
            best['score']) + ' ' + str(score)
        display_message(self.aid.localname, f'{self.name} {score} ВЫДАЛ ЗАДАНИЕ РАБОЧЕМУ!')
        message.set_content(pt_cont)

        self.send(message)


    # Отправляет информацию менеджеру для внесения в календарь, что рабочий начал изготавливать деталь
    def send_to_calendar(self, product):
        message = ACLMessage(ACLMessage.INFORM)
        message.set_performative('inform-if')
        message.set_sender(self.aid)
        message.add_receiver('manager')
        message.set_datetime_now()
        message.set_content(self.name + ' для ' + product)
        self.send(message)
