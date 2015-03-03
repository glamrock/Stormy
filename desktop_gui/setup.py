from setuptools import setup, find_packages

setup(	
	
    # Application name:
    name="Stormy",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="stormy author",
    author_email="author@stormy.com",
    
    scripts = ["StormyApps"], # scrypt for first call on this apps

    # Packages
    packages=find_packages(),

    include_package_data=True,
    package_data={'Stormy': ['Stormy/assets/how_to/*'], 'Stormy': ['Stormy/assets/images/*'], 'Stormy': ['Stormy/assets/shell_script/installer/*'], 'Stormy': ['Stormy/assets/shell_script/visit_service/*']},

    # Details
    url="http://pypi.python.org/pypi/Stormy/",

    # license="LICENSE.txt",
    description="Stormy software installer.",

    # long_description=open("README.txt").read(),

    )
