#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 10:50:21 2017

@author: taylorsorenson, zhaoqiwang
"""

import numpy as np 
import math
import random
import readDoses

class Blood(object):
    ''' A Blood cell with an initial position (and velocity)
    '''
    def __init__(self, position, init_dose = 0):
        self.position = position
        self.dose_added = init_dose
        
    def get_dose(self):
        return self.dose_added
     
    def set_dose(self,dose):
        self.dose_added += dose
        
    def get_position(self):
        return self.position
    

class Position(object):
    '''A position within the blood vessel
    '''
    def __init__(self, x, y, z):
        #assumes velocity and position are tuples in all three dimensions
        #in 1D case, vy and vz are 0 --> velocity = (vx, 0, 0)
        self.x = x
        self.y = y
        self.z = z
        self.position = (self.x, self.y, self.z)
        
    def get_position(self):
        return self.position    
    
    def get_new_position(self, vx,vy,vz, dt):
        #dt is the change in time dt
        old_x, old_y, old_z = self.x, self.y, self.z
        dx = vx * dt
        dy = vy * dt
        dz = vz * dt
        
        new_x, new_y, new_z = (old_x + dx), (old_y + dy), (old_z + dz)
        return Position (new_x, new_y, new_z)
        
class const_vector_field(object):
        #assumes the velocity everywhere is constant in one direction
        def __init__(self, x_dim, y_dim, z_dim, vx,  vy = 0, vz = 0): #change the order of these later
            '''Assumes x_dim is a scalar of the number of units in our matrix
            In one dimension, y_dim and z_dim should just be 1
            #TODO - Adjust this later to match up with the velocity fields  in vdx files 
            '''             
            self.vx = vx
            self.vy = vy
            self.vz = vz
            self.velocity = (self.vx, self.vy, self.vz)
            #create three 3-D velocity matrices, each containing the velocity in one direction x,y,or z
            self.vx_field = np.zeros((z_dim,y_dim, x_dim)) + self.vx   
            self.vy_field = np.zeros((z_dim,y_dim, x_dim)) + self.vy  
            self.vz_field = np.zeros((z_dim,y_dim, x_dim)) + self.vz   
        
        def get_velocity(self):
            return self.velocity
        
        def get_vx_at_position(self,x,y,z):
            return self.vx_field[x][y][z]
        
        def get_vy_at_position(self,x,y,z):
            return self.vy_field[x][y][z]
        
        def get_vz_at_position(self,x,y,z):
            return self.vz_field[x][y][z]
        
        def get_velocity_fields(self):
            return [self.vx_field, self.vy_field, self.vz_field]


#field = const_vector_field(10,1,1,5.2)
#print(field.get_field())
#print(field.get_v_at_position((0,0,1)))



def make_blood(num_blood_cells):
    '''makes num_blood_cells objects and gives them all an initial position
    '''
    
        
def find_blood():
    '''finds which blood cells are in the path of the beam
    '''       
        
def add_constant_dose(blood, dose):
    '''
    add a constant dose of radiation to all blood within the radiation beam
    blood - a list of blood objects that are
    '''
    #time?
    pass 

def simulate_blood_flow(total_time, dt):
    pass
        
def make_pdf(blood):
    pass


def make_cdf():
    pass

def make_dvh():
    pass
        
        
    
        


