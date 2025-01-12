import sys
import os

from itsdangerous import NoneAlgorithm

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


from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent
from pade.acl.aid import AID
from pade.acl.messages import ACLMessage
from pade.behaviours.protocols import FipaContractNetProtocol
import random



# Класс для инициатора запросов
class CompContNet1(FipaContractNetProtocol):
    '''CompContNet1

       Initial FIPA-ContractNet Behaviour that sends CFP messages
       to other feeder agents asking for restoration proposals.
       This behaviour also analyzes the proposals and selects the
       one it judges to be the best.'''

    def __init__(self, agent, message):
        super(CompContNet1, self).__init__(
            agent=agent, message=message, is_initiator=True)
        self.cfp = message

    def handle_all_proposes(self, proposes):
        """
        """

        super(CompContNet1, self).handle_all_proposes(proposes)

        best_proposer_worker = None
        other_proposers = list()
        max_score = 0.0

        display_message(self.agent.aid.name, 'Analyzing proposals...')
        display_message(self.agent.aid.name, f'Все агенты')

        new_prop = []
        proposes = list(set(proposes))
        propop = []
        for i in proposes:
            x = str(self.agent.aid.localname) + str(i.sender.localname)
            if x not in propop:
                new_prop.append(i)
                propop.append(x)

        proposes = new_prop
        for message in proposes:
            display_message(self.agent.aid.name, f'Все агенты {self.agent.aid.localname} {message.sender.localname}')

        # Выбираем рабочего, которого хотим выбрать
        for message in proposes:
            content = message.content
            worker_score = float(content)
            display_message(self.agent.aid.name,
                            'Предложено рабочим: {pot}'.format(pot=worker_score))
            if worker_score > max_score:
                if best_proposer_worker is not None:
                    other_proposers.append(best_proposer_worker)

                max_score = worker_score
                best_proposer_worker = message.sender
            else:
                other_proposers.append(message.sender)

        display_message(self.agent.aid.name,
                        'Лучший счет: {pot}'.format(
                            pot=max_score))

        print(other_proposers)
        print(best_proposer_worker)

        # Отправляем отказ на изменения остальным рабочим
        if other_proposers:
            answer = ACLMessage(ACLMessage.REJECT_PROPOSAL)
            answer.set_protocol(ACLMessage.FIPA_CONTRACT_NET_PROTOCOL)
            answer.set_content(str(self.agent.time))
            for agent in other_proposers:
                answer.add_receiver(agent)
            self.agent.send(answer)



        if best_proposer_worker is not None:
            display_message(self.agent.aid.name,
                            f'Принимает {best_proposer_worker.localname}')
            answer = ACLMessage(ACLMessage.ACCEPT_PROPOSAL)
            answer.set_protocol(ACLMessage.FIPA_CONTRACT_NET_PROTOCOL)
            answer.set_content(self.agent.name + ' ' + str(self.agent.time))
            answer.add_receiver(best_proposer_worker)
            self.agent.send(answer)


    def handle_inform(self, message):
        """
        """
        super(CompContNet1, self).handle_inform(message)

        #display_message(self.agent.aid.name, 'ЧАСТЬ ВРОДЕ КАК ОБРАБОТАНА!')



# Класс для подписчиков
class CompContNet2(FipaContractNetProtocol):
    '''CompContNet2

       FIPA-ContractNet Participant Behaviour that runs when an agent
       receives a CFP message. A proposal is sent and if it is selected,
       the restrictions are analized to enable the restoration.'''

    def __init__(self, agent):
        super(CompContNet2, self).__init__(agent=agent,
                                           message=None,
                                           is_initiator=False)

    def handle_cfp(self, message):
        """
        """
        #self.agent.call_later(1.0, self._handle_cfp, message)
        self._handle_cfp(message)

    def _handle_cfp(self, message):
        """
        """
        super(CompContNet2, self).handle_cfp(message)
        self.message = message

        msg_cont = message.content.split()
        part_name = msg_cont[0]
        part_time = float(msg_cont[1])
        prod_name = msg_cont[2]
        client_name = msg_cont[3]
        part_equipt = msg_cont[4].split(',')


        answer = self.message.create_reply()
        answer.set_performative(ACLMessage.PROPOSE)

        flag = 0
        for i in part_equipt:
            if i in self.agent.machines:
                flag = 1

        if flag == 0:
            return_num = 0
        else:
            if random.random() < self.agent.probability:
                return_num = 0
            else:
                return_num = (part_time/self.agent.coefficient) + (2.5 / 40 * self.agent.busy)


        answer.set_content(str(return_num))
        self.agent.send(answer)

    def handle_reject_propose(self, message):
        """
        """
        super(CompContNet2, self).handle_reject_propose(message)

        #display_message(self.agent.aid.name,'РАБОЧИЙ НЕ МЕНЯЕТ ВРЕМЯ!!!')

    def handle_accept_propose(self, message):
        """
        """
        super(CompContNet2, self).handle_accept_propose(message)

        display_message(self.agent.aid.name,'ЛУЧШИЙ НАЙДЕН!!!')
        self.agent.send_to_calendar(message.content[1], message.content[1], 'client')
