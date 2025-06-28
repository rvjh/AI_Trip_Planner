from setuptools import find_packages, setup # type: ignore
from typing import List

def get_requirements()->List[str]:
    """This function is used to get the list of required packages for the project."""
    requirements_list : List[str] = []
    
    try:
        with open("requirements.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print("The requirements.txt file is not found in the project directory.")

    return requirements_list

print(get_requirements())

setup(
    name='AI-TRAVEL_PLANNER',
    version='1.0.0',
    packages=find_packages(),
    install_requires=get_requirements(),
    author='Rohan',
    author_email='rohan@gmail.com',
)


