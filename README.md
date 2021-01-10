# Chat_udp_socket_multithreading
This is a simple chat app created using UDP protocol, socket programming and multi-threading concepts.
User Datagram Protocol (UDP) is one of the core members of the Internet protocol suite. With UDP, computer applications can send messages, in this case referred to as datagrams, to other hosts on an (IP) network. UDP uses a simple connectionless communication model with a minimum of protocol mechanisms. UDP provides checksums for data integrity, and port numbers for addressing different functions at the source and destination of the datagram.
Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket(node) listens on a particular port at an IP, while other socket reaches out to the other to form a connection.
Socket programming alone won’t help us to achieve our goal because here in our application we want both send and receiver program to work in parallel with each other so that we can read the message sent by the user and also be able to send the message at the same time. To achieve this kind of parallelism we will be using multithreading.
In computer architecture, multithreading is the ability of a (CPU) to provide multiple threads of execution concurrently, supported by the operating system.

-- As the no. of clients increases it takes more and more time.
-- we need to know the IP and the port number to communicate.
-- udp doesn't assure that the msg is recevied or not.

SOCKET PROGRAMMING:-
Socket programming is a programming schema in which sockets are used and manipulated to create a connection between software. Sockets are used to connect software either between different computers or within the same computer so the programs can share data. Socket programming is used with instant messaging, Internet browsers, file sharing programs, and anything that forces the computer to connect to a system. Most sockets are programmed automatically, but some operating systems (OS) place this responsibility in the hands of the user.
Here, we are using Socket Programming of Python, to establish one Chat Server between two Operating System, using Sockets.
SOCKET:-
A network socket is a software structure within a network node of a computer network that serves as an endpoint for sending and receiving data across the network. The structure and properties of a socket are defined by an application programming interface for the networking architecture.
