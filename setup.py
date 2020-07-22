from setuptools import setup, find_packages

setup(name='talert',
		version='0.1.1',
		description='Telegram bot for workalert',
		author='Junghoon Jung',
		author_email='jh.jung@uos.ac.kr',
		packages=find_packages(),
		setup_requires=['python-telegram-bot'],
		install_requires=['python-telegram-bot','ipykernel']
	 )
