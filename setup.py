from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    """_summary_

    Args:
        file_path (str): _description_
        ('requirements.txt')

    Returns:
        List[str]: This function is going to return list of all the requirements.
    """
    final_requirement = []                      # Creating a empty list to store required package.
    with open (file_path) as file_obj:          # with open ("requirements.txt") as file_obj:
        requirements = file_obj.readlines()     # requirements = ["pandas\n","numpy\n",......,"-e .\n"]

        for word in requirements:               # for word in ["pandas\n","numpy\n",......,"-e .\n"]
            word = word.replace("\n","")        # "pandas\n".replace("\n","") ==> pandas ∴ word = pandas and and so on...
            final_requirement.append(word)      # final_requirement.append(pandas) and and so on...

        if "-e ." in final_requirement:         # if "-e ." in ["pandas","numpy",......,"-e ."]:
            final_requirement.remove("-e .")    # final_requirement.remove("-e .") 
        return final_requirement                # ["pandas","numpy",......,"seaborn"]

        
setup(
name  = "Delivery Time Prediction",
version = "0.0.1",
author = "Aakash Pal",
author_email = "aakashpal1198@gmail.com",
# find_packages will find all the __init__.py file inside all the folder and
# make that folder as package so that we can use that in our project.
packages = find_packages(),                              
install_requires = get_requirements('requirements.txt'), # ["pandas","numpy",......,"seaborn"]
)