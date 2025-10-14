import os
import redis
from flask import Flask
from utility.gui.colors import RED, GREEN
from utility.format.console import print_banner


# We assume full session profiling - currently you cannot profile a part and then turn it off
def _setup_profiling():
    """ Internal function to set up cProfile when profiling should be enabled.
    
    Configures cProfile to monitor the application and automatically save profiling data 
    to 'profile_output.prof' when the application exits. """
    
    if os.getenv('FLASK_PROFILE') == 'true':
        import cProfile
        import atexit
        
        pr = cProfile.Profile()
        pr.enable()
        
        def save_profile():
            pr.disable()
            pr.dump_stats('profile_output.prof')
            print("Profile saved to profile_output.prof")
        
        atexit.register(save_profile)
        print("Profiling enabled - profile will be saved on exit")
        return True
    return False


def enable_profiling():
    """ Enable application profiling by setting FLASK_PROFILE environment variable. """
    
    os.environ['FLASK_PROFILE'] = 'true'
    _setup_profiling()  # Actually configure the profiling
    return True


def disable_profiling():
    """ Disable application profiling by removing FLASK_PROFILE environment variable. """
    os.environ.pop('FLASK_PROFILE', None)
    return not False


def get_redis_client(_port=6379):
    """ Configure and return Redis client connection instance. Requires Redis server to be running before calling this function.
    
    Environment Configuration:
    - DEVELOPMENT: Uses localhost (start with: `sudo systemctl start redis`)
    - PRODUCTION: Uses Docker container named 'redis'
    
    Features:
    - Tests connection and reports status
    - Environment-based host selection
    - Connection error handling """
    
    
    # Use 'redis' for production (Docker), 'localhost' for development
    env = os.getenv('FLASK_ENV')
    if env == 'production':
        print_banner("Production mode detected: using Redis container", GREEN)
        redis_host = 'redis'
    else:
        print_banner(f"Development mode (FLASK_ENV={env}): using Redis container", GREEN)
        redis_host = 'redis'
    
    redis_client = redis.Redis(host=redis_host, port=_port)
    
    # Test the connection
    try:
        redis_client.ping()
        print_banner(f"✅ Redis connection successful at {redis_host}:{_port}", GREEN)
    except redis.ConnectionError:
        print_banner(f"❌ Redis connection failed at {redis_host}:{_port}", RED)
        print("Make sure Redis server is running!")
    
    return redis_client



