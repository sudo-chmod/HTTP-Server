import socket
import os
import subprocess

# Server configuration
HOST = '127.0.0.1'
PORT = 2728
BASE = 'htdocs'

# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

# Listen for incoming connections
server.listen(5)

# Accept connections
while True:
    # Wait for a connection
    client, address = server.accept()
    print(f"\n[NEW CONNECTION] {address} connected...\n")

    # Receive requset data
    req = client.recv(4096).decode('utf-8').split("\r\n")
    # print(req)

    # Getting the request type
    req_type = req[0].split(" ")[0]
    # print(req_type)

    # Getting the request path and user input data
    if (req_type == "GET") and ("?" in req[0]):
        req_path, req_data = req[0].split(" ")[1].split("?")
        req_data = req_data.split("&")
    elif (req_type == "GET"):
        req_path = req[0].split(" ")[1]
        req_data = []
    elif (req_type == "POST"):
        req_path = req[0].split(" ")[1]
        if (req[-1] != ""):
            req_data = req[-1].split("&")
        else:
            req_data = []
    # print(req_path)
    # print(req_data)

    # Getting the file location
    file_location = os.path.join(BASE, req_path.lstrip("/"))
    # print(file_location)

    # Check if file exists
    if (os.path.exists(file_location)):
        # Check if file is a directory
        if (os.path.isdir(file_location)):
            # Check if index.php exists
            if os.path.exists(os.path.join(file_location, "index.php")):
                file_location = os.path.join(file_location, "index.php")
            else:
                res = "HTTP/1.1 404 Not Found\r\n\r\n404 File Not Found"

        # Check if the called file is a php file or not
        if (file_location.endswith(".php")):
           
            # Creating the data array (dictionary)
            if (len(req_data) > 1):
                req_data_arr = dict(
                    map(lambda x: [i for i in x.split("=")], req_data))
            elif (len(req_data) == 1):
                req_data_arr = dict(
                    {req_data[0].split("=")[0]: req_data[0].split("=")[1]})
            else:
                req_data_arr = dict()
            # print(req_data_arr)

            # Creating the php data array
            if (req_type == "GET"):
                php_head = "<?php\n$_GET = array(\n"
                for variable_name, data in req_data_arr.items():
                    php_head += f"\t'{variable_name}' => '{data}',\n"
                php_head += ");\n?>" + "\n"
            elif (req_type == "POST"):
                php_head = "<?php\n$_POST = array(\n"
                for variable_name, data in req_data_arr.items():
                    php_head += f"\t'{variable_name}' => '{data}',\n"
                php_head += ");\n?>" + "\n"
            else:
                php_head = ''
            # print(php_head)

            # Reading the current php file
            current_php_file = open(file_location, "r")
            current_php_file_data = current_php_file.read()
            current_php_file.close()

            # Creating the output php file
            current_directory = os.getcwd()
            output_file_location = os.path.join(
                current_directory, BASE, "output.php")

            # Writing the output php file
            output_file = open(output_file_location, "w")
            output_file.write(php_head + current_php_file_data)
            output_file.close()

            # print(php_head + current_php_file_data)

            # Executing the output php file
            try:
                output = subprocess.check_output(
                    ["php", output_file_location]).decode('utf-8')
                res = "HTTP/1.1 200 OK\r\n\r\n" + output

            except:
                res = "HTTP/1.1 500 Internal Server Error\r\n\r\n500 Internal Server Error"

            # Deleting the output php file
            os.remove(output_file_location)

        else:  # If the file is not a php file
            try:
                current_file = open(file_location, "r")
                output = current_file.read()
                current_file.close()
                res = "HTTP/1.1 200 OK\r\n\r\n" + output
            except:
                res = "HTTP/1.1 500 Internal Server Error\r\n\r\n500 Internal Server Error"
    else:
        print("File not exists")

        res = "HTTP/1.1 404 Not Found\r\n\r\n404 File Not Found"

    # Send response
    client.sendall(res.encode('utf-8'))

    # Close the connection
    client.close()
