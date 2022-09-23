import os
from setuptools import setup, find_namespace_packages

with open("requirements.txt", "r") as file:
    requirements = [
        line
        for line in file.read().splitlines()
        if line or not line.startswith("#")
    ]

with open(os.path.join("src", "financetoolbox", "VERSION"), "r") as file:
    version = file.read().strip()


setup(
    name="financetoolbox",
    version=version,
    description="Financial Toolbox",
    author="Rodrigo H. Mota",
    author_email="contact@rhdzmota.com",
    install_requires=requirements,
    packages=find_namespace_packages(where="src"),
    package_dir={
        "": "src"
    },
    scripts=[
        "bin/financetoolbox"
    ],
)
