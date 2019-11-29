#!/usr/bin/env python

from setuptools import setup
from setuptools.command.install import install as _install

class install(_install):
    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()

if __name__ == '__main__':
    setup(
        name = 'MyAPIProject',
        version = '1.0',
        description = 'Example PyBuilder / Git project',
        long_description = ' This WebService is responsible for returning filtered quotes by movie and character fields ',
        author = 'Uday Vakalapudi',
        author_email = 'uday.vakalapudi@gmail.com',
        license = 'None',
        url = 'https://github.com/Udayaprasad/MyAPIProject',
        scripts = [],
        packages = [],
        namespace_packages = [],
        py_modules = [
            'WebServiceExercise',
            'response_data'
        ],
        classifiers = [
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python'
        ],
        entry_points = {},
        data_files = [],
        package_data = {},
        install_requires = [
            'Flask==1.1.1',
            'configparser==4.0.2',
            'parameterized==0.7.1',
            'requests==2.22.0',
            'urllib3==1.25.7'
        ],
        dependency_links = [],
        zip_safe = True,
        cmdclass = {'install': install},
        keywords = '',
        python_requires = '<3.7,>=2.7',
        obsoletes = [],
    )
