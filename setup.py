#!/usr/bin/python3
from setuptools import setup

setup(name='uneye',
      version='0.1',
      packages=['uneye'],
      install_requires=["scikit-image",
                        "torch",
                        "numpy",
                        "scipy",
                        "scikit-learn",
                        "matplotlib",
                       ],
      include_package_data=True
)
