from distutils.core import setup, Extension

setup(name='idlememstat',
      description='Idle memory tracker',
      version='1.0',
      license='GPLv2',
      packages=['idlememstat'],
      ext_modules=[Extension('idlememstat.kpageutil',
                             ['idlememstat/kpageutil.cpp'],
                             extra_compile_args=['-std=c++11'])],
      scripts=['bin/idlememstat'],
      )
