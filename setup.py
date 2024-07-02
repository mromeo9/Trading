from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path:str)->List:

    requirements = []
    with open(file_path) as obj:
        requirements = obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]
        
        if '-e .' in requirements:
            requirements.remove('-e .')

setup(
    name='Trading_bot',
    version='0.1',
    author='Michael Romeo',
    author_email='romeo-michael@outlook.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)