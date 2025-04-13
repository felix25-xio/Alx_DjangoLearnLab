# In settings.py
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'templates'],
    },
]