from setuptools import setup, find_packages

try:
    import pypandoc

    long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

if __name__ == "__main__":
    setup(
        package_dir={"": "kiwi"},
        packages=find_packages(where='kiwi'),
        include_package_data=True,
        long_description=long_description,
    )
