from distutils.core import setup, Extension

wavi_yescrypt_module = Extension('wavi_yescrypt',
                            sources = ['yescrypt.c'],
                            extra_compile_args=['-march=native', '-funroll-loops', '-fomit-frame-pointer'],
                            include_dirs=['.'])

setup (name = 'wavi_yescrypt',
       version = '1.0',
       description = 'Bindings for yescrypt proof of work used by yenten',
       ext_modules = [wavi_yescrypt_module])
