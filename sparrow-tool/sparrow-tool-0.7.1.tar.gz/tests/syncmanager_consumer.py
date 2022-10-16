if __name__ == "__main__":
    from sparrow.multiprocess.client import Client
    client = Client()
    print(client.get_dict_data())
