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
        maintainer=aminobots.__author__,
        maintainer_email=aminobots.__author_email__,
        url=aminobots.__url__,
        packages=find_packages(),
        licence=aminobots.__license__,
        long_description_content_type='text/markdown',
        keywords=[
            'async',
            'amino',
            'bot',
            'aminobots',
            'python-aminobots',
            'ViktorSky'
        ],
        install_requires=requirements.read().split(),
        classifiers=[
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11'
        ],
        python_requires='>=3.10',
        package_data={'aminobots': ['py.typed']},
    )
