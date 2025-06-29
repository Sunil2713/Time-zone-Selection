import socket
import ssl

def display_time_zones():
    print("Available Time Zones:")
    print("1. UTC (Coordinated Universal Time)")
    print("2. EST (Eastern Standard Time)")
    print("3. CST (Central Standard Time)")
    print("4. MST (Mountain Standard Time)")
    print("5. PST (Pacific Standard Time)")

def main():
    server_address = ('192.168.43.103', 12345)

    # Create SSL context with CA certificate
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_verify_locations("ca-cert.pem")  # Load the CA certificate
    context.check_hostname = False  # Disable hostname check
    ssl_client_socket = context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    ssl_client_socket.connect(server_address)

    try:
        while True:
                    print("1. Get current time")
                    print("2. Set timezone")
                    choice = input("Enter your choice: ")

                    if choice == "1":
                        ssl_client_socket.send("get_time".encode('utf-8'))
                        server_time = ssl_client_socket.recv(1024).decode('utf-8')
                        print("Current time:", server_time)
                    elif choice == "2":
                        display_time_zones()
                        timezone_choice = input("Enter the number corresponding to your desired time zone: ")
                        if timezone_choice.isdigit():
                            timezone_choice = int(timezone_choice)
                            if timezone_choice >= 1 and timezone_choice <= 5:
                                time_zones = ["UTC", "EST", "CST", "MST", "PST"]
                                selected_timezone = time_zones[timezone_choice - 1]
                                ssl_client_socket.send(f"set_timezone:{selected_timezone}".encode('utf-8'))
                                response = ssl_client_socket.recv(1024).decode('utf-8')
                                print(response)
                            else:
                                print("Invalid timezone choice.")
                        else:
                            print("Invalid input.")
                    else:
                        print("Invalid choice.")
                        
    except KeyboardInterrupt:
                print("Client shutting down.")

if __name__ == "__main__":
    main()