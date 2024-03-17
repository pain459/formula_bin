from setuptools import find_packages, setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='formula_bin',
    packages=find_packages(include=['formulas']),
    # packages=find_packages(),
    version='0.1.0',
    package_data={'formula-bin': ['formulas/basic']},
    description='Formula implementations in Python',
    author='Pain',
    install_requires=requirements,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)