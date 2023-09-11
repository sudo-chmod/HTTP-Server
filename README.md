# Simple HTTP Server with Python

This is a simple Python-based server that can handle PHP files. It listens for incoming connections and serves the requested files, including PHP scripts. The server is configured to execute PHP scripts and pass data from GET and POST requests to the PHP scripts.

## How to Use

1. **Server Configuration**:
   - You can change the server's IP address and port by modifying the `HOST` and `PORT` variables in the code.
   - The base directory for serving files is set in the `BASE` variable.

2. **Running the Server**:
   - Execute the Python script in your terminal or preferred Python environment.

   ```bash
   python server.py

3. **Accessing the Server**:
    - Open a web browser and navigate to http://127.0.0.1:2728 (or use the IP and port you configured).

4. **Using the Server**:
    - The server can handle both GET and POST requests.
    - For GET requests, you can pass data in the URL as query parameters.
    - For POST requests, you can send data in the request body.

5. **PHP Execution**:
    - PHP files are executed using the PHP interpreter, and any output is returned to the client.

## Files and Directories

 - server.py : The Python script for the server.
 - htdocs/ : The base directory for serving files. Place your HTML, PHP, and other files here.

### Important Notes
   - Make sure you have PHP installed on your system for PHP execution to work.
   - This is a simple and basic server model and may not be suitable for production use without further hardening and security measures.
