from setuptools import setup, find_packages

_deps = [
    "pydantic>=1.8.0"
]

setup(
    name="atakcots",
    version="1.0",
    author="Kyle Sayers",
    description="",
    install_requires=_deps,
    package_dir={"": "src"},
    packages=find_packages("src", include=["atakcots"], exclude=["*.__pycache__.*"])
)
