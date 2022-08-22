## This is application aims to exchange messages in a client/server TCP/UDP connection using sockets, being a work of Computer Networking course at UFPel's Computer Engineering .

- The user (client) inputs the connection type with the server (TCP/UDP)
- The user (client) inputs a string and select if wants to convert it to lower or upper case.
- The messege sended to the server has a format `{0|1};{user_input_string}` where 0 indicates to set the string to lower case and 1 to upper case.
- The TCP connection is closed once the client don't want to send any more sentences.
