import pathlib

from setuptools import find_packages, setup

from qiwi import __version__

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='async-qiwi',
    version=__version__,
    description='Simple wrapper for QIWI Kassa',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/andrew000/async-qiwi',
    author='Andrew King',
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='async-qiwi async qiwi wrapper',
    packages=find_packages(where='qiwi'),
    python_requires='>=3.7, <4',
    install_requires=['aiohttp==3.7.*', 'pydantic==1.8.*'],
    project_urls={
        'Bug Reports': 'https://github.com/andrew000/async-qiwi/issues',
        # 'Funding': 'https://donate.pypi.org',
        # 'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': 'https://github.com/andrew000/async-qiwi',
    },

)
