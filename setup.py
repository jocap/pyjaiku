#!/usr/bin/env python
#encoding=utf-8
#from distutils.core import setup
from setuptools import setup, find_packages

setup(name="jaiku",
      version="1.0.0",
      description="Library for the Jaiku OAuth API.",
      author="John Ankarström",
      author_email="john.ankarstrom@gmail.com",
      url="http://github.com/jocap/pyjaiku",
      packages = find_packages(),
      install_requires = ['oauth2'],
      license = "MIT License",
      keywords="jaiku oauth",
      zip_safe = True)