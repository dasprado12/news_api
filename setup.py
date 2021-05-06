from setuptools import setup
import io
from setuptools import setup, find_packages
import io
import re


with io.open('README.md', encoding='utf8') as readme:
    long_description = readme.read()


setup(
    name='app',
    description='Teste',
    author='Daniel Prado',
    install_requires=[  "flask", 'uwsgi', 'requests', 'pandas', 'bs4', 'selenium', \
                        "cchardet", "feedparser", "nltk", "flask-cors" ],
    setup_requires=['pytest-runner'],
    entry_points={
        'console_scripts': [
            'app = app.__main__:start_server',
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.7',
    ],
    tests_require=['pytest']
)
