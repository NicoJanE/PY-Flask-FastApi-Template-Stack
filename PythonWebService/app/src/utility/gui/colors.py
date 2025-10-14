"""
ANSI color codes for console output formatting.

This module provides standardized color constants for consistent
terminal output formatting across the application.
"""

# Text colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'

# Text styles
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
REVERSE = '\033[7m'

# Background colors
BG_RED = '\033[41m'
BG_GREEN = '\033[42m'
BG_YELLOW = '\033[43m'
BG_BLUE = '\033[44m'

# Reset formatting
RESET = '\033[0m'

# Convenience functions
def colored(text, color=None, bg_color=None, style=None):
    """
    Apply color and style formatting to text.
    
    Args:
        text (str): Text to format
        color (str): Text color code
        bg_color (str): Background color code
        style (str): Style code (bold, underline, etc.)
    
    Returns:
        str: Formatted text with ANSI codes
    """
    formatted = ""
    if style:
        formatted += style
    if bg_color:
        formatted += bg_color
    if color:
        formatted += color
    formatted += text + RESET
    return formatted