from distutils.core import setup, Extension

ytn_yescrypt_module = Extension('ytn_yescrypt',
                            sources = ['yescrypt.c'],
                            extra_compile_args=['-march=native', '-funroll-loops', '-fomit-frame-pointer'],
                            include_dirs=['.'])

setup (name = 'ytn_yescrypt',
       version = '1.0',
       description = 'Bindings for yescrypt proof of work used by yenten',
       ext_modules = [ytn_yescrypt_module])
