#!/usr/bin/env python
# encoding: utf-8

"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""
import os
from setuptools import setup

VERSION='1.6.0'
targetfile = "seafileweb.py"

APP = [targetfile]
DATA_FILES = []
PACKAGES = []
INCLUDES = ["utils"]
EXCLUDES = ["local_settings", "test"]
PLIST = {"LSBackgroundOnly":True,
         "CFBundleIdentifier":"seafile.seafileweb",
         "NSHumanReadableCopyright":u"Copyright © 2012 海文互知. All rights reserved.",
         "CFBundleVersion":VERSION}
OPTIONS = {"packages":PACKAGES, "includes":INCLUDES,
           "excludes":EXCLUDES, "plist":PLIST }


destdir = "dist/seafileweb.app/Contents/Resources/"

try:
    os.system("rm -rf diet; rm -rf build; cp main.py "+ targetfile)
except Exception, e:
    pass    


setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

os.system ("cp -rf i18n "+destdir + "i18n")
os.system ("cp -rf static "+destdir + "static")
os.system ("cp -rf templates "+destdir + "templates")

