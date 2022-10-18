# Ref : 
#   https://www.geeksforgeeks.org/fernet-symmetric-encryption-using-cryptography-module-in-python/
#   https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5

import binascii
import os
from io import StringIO
from pathlib import Path

from cryptography.fernet import Fernet  # pip install cryptography
from decouple import Config, Csv, RepositoryEnv  # pip install python-decouple


class OutboxEncryption:
    keyword_local = ''              # keyword must be only exist in local, if not assumtion script run in server
    env_list = 'PS1'                # os.environ.get("PS1") --> list of environment
    env_local = '.env.local'        # environment name local
    env_server = '.env.server'      # environment name server
    BASE_DIR = ''

    # constructor
    def __init__(self, base_dir=None):
        self.keyword_local = 'env_opd'
        if not base_dir:
            self.BASE_DIR = Path(__file__).resolve().parent.parent
        else:
            self.BASE_DIR = base_dir
        # pass        
    
    def bytes2hex(self, bytes_text):
        res_hex = binascii.hexlify(bytes_text)
        return res_hex.decode()

    def hex2bytes(self, hex_text):
        res_bytes = binascii.unhexlify(hex_text)
        return res_bytes    # return in bytes format

    def generate_key(self):
        # save key to file
        return Fernet.generate_key()
    
    def encrypt(self, plain_text, key):
        # key created using generate_key()
        f = Fernet(key)

        # the plain_text is converted to ciphertext
        return f.encrypt(plain_text)

    def decrypt(self, cipher_text, key):
        # Load existing key
        f = Fernet(key)
        
        # the ciphertext converted to plain_text
        return f.decrypt(cipher_text)

    def set_keyword_local(self, keyword):
        '''
            Update keyword sesuai project, misal :
            env_opd
            env_outbox
        '''
        self.keyword_local = keyword

    def encrypt_environ(self, env_name, plain_text):
        '''
            Write directly to environment file
            plain_text in dictionary format :
                {db_password: 123},
                {secret_key: &#^@#&^$^}
                {etc: etc..}
        '''
        dict1 = {}

        # 1. Read ALL data
        file_path = os.path.join(self.BASE_DIR, env_name)
        # print('file_path =', file_path, Path(file_path).is_file())

        # create file if not exists
        if not Path(file_path).is_file():
            with open(file_path, "w") as f:
                f.write('\n') 
                f.close()

            if Path(file_path).is_file():
                print('File is created')
            else:
                print('Fail create!')

        # print(file_path)
        with open(file_path, "r") as f:
            for line in f.readlines():                
                values = line.split('=')
                if len(values) > 1:                    
                    dict1[values[0]] = values[1]

            f.close()
                
        # 2. Encrypt data        
        key = self.generate_key()
        # print(key)
        key_in_hex = self.bytes2hex(key)
        # print(key_in_hex)

        # get key, value from parameter (plain_text)
        values = list(plain_text.values())        
        keys = list(plain_text.keys())

        # Khusus data yg di enkripsi aja (simpan di parameter plain_text)
        # data yg tidak di enkripsi seperti debug=True dll, di tulis manual
        enc = []
        enc_in_hex = []
        for i in range(len(keys)):
            tmp = self.encrypt(values[i].encode(), key)
            enc.append(tmp)
            enc_in_hex.append(self.bytes2hex(tmp))

        # 3. Update Data        
        # dict1['DB_USER'] = '123\n'
        for i in range(len(keys)):
            dict1[keys[i]] = enc_in_hex[i]

        dict1['DB_KEY'] = key_in_hex

        # 4. Write Back Data        
        values = list(dict1.values())        
        keys = list(dict1.keys())

        with open(file_path, "w") as f:
            # tulis ulang DB_KEY (Penambahan ada di dict1)           
            # f.write('DB_KEY' + '=' + key_in_hex + '\n')
            
            # tulis ulang DB_PASSWORD, SECRET_KEY
            for i in range(len(keys)):
                if '\n' in values[i]:
                    f.write(keys[i] + '=' + values[i])
                else:
                    f.write(keys[i] + '=' + values[i] + '\n') 

            f.close()

        print('File is create on :', file_path)
            
    def decrypt_environ(self, mplaint_key, mplaint_list=[], mplaint_tuple=[]): #, env_name, cipher_text, key_hex):
        '''        
            Read directly from environment file
            cipher_text and key_hex, in hexadecimal format            
        '''
        # text = self.hex2bytes(cipher_text)
        # key = self.hex2bytes(key_hex)
        # BASE_DIR = Path(__file__).resolve().parent.parent

        env_list = os.environ.get(self.env_list)
        is_run_from_server = True

        # create file if not exists        
        # create sebelum dibaca oleh RepositoryEnv di path tersebut jika tidak ada file maka akan muncul error
        file_path = self.BASE_DIR / self.env_local
        if not Path(file_path).is_file():
            with open(file_path, "w") as f:
                f.write('\n') 
                f.close()               

            if Path(file_path).is_file(): 
                print('File is created')
            else:
                print('Fail create!')

        file_path = self.BASE_DIR / self.env_server
        if not Path(file_path).is_file():
            with open(file_path, "w") as f:
                f.write('\n') 
                f.close()

            if Path(file_path).is_file(): 
                print('File is created')
            else:
                print('Fail create!')

            # print('File is created')

        if env_list:
            if self.keyword_local in env_list:
                env_config = Config(RepositoryEnv(self.BASE_DIR / self.env_local))
                file_path = os.path.join(self.BASE_DIR, self.env_local)
                print('Load Setting From env.local')
                is_run_from_server = False

        if is_run_from_server:
            env_config = Config(RepositoryEnv(self.BASE_DIR / self.env_server))
            file_path = os.path.join(self.BASE_DIR, self.env_server)
            print('Load Setting From env.server')
        


        print('File is load from :', file_path)
        # Get ALL env_config data
        dict1 = {}        
        with open(file_path, "r") as f:
            for line in f.readlines():                
                values = line.split('=')
                if len(values) > 1:                    
                    dict1[values[0]] = values[1].replace('\n','')
            f.close()

        # print(dict1)
        keys = list(dict1.keys())
        values = list(dict1.values())
        # print(keys)

        # decrypt DB_KEY
        # dapatkan key dulu untuk proses decrypt yg lain
        tmp_keys = ''
        for i in range (len(keys)):        
            if keys[i]=='DB_KEY':                
                tmp_keys = self.hex2bytes(values[i])                
                # dict1[keys[i]] = tmp_keys # key tetap rahasia, jangan disimpan di dict
                break

        for i in range (len(keys)):        
            if keys[i] in mplaint_key:  # khusus tipe data enkripsi
                tmp = self.hex2bytes(values[i])
                tmp = self.decrypt(tmp, tmp_keys).decode()
                # print(keys[i], tmp)                
                dict1[keys[i]] = tmp

            elif keys[i] in mplaint_list:   # khusus tipe data list
                # dict1[keys[i]] = env_config(keys[i], cast=lambda v: [s.strip() for s in v.split(',')])
                dict1[keys[i]] = env_config(keys[i], cast=Csv())

            elif keys[i] in mplaint_tuple:   # khusus tipe data tuple
                # contoh di environment : os.environ['SECURE_PROXY_SSL_HEADER'] = 'HTTP_X_FORWARDED_PROTO, https'
                # proses casting : config('SECURE_PROXY_SSL_HEADER', cast=Csv(post_process=tuple))  <--
                # ('HTTP_X_FORWARDED_PROTO', 'https')
                
                dict1[keys[i]] = env_config(keys[i], cast=Csv(post_process=tuple))

            else:                           # konversi sesuai tipe data python standart
                # print(keys[i], values[i])
                #dict1[keys[i]] = values[i]
                # Ambil sesuai tipe data
                if values[i] in ['True', 'False']:
                    dict1[keys[i]] = env_config(keys[i], default=True, cast=bool)
                elif values[i].isnumeric():
                    dict1[keys[i]] = env_config(keys[i], default=0, cast=int)

            # selain kondisi di atas, biarkan apa adanya (default = string)

        # print('hasilnya = ', dict1)
        return dict1
            

