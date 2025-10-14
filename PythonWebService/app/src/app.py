
"""
Flask + FastAPI Template

Quick Start: Flask/Jinja2 + FastAPI template for beginners and returning users.
Topics: Jinja2, Flask, FastAPI fundamentals.
More detailed documentation: See README.md for detailed examples and explanations.
"""

import os
import time
import redis
import socket

# Imported the needed Flask modules
from flask import Flask, render_template, request, redirect, url_for


# For import mechanisms see GUIDE.md (section 4.1 Imports)
import config.app_system as app_sys
from routes.app.routes import AppRoutes
from logic.services_redis.analytics import AnalyticsService

global_app = None
global_route_app = None

# Define Flask and make sure Flask sees the static and templates folder
def _define_app():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    app_root = os.path.dirname(current_dir)    
    app = Flask(__name__, template_folder=os.path.join(app_root, 'templates'), static_folder=os.path.join(app_root, 'static'))    
    
    # Important! initializes the AppRoutes class with the Flask app instance (variable is intentionally unused)
    _global_route_app = AppRoutes(app)
    return app


# Define global objects  
global_app = _define_app()                  # Get the Flask app instance from the config module (module-level global)


# Main entry point
# ---------------------------------------------------------------------------------------------------------------------------------------- 
#
if __name__ == "__main__":    
    # app_sys.enable_profiling()            # set this to profile
    
    global_app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=False)
    # Reload true in debug mode, monitors file in source(including sub direcoties) and reload the server
    # so that changes are direct viewable for a developer without need to restart server manually (python concept feature)
    #   -   TURN OFF in Production.
    #   -   use_reloader=true may have the effect that application runs twice, once with the debugger setting and once without, also it
    #       has the result that one has to stop the debugger action twice. This is super annoying, so we turn it off here. 


# On host: http://localhost:5070/ (Default)

# Example Backup to host( The: T make sure everything is overriden, remove it if you don't want it!):
# from: /home/nico
# cp -rT ./app  /mnt/c/temp/app_new
