# ----- DB SERVER 연결 시작 -----
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dsdetection',
        'USER': 'nsquare',
        'PASSWORD': 'nsquare@123',
        'HOST': '121.156.13.63',
        'PORT': '7070',
        #'read_default_file': '/path/to/my.cnf',
    }
}

# ----- DB SERVER 연결 끝 -----