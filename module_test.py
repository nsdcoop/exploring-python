#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 21:47:23 2019

@author: nicholascooper
"""
#%%
import testmodule

testmodule.HelloWorld()

print(testmodule.squares(100))

print("the test worked!")

#%%
import testmodule as t

t.HelloWorld()
print(t.squares(100))
print("the test worked!")

#%%
from testmodule import *

HelloWorld()
#%%
from testmodule import *

HelloWorld()