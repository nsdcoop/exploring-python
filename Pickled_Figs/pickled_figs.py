#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 16:51:35 2019

@author: nicholascooper

Demonstrates how to save an interactive version of your matplotlib figures.
Two ways of plotting are treated here, plt.subplots() and plt.figure()
There is a common error and here the function show_figure is defined, and is an 
effective method of overcoming the "no attribute 'manager'" error.

This method could be implemented by writing a small script that one would use to 
load and view interactive plots.
"""

import pickle
import matplotlib.pyplot as plt
import numpy as np
#%% Some Functions

# Function to give the figure a canvas manager so it will be displayed

def show_figure(fig):
    '''
    If the pickled figure is missing the attribute 'manager' such an
    error will be raised.  This is common especially if the figure was created 
    using plt.figure().  This function should resolve the error.
    Creates a dummy figure and use its manager to display "fig"  
    '''
    dummy = plt.figure()
    new_manager = dummy.canvas.manager
    new_manager.canvas.figure = fig
    fig.set_canvas(new_manager.canvas)
    return

# A function that will do it all
def pickled_fig(path, get_data=False, axis_dict=False):
    '''
    Function to show an interactive matplotlib figure that has been pickled.  
    In the case of a specific error with the canvas manager of the figure 
    the function "show_figure"defined below should solve the problem.  
    
    ----------
    Parameters
    ----------
    path : str 
        The path (or filename if in current working directory) to a .pickle 
        file containing a matplotlib object
    get_data : boolean, optional
        Extracts the data used to create the plots
    line_dict : boolean, optional
        Gives the data as dictionaries of lines for each axis instead of lists 
        of lines for each axis.
    -------
    Returns
    -------
    fig : matplotlib figure
        The function returns a matplotlib figure that should show itself automatically.
        If the figure doesn't show itself automatically a simple fig.show() should 
        show it.
    data : dictionary, optional
        If get_data==True then the function will return a tuple of the mpl figure and a 
        dictionary with the x, y data from the plot.  Each key in the dictionary represents 
        the axis (or subplot), and has a numpy array with two 1-D arrays inside - the x and y values.
        Numpy arrays are used for some of the ways they can be sliced.  If the axis has more than
        one line plotted on it the numpy array has another two arrays added to it for the other
        line's x and y values.  This is true for as many lines as are on the axis.  
        If axis_dict==True then the dictionary will contain a dictionary for each 
        axis containing all the lines on that axis in list form rather than numpy arrays.  
        This could be good for organization if there are many lines on any axis.
        
    
    - Nicholas Cooper
    '''
    
    def show_figure(fig):
        '''
        If the pickled figure is missing the attribute 'manager' such an
        error will be raised.  This is common especially if the figure was created 
        using plt.figure().  This function should resolve the error.
        Creates a dummy figure and use its manager to display "fig"  
        
        - Found on Stack Overflow
        https://stackoverflow.com/questions/49503869/attributeerror-while-trying-to-load-the-pickled-matplotlib-figure
        '''
        dummy = plt.figure()
        new_manager = dummy.canvas.manager
        new_manager.canvas.figure = fig
        fig.set_canvas(new_manager.canvas)
        
        return
    
    # Begin Function -----------------------------------------
    
    import pickle
    import matplotlib.pyplot as plt
    
    # Avoiding errors
    if get_data == False and axis_dict == True:
        return "ERROR: axis_name cannot be True while get_data is False"
    
    # Load figure
    with open(path, 'rb') as file:
        fig = pickle.load(file)
    
    # Check for attribute error
    if fig.canvas==None:
        show_figure(fig)
    
    # Get data from plot
    if get_data == True:
        data = {}
        for axis in range(len(fig.axes)):
            axis_name = "Axis "+str(axis)
            
            if axis_dict == False:
                data[axis_name] = [] # Good for if there is only one line per axis
                
                for line in range(len(fig.axes[axis].lines)): 
                    data[axis_name].append(fig.axes[axis].lines[line].get_data())
                    
                data[axis_name] = np.array(data[axis_name]) # Convert to numpy array for slicing ability
                    
            if axis_dict == True:
                data[axis_name] = {} # Possibly good for when there are multiple lines on one axis
                
                for line in range(len(fig.axes[axis].lines)): 
                    line_name = "Line "+str(line)
                    data[axis_name][line_name] = fig.axes[axis].lines[line].get_data()
                
        return fig, data
                
    else:
        
        return fig
#%%

loadfig1 = pickle.load(open("testfig.fig.pickle", 'rb'))
#%% 
# Method of using plt.subplots()
# usually works with no problems
x = np.linspace(0, 10, 100)
y = np.cos(x)

fig, ax = plt.subplots()

ax.plot(x, y, label = "cos(x)")
ax.set_title("This is a Test")
ax.grid(b=True)
ax.legend()
fig.show()

# "pickle" the image
pickle.dump(fig, open("testfig2.pickle", 'wb'))
#%% Load the image
# Should show the figure immediately
# Should be able to call the variable wherever and it will show the figure
with open("testfig2.pickle", 'rb') as f:
    loadfig2 = pickle.load(f)
#loadfig2 = pickle.load(open("testfig2.pickle", 'rb'))
#%% This is how you get the data that was used to plot if you want that
data = loadfig2.axes[0].lines[0].get_data()
# Could load the data into other forms of plots as well
#%%
# Method of using plt.figure()
x = np.linspace(0, 10, 100)
y = np.cos(x)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(data[0], data[1])
#ax.plot(x, y)

# "pickle" the image
pickle.dump(fig, open("testfig3.pickle", 'wb'))

#%% Load the image
# usually does not open the image, it has a problem
# the figure will need a canvas manager, so you have to give it one
loadfig3 = pickle.load(open("testfig3.pickle", 'rb'))

#%%
        
x = np.linspace(0, 10, 100)
y = np.cos(x)

fig = plt.figure()

plt.plot(data[0], data[1])
#ax.plot(x, y)

# "pickle" the image
pickle.dump(fig, open("testfig4.pickle", 'wb'))
#%%
with open("testfig4.pickle", 'rb') as file:
    loadfig4 = pickle.load(file)
#%%
    
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = x


fig, (ax1, ax2, ax3) = plt.subplots(ncols=3)

ax1.plot(x, y1)
ax1.plot(x, y2)
ax3.plot(x, y3)

pickle.dump(fig, open("testfig4.pickle", 'wb'))
#%%

fig, data = pickled_fig("testfig4.pickle", get_data=True)

# First plot's x and y values
x_values = data["Axis 0"][:,0] # slicing with numpy arrays
y_values = data["Axis 0"][:,1]

