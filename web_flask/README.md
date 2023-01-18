# web_flask

- 0-hello_route.py, __init__.py
##### In this script, we first import the Flask module, then create a Flask web server from the Flask module. We then use the @app.route decorator to bind a function to a specific URL route (in this case, the root URL '/'). The function returns a string "Hello HBNB!" which will be displayed on the web page when the root URL is accessed. Finally, we check if the script is being run directly, and if so, we start the web server on the IP address 0.0.0.0 and port 5000 using the app.run() method, strict_slashes is set to false to allow both "/" and "/" in the URL.
