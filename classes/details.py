import sys
import os
import time

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


class Product(Agent):
    def __init__(self, aid, name=None, time=None, parts=None, full_part = None, workers = None):
        super(Product, self).__init__(aid=aid, debug=False)
        self.name = name
        self.time = time
        self.parts = parts
        self.full_parts = full_part
        self.workers = workers

        # для удобных расчетов с рабочими
        self.coef_dict = {'High': 1, 'Medium': 0.8, 'Low': 0.5}
        self.count = 0
        self.wait = 0.0



    def on_start(self):
        super(Product, self).on_start()
        display_message(self.aid.localname, f'Деталь {self.name} создан')


    def react(self, message):
        super(Product, self).react(message)

        # Продукт посылает сообщение всем своим частям
        # делает это после того, как менеджер нашел продукт
        if 'manager' in message.sender.name:
            msg_cont = message.content.split()
            if msg_cont[0] == self.name:
                display_message(self.aid.localname, f'Я именно тот продукт {msg_cont[0]} для {msg_cont[1]}')
                self.sending_to_parts(msg_cont[1])


        # CRINGE ALERT ALERT!!! Вычисляет score для всех рабочих ДЛЯ ПРОДУКТА
        if 'part' in message.sender.name and message.performative == 'inform-if':
            # деталь собрана, добавляем +1 в счетчик
            self.count += 1
            #сохрняем инфу о том, для какого клиента продукт + время конца сборки последней детали
            msg_cont = message.content.split()
            client_name = msg_cont[0]
            last_time = msg_cont[1]
            self.wait = max(self.wait, float(last_time))

            # если собраны все части продукта
            if self.count == len(self.parts):
                #self.wait = float(last_time)
                print(f'ЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯ {self.name} {client_name} {self.wait} ЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯ')


                for worker in self.workers:
                    worker['score'] = (self.time / self.coef_dict[worker['qualification']]) + (2.5 / 40 * worker['busy'])

                sorted_workers = sorted(self.workers, key=lambda x: x['score'], reverse=True)
                real_inter = ()
                print(self.name)
                print(sorted_workers, '\n')

                for z in range(len(sorted_workers)):

                    worker = sorted_workers[z]  # получаем рабочего из отсортированного списка
                    original_index = self.workers.index(worker)  # ищем индекс рабочего в оригинальном списке
                    print(worker)
                    found = False  # Флаг для отслеживания, найден ли подходящий интервал

                    # Если список пустой, или можем впихнуть задачу в начало
                    if ((not worker['inters']) or (worker['inters'] and worker['inters'][0][0] >= self.time)) and self.wait <= 0:
                        t_old = 0
                        t_new = self.time
                        worker['inters'] = [(t_old, t_new)] + worker['inters']

                        # т.к. пихаем в начало - то и интервал берем первый
                        real_inter = [(t_old, t_new)]

                        self.workers[original_index]['inters'] = worker['inters']  # обновляем оригинальный список
                        best = worker
                        print(0, best)
                        found = True  # Установим флаг в True

                    # иначе - смотрим, между какими интервалами задачу выполнить можно
                    else:
                        # если в начало нельзя - смотрим между интервалами, например - (3-4)
                        print(1)
                        for i in range(len(worker['inters']) - 1):
                            print(f"время между интервалами {worker['inters'][i + 1][0] - worker['inters'][i][1]} время сборки {self.time}")
                            if worker['inters'][i + 1][0] - worker['inters'][i][1] >= self.time and worker['inters'][i][1] > self.wait:
                                t_old = worker['inters'][i][1]
                                t_new = t_old + self.time

                                # тут вставляем в середину
                                real_inter = (t_old, t_new)

                                worker['inters'].insert(i + 1, (t_old, t_new))
                                self.workers[original_index]['inters'] = worker[
                                    'inters']  # обновляем оригинальный список
                                best = worker
                                print(1, best)
                                found = True  # Установим флаг в True
                                break
                        else:
                            print(2)
                            # full_busy - сколько часов работает рабочий в целом
                            # Если не нашли промежутков в интервалах, куда можно впихнуть работу - смотрим
                            # хватает ли у рабочего "рабочего времени", чтобы впихнуть работу в конец, например - (10-11)
                            if sum(b - a for a, b in worker['inters']) + self.time <= worker['busy']:
                                #t_old = worker['inters'][-1][1]

                                # жесткий костыль, вообще это должно быть в другом месте
                                if worker['inters']:
                                    t_old = max(self.wait, worker['inters'][-1][1])
                                else:
                                    t_old = self.wait

                                t_new = t_old + self.time
                                # тут вставляем в конец
                                real_inter = (t_old, t_new)

                                worker['inters'].append((t_old, t_new))
                                self.workers[original_index]['inters'] = worker[
                                    'inters']  # обновляем оригинальный список
                                best = worker
                                print(2, best)
                                found = True  # Установим флаг в True
                    if found:
                        break


                #best = max(self.workers, key=lambda x: x['score'])
                # ЭТО МЕНЯЕТСЯ ИМЕННО ДОСТУПНОЕ ВРЕМЯ РАБОТЫ (т.е. сколько всего рабочий еще может проработать)
                best['busy'] = round(best['busy'] - self.time, 1)

                name = best['name']
                score = round(best['score'], 6)
                full_time = best['full_time']
                wait_time = best['wait_time']

                print(f'{name} Начал собирать продукт {self.name} для клиента {client_name}. Счет {score}. Время {real_inter[0]}:{real_inter[1]}')
                self.send_to_manager_accepted(name, client_name, str(score), str(real_inter[0]), str(real_inter[1]), str(full_time), str(wait_time))
                self.count = 0
                self.wait = 0


    # Отправляет запрос всем агентам-частям, чтобы найти те, которое соответсвуют частям продукта
    def sending_to_parts(self, client):
        print(148 * "-")
        for product_part in self.parts:
            message = ACLMessage(ACLMessage.REQUEST)
            message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
            message.set_performative('query-if')
            message.set_sender(self.aid)
            message.receivers = []

            for i in self.full_parts:
                pd_res = 'part' + str(i['num'])
                message.add_receiver(AID(pd_res))

            pd_cont = product_part + ' ' + self.name + ' ' + client
            message.set_content(pd_cont)
            self.send(message)
            display_message(self.aid.localname,
                            f'Продукт {self.name} отправил сообщение {message.content} всем деталям')


    # CRINGE ALERT ALERT!!! Отправляет информацию в календарь (рабочий собрал продукт)
    def send_to_manager_accepted(self, worker_name, client_name, score, busy_old, busy_new, full_time, wait_time):
        message = ACLMessage(ACLMessage.INFORM)
        message.set_performative('inform-iff')
        message.set_sender(self.aid)
        message.add_receiver('manager')
        message.set_datetime_now()
        message.set_content(f'{worker_name} {self.name} {client_name} {score} {busy_old} {busy_new} {full_time} {wait_time}')
        self.send(message)
