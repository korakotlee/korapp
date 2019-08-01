import os
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, "README.rst")) as fid:
    README = fid.read()

setup(
    name='korapp',
    packages=['korapp'],  # this must be the same as the name above
    version='0.1.5',
    description='Python package to generate app from mind map',
    # long_description_content_type="text/markdown",
    long_description=README,
    author='Korakot Leemakdej',
    author_email='kleemakdej@gmail.com',
    url='https://github.com/korakotlee/korapp',
    keywords=['mind map', 'app generator'],  # arbitrary keywords
    install_requires=['untangle', 'stringcase', 'xmltodict', 'pyyaml', \
                      'Flask', 'markdown2'],
    license="MIT",
    package_data={'': ['*.css']},
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    entry_points={
        'console_scripts': [
            'korapp = korapp:cli'
        ]},
)
