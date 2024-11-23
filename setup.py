from setuptools import find_packages,setup
from typing import List

hypen_e_dot='-e .'
def get_requirements(file_path:str)->List[str]:

    '''
    this function will return the list of all requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
        
    return requirements

setup(
    name='End to End ML project',
    version='1.0',
    author='Anindya Banerjee',
    author_email='anindya.banerjee@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)