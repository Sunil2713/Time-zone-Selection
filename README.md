# 🕐 SSL-Enabled Time Server

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Security](https://img.shields.io/badge/Security-SSL%2FTLS-red.svg)](https://en.wikipedia.org/wiki/Transport_Layer_Security)

A secure, SSL/TLS-enabled time server and client implementation in Python that provides real-time time synchronization across multiple time zones with encrypted communication. Perfect for Computer Networks projects and learning SSL/TLS implementation.

## ✨ Features

- 🔒 **Secure Communication**: SSL/TLS encryption for all client-server communications
- 🌍 **Multi-timezone Support**: Supports 12 different time zones globally
- ⚡ **Real-time Synchronization**: Get current server time with instant timezone adjustments
- 🔄 **Multi-threaded Server**: Handles multiple client connections simultaneously
- 🎯 **Interactive Client**: User-friendly command-line interface with intuitive menu
- 🛡️ **Certificate-based Authentication**: X.509 certificate validation
- 📊 **Connection Logging**: Detailed connection and operation logging

## 🏗️ System Architecture

```
┌─────────────────┐    SSL/TLS    ┌─────────────────┐
│   Client        │ ◄──────────►  │   Server        │
│   (client.py)   │   Encrypted   │   (server.py)   │
└─────────────────┘               └─────────────────┘
        │                                   │
        │                                   │
        ▼                                   ▼
┌─────────────────┐               ┌─────────────────┐
│   User Input    │               │   Time Zone     │
│   & Display     │               │   Processing    │
└─────────────────┘               └─────────────────┘
```

## 📋 Prerequisites

- **Python**: 3.6 or higher
- **OpenSSL**: For certificate generation
- **Network Access**: Both client and server must be on the same network
- **Firewall**: Port 12345 must be open

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/Sunil2713/Time-zone-Selection.git
cd Time-zone-Selection
```

### 2. Generate SSL Certificates
```bash
# Generate CA certificate
openssl genrsa -out ca-key.pem 2048
openssl req -new -x509 -days 365 -key ca-key.pem -out ca-cert.pem

# Generate server certificate
openssl genrsa -out server-key.pem 2048
openssl req -new -key server-key.pem -out server.csr
openssl x509 -req -in server.csr -CA ca-cert.pem -CAkey ca-key.pem -CAcreateserial -out server-cert.pem -days 365
```

### 3. Configure Network Settings
Update the IP addresses in both files to match your network:
- **server.py** (line 47): `server.bind(('YOUR_IP_ADDRESS', 12345))`
- **client.py** (line 8): `server_address = ('YOUR_IP_ADDRESS', 12345)`

### 4. Start the Server
```bash
python server.py
```
**Output**: `🚀 Time server started on 192.168.43.103:12345`

### 5. Run the Client
```bash
python client.py
```

## 🎯 Usage Guide

### Server Operations
The server runs continuously and handles:
- ✅ SSL/TLS handshake with clients
- ✅ Time requests from multiple clients
- ✅ Timezone configuration requests
- ✅ Multi-threaded connection management

### Client Menu Options

```
┌─────────────────────────────────────┐
│         TIME SERVER CLIENT          │
├─────────────────────────────────────┤
│ 1. Get current time                 │
│ 2. Set timezone                     │
│ 3. Show available timezones         │
│ 4. Exit                             │
└─────────────────────────────────────┘
```

#### Option 1: Get Current Time
Retrieves the current server time in the configured timezone.

#### Option 2: Set Timezone
Configure your preferred timezone from the available options.

#### Option 3: Show Available Timezones
Displays all supported time zones with their full names.

## 🌍 Supported Time Zones

| Code | Name | UTC Offset | Region |
|------|------|------------|---------|
| UTC | Coordinated Universal Time | +0:00 | Global |
| EST | Eastern Standard Time | -5:00 | North America |
| CST | Central Standard Time | -6:00 | North America |
| MST | Mountain Standard Time | -7:00 | North America |
| PST | Pacific Standard Time | -8:00 | North America |
| IST | Indian Standard Time | +5:30 | Asia |
| JST | Japan Standard Time | +9:00 | Asia |
| AEST | Australian Eastern Standard Time | +10:00 | Australia |
| CET | Central European Time | +1:00 | Europe |
| EET | Eastern European Time | +2:00 | Europe |
| NST | Newfoundland Standard Time | -3:30 | North America |
| HKT | Hong Kong Time | +8:00 | Asia |

## 🔒 Security Features

### SSL/TLS Implementation
- **Certificate-based Authentication**: Server authentication using X.509 certificates
- **Encrypted Communication**: All data transmitted over SSL/TLS
- **Certificate Validation**: Client verifies server certificate
- **Secure Socket Wrapping**: Proper SSL context configuration

### Security Best Practices
- ✅ Certificate files excluded from version control
- ✅ Input validation and sanitization
- ✅ Connection timeout handling
- ✅ Error handling for SSL operations

## 📁 Project Structure

```
Time-zone-Selection/
├── server.py              # SSL-enabled time server
├── client.py              # SSL-enabled time client
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
├── server-cert.pem       # Server certificate (local)
├── server-key.pem        # Server private key (local)
└── ca-cert.pem           # CA certificate (local)
```

## ⚠️ Important Security Notes

### Certificate Management
- **Never commit certificate files** to version control
- **Keep private keys secure** and restrict file permissions
- **Rotate certificates regularly** for production use
- **Use strong key sizes** (2048 bits minimum)

### Network Security
- **Update IP addresses** to match your network configuration
- **Configure firewall rules** to allow port 12345
- **Use VPN** for remote connections in production
- **Monitor connection logs** for suspicious activity

## 🛠️ Troubleshooting

### Common Issues and Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| SSL Certificate Error | Missing or invalid certificates | Generate certificates using OpenSSL |
| Connection Refused | Server not running or wrong IP | Check server status and IP configuration |
| Permission Denied | Certificate file permissions | Set proper read permissions (600) |
| Timeout Error | Network connectivity issues | Check firewall and network settings |

### Debug Mode
Enable debug mode for SSL troubleshooting:
```python
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
```

### Log Analysis
Monitor server output for:
- Connection establishment messages
- SSL handshake success/failure
- Client request processing
- Error messages and stack traces

## 🔧 Advanced Configuration

### Customizing Server Settings
```python
# In server.py
SERVER_HOST = '0.0.0.0'  # Listen on all interfaces
SERVER_PORT = 12345      # Custom port
MAX_CONNECTIONS = 10     # Increase connection limit
```

### SSL Configuration Options
```python
# SSL context options
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True
context.minimum_version = ssl.TLSVersion.TLSv1_2
```

## 📊 Performance Considerations

- **Connection Pooling**: Server handles multiple concurrent connections
- **Memory Management**: Proper socket cleanup on connection close
- **CPU Usage**: Minimal overhead for time calculations
- **Network Bandwidth**: Efficient message format for time requests

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Contribution Guidelines
- Follow PEP 8 style guidelines
- Add comments for complex logic
- Include error handling
- Test your changes thoroughly
- Update documentation if needed

## 📄 License

This project is for educational purposes. All rights reserved.

## 👨‍💻 Author

**Sunil2713**
- GitHub: [@Sunil2713](https://github.com/Sunil2713)
- Project: [Time-zone-Selection](https://github.com/Sunil2713/Time-zone-Selection)

## 🙏 Acknowledgments

- **Python SSL/TLS Documentation** for implementation guidance
- **OpenSSL** for certificate generation tools
- **Computer Networks Community** for project inspiration

## 📞 Support

If you encounter any issues or have questions:

1. **Check the troubleshooting section** above
2. **Search existing issues** on GitHub
3. **Create a new issue** with detailed information
4. **Contact the author** for direct support

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

*Built with ❤️ for Computer Networks education*

</div> 