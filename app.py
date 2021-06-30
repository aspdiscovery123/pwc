# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 13:20:40 2021

@author: aspdiscovery
"""

from flask import Flask

app=Flask(__name__)

@app.route('/')

def abcd():
    return "hello flask"

