from setuptools import setup, find_packages

setup(name='mymodule_amoro23',
      description='My first module, it draws 10 random circles',
      url='https://github.com/amoro23',
      author='Alice Moro',
      author_email='a.moro23@campus.unimib.it',
      version='0.0.1',
      packages=find_packages(),
      install_requires=['numpy', 'matplotlib']) # 'random' is a built-in module, part of the Python Standard Library, so it doesn't need to be listed here