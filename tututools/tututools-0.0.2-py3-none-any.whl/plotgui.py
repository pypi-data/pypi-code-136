import zmq
from matplotlib import pyplot as plt
import pickle
import argparse

class rpyplot_gui(object):
    def __init__(self, remote_url, port = 1234) -> None:
        self.pipe = zmq.Context().socket(zmq.PAIR)
        self.pipe.connect('tcp://{}:{}'.format(remote_url, str(port)))

    def run(self, ):        
        while True:
            recv_data = self.pipe.recv()
            recv_data = pickle.loads(recv_data)
            op = recv_data['op']

            if op == 'imshow':
                data = recv_data['data']
                data = pickle.loads(data)
                plt.imshow(data)
            
            if op == 'show':
                plt.show()
                self.pipe.send_string('end_show')
            
            if op == 'subplot':
                index = recv_data['index']
                plt.subplot(index)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--port",
        "-P",
        "-p",
        help="The listening port in remote server",
        default = 1234,
        type = int,
    )

    parser.add_argument(
        "--addr",
        "-A",
        "-a",
        help="The remote ip address in remote server",
        default = '127.0.0.1',
        type = str,
    )
    args = parser.parse_args()
    print('--> Connection will be built with {}:{} <--'.format(args.addr, args.port))
    rgui = rpyplot_gui(args.addr, args.port)
    rgui.run()

if __name__ == '__main__':
    main()