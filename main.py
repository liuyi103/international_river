__author__ = 'liu'

import numpy as np
from ortools.linear_solver import pywraplp

class Country:
    '''
    The class for a country with upstream country and downstram country. The utility of this country is depends on both
     of the two countries. For the upstream one, there is a threshold and for the downstream one, there is a output
     stream distribution among months and extra costs to increase the utility of downstream country.
    '''
    def __init__(self, weights = np.zeros(12), f_weight = 0, upstream = None, downstream = None, max_flow = [1e9] * 12):
        '''

        :param weights: weights for outflow
        :param f_weight: weights for outfish
        :param upstream: the upstream country
        :param downstream: the downstream country
        :param max_flow: upper bound for outflow
        :return:
        '''
        self.solver = pywraplp.Solver('CoinsGridGLPK',\
                             pywraplp.Solver.GLPK_MIXED_INTEGER_PROGRAMMING)
        self.upstream = upstream
        self.downstream = downstream
        self.weights = weights
        self.f_weight = f_weight
        self.outflow = self.solver
        self.outfish = tf.placeholder(tf.float32)
        self.power = 1. # the power of a country
        self.threshold = 100

    def utility(self):
        '''
        :return:the utility of the country
        '''
        utility = self.weights * self.outflow - self.outfish
        if self.downstream != None:
            tf.mul()
            utility -= self.downstream.power * (self.downstream)

if __name__ == '__main__':
