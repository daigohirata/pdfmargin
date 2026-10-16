from setuptools import setup

setup(
    name='pdfdm',
    version='0.0.0',
    packages=['pdfdm'],
    install_requires=[
        'pypdf>=3.0.0',
    ],
    entry_points={
        'console_scripts': [
            'pdfmargin=pdfdm.pdfmargin:main',
            'pdfdivide=pdfdm.pdfdivide:main',
        ],
    },
    author='Daigo Hirata',
    description='PDF margin and division command-line tools',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
