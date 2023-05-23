from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A Diamond price prediction package'
LONG_DESCRIPTION = 'A Machine Learning Project that takes diamond price data from online and predicts what price is going to be'

HYPHEN_E = '-e .'
def requiredPacks(file_path:str):
    requirement_list = []
    with open(file_path, 'r') as file:
        line = file.readline()
        while line:
            requirement_list.append(line.replace('\n', ''))
            line = file.readline()
            if line == HYPHEN_E:
                return requirement_list
setup (
    name = 'venv',
    version = VERSION,s
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    author = 'Dhrumil V.',
    author_email = "__None__",
    license = 'DIT',
    packages = find_packages(),
    install_requires = requiredPacks('requirements.txt'),
    keywords = 'conversion'
)
    
