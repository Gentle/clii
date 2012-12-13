from setuptools import setup, find_packages

setup(
    name='clii',
    version='0.1',
    url='https://github.com/Gentle/clii',
    author='Ramon Klass',
    author_email='tier@schokokeks.org',
    description='commandline helper utilities',
    packages=find_packages(),
    install_requires=[
        'pytest',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
