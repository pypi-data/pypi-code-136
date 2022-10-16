if __name__ == "__main__":
    from sparrow.multiprocess.client import Client
    client = Client()
    client.update_dict({'a': 1, 'b': 2})