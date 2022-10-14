import os
from os.path import isfile, join
import multiprocessing as mp
from decouple import AutoConfig
from hitrustai_lab.model_train.core.message import MessageQueue
from hitrustai_lab.model_train.core.utils import return_code, decrypt_passwd, open_connection, close_connection
from hitrustai_lab.orm.Tables.TBMarchant import TbMarchatriskValidationReport
from hitrustai_lab.algorithm.ahp import AHPWeight


class HitrustaiTrainTemple:
    def __init__(self, dict_ahp_weight, dict_model, so_name="./data/passwd.so"):
        self.kg_list = None
        self.accuracy = None
        self.precision = None
        self.recall = None
        self.f1_score = None
        self.finish_reason = None
        self.SQLALCHEMY_DATABASE_URI = None
        self.mq_info = None
        self.so_name = so_name
        self.dict_weight = dict_ahp_weight
        self.dict_model = dict_model
        self.train_info = None

    def read_train_conf(self):
        config = AutoConfig(search_path=os.getcwd() + "/env")
        # check docker environment exist
        TYPE = os.environ.get('TYPE')
        CUSTOMER_ID = os.environ.get('CUSTOMER_ID')
        MODEL_ID = os.environ.get('MODEL_ID')
        TRAINING_ID = os.environ.get('TRAINING_ID')
        KAFKA_TOPIC = os.environ.get('KAFKA_TOPIC')
        SOURCE_START_DATE = os.environ.get('SOURCE_START_DATE')
        SOURCE_END_DATE = os.environ.get('SOURCE_END_DATE')
        TOTAL_DATA_ROW = os.environ.get('TOTAL_DATA_ROW')

        if TYPE is None:
            TYPE = "development"
        if TYPE == "development":
            CUSTOMER_ID = "001584054110001" if CUSTOMER_ID is None else CUSTOMER_ID
            MODEL_ID = "model22222" if MODEL_ID is None else MODEL_ID
            TRAINING_ID = "training33333" if TRAINING_ID is None else TRAINING_ID
            KAFKA_TOPIC = "AiTrainingZoneAgent" if KAFKA_TOPIC is None else KAFKA_TOPIC
            SOURCE_START_DATE = "2021-07-01 00:00:00" if SOURCE_START_DATE is None else SOURCE_START_DATE
            SOURCE_END_DATE = "2021-09-11 00:00:00" if SOURCE_END_DATE is None else SOURCE_END_DATE
            TOTAL_DATA_ROW = "1000000" if TOTAL_DATA_ROW is None else TOTAL_DATA_ROW
        else:
            if CUSTOMER_ID is None or MODEL_ID is None or TRAINING_ID is None or KAFKA_TOPIC is None:
                print('Error: Invalid docker Env. Expected keys [CUSTOMER_ID, MODEL_ID, TRAINING_ID, KAFKA_TOPIC]')
                os.kill(0, 4)
            if SOURCE_START_DATE is None or SOURCE_END_DATE is None or TOTAL_DATA_ROW is None:
                print('Error: Invalid docker Env. Expected keys [SOURCE_START_DATE, SOURCE_END_DATE, TOTAL_DATA_ROW]')
                os.kill(0, 4)

        # check service .env file exist
        kafka_node = config('KAFKA_N', default='0')
        bootstrap_servers = []
        for i in range(int(kafka_node)):
            host = config('KAFKA_HOST_' + str(i + 1), default='')
            port = config('KAFKA_PORT_' + str(i + 1), default='')
            if host == "" or port == "":
                print('Error: Invalid variable in env. Expected keys [KAFKA_HOST, KAFKA_PORT]')
                os.kill(0, 4)
            bootstrap_servers.append(host + ":" + port)

        mq_info = {
            "servers": bootstrap_servers,
            "customer_id": CUSTOMER_ID,
            "model_id": MODEL_ID,
            "training_id": TRAINING_ID,
            "topic": KAFKA_TOPIC
        }
        train_info = {
            "source_start_date": SOURCE_START_DATE,
            "source_end_date": SOURCE_END_DATE,
            "total_data_row": TOTAL_DATA_ROW
        }
        
        mq = MessageQueue(mq_info["servers"], mq_info["customer_id"], mq_info["model_id"], mq_info["training_id"], mq_info["topic"])

        dataset_path = config('SOURCE_PATH_DATASET', default='')
        kg_path = config('SOURCE_PATH_KNOWLEDGE', default='')
        lib_path = config('SOURCE_PATH_LIB', default='')

        if dataset_path == ""  or lib_path == "":
            print("No dataset/kg/lib path")
            mq.startup(return_code["container_start_fail"], "No dataset/kg/lib path")
            return

        db_pass = config('DB_PASS', default='')
        password = decrypt_passwd(self.so_name, db_pass)
        SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
            config('DB_ENGINE', default='mysql+pymysql'),
            config('DB_USERNAME', default='test'),
            password,
            config('DB_HOST', default='127.0.0.1'),
            config('DB_PORT', default=3306),
            config('DB_NAME', default='testdb')
        )
        return mq_info, train_info, SQLALCHEMY_DATABASE_URI, kg_path, lib_path, dataset_path, mq

    def process(self, manager_dict, lock, model, dataset_path, kg_path, lib_path, end_date, dict_model):
        print("[{}] Start to train model".format(model))
        try:
            train_model = dict_model[model]
            result = train_model.train()
        except Exception:
            manager_dict["mq"].send(return_code["train_fail"], "0")
            print('Error: [{}] training fail'.format(model))
            os.kill(0, 4)

        lock.acquire()
        manager_dict["progress"] += 1
        manager_dict[model] = result
        lock.release()
        
        if manager_dict["progress"] < len(dict_model.keys()):
            print("[{}] Send progress: {}".format(model, manager_dict["progress"]))
            manager_dict["mq"].send(result["return_code"], str(manager_dict["progress"]*16), result["reason"])
        print("[{}] {}".format(model, result))

        if result["return_code"] != return_code["train_success"]:
            print('Error: [{}] training fail'.format(model))
            os.kill(0, 4)
        print("[{}] Process finish".format(model))

    def train(self):
        mq_info, train_info, SQLALCHEMY_DATABASE_URI, kg_path, lib_path, dataset_path, mq = self.read_train_conf()
        self.SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
        self.mq_info = mq_info
        self.train_info = train_info
        # Generate Train and Val csv file
        # val_quantity = 450

        # Manager to create shared object.
        manager = mp.Manager()
        # Create a lock.
        lock = manager.Lock()
        # Create and Init global variables.
        manager_dict = manager.dict()
        manager_dict["mq"] = mq
        manager_dict["progress"] = 0

        models_list = list(self.dict_model.keys())

        # Multiprocess pool.
        pools = []
        for model in models_list:
            p = mp.Process(
                target=self.process,
                args=(manager_dict, lock, model, dataset_path, kg_path, lib_path, train_info["source_end_date"], self.dict_model)
            )
            pools.append(p)

        for p in pools:
            p.start()
        for p in pools:
            p.join()

        # Waiting for backing to main process
        if manager_dict["progress"] < len(models_list):
            manager_dict["mq"].send(return_code["train_fail"], str(manager_dict["progress"] * 16, "Train Fail"))
            os.kill(0, 4)

        progress = "100"
        kg_list = [f for f in os.listdir(lib_path) if isfile(join(lib_path, f)) and (".pkl" in f or ".joblib" in f)]

        init_score = 0
        accuracy, precision, recall, f1_score = init_score, init_score, init_score, init_score

        finish_reason = []
        for model in models_list:
            if model not in manager_dict:
                manager_dict["mq"].send(return_code["train_fail"], progress, manager_dict[model]["reason"])
                os.kill(0, 4)

            if manager_dict[model]["return_code"] != return_code["train_success"]:
                finish_reason.append(manager_dict[model]["reason"])
            accuracy += manager_dict[model]["report"]["accuracy"] * self.dict_weight[model]
            precision += manager_dict[model]["report"]["precision"] * self.dict_weight[model]
            recall += manager_dict[model]["report"]["recall"] * self.dict_weight[model]
            f1_score += manager_dict[model]["report"]["f1_score"] * self.dict_weight[model]
        accuracy = 1.0 if accuracy > 1 else round(accuracy, 2)
        precision = 1.0 if precision > 1 else round(precision, 2)
        recall = 1.0 if recall > 1 else round(recall, 2)
        f1_score = 1.0 if f1_score > 1 else round(f1_score, 2)
        
        self.kg_list = kg_list
        self.accuracy = accuracy
        self.precision = precision
        self.recall = recall
        self.f1_score = f1_score
        self.finish_reason = finish_reason
        return manager_dict

    def orm_to_table(self, tb, manager_dict):
        val_quantity = 450
        progress = 100
        try:
            session = open_connection(db_uri=self.SQLALCHEMY_DATABASE_URI)
            val_quantity = 450
            session.addprogress = 100

            session.add(tb)
            session.commit()  
            close_connection(session)
            print("Save Fraud Detect Validation Report successfully insert into db")
        except Exception as e:
            session.rollback()
            print("Save validation report fail: " + str(e))

        val_report = {
            "source_start_date": self.train_info["source_start_date"],
            "source_end_date": self.train_info["source_end_date"],
            "model_name": "fraud_detect",
            "training_sample_count": str(int(self.train_info["total_data_row"]) - val_quantity),
            "validation_sample_count": str(val_quantity),
            "accuracy": str(self.accuracy),
            "precision": str(self.precision),
            "recall": str(self.recall),
            "f1_score": str(self.f1_score)
        }
        manager_dict["mq"].finish(return_code["train_all_success"], progress, self.kg_list, val_report, ", ".join(self.finish_reason))



if __name__ == '__main__':
    pass
