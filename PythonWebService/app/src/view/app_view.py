"""
View layer for the Flask application.

This module handles the presentation logic and template rendering.
Views are responsible for preparing data and rendering HTML templates
in response to route handler requests.

"""

from flask import render_template
from logic.services_redis import analytics
import socket


class AppView:
    """
    Handles presentation logic and template rendering.
    
    This class acts as the View layer in the application architecture,
    responsible for:
    - Preparing data for template rendering
    - Calling Flask's render_template function
    - Coordinating with business logic services
    
    Naming Convention:
    - View methods use 'vw_' prefix (e.g., vw_login)
    - Corresponding route methods use 'rt_' prefix (e.g., rt_login)
    - This creates a clear mapping between routes and views
    
    """
    
    
    def __init__(self):
        """
        Initialize the AppView with required services.        
        - Sets up analytics service for tracking application metrics.
        
        """
        
        self.analytics_service = analytics.AnalyticsService()


    def vw_login(self, hostname, yourName):
        """
        Render the login/home page template.
        - Coordinates with analytics service to get hit count and renders the index.html template with the provided data.
        
        Args:
            hostname (str): Server hostname to display
            yourName (str): User name or identifier to display
            
        Returns:
            str: Rendered HTML content from index.html template
            
        """
        
        count_general = self.analytics_service.get_hit_count()
        count_user = self.analytics_service.get_hit_count(yourName)
        return render_template('index.html', hostname=hostname, count_general=count_general, count_user=count_user,yourName=yourName)
