from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='python_optional',
    packages=['python_optional'],
    version='1.0.0',
    license='MIT',
    description='Returns None if a dict key does not exist',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Roger Vilà',
    author_email='rogervila@me.com',
    url='https://github.com/rogervila/python_optional',
    download_url='https://github.com/rogervila/python_optional/archive/1.0.0.tar.gz',
    keywords=['optional dict key', 'catch keyerror'],
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
)
