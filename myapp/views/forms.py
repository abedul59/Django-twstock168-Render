# -*- coding: utf-8 -*-
"""
Created on Mon May  2 09:02:05 2022

@author: green
"""

from django import forms

class NameForm(forms.Form):
    cStockID = forms.CharField(max_length=4)