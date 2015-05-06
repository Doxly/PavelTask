try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : 'Count all summands',
    'author' : 'Pichugin Viacheslav',
    'url' : 'URL to get it at.',
    'download_url' : 'Where to download it.',
    'author_email' : 'pva33@mail.ru',
    'version' : '0.1',
    'install_requeries' : ['nose'],
    'packages' : ['sumTask'],
    'scripts' : [],
    'name' : 'SumTask'
}

setup(**config)