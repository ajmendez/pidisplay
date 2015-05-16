%module pidisplay

%{
#include <wiringPi.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <sys/sysinfo.h>
#include <unistd.h>
#include "PCD8544.h"
%}

%include "PCD8544.h"