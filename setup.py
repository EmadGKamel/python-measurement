import multiprocessing

from setuptools import setup, find_packages

requirements = []
with open('requirements.txt', 'r') as in_:
    requirements = in_.readlines()

setup(
    name='measurement',
    version='0.0.1',
    url='http://bitbucket.org/latestrevision/python-measurement/',
    description='Easily use and manipulate unit-aware measurements in Python',
    author='Adam Coddington',
    author_email='me@adamcoddington.net',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages=find_packages(),
    install_requires=requirements,
    test_suite='nose.collector',
    tests_require=[
        'mimic',
        'nose',
    ]
)