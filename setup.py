from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
    name='atzlib',
    version='0.0.1',
    description='Bunch of small python tools.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    
    author='jhlee29',
    author_email='leejinha829@gmail.com',
    url='https://github.com/xinagand/atzlib.git',
    keywords=['jhlee29', 'python'],
    
    install_requires=[],
    packages=find_packages(exclude=[]),
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)