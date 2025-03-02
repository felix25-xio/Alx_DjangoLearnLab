import os
from django.core.exceptions import ImproperlyConfigured

# 1. Set DEBUG to False in Production
DEBUG = False

# 2. Allow only specific hosts
ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com']

# 3. Secure Browser Settings
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True

# 4. Enable HTTPS Settings
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# 5. Content Security Policy (Optional, requires django-csp)
CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'", 'https://trusted.cdn.com')
CSP_STYLE_SRC = ("'self'", 'https://trusted.cdn.com')
CSP_IMG_SRC = ("'self'", 'https://trusted.cdn.com')

# 6. Secure Secret Key Management
def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = f"Set the {var_name} environment variable"
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_env_variable('DJANGO_SECRET_KEY')
