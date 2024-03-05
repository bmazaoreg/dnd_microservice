import zmq

# Constants for ZeroMQ
SERVER_ENDPOINT = "tcp://127.0.0.1:5555"

# Dummy data for character attributes
character_data = {
    'name': 'John Doe',
    'race': 'Human',
    'class': 'Wizard',
    'background': 'Acolyte',

}

# Function to handle requests from the client
def handle_request(request):
    command = request['command']
    character = character_data.copy()  # Create a copy to avoid modifying the original data

    if command == 'edit_race':
        new_race = request.get('new_race')
        if new_race:
            character['race'] = new_race

    elif command == 'edit_class':
        new_class = request.get('new_class')
        if new_class:
            character['class'] = new_class

    elif command == 'edit_background':
        new_background = request.get('new_background')
        if new_background:
            character['background'] = new_background

    return character

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(SERVER_ENDPOINT)

    print("Character Edit Microservice is running...")

    while True:
        # Wait for a request from the client
        request = socket.recv_json()

        # Handle the request and send back the updated character
        updated_character = handle_request(request)

        # Send the response back to the client
        socket.send_json(updated_character)

if __name__ == "__main__":
    main()
