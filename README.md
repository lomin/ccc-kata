This Kata prepares you for the Craftsmen-Coding-Contest. Your task is to implement a program, that

1. listens on a port for a message containing a simple mathematical task
2. calculates the result
3. sends the result back to the server
4. repeats until message is "__SHUTDOWN__"

The content of the messages are strings with the following structure:

<function>:<uuid>:<parameter>:<parameter>[:<parameter>]*

where <function> is one of {"ADD", "MULTIPLY", "SUBTRACT"}. Parameters are integers. There are at least two parameters, but there can be more.

Example server messages are:

"ADD:4160806a2f2846759d6c7e764f4bcbd5:184:106:107"
"SUBTRACT:45429b851ac549fc9e2e38f9ee289061:27:107:91:55"
"MULTIPLY:6868c974bf7140eabb18b826bedacd54:175:126:172:119"

The structure of the expected response are:

<uuid>:<result>

The correct responses for the example server messages are respectively:

"4160806a2f2846759d6c7e764f4bcbd5:397"
"45429b851ac549fc9e2e38f9ee289061:-226"
"6868c974bf7140eabb18b826bedacd54:451319400"

All communication happens through UDP.

To verify your program, start it and then start the python script ccc_kata_test.py. The script expects two command line arguments, which define the client port and the server port. The client port is the port your program listens to for new messages. The server port is the port on which the script listens for responses.

This is how you start the script with port 9000 as client port and port 9001 as server port:

python ccc_kata_test.py 9000 9001

The script will send three messages. If all messages are answered correctly, it will print "successful!", otherwise "unsuccessful!".

The goals of the Kata are to make you comfortable with the socket interface of your chosen language and the structure of a text-based protocol, which is similiar to the protocol used in the Craftsmen-Coding-Contest.