from setuptools import setup, find_packages

setup(
	name = 'AlphabetPy',
	version = '1.0',
	packages = find_packages(),
	license = 'MIT',
	author = 'Ray Zhao',
	author_email = 'rayzhao98@163.com',
	url = 'https://github.com/RayZhao1998/alphabetPy',
	description = 'A python tool to output characters in console/shell',
	
	entry_points = {
		'console_scripts': [
		    'alphabetPy = AlphabetPy:start'
		],
	}
)