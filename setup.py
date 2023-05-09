from setuptools import setup, find_packages

setup(name='raiderio',
      version='1.1',
      author='amas0',
      description='Python client library for raider.io\'s public API',
      packages=find_packages(),
      install_requires=[
            'requests'
      ])
