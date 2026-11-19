'''
Trebuchet Dimensions Calculator
Date Created: 10-4-2026
Author: Drew Cutright

Description
This document serves to calculate dimensions of a trebuchet via optimization methods

'''

# Import 
import numpy as np

# Dimensions of arm
L_1 = 10 # Feet lenght of the arm
L_2 = 10 # Initial length of the sling
d_1 = 2 # Feet | counterweight arm
d_2 = 3 # Feet | counterwieght width
d_3 = 2 # Feet | counterweightlength

# Densities
rho_wood = 10 # lbs / feet^3 | density of the wood... need to find / test
rho_cw = 10 # lbs / feet^3 | desity of the counterweight.... probably also wood

# TODO this should be computed based on the volume of the wood samples
# Masses of arm
m_1 = 10 # lbs
m_2 = 2 # lbs
m_3 = 8 # lbs
m_p = 1 # Mass of the projectile

# Momment of inertia of the arm including the arm length, the counterweight arm, and the counterwieght. This should be a 
# system where the center of mass is at the pivot.
I_arm = 1/3 * m_1 * L_1**2 + 1/3*m_2*d_1**2 + 1/12*m_3*d_3**2 + (d_1 + 0.5 * d_2)**2 * m_3

# Dimensions of the pulley
grav = 9.81 #m/s**2
r_1 = 0.5 # feet radius of the pulley
m_c = 100 # lbs weight of the counterwieght

# Angles of the treb
theta = 1 # degrees | starts at the top horizontal line, and loops clockwise
alpha = 1 # degrees | starts at some angle probably 45 between the arm and the sling. Increases clockcwise 

# position of the projectile with respect to the alpha and the theta
x_p = L_1 * np.sin(theta) + L_2 * np.sin(alpha - theta)
y_p = -L_1 * np.cos(theta) + L_2 * np.sin(alpha - theta)

# acceleration of the projectile is equal to the tention force per direction divided by the mass of the projectile
dx2dt2 = 1/m_p * -T_1 * np.sin(alpha - theta) 
dy2dt2 = 1/m_p * -T_1 * np.cos(alpha - theta) - m_p * grav

T_1 = -1 * 1/np.sin(alpha - theta) * dx2dt2
T_2 = r_1 * m_c * grav
theta_second_time_derivative = 1/I_arm * (T_1 * np.sin(alpha)*L_1 - r_1 * T_2)

# Conditions
max_theta = 360 # degrees
max_alpha = 360 - 45 # degrees The angle in which the sling releases
v_max = (dx2dt2 ** 2 + dy2dt2 ** 2)**0.5
distance = v_max ** 2 / (grav)

# Iteration






