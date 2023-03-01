from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

if __name__ == "__main__":
    setup(
        packages=find_packages(),
        long_description=long_description,
        entry_points={
            'console_scripts': [
                'kiwi-gen = scripts.gen:main',
            ],
        }
    )
