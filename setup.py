# coding: utf-8

from setuptools import setup, find_packages


with open('README.md') as f:
    long_description = f.read()

setup(name='full stack python',
      description='Full Stack Python Project',
      long_description=long_description,
      author='Paulo Pinto',
      author_email='pmsppinto@me.com',
      packages=find_packages(),
      install_requires=['celery', 'redis']
      )
