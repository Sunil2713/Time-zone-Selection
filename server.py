import socket
import ssl
import threading
from datetime import datetime, timedelta

TIME_ZONES = {
    "UTC": 0,
    "EST": -5,
    "CST": -6,
    "MST": -7,
    "PST": -8,
    "IST": +5,   
    "JST": +9,    
    "AEST": +10,  
    "CET": +1,    
    "EET": +2,    
    "NST": -3.5,  
    "HKT": +8     
}


def handle_client(client_socket, time_difference):
    while True:
        try:
            request = client_socket.recv(1024).decode('utf-8')
            if not request:
                break
            if request == "get_time":
                print("Client is requesting current time.")
                current_time = datetime.now() + time_difference
                client_socket.send(str(current_time).encode('utf-8'))
            elif request.startswith("set_timezone"):
                _, timezone = request.split(':')
                print(f"Client is setting timezone to {timezone}.")
                if timezone.upper() in TIME_ZONES:
                    timezone_offset = TIME_ZONES[timezone.upper()]
                    client_socket.send(f"Timezone set to {timezone} successfully.".encode('utf-8'))
                    time_difference = timedelta(hours=timezone_offset)
                else:
                    client_socket.send("Invalid timezone.".encode('utf-8'))
        except Exception as e:
            print("Error handling client:", e)
            break

    client_socket.close()


def main():
    initial_time_difference = timedelta(minutes=45)

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="server-cert.pem", keyfile="server-key.pem")

    ssl_client_socket = context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM), server_side=True)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('192.168.43.103', 12345))
    server.listen(5)
    print("Time server started.")

    try:
        while True:
            client_socket, addr = server.accept()
            print(f"Connection from {addr} has been established.")
            ssl_client_socket = context.wrap_socket(client_socket, server_side=True)
            client_thread = threading.Thread(target=handle_client, args=(ssl_client_socket, initial_time_difference))
            client_thread.start()
    except KeyboardInterrupt:
        print("Server shutting down.")
        server.close()


if __name__ == "__main__":
    main()