import sys

if sys.version_info < (3, 8):
    raise RuntimeError('aminobots requires Python 3.8+')


from setuptools import setup, find_packages
import aminobots


with open('README.md') as readme, open('requirements.txt') as requirements:
    setup(
        name=aminobots.__title__,
        version=aminobots.__version__,
        description=aminobots.__description__,
        long_description=readme.read(),
        author=aminobots.__author__,
        author_email=aminobots.__author_email__,
        url=aminobots.__url__,
        download_url=None,
        packages=find_packages(),
        licence=aminobots.__licence__,
        long_description_content_type='text/markdown',
        keywords=[
            'amino',
            'aminobot',
            'async-amino',
            'async-aminobot',
            'async-bot',
            'async-chatbot',
            'bot',
            'chatbot',
            'python-aminobots',
            'python-bot',
            'ViktorSky'
        ],
        install_requires=requirements.read().split(),
        classifiers=[
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10"
        ]
    )
