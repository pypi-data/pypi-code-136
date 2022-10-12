import select
import socket
import requests
import json


class RfidReaderServ:

    def __init__(self, callback_func, rfid_addr='172.16.6.194',
                 rfid_port=18800, listener_addr='10.100.10.254',
                 listener_port=8686):
        # Говорит о том, сколько дескрипторов единовременно могут быть открыты
        self.MAX_CONNECTIONS = 2

        # Откуда и куда записывать информацию
        self.INPUTS = list()
        self.OUTPUTS = list()

        #Параметры РФИД и Считывания
        # rfid_addr = '192.168.100.71'
        self.rfid_addr = rfid_addr
        self.rfid_api_port = rfid_port
        #listener_addr = '10.100.10.254'
        #listener_addr = '172.16.6.200'
        self.listener_addr = listener_addr
        self.listener_port = listener_port
        self.callback_func = callback_func
        self.SERVER_ADDRESS = (self.listener_addr, self.listener_port)
        self.startListGet = f'http://{self.rfid_addr}:{self.rfid_api_port}/setNotification?url=tcp://{self.listener_addr}&port={self.listener_port}'
        self.addGet = 'http://{}:{}/addNewReader?vendor=ER8210&connectionType=TCP&host=127.0.0.1&port=30001'.format(
            self.rfid_addr, self.rfid_api_port)
        self.configureGet = 'http://{}:{}/currentReader?readerID={}'.format(
            self.rfid_addr, self.rfid_api_port, self.get_rfid_id())
        self.startReadGet = 'http://{}:{}/startRead'.format(self.rfid_addr,
                                                            self.rfid_api_port)

    def get_rfid_id(self):
        getIdRow = 'http://{}:{}/getReaders'.format(self.rfid_addr, self.rfid_api_port)
        reqReturn = requests.get(getIdRow)
        readerList = reqReturn.json()
        for read in readerList["readers"]:
            rfid_id = str(read['readerID'])
            return rfid_id

    def RfidParser(self, data):
        """
        Функция обработки данных с RFID
        :param data: данные полученные от RDID
        :return: Возвлащает лист меток по антеннам
        """
        rfid_list = {1: {'EPC': None, 'time': None},
                     2: {'EPC': None, 'time': None},
                     3: {'EPC': None, 'time': None},
                     4: {'EPC': None, 'time': None}}
        try:
            json_list = json.loads(data)
            for mark in json_list["tags"]:
                mark_ant = mark['ant']
                if rfid_list[mark_ant]['EPC'] is None:
                    rf_id = mark['EPC']
                    rf_time = mark['time']
                    rfid_list[mark_ant]['EPC'] = rf_id
                    rfid_list[mark_ant]['time'] = rf_time
        except json.decoder.JSONDecodeError:
            pass
        return rfid_list


    def start_reading(self):
        """
        Запрос начала пересылки событий считывания
        """
        x = requests.get(self.startListGet)
        print(x.status_code)


    def re_add_reader(self):
        """
        Добавление и конфигурирование RFID считывателя повторно
        """
        # Добавление RFID считывателя повторно
        x = requests.get(self.addGet)
        print(x.status_code)
        # Конфигруирование RFID
        x = requests.get(self.configureGet)
        print(x.status_code)
        # Начало считывания меток
        x = requests.get(self.startReadGet)
        print(x.status_code)


    def get_non_blocking_server_socket(self):

        # Создаем сокет, который работает без блокирования основного потока
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setblocking(0)
        # Биндим сервер на нужный адрес и порт
        server.bind(self.SERVER_ADDRESS)
        # Установка максимального количество подключений
        server.listen(self.MAX_CONNECTIONS)
        return server


    def handle_readables(self, readables, server):
        """
        Обработка появления событий на входах
        """
        for resource in readables:
            # Если событие исходит от серверного сокета, то мы получаем новое подключение
            if resource is server:
                connection, client_address = resource.accept()
                connection.setblocking(0)
                self.INPUTS.append(connection)
                print("new connection from RFID {address}".format(address=client_address))
            # Если событие исходит не от серверного сокета, но сработало прерывание на наполнение входного буффера
            else:
                data = ""
                try:
                    data = resource.recv(1024)
                # Если сокет был закрыт на другой стороне
                except ConnectionResetError:
                    pass
                if data:
                    # Обработка даных с RFID
                    rfid_list = self.RfidParser(data)
                    # print(rfid_list)
                    self.callback_func(rfid_list)
                    # Говорим о том, что мы будем еще и писать в данный сокет
                    if resource not in self.OUTPUTS:
                        self.OUTPUTS.append(resource)
                # Если данных нет, но событие сработало, то ОС нам отправляет флаг о полном прочтении ресурса и его закрытии
                else:
                    print("No DATA")
                    # Очищаем данные о ресурсе и закрываем дескриптор
                    self.clear_resource(resource)
                    self.re_add_reader()
                    self.start_reading()


    def clear_resource(self, resource):
        """
        Метод очистки ресурсов использования сокета
        """
        if resource in self.OUTPUTS:
            self.OUTPUTS.remove(resource)
        if resource in self.INPUTS:
            self.INPUTS.remove(resource)
        resource.close()
        print('closing connection Rfid listener ' + str(resource))

    def mainloop(self):
        # Создаем серверный сокет без блокирования основного потока в ожидании подключения
        server_socket = self.get_non_blocking_server_socket()
        self.INPUTS.append(server_socket)
        # Запускаем рассылку сообщений на адресс сервера
        self.start_reading()
        print("Rfid listener server is running, please, press ctrl+c to stop")
        try:
            while self.INPUTS:
                readables, writables, exceptional = select.select(self.INPUTS, self.OUTPUTS, self.INPUTS)
                self.handle_readables(readables, server_socket)
        except KeyboardInterrupt:
            self.clear_resource(server_socket)
            print("Rfid listener  Server stopped! Thank you for using!")


# Test launc Func
# def foo(data):
#     print(data)
#
#
# lint = RfidReaderServ(callback_func=foo)
# lint.mainloop()