# test module level
if __name__=='__main__':
    # print('Begin Test ENCRYPTION')
    # print('---------------------')
    # secret_text = input("Input Secret Text: ")    

    lib = OutboxEncryption()
    # key = lib.generate_key()    

    # # Out key in hexadecimal format
    # key = lib.bytes2hex(key)
    # print('Key:', key)
    
    # res_enc = lib.encrypt(secret_text.encode(), lib.hex2bytes(key))

    # # Out in hexadecimal
    # res_enc = lib.bytes2hex(res_enc)
    # print('Encrypt result:', res_enc)

    # print('')
    # print('Begin Test DECRYPTION')
    # print('---------------------')
    
    # res_dec = lib.decrypt(lib.hex2bytes(res_enc), lib.hex2bytes(key))
    # print('Decrypt result:', res_dec.decode())
    # print('')
    
    print('')
    print('Encrypt to Environment')
    print('----------------------')
    # BASE_DIR = Path(__file__).resolve().parent.parent
    # print(BASE_DIR)

    # mplaint_text = {
    #     'DB_PASSWORD': 'password untuk koneksi ke database',
    #     'SECRET_KEY': 'secret key yg ada di setting.py'
    # }

    mplaint_text = {
        'DB_PASSWORD': '',
        'SECRET_KEY': 'xxg_7me8rl2m#a_h2oresgt2#ni=3_4*!ai*=rtsq)yi!g7_5-51xx'
    }


    lib.encrypt_environ('.env.local', mplaint_text)
    print('Show Hidden File to Show .env.local')


    print('')
    print('Decrypt From Environment')
    print('----------------------')
    # agar bisa mendeteksi environment local
    lib.set_keyword_local('env_outbox_encrypt')

    # kunci yg di buka khusus, karena ada proses enkripsi
    # selain kunci ini, langsung ambil datanya, tipe data string

    mplaint_key = list(mplaint_text.keys())
    mplaint_list = ['ALLOWED_HOSTS']    # daftar tipe data list (cara konversinya khsusus)
    mplaint_tuple = ['SECURE_PROXY_SSL_HEADER']

    # mplaint_key = [
    #     'DB_PASSWORD', 'SECRET_KEY'
    # ]

    lib.decrypt_environ(mplaint_key, mplaint_list, mplaint_tuple)
    print('Decrypt Finish')
