try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'minimalist CLI to parse email addresses from command line',
    'author': 'Austin Ogilvie',
    'keywords': 'parse email addresses',
    'url': '',
    'download_url': '',
    'author_email': 'a@yhathq.com',
    'version': '0.1',
    'install_requires': ['nose', 'docopt', 'flanker'],
    'packages': ['addrparse'],
    'include_package_data': True,
    'scripts': ['bin/cli.py'],
    'entry_points': {'console_scripts':  ['addrparse=addrparse.bin.cli:main']}
    'zip_safe': False,
    'name': 'addrparse',
    'license': 'MIT'
}

setup(**config)
