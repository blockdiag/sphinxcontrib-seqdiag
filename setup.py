# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

requires = ['blockdiag>=1.5.0', 'seqdiag>=0.9.3', 'Sphinx>=0.6']

setup(
    name='sphinxcontrib-seqdiag',
    version='0.8.5',
    url='http://github.com/blockdiag/sphinxcontrib-seqdiag',
    license='BSD',
    author='Takeshi KOMIYA',
    author_email='i.tkomiya@gmail.com',
    description='Sphinx "seqdiag" extension',
    long_description=open('README.rst').read(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
