from distutils.core import setup
# from setuptools import setup

setup(
      name='fuzzy',
      version='0.1',
      description='Fuzzy plot for uncertainty',
      url='https://github.com/WintonCentre/python-fuzzy-plots',
      author='Jin Park',
      author_email='jp835@cam.ac.uk',
      license='MIT',
      packages=['fuzzy', 'plotly', 'scipy'],
      zip_safe=True
)
