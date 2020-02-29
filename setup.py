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
    url="",
    packages=find_packages("src"),
    scripts=[
        "src/scripts/spk_ase.py",
        "src/scripts/spk_load.py",
        "src/scripts/spk_md.py",
        "src/scripts/spk_parse.py",
        "src/scripts/spk_run.py",
    ],
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=[
        "torch>=1.1",
        "numpy",
        "ase>=3.18",
        "h5py",
        "tensorboardX",
        "tqdm",
        "pyyaml",
    ],
    extras_require={"test": ["pytest", "sacred", "pytest-console-scripts"]},
    license="MIT",
    description="SchNetPack - Deep Neural Networks for Atomistic Systems",
    long_description="""
        SchNetPack aims to provide accessible atomistic neural networks that can be
        trained and applied out-of-the-box, while still being extensible to custom 
        atomistic architectures""",
)
