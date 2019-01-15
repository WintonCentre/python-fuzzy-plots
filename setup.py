from distutils.core import setup
# from setuptools import setup

long_description = '''Fan charts and their variations explored by the Winton Centre for Risk and Evidence Communication.
 Similar to fan chart by Office for National Statistics. See doc at https://github.com/WintonCentre/python-fuzzy-plots
 '''

setup(
      name='fuzzy-plotly',
      version='1.0.1',
      description='Fan chart and various other uncertainty charts.',
      long_description=long_description,
      url='https://github.com/WintonCentre/python-fuzzy-plots',
      author='Jin Park',
      author_email='jp835@cam.ac.uk',
      license='MIT',
      packages=['fuzzy'],
      install_requires=['plotly', 'scipy'],
      zip_safe=True
)
