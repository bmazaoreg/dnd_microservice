import zmq

# Constants for ZeroMQ
SERVER_ENDPOINT = "tcp://127.0.0.1:5555"


def send_request(command, data):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(SERVER_ENDPOINT)

    request = {'command': command, **data}
    socket.send_json(request)

    response = socket.recv_json()
    print("Response:", response)


if __name__ == "__main__":
    send_request('edit_race', {'new_race': 'Elf'})
