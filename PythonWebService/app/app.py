import debugpy
import os
import time
import redis
import socket
# Imported the needed Flask modules
from flask import Flask, render_template, request, redirect, url_for


# Wanna use debug mode? can only be used in container is defined for debug, FLASK_ENV= development (see compose file)  
#debugMode = True;
#    
##def is_port_in_use(port):
#    import socket
#    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#        return s.connect_ex(('localhost', port)) == 0
# 
#if (os.getenv('FLASK_ENV') == 'development' and debugMode):
#    debug_port = 5670
#    
#if not is_port_in_use(debug_port):            
#    debugpy.listen(('127.0.0.1', debug_port)) 
#    debugpy.wait_for_client()               
#    debugpy.breakpoint()        
#    print(f"Debugger is active on port {debug_port}")
#else:        
#    print(f" Port {debug_port} is already in use, skipping debugpy setup.")


def setup_debugger(debug_port=5670):
    """
    Sets up debugpy if the container is in development mode.
    Returns True if the debugger was successfully activated, False otherwise.
    """
    debug_enabled = os.getenv('FLASK_ENV') == 'development'

    def is_port_in_use(port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('0.0.0.0', port)) == 0

    if not debug_enabled:
        print("Debug mode not enabled; running in production mode.")
        return False

    if is_port_in_use(debug_port):
        print(f"Port {debug_port} is already in use, skipping debugger setup.")
        return False

    # Start debugger
    debugpy.listen(('0.0.0.0', debug_port))
    print(f"Debugger is listening on port {debug_port}, waiting for client...")
    debugpy.wait_for_client()
    debugpy.breakpoint()
    print(f"Debugger successfully activated on port {debug_port}")
    return True

# Move to other file



debugger_active = setup_debugger(5670)
if debugger_active:
    print("DEBUGGER MODE ACTIVE: Developer can attach a client.")
else:
    print("Debugger not active; running normally.")


app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
             return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

#Excute this when root page is openend
@app.route("/")
def index():
    count = get_hit_count()
    hostname = socket.gethostname()
    return render_template('index.html', hostname=hostname, count=count)


#Excute this when login page  is opened(currently vi root forms)
@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return render_template('index.html', yourName=user, count=get_hit_count())        
    else:
        user = ""
        user_name = request.args.get('nm')
        if user_name is None:
            user_name = ""
        user = user_name + "(None POST)"        
        return render_template('index.html', yourName=user, count=get_hit_count())


# Main setup
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=debugger_active, use_reloader=False)   # Reload true in debug mode, monitors file in source(including sub direcoties) and reload the server
                                                            # so that changes are direct viewable for a developer without need to restart server manually (python concept feature)
                                                            # TURN OFF in Production.
# use_reloader=true may have the effect that application runs twice, once with the debugger setting and once without, also it
# has the result that one has to stop the debugger action twice. This is super annoying, so we turn it off here. 
# No Idea what the option true brings to the table beside this annoyance. (not handy for debugging)
