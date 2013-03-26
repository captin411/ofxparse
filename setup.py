from setuptools import setup, find_packages

# Read the version from __init__ to avoid importing ofxparse while installing.
# This lets the install work when the user does not have BeautifulSoup
# installed.
import re
VERSION = re.search(r"__version__ = '(.*?)'",
                    open("ofxparse/__init__.py").read()).group(1)


setup(name='ofxparse',
      version=VERSION,
      description=("Tools for working with the OFX (Open Financial Exchange)"
                   " file format"),
      long_description=open("./README", "r").read(),
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: Utilities",
          "License :: OSI Approved :: MIT License",
      ],
      keywords='ofx, Open Financial Exchange, file formats',
      author='Jerry Seutter',
      author_email='jseutter.ofxparse@gmail.com',
      url='http://sites.google.com/site/ofxparse',
      license='MIT License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
          "BeautifulSoup>=3.0",
      ],
      entry_points="""
      """,
      use_2to3=True,
      test_suite='tests',
      )
