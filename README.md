# lanchat-XiananLi

This program contains two python files: lanchat.py and server.py. The server can be set up 
on any computer to be a server node, and using that computer's private IP address as the server
IP address. The specific function and usage are indicate in the beginning of each file.

 - discovers other computers on the same LAN
    - provides a user friendly display of information about each discovered peer

 - supports sending text messages carried in UDP packets
    - support either unicast or broadcast packet transmission
    - for either unicast or multicast chat provide a default port and allow optional 
      selection of a different port
    - allows the selection of a specific IP address for the unicast chat

 - the program should be written so that:
    - it provides useful user feed-back on errors
    - provides a '-h' or '--help' option that displays useful help for the application
    - includes a 'readme.md' file with useful information about the program
