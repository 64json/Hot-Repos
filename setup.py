from setuptools import setup
from setuptools.command.install import install


def _post_install():
    from hotrepos.db import create_table
    create_table()


class CustomInstallCommand(install):
    def run(self):
        install.run(self)
        self.execute(_post_install, ())


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
      ],
      cmdclass={
          'install': CustomInstallCommand,
      })
