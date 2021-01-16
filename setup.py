from setuptools import setup

setup(
    name='typarse',
    version='0.0.1',
    packages=[''],
    url='https://redtachyon.me',
    license='GNU GPLv3',
    author='redtachyon',
    author_email='ariel.j.kwiatkowski@gmail.com',
    description='A simple type-hint-based argument parsing library',
    extras_require={
        "tests": [
            "pytest",
        ]
    }
)
