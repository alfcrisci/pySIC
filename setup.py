from distutils.core import setup
setup(name='pySIC',
      version='1.2',
      description='Python Simple Image Cropper',
      author='David Risaliti',
      author_email='davdag24@gmail.com',
      url='',
      license='MIT',
      py_modules=['pySIC','reader','cropper','maker','merger'],  
      package_data={
      'pySIC.fonts': ['*'],
      }
     )
