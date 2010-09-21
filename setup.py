from setuptools import setup, find_packages

version = '2.0'

setup(name='optilux.codeexamples',
      version=version,
      description="Zope code examples",
      long_description=open("README.txt").read() + "\n",
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Martin Aspeli',
      author_email='optilude@gmail.com',
      url='http://optilux-cinemas.com',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['optilux'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
      ],
      extras_require={
          'test': ['plone.app.testing',]
      },
      )
