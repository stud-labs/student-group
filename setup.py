# This is your "setup.py" file.
# See the following sites for general guide to Python packaging:
#   * `The Hitchhiker's Guide to Packaging <http://guide.python-distribute.org/>`_
#   * `Python Project Howto <http://infinitemonkeycorps.net/docs/pph/>`_

from setuptools import setup, find_packages
import sys, os
#from Cython.Build import cythonize
from setuptools.extension import Extension

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.rst')).read()

version = '0.2'

requires = [
    'plaster_pastedeploy',
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'waitress',
    'cornice',
]

tests_require = [
    'WebTest',
    'pytest',
    'pytest-cov',
]

print(":::::", find_packages("src"))

setup(
    name='studentgroup',
    version=version,
    description="python REST mongodb",
    long_description=README + '\n\n' + NEWS,
    keywords='python REST mongodb pyramid pylons',
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='Evgeny Cherkashin',
    author_email='eugeneai@irnok.net',
    url='',
    license='GPLv3.0',
    # packages=find_packages("src"),
    packages=['studentgroup', 'studentgroup.serv'],
    package_dir={'': "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    extras_require={
        'testing': tests_require,
    },
    entry_points={
        'paste.app_factory': ['main = studentgroup:main'],
        'console_scripts': ['student-group=studentgroup:main']
    },
)
