from setuptools import setup, find_namespace_packages

with open("requirements.txt", "r") as file:
    requirements = [
        line
        for line in file.read().splitlines()
        if line or not line.startswith("#")
    ]


setup(
    name="financetoolbox",
    version="0.1.0",
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
