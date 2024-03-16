from setuptools import find_packages, setup

setup(
    name='formula_bin',
    packages=find_packages(include=['formulas']),
    version='0.1.0',
    description='Formula implementations in Python',
    author='Me',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)