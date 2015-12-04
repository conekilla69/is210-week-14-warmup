#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""Buying fruits"""


from data import fruit

def get_cost_per_item ():
    shoplist = fruit.iteritems
    return {fruit[key]: value * 'price' for key, value in fruit.iteritems()}:

def get_total_cost():
    shoplist = fruit.iteritems
    return {key + '' + value for key, value in fruit.iteritems()}:
    
        
    
    
