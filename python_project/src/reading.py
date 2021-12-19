import numpy as np
class Reading:
    def __init__(self, frequency, re_s11, im_s11, re_s21, im_s21, re_s12, im_s12, re_s22, im_s22):
        self.frequency = frequency
        self.re_s11 = float(re_s11)
        self.im_s11 = float(im_s11)
        self.re_s21 = float(re_s21)
        self.im_s21 = float(im_s21)
        self.re_s12 = float(re_s12)
        self.im_s12 = float(im_s12)
        self.re_s22 = float(re_s22)
        self.im_s22 = float(im_s22)
        self.s11 = complex(self.re_s11, self.im_s11)
        self.s21 = complex(self.re_s21, self.im_s21)
        self.s12 = complex(self.re_s12, self.im_s12)
        self.s22 = complex(self.re_s22, self.im_s22)
        self.det_S = (self.s11*self.s22)-(self.s12*self.s21)
        self.t11 = -(self.det_S/self.s21)
        self.t12 = self.s11/self.s21
        self.t21 = -(self.s22/self.s21)
        self.t22 = 1/self.s21
        self.t_mat = np.array([[self.t11, self.t12], [self.t21, self.t22]])
        self.t_mat_inv = np.linalg.inv(self.t_mat)

    def print_data(self):
        print(self.frequency)
        print(self.re_s11)
        print(self.im_s11)
        print(self.re_s21)
        print(self.im_s21)
        print(self.re_s12)
        print(self.im_s12)
        print(self.re_s22)
        print(self.im_s22)
