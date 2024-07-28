from setuptools import find_packages,setup
from typing import List

def find_req()->List[str]:
    with open('requirements.txt','r') as req:
        req=req.readlines()
    req=[r.replace('\n','') for r in req]
    req.remove('-e .')
    return req


setup(
    name="completeml",
    version='0.0.1',
    author='Sivasuthan S',
    author_email='sivasuthansukumar@gmail.com',
    packages=find_packages(),
    requires=find_req(),
)