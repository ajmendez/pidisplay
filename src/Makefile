# SWIG_FEATURES='-L/usr/local/lib -lwiringPi'
all:
	swig -c++ -python -o pidisplay_swig.cc pidisplay_swig.i
	python setup.py build_ext --inplace