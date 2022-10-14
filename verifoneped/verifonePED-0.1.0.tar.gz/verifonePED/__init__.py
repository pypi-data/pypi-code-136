import socket
import time


class verifone_device:


    def __init__(self, username, password, ip_address, port=25000):
        self.endpoint = ip_address, port
        self.username = username
        self.password = password
        self.logged_in = False
        

    def login(self):
        l_data = ['L2', self.username, self.password, '4'] # *=all-menu, 4=logout-only empty=no-menu
        l_record = ','.join(l_data)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(self.endpoint)

        try:
            s.sendall(l_record.encode())
            while True:
                data = s.recv(1024).decode()
                response = data.split(',')
                if response[0] in ['0', '-84']:
                    self.logged_in = True
                    return True
                elif not data:
                    break
            self.logged_in = False
            return False

        except Exception as e:
            self.logged_in = False
            return False


    def logout(self):
        o_data = ['O', '0']
        o_record = ','.join(o_data)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(self.endpoint)

        try:
            s.sendall(o_record.encode())
            while True:
                data = s.recv(1024).decode()
                response = data.split(',')
                if response[0] == '0':
                    self.logged_in = False
                    return True
                elif not data:
                    break
            return False

        except Exception as e:
            return False



    def transaction(self, amount):
        if self.logged_in:

            # Build transaction data
            t_data = [''] * 29
            t_data[1] = 'T'             # Message type. T = Transaction
            t_data[3] = '01'            # Transaction type, 01 = Purchase
            t_data[4] = '0000'          # Modifier, 0000 = Cardholder Present
            t_data[11] = str(amount)    # Transaction value, decimal
            t_data[12] = ''             # Cashback value, decimal
            t_data[27] = '0'            # Register for account on file, 2=register

            # Remove element 0 (Documentation starts from 1. Keeps above more logical)
            t_data.pop(0)

            # Build CSV
            t_record = ','.join(t_data)
            time.sleep(2)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(self.endpoint)

            try:
                s.send(t_record.encode())
                while True:
                    data = s.recv(1024).decode()
                    response = data.split(',')
                    print(response)
                    if response[0] in ['0', '7']:
                        print(response[5])
                        print(response[12])
                        print(response[17])
                        print(response[18])
                        return True
                    elif not data:
                        break

            except:
                self.logged_in = False
                return False

        else:
            return False
        