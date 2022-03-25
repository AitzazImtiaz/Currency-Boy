from setuptools import setup

setup(
    name = "currencyboy",
    version = "0.1.0",
    description = "A good version for Economists people",
    author = "AitzazImtiaz",
    url = "https://github.com/AitzazImtiaz/Currency-Boy",
    packages = ["currencyboy"],
    entry_points = {
        'console_scripts': [
            'currencyboy = currencyboy.__main__:main'
        ]
    },
)
