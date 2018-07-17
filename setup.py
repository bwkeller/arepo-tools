#!/usr/bin/env python
from distutils.core import setup

setup(
		name="arepo-tools",
		version='0.1',
		author='BW Keller',
		author_email='malzraa@gmail.com',
		url='https://github.com/bwkeller/arepo-tools',
                package_dir={'arepo_tools/':''},
		packages=['arepo_tools'],
		license='LICENCE.txt',
		long_description=open('README.md').read(),
		install_requires=[
			"Numpy >= 1.5.1"
			],
)
