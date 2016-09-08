from setuptools import setup

setup(name='hotrepos',
      version='0.1',
      description='Periodically share links of hot GitHub repositories on FB',
      url='http://github.com/parkjs814/hotrepos',
      author='Jason Park',
      author_email='parkjs814@gmail.com',
      license='MIT',
      packages=['hotrepos'],
      install_requires=[
          'schedule',
          'requests',
          'records',
          'facebook-sdk'
      ])
