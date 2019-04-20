from setuptools import setup, find_packages

version = '0.0.1'
setup(
    name="movie_checker",
    version=version,
    packages=find_packages("."),
    package_dir={'movie_check': 'movie_check'},
    include_package_data=True,
    license='MIT License',
    description='Checks movie bookings in Python.',
    url='https://https://github.com/Rangeeshar/movie_checker',
    download_url="https://github.com/Rangeeshar/movie_checker/tarball/%s" % version,
    author='Rangeesh, SherwinJoel',
    author_email='rangees28@gmail.com, sherwinjoel@gmail.com',
    install_requires=[
    'urllib3',
    'telegram',
    'bs4',
    'requests',
    'lxml',
    'argparse',
    'python-telegram-bot'
    ],
    classifiers=[
        'Intended Audience :: Developers, Normal users',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

