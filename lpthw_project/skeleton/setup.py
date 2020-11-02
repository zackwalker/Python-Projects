try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
'description':'my project',
'author':'Zack',
'url':'none',
'download_url':'',
'author_email':'',
'version':'',
'install_requires':['nose'],
'packages':['flaskProject'], 
'scripts':'',
'names':'',
}

setup(**config)