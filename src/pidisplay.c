/*
pidisplay
*/


#include <python.h>
#include <wiringPi.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <sys/sysinfo.h>
#include "PCD8544.h"
#include <unistd.h>


// pin setup
int _din = 1;
int _sclk = 0;
int _dc = 2;
int _rst = 4;
int _cs = 3;


static PyObject * setup(PyObject * self, PyObject * args) {
    char * input;
    
}
