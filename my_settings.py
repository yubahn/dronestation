# ----- DB SERVER 연결 시작 -----
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dsdetection',
        'USER': 'nsquare',
        'PASSWORD': 'nsquare@123',
        'HOST': '121.156.13.63',
        'PORT': '7070',
    },
    'second_db': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DroneStation',
        'USER': 'nsquare',
        'PASSWORD': 'nsquare@123',
        'HOST': '121.156.13.63',
        'PORT': '7070',
    },
}

# ----- DB SERVER 연결 끝 -----