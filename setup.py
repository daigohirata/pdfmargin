from setuptools import setup, find_packages

setup(
    name='pdfmargin',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'pypdf>=3.0.0',
    ],
    entry_points={
        'console_scripts': [
            'pdfmargin=pdfmargin.cli:main',  # ← pdfmargin コマンドで main() 実行
        ],
    },
    author='Daigo Hirata',
    description='CLI tool to add margins to PDF files',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
