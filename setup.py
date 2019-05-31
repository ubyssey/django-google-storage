# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='django-google-storage-updated',
    version='0.5.3',
    packages=['django_google_storage', ],
    author='Maxim Smirnoff',
    author_email='smirnoffmg@gmail.com',
    url='https://github.com/budurli/django-google-storage',
    license='LICENSE.txt',
    description='Django storage for Google Storage',
    install_requires=[
        "boto",
    ],
)
