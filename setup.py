from setuptools import setup, find_packages

setup(
    name="google_code_discovery",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        'requests',
        'html5lib'
    ],
    license="MIT",
    entry_points = {
        "console_scripts": [
            "gcd-find = gcd.user_interface.cli:main",
        ]
    }
)
