from setuptools import setup, find_packages

setup(
    name="google-code-discovery",
    version="0.0.1",
    packages=find_packages(
        where="gcd"
    ),
    install_requires=[
        "requests",
        "lxml",
        "urllib3",
        "enum34;python_version<'3.4'"
    ],
    license="MIT",
    entry_points = {
        "console_scripts": [
            "gcd-find = gcd.user_interface.cli:main",
        ]
    }
)
