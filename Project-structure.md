CV_Maker/           # Root directory for the project
├── .env            # Environment variables file (for sensitive data)
├── .gitignore      # Specifies files and directories Git should ignore
├── README.md       # Project documentation
├── manage.py       # Django’s command-line utility
├── requirements.txt# List of dependencies for the project
├── config/         # Main configuration for the Django project
│   ├── __init__.py
│   ├── asgi.py     # ASGI entry point for asynchronous capabilities
│   ├── settings.py # Base settings for the project
│   ├── urls.py     # Main URL routing for the project
│   └── wsgi.py     # WSGI entry point for deployment
├── apps/           # Custom applications directory
│   ├── accounts/   # User management app
│   │   ├── migrations/
│   │   ├── templates/accounts/ # Account-related templates (e.g., login, signup)
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py     # URLs for accounts app
│   │   └── views.py
│   ├── profiles/   # Profile and user data management app
│   │   ├── migrations/
│   │   ├── templates/profiles/ # Profile-related templates
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py     # URLs for profiles app
│   │   └── views.py
│   ├── cv/         # CV generation and management app
│   │   ├── migrations/
│   │   ├── templates/cv/       # CV templates for preview and download
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── pdf_utils.py  # Helper functions for PDF generation
│   │   ├── tests.py
│   │   ├── urls.py       # URLs for CV app
│   │   └── views.py
├── static/         # Static files (CSS, JavaScript, images)
│   ├── css/
│   ├── js/
│   └── images/
└── templates/      # Global templates directory (e.g., base.html)
    ├── base.html   # Base template for extending other templates
    └── 404.html    # Custom 404 error page

