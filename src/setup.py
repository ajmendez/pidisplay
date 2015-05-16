from distutils.core import setup, Extension

extension_mod = Extension("_pidisplay", ["pidisplay_swig.cc", "PCD8544.c"],
                          extra_link_args=['-I', '.'],
                          extra_compile_args=['-lwiringPi', '-L/usr/local/lib'])

setup(name="pidisplay", 
      include_dirs=['.'],
      ext_modules=[extension_mod])
      
#https://scipy-lectures.github.io/advanced/interfacing_with_c/interfacing_with_c.html

# gcc -pthread -fno-strict-aliasing -lwiringPi -L/usr/local/lib -fPIC -I/usr/include/python2.7 -c PCD8544.c -o build/temp.linux-armv6l-2.7/PCD8544.o -lwiringPi -L/usr/local/lib -Wno-strict-prototypes
# gcc -pthread -fno-strict-aliasing -lwiringPi -L/usr/local/lib -fPIC -I/usr/include/python2.7 -c pidisplay_swig.c -o build/temp.linux-armv6l-2.7/pidisplay_swig.o -lwiringPi -L/usr/local/lib -Wno-strict-prototypes
# gcc -pthread -O2 -fPIC -I/usr/include/python2.7 -c PCD8544.c -lwiringPi -L/usr/local/lib
# gcc -pthread -O2 -fPIC -I/usr/include/python2.7 -c pidisplay_swig.cc -lwiringPi -L/usr/local/lib
# gcc -pthread -g -fwrapv -shared PCD8544.o pidisplay_swig.o -lwiringPi -L/usr/local/lib -o _pidisplay.so
#
#
#
# gcc -pthread -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes
# -fPIC -I/usr/include/python2.7 -c pidisplay_swig.cc -o build/temp.linux-armv6l-2.7/pidisplay_swig.o
# -lwiringPi -L/usr/local/lib
