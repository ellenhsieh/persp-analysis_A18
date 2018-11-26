<<<<<<< HEAD
def get_r(K, L, alpha, Z, delta):
	'''
	This function generate the interest rate or vector of interest rates
	'''
    
	r = alpha * Z * (L / K) ** (1 - alpha) - delta 

	return r




=======
'''
------------------------------------------------------------------------
This module contains the function get_r()
------------------------------------------------------------------------
'''


def get_r(K, L, alpha, Z):
    r = alpha + Z * (L / K) ** alpha

    return r
>>>>>>> upstream/master
