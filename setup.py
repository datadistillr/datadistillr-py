from distutils.core import setup
setup(
  name = 'datadistillr-py',         # How you named your package folder (MyLib)
  packages = ['datadistillr-py'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='apache-2.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Be able to easily use Datadistillr from Python',   # Give a short description about your library
  author = 'Forrest Rogers',                   # Type in your name
  author_email = 'forrest@datadistillr.com',      # Type in your E-Mail
  url = 'https://github.com/datadistillr/datadistillr-py',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/datadistillr/datadistillr-py/archive/refs/tags/v_01.tar.gz',    # I explain this later on
  keywords = ['Datadistillr', 'Database', 'Data'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests',
          'http.cookiejar',
          'json',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: Apache License 2.0  ',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
