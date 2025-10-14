# Application Architecture

This document explains the core architecture of the Flask application and how the three main packages work together.

## Core Packages Overview

### 📁 `logic/` - Business Logic Layer

**Purpose**: Contains the core business logic and services that handle data processing and business rules.

- **Location**: `src/logic/`
- **Responsibility**: Data processing, external service integrations, business rules
- **Key Components**:
  - `services_redis/analytics.py` - Analytics service for tracking application metrics
  - Service classes that encapsulate business functionality
- **Dependencies**: Only depends on `config/` for system configuration

### 📁 `routes/` - Controller Layer

**Purpose**: Handles HTTP requests and coordinates between views and business logic.

- **Location**: `src/routes/`
- **Responsibility**: URL routing, request handling, HTTP method processing
- **Key Components**:
  - `app/routes.py` - Main route handlers using class-based organization
  - Route registration and URL mapping
- **Dependencies**: Imports from `view/` for rendering responses

### 📁 `view/` - Presentation Layer

**Purpose**: Manages the presentation logic and template rendering.

- **Location**: `src/view/`
- **Responsibility**: Template rendering, response formatting, UI logic
- **Key Components**:
  - `app_view.py` - View classes that handle template rendering
  - Data preparation for templates
- **Dependencies**: Imports from `logic/` to get business data

## Architecture Flow

```text
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Request   │───▶│   routes/   │───▶│    view/    │───▶│  Response   │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
                           │                   │
                           ▼                   ▼
                   ┌─────────────┐    ┌─────────────┐
                   │   logic/    │    │ Templates   │
                   │ (services)  │    │   HTML      │
                   └─────────────┘    └─────────────┘
```

## Dependency Flow

The application follows a clean unidirectional dependency pattern:

1. **`app.py`** → imports from `routes/` and `logic/`
2. **`routes/`** → imports from `view/`
3. **`view/`** → imports from `logic/`

This ensures:

- ✅ No circular dependencies
- ✅ Clear separation of concerns
- ✅ Easy testing and maintenance
- ✅ Scalable architecture

## Example Request Flow

1. **HTTP Request** arrives at Flask application
2. **Route Handler** (`routes/app/routes.py`) processes the request
3. **View Class** (`view/app_view.py`) is called to prepare the response
4. **Business Logic** (`logic/services_redis/analytics.py`) provides data
5. **Template** is rendered with the data
6. **HTTP Response** is returned to client

## Benefits of This Architecture

- **Modularity**: Each layer has a single responsibility
- **Testability**: Business logic is separated from web concerns
- **Maintainability**: Changes in one layer don't cascade to others
- **Scalability**: Easy to add new routes, views, or services
- **Clarity**: Clear distinction between web, business, and presentation logic

## File Organization Example

```text
src/
├── app.py                          # Main application entry point
├── routes/
│   └── app/
│       └── routes.py              # Route handlers (Controller)
├── view/
│   └── app_view.py                # View logic (Presentation)
└── logic/
    └── services_redis/
        └── analytics.py           # Business services (Logic)
```

This architecture follows established web application patterns and provides a solid foundation for growth and maintenance.

## Appendix: Project Folder Structure

```text
/home/nico/app/
├── app/                           # Additional app resources
│   └── static/
│       └── css/
├── src/                           # Main source code directory
│   ├── config/                    # Configuration management
│   ├── logic/                     # Business Logic Layer
│   │   └── services_redis/        # Redis-based services
│   ├── routes/                    # Controller Layer
│   │   └── app/                   # App-specific routes
│   ├── tests/                     # Test files
│   ├── utility/                   # Utility functions and helpers
│   │   ├── format/                # Formatting utilities
│   │   └── gui/                   # GUI utilities
│   └── view/                      # Presentation Layer
├── static/                        # Static web assets
│   ├── css/
│   └── images/
└── templates/                     # Jinja2 templates
```

### Key Directory Purposes

- **Root Level**: Documentation and configuration files
- **`src/`**: All source code organized by architectural layers
- **`static/`**: Web assets (CSS, images, JavaScript)
- **`templates/`**: HTML templates for rendering views
- **`app/`**: Additional application resources and assets
- **`__pycache__/`**: Python bytecode cache (auto-generated)

### Architectural Layers in Detail

1. **Entry Point**: `src/app.py` - Application bootstrap and configuration
2. **Configuration**: `src/config/` - System settings and environment setup
3. **Business Logic**: `src/logic/` - Core application logic and services
4. **Controllers**: `src/routes/` - HTTP request handling and routing
5. **Views**: `src/view/` - Presentation logic and template coordination
6. **Utilities**: `src/utility/` - Shared helper functions and tools
7. **Tests**: `src/tests/` - Application test suites