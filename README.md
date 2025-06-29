# SSL-Enabled Time Server

A secure, SSL/TLS-enabled time server and client implementation in Python that provides time synchronization across different time zones with encrypted communication.

## 🌟 Features

- **Secure Communication**: SSL/TLS encryption for all client-server communications
- **Multi-timezone Support**: Supports 12 different time zones including UTC, EST, CST, MST, PST, IST, JST, AEST, CET, EET, NST, and HKT
- **Real-time Time Synchronization**: Get current server time with timezone adjustments
- **Multi-threaded Server**: Handles multiple client connections simultaneously
- **Interactive Client**: User-friendly command-line interface for time operations

## 🏗️ Architecture

- **Server** (`server.py`): SSL-enabled server that handles time requests and timezone settings
- **Client** (`client.py`): SSL-enabled client with interactive menu for time operations
- **SSL/TLS Security**: Certificate-based authentication and encrypted communication

## 📋 Prerequisites

- Python 3.6 or higher
- SSL certificates (server-cert.pem, server-key.pem, ca-cert.pem)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd CN-project
```

### 2. Generate SSL Certificates
Before running the application, you need to generate SSL certificates:

```bash
# Generate CA certificate
openssl genrsa -out ca-key.pem 2048
openssl req -new -x509 -days 365 -key ca-key.pem -out ca-cert.pem

# Generate server certificate
openssl genrsa -out server-key.pem 2048
openssl req -new -key server-key.pem -out server.csr
openssl x509 -req -in server.csr -CA ca-cert.pem -CAkey ca-key.pem -CAcreateserial -out server-cert.pem -days 365
```

### 3. Update Configuration
Edit the server and client files to use your actual IP address:
- In `server.py`: Update the bind address (line 47)
- In `client.py`: Update the server address (line 8)

## 🎯 Usage

### Starting the Server
```bash
python server.py
```
The server will start listening on the configured IP and port (default: 192.168.43.103:12345)

### Running the Client
```bash
python client.py
```

### Client Menu Options
1. **Get Current Time**: Retrieves the current server time
2. **Set Timezone**: Configure the timezone for time display

### Supported Time Zones
- UTC (Coordinated Universal Time)
- EST (Eastern Standard Time)
- CST (Central Standard Time)
- MST (Mountain Standard Time)
- PST (Pacific Standard Time)
- IST (Indian Standard Time)
- JST (Japan Standard Time)
- AEST (Australian Eastern Standard Time)
- CET (Central European Time)
- EET (Eastern European Time)
- NST (Newfoundland Standard Time)
- HKT (Hong Kong Time)

## 🔒 Security Features

- **SSL/TLS Encryption**: All communications are encrypted
- **Certificate-based Authentication**: Server authentication using X.509 certificates
- **Secure Socket Wrapping**: SSL context with proper certificate validation

## 📁 Project Structure

```
CN-project/
├── server.py          # SSL-enabled time server
├── client.py          # SSL-enabled time client
├── .gitignore         # Git ignore rules
└── README.md          # Project documentation
```

## ⚠️ Important Notes

- **Certificate Files**: The `.pem` files are excluded from version control for security reasons
- **IP Configuration**: Update the IP addresses in both files to match your network configuration
- **Firewall**: Ensure the server port (12345) is open in your firewall
- **Network**: Both client and server must be on the same network or have proper network access

## 🛠️ Troubleshooting

### Common Issues

1. **SSL Certificate Errors**: Ensure all certificate files are in the same directory as the scripts
2. **Connection Refused**: Check if the server is running and the IP/port configuration is correct
3. **Permission Denied**: Ensure you have read permissions for the certificate files

### Debug Mode
Add debug prints to troubleshoot SSL handshake issues:
```python
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

Created as part of a Computer Networks project demonstrating SSL/TLS implementation in Python.

---

**Note**: This is a demonstration project. For production use, ensure proper certificate management and security practices. 