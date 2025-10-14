"""
Analytics service for tracking application metrics.

This module provides functionality for tracking and retrieving
application usage statistics such as hit counts.
"""

import time
import redis
import config.app_system as app_sys


class AnalyticsService:
    """ Service class for handling application analytics and metrics.    
    This class encapsulates all analytics-related functionality, providing a clean separation of concerns from routing logic."""
    

    def __init__(self):
        """ Initialize the analytics service. """
    
        self.redis_client = app_sys.get_redis_client()

    
    def get_hit_count(self, user=None):
        """ Get the hit count for the application, with retry logic for Redis connection failures.

        This function attempts to retrieve and increment the hit count stored in Redis.`1
        It implements retry logic to handle Redis connection failures, attempting up to 5 retries.
        On each failure, it waits for 0.5 seconds before retrying.
        If all retries fail or an unexpected exception occurs, it returns an error message.  """
        
        # Determine the Redis key based on user parameter
        key = 'hits' if user is None else f'hits:{user}'
        
        retries = 5
        while True:
            try:
                return self.redis_client.incr(key) # increment the counter for the key an return the new count value
            except redis.exceptions.ConnectionError as exc:
                if retries == 0:
                    print(f"Redis connection failed: {exc}")
                    return False
                retries -= 1
                time.sleep(0.5)
            except Exception as exc:
                print(f"Unexpected error in get_hit_count: {exc}")
                return False