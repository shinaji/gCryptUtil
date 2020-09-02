from setuptools import setup, find_packages
from gCryptUtil import __version__

REQUIRES = ["google-cloud-kms>=2.0.1"]
CLASSIFIERS = [
    "Intended Audience :: Developers",
    "Development Status :: 4 - Beta",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Operating System :: OS Independent",
    "Topic :: Software Development"]

setup(
    name='gCryptUtil',
    version=__version__,
    description='extended dictionary class',
    url='https://github.com/shinaji/gCryptUtil',
    author='shinaji',
    author_email='shina.synergy@gmail.com',
    license='MIT',
    keywords='',
    packages=find_packages(),
    install_requires=REQUIRES,
    classifiers=CLASSIFIERS,
)
