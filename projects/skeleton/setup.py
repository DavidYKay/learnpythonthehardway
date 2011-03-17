try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = {
    'description': 'My Project',
    'author': 'David Kay',
    'url': 'http://project.com',
    'download_url': 'http://project.com/download',
    'author_email': 'davidykay@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname',
}

setup(**config)
