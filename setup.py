import os
import io

from setuptools import setup, find_packages

def read(fname):
    with io.open(os.path.join(os.path.dirname(__file__), fname), encoding="utf-8") as f:
        return f.read()


setup(
    name="optimizer",
    version="0.0.1",
    author="Daan Scheepens, Johannes Stangl, Benedict Braunsfeld",
    email="b.braunsfeld@gmail.com",
    url="https://github.com/bbraunsfeld/Learning-automata",
    packages=find_packages("Learning automata to optimize complex functions/src"),
    scripts=[
        "src/scripts/opt_run",
    ],
    package_dir={"": "Learning automata to optimize complex functions/src"},
    python_requires=">=3.6",
    install_requires=[
        "numpy",
        "matplotlib",
        "sys",
    ],
    description="Optimizer - Learning automata for optimization of continuous complex functions",
    long_description="""
        This optimizer is the reproduction of the paper mentioned in the docs and is part of a project at the university""",
)
