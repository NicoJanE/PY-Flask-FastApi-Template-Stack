""" Route handlers for the Flask application.

This module contains the Controller layer of the application architecture.
Routes handle HTTP requests, process request data, and coordinate with 
the View layer to generate responses. """

import socket
from flask import request
from view.app_view import AppView


class AppRoutes:
    """ Handles HTTP routing and request processing.
    
    This class acts as the Controller layer in the application architecture,
    responsible for:
    - Registering URL routes with Flask
    - Processing HTTP requests (GET, POST, etc.)
    - Coordinating between request data and view rendering
    - Managing application flow logic
    
    Naming Convention:
    - Route methods use 'rt_' prefix (e.g., rt_login)
    - Corresponding view methods use 'vw_' prefix (e.g., vw_login)
    - This creates a clear mapping between routes and views
    
    Architecture Note:
    - Uses class-based routing instead of @app.route decorators
    - Enables better organization and dependency injection
    - Allows for easy testing and maintenance """
    
    
    def __init__(self, app):
        """ Initialize routes with Flask app and dependencies.        
        - Args: 
          - app: Flask application instance for route registration """
        
        self.hostname = socket.gethostname()        
        self.app = app
        self.view = AppView()
        self._register_routes()


    def _register_routes(self):
        """ Register all application routes with Flask.
        Route Mappings:
            - '/' → rt_index (GET)
            - '/login' → rt_login (GET, POST) """
        
        self.app.add_url_rule('/', 'index', self.rt_index, methods=['GET'])
        self.app.add_url_rule('/login', 'rt_login', self.rt_login, methods=['GET', 'POST'])
        self.app.add_url_rule('/login', 'rt_login_get', self.rt_login, methods=['GET'])


    def rt_index(self):
        """ Handle home page requests (/).        
        Returns:
            str: Rendered HTML for the home page """
        
        return self.view.vw_login(self.hostname, 'Init')


    def rt_login(self):        
        """ Handle login page requests (/login) for GET and POST.
            - POST: Extracts user name from form data
            - GET: Extracts user name from URL parameters (optional)
        Returns:
            str: Rendered HTML for the login page """
        
        if request.method == 'POST':
            user = request.form['nm']        
        else:
            user = ""
            user_name = request.args.get('nm')
            if user_name is None:
                user_name = ""
            user = user_name + "(None POST)"        
            
        return self.view.vw_login(self.hostname, user)