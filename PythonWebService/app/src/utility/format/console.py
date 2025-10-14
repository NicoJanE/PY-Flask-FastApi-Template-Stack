"""
Console formatting utilities for enhanced terminal output.

This module provides functions for formatting console output with colors,
borders, and spacing to improve readability and visual impact.
"""

from utility.gui.colors import RESET


def print_banner(message, color, width=80, border_char="="):
    """
    Print a prominently displayed banner message with borders and color.
    
    Args:
        message (str): The message to display
        color (str): ANSI color code for the banner
        width (int): Terminal width for the banner (default: 80)
        border_char (str): Character to use for borders (default: "=")
    
    Example:
        print_banner("Server starting", GREEN)
        print_banner("Warning!", YELLOW, border_char="-")
    """
    border = border_char * width
    centered_message = message.center(width)
    
    print(f"\n\n{color}{border}")
    print(centered_message)
    print(f"{border}{RESET}\n\n")


def print_status(message, color):
    """
    Print a simple colored status message.
    
    Args:
        message (str): The status message
        color (str): ANSI color code
    """
    print(f"{color}{message}{RESET}")


def print_section_header(title, color, width=60):
    """
    Print a section header with underline formatting.
    
    Args:
        title (str): Section title
        color (str): ANSI color code
        width (int): Width of the underline
    """
    underline = "-" * len(title)
    print(f"\n{color}{title}")
    print(f"{underline}{RESET}\n")