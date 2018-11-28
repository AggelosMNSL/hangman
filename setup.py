import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


setup(
    name="hangman",
    version="0.1.0",
    url="https://github.com/name-placeholder/hangman",
    license='GPL-3.0',

    author="Ousoultzoglou Orestis",
    author_email="oorestis@csd.auth.gr",

    description="A simple hangman game functioning as hands-on introduction to Python",
    long_description=read("README.md"),

    packages=find_packages(exclude=('tests',)),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: GPL-3.0',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
    ],
)
