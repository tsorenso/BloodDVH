import numpy as np

class Dose(object):
    ''' A Blood voxel with an position and dose
    '''

    def __init__(self, dose_field, time_on, time_gap=[0]):
        self.dose_field = dose_field  # a list of dose_field matrices (2d or 3d)
        self.time_on = time_on
        self.time_gap = time_gap
        # assume that all the dose_field have the same dimentions
        (self.x_dim, self.y_dim, self.z_dim) = self.dose_field[0].shape

    def get_dose_field(self):
        return self.dose_field

    def multiplyDoses(self):
        for dose in range(len(self.dose_field)):
            mult = float(input('How much would you like to vary the %s dose input?', dose))
            self.dose_field[dose] *= mult

    def get_shape(self):
        return (self.x_dim, self.y_dim, self.z_dim)

    def get_dose_time(self):
        return self.time_on

    def get_dose_time_gap(self):
        return self.time_gap

    def add_new_dose(self, dose):
        new_dose = dose.get_dose_field()
        new_time_on = dose.get_dose_time()
        new_time_gap = dose.get_dose_time_gap()
        self.dose_field += new_dose
        self.time_on += new_time_on
        self.time_gap += new_time_gap


# def rotate(self, theta = math.pi/2 ,axis = [1,0,0]):
#        """
#        Return the rotation matrix associated with counterclockwise rotation about
#        the given axis by theta radians.
#        """
#        axis = np.asarray(axis)
#        axis = axis/math.sqrt(np.dot(axis, axis))
#        a = math.cos(theta/2.0)
#        b, c, d = -axis*math.sin(theta/2.0)
#        aa, bb, cc, dd = a*a, b*b, c*c, d*d
#        bc, ad, ac, ab, bd, cd = b*c, a*d, a*c, a*b, b*d, c*d
#        for i in
#        return np.array([[aa+bb-cc-dd, 2*(bc+ad), 2*(bd-ac)],
#                         [2*(bc-ad), aa+cc-bb-dd, 2*(cd+ab)],
#                         [2*(bd+ac), 2*(cd-ab), aa+dd-bb-cc]])
#
# v = [1, 0, 0]
# axis = [0, 0, 1]
# theta = math.pi/2
#
# print(np.dot(rotation_matrix(axis,theta), v))
#TODO add those two function to proper class
def match_field(field, dimensions):
    '''resize the dose_field to have required dimensions'''
    if field.shape != dimensions:
        new_field = np.zeros(dimensions)
        x_dim, y_dim, z_dim = field.shape
        new_field[0:x_dim, 0:y_dim, 0:z_dim] = field
    else:
        new_field = field

    return new_field

def stack_field(field,times=1,axis=0):
    '''stack a field many times to make it thicker'''
    f1 = np.copy(field)
    new_field = np.copy(field)
    for i in range(times-1):
       new_field = np.concatenate((new_field,f1),axis)
    return new_field