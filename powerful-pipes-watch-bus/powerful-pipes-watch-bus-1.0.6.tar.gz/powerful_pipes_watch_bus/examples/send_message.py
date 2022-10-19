from powerful_pipes_watch_bus.brokers import BusInterface, connect_bus


def main():
    connection: BusInterface = connect_bus("redis://")
    connection.send_json_message("three", {"hello!": "word!"})


if __name__ == '__main__':
    main()
