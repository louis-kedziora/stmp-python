# Louis Kedziora
# V00820695
# CSC-361/lab3

from socket import *

TODO = None
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("smtp.uvic.ca", 587)

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')

# print("\nHELO")
# Send HELO command and print server response.
heloCommand = 'EHLO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Replace '&&&&&' with sending address
mailfromCmd = 'MAIL FROM:<&&&&&>\r\n'
clientSocket.send(mailfromCmd.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Replace '&&&&&' with receiving address
# Send RCPT TO command and print server response. 
mailtoCmd = 'RCPT TO:<&&&&&>\r\n'
clientSocket.send(mailtoCmd.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')


# Send DATA command and print server response.
dataCmd = 'DATA\r\n'
clientSocket.send(dataCmd.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')

# Send message data.
# print("send")
clientSocket.send(msg.encode())


# Message ends with a single period.
# print("period")
clientSocket.send(endmsg.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send QUIT command and get server response.
# print("quit")
quitCmd = 'QUIT\r\n'
clientSocket.send(quitCmd.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
