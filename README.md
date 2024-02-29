# dnd_microservice
1. Requesting Data:
   Use the send_request function in your code to send requests to the microservice. The function takes two parameters: 'command', examples being edit_race, edit_background, and edit_class, and 'data', which the the data specific to each command.
Example call:
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


2. Receiving Data:
   Data is automatically sent back to the client when the request is received. It is in the form of a JSON, containing the data with the edited fields.

3. UML Diagram:
![image](https://github.com/bmazaoreg/dnd_microservice/assets/114183065/db0ed496-1f2c-4c8b-8567-bb0ea8070599)
