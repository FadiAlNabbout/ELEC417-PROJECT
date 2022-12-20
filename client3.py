import requests

def send_request(url):
    # Set up a new TOR circuit
    new_circuit()

    # Send a request to the server
    response = requests.get(url)

    # Print the response from the server
    print(response.text)

if __name__ == "__main__":
    send_request("http://localhost:8000/")

