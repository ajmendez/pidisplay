# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pidisplay', [dirname(__file__)])
        except ImportError:
            import _pidisplay
            return _pidisplay
        if fp is not None:
            try:
                _mod = imp.load_module('_pidisplay', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pidisplay = swig_import_helper()
    del swig_import_helper
else:
    import _pidisplay
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


BLACK = _pidisplay.BLACK
WHITE = _pidisplay.WHITE
LCDWIDTH = _pidisplay.LCDWIDTH
LCDHEIGHT = _pidisplay.LCDHEIGHT
PCD8544_POWERDOWN = _pidisplay.PCD8544_POWERDOWN
PCD8544_ENTRYMODE = _pidisplay.PCD8544_ENTRYMODE
PCD8544_EXTENDEDINSTRUCTION = _pidisplay.PCD8544_EXTENDEDINSTRUCTION
PCD8544_DISPLAYBLANK = _pidisplay.PCD8544_DISPLAYBLANK
PCD8544_DISPLAYNORMAL = _pidisplay.PCD8544_DISPLAYNORMAL
PCD8544_DISPLAYALLON = _pidisplay.PCD8544_DISPLAYALLON
PCD8544_DISPLAYINVERTED = _pidisplay.PCD8544_DISPLAYINVERTED
PCD8544_FUNCTIONSET = _pidisplay.PCD8544_FUNCTIONSET
PCD8544_DISPLAYCONTROL = _pidisplay.PCD8544_DISPLAYCONTROL
PCD8544_SETYADDR = _pidisplay.PCD8544_SETYADDR
PCD8544_SETXADDR = _pidisplay.PCD8544_SETXADDR
PCD8544_SETTEMP = _pidisplay.PCD8544_SETTEMP
PCD8544_SETBIAS = _pidisplay.PCD8544_SETBIAS
PCD8544_SETVOP = _pidisplay.PCD8544_SETVOP
CLKCONST_1 = _pidisplay.CLKCONST_1
CLKCONST_2 = _pidisplay.CLKCONST_2
LSBFIRST = _pidisplay.LSBFIRST
MSBFIRST = _pidisplay.MSBFIRST

def LCDInit(*args):
  return _pidisplay.LCDInit(*args)
LCDInit = _pidisplay.LCDInit

def LCDcommand(*args):
  return _pidisplay.LCDcommand(*args)
LCDcommand = _pidisplay.LCDcommand

def LCDdata(*args):
  return _pidisplay.LCDdata(*args)
LCDdata = _pidisplay.LCDdata

def LCDsetContrast(*args):
  return _pidisplay.LCDsetContrast(*args)
LCDsetContrast = _pidisplay.LCDsetContrast

def LCDclear():
  return _pidisplay.LCDclear()
LCDclear = _pidisplay.LCDclear

def LCDdisplay():
  return _pidisplay.LCDdisplay()
LCDdisplay = _pidisplay.LCDdisplay

def LCDsetPixel(*args):
  return _pidisplay.LCDsetPixel(*args)
LCDsetPixel = _pidisplay.LCDsetPixel

def LCDgetPixel(*args):
  return _pidisplay.LCDgetPixel(*args)
LCDgetPixel = _pidisplay.LCDgetPixel

def LCDfillcircle(*args):
  return _pidisplay.LCDfillcircle(*args)
LCDfillcircle = _pidisplay.LCDfillcircle

def LCDdrawcircle(*args):
  return _pidisplay.LCDdrawcircle(*args)
LCDdrawcircle = _pidisplay.LCDdrawcircle

def LCDdrawrect(*args):
  return _pidisplay.LCDdrawrect(*args)
LCDdrawrect = _pidisplay.LCDdrawrect

def LCDfillrect(*args):
  return _pidisplay.LCDfillrect(*args)
LCDfillrect = _pidisplay.LCDfillrect

def LCDdrawline(*args):
  return _pidisplay.LCDdrawline(*args)
LCDdrawline = _pidisplay.LCDdrawline

def LCDsetCursor(*args):
  return _pidisplay.LCDsetCursor(*args)
LCDsetCursor = _pidisplay.LCDsetCursor

def LCDsetTextSize(*args):
  return _pidisplay.LCDsetTextSize(*args)
LCDsetTextSize = _pidisplay.LCDsetTextSize

def LCDsetTextColor(*args):
  return _pidisplay.LCDsetTextColor(*args)
LCDsetTextColor = _pidisplay.LCDsetTextColor

def LCDwrite(*args):
  return _pidisplay.LCDwrite(*args)
LCDwrite = _pidisplay.LCDwrite

def LCDshowLogo():
  return _pidisplay.LCDshowLogo()
LCDshowLogo = _pidisplay.LCDshowLogo

def LCDdrawchar(*args):
  return _pidisplay.LCDdrawchar(*args)
LCDdrawchar = _pidisplay.LCDdrawchar

def LCDdrawstring(*args):
  return _pidisplay.LCDdrawstring(*args)
LCDdrawstring = _pidisplay.LCDdrawstring

def LCDdrawstring_P(*args):
  return _pidisplay.LCDdrawstring_P(*args)
LCDdrawstring_P = _pidisplay.LCDdrawstring_P

def LCDdrawbitmap(*args):
  return _pidisplay.LCDdrawbitmap(*args)
LCDdrawbitmap = _pidisplay.LCDdrawbitmap

def LCDspiwrite(*args):
  return _pidisplay.LCDspiwrite(*args)
LCDspiwrite = _pidisplay.LCDspiwrite

def shiftOut(*args):
  return _pidisplay.shiftOut(*args)
shiftOut = _pidisplay.shiftOut

def _delay_ms(*args):
  return _pidisplay._delay_ms(*args)
_delay_ms = _pidisplay._delay_ms
# This file is compatible with both classic and new-style classes.


