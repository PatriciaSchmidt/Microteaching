# -*- coding: utf-8 -*-
#
#       Copyright 2020
#       Patricia Schmidt <pschmidt@star.sr.bham.ac.uk>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.



import numpy as np
import matplotlib.pyplot as plt

from scipy import stats



def generate_HT(pheads=0.5):
    
    '''
    Function to generate a random number to represent head (H=1) or tail (H=0) in a coin toss. 
    
    Through the parameter pheads in [0.0, 1.0] you can specify how biased you want your coin to be. 
    If pheads = 0, you have a totally biased coin in favour of tails; if pheads = 1.0 you have a 
    totally biased coin in favour of heads.
    '''
    
    # Distribution with heads only
    if pheads == 1.0:
        rnd = 1;
    
    # Distribution with tails only
    if pheads == 0.0:
        rnd = 0;
    
    # A mixed distribution 
    if 0.0 < pheads < 1.0:
        rnd = np.random.random()
        if(rnd < pheads):
            rnd = 1
        else:
            rnd = 0
    
    if rnd > 1:
        return 0
    else:
        return rnd
        
        
def simulation(N=100, pheads=0.5):
    
    '''
    This function simulates N tosses of a coin. You can bias your coin by specifyin pheads in the range
    0.0 to 1.0. 
    
    The function returns:
        X: The number of heads obtained in N tosses
        T = N-X: The number of tails on N tosses
        outcomes: A list containing all outcomes in sequential order
    '''
    
    outcomes = [];
    
    X = 0;
    
    for i in range(N):
        out = generate_HT(pheads);
        if out == 1:
            X += 1
        outcomes.append(out);
    T = N-X;
        
    return X, T, outcomes
    
    
def plot_posterior(X, T):
    
    '''
    Function to plot the posterior distribution.
    
    The assumption here is that each toss is independent of the others, and we use a binomial to model 
    the likelihood function. Because we don't know have any idea of the fairness of the coin, we just
    use a uniform distribution to model the prior. 
    
    X: Number of heads in N tosses
    T: Number of tails in N tosses
    '''
    
    # F is our measure of fairness, which can take values between 0 and 1
    F = np.linspace(1e-6,1.-1e-6,500)
    
    # Calculate the posterior probability of F assuming a uniform prior
    lny = X*np.log(F) + T*np.log(1-F)
    
    if len(lny) > 1:
        lny = lny - np.max(lny)
    
    y = np.exp(lny)
    
    # Normalise the distribution
    y = y/np.sum(y);
    
    # maximum a-posteriori value of F
    idx = np.argmax([y]);
    print(F[idx]);
    
    plt.plot(F, y, c='blue')
    plt.xlabel('Bias-weighting for heads', fontsize = 14)
    plt.ylabel('Probability(H)', fontsize = 14)
    plt.axvline(0.5, ls='--', c='k')
    plt.axvline(F[idx], ls='--', c='blue')
    plt.title(str(X) + ' heads, ' + str(T) + ' tails, total ' + str(X+T) +' tosses')
    plt.show()
    

def calculate_fairness(data):
    
    '''
    Function to calculate the fairness F of a coin given some data, e.g. the result
    of your N coin flips, assuming a uniform prior on F.
    
    It returns the posterior probability density of F and the maximum a-posteriori value.
    '''
    
    # Number of heads in my data:
    X = data.count(1)
    
    # Number of tails:
    T = len(data)-X
    
    # The range of our fairness parameter H:
    F = np.linspace(1e-6,1.-1e-6,500)
    
    lny = X*np.log(F) + T*np.log(1-F)
    
    if len(lny) > 1:
        lny = lny - np.max(lny)    
        y = np.exp(lny)
    
    # Normalise the distribution
    y = y/np.sum(y);
    
    # maximum a-posteriori value of H
    idx = np.argmax([y]);
    print("The maximum posterior probability of the fairness of your coin is: %f"%F[idx]);
    
    plt.plot(F, y, c='blue')
    plt.xlabel('Fairness H', fontsize = 14)
    plt.ylabel('Probability(H)', fontsize = 14)
    plt.axvline(0.5, ls='--', c='k')
    plt.axvline(F[idx], c='blue')
    plt.title(str(X) + ' heads, ' + str(T) + ' tails, total ' + str(X+T) +' tosses')
    plt.show()
    

def calculate_fairness_Gaussian(data):
    
    '''
    Function to calculate the fairness F of a coin given some data, e.g. the result
    of your N coin flips, assuming a Gaussian prior on F peaked at 0.5.
    
    It returns the posterior probability density of F and the maximum a-posteriori value.
    '''
    
    # Number of heads in my data:
    X = data.count(1)
    
    # Number of tails:
    T = len(data)-X
    
    # The range of our fairness parameter H:
    F = np.linspace(1e-6,1.-1e-6,500)
    
    # Gaussian prior for the fairness:
    prior = stats.norm.pdf(F, loc=0.5, scale=0.05)
    
    lny = X*np.log(F) + T*np.log(1-F) + np.log(prior)
    
    if len(lny) > 1:
        lny = lny - np.max(lny)    
        y = np.exp(lny)
    
    # Normalise the distribution
    y = y/np.sum(y);
    
    # maximum a-posteriori value of F
    idx = np.argmax([y]);
    print("The maximum posterior probability of the fairness of your coin is: F=%f"%F[idx]);
    
    plt.plot(F, y, c='blue')
    plt.xlabel('Fairness F', fontsize = 14)
    plt.ylabel('Probability(F)', fontsize = 14)
    plt.axvline(0.5, ls='--', c='k')
    plt.axvline(F[idx], c='blue')
    plt.title(str(X) + ' heads, ' + str(T) + ' tails, total ' + str(X+T) +' tosses')
    plt.show()
    
    
def vary_tosses(pheads=0.5):
    
    '''
    Function to compute the posterior probability of N coin tosses, where N is varied between
    1 and 4096. We assume a uniform prior on the fairness F.
    
    '''
    
    fig = plt.figure(figsize = (15,15))
    n_tosses = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

    F = np.linspace(1e-6,1.-1e-6,500)
    
    X_4096, T_4096, result_4096 = simulation(N=4096, pheads=pheads)
    
    for i, toss in enumerate(n_tosses):
        
        # Get the result up to N=toss
        result = result_4096[0:toss]
        
        # Get the number of heads
        X = result.count(1)
        
        # Get the number of tails
        T = toss - X
        
        # Calculate the posterior probability of F
    
        lny = X*np.log(F) + T*np.log(1-F)
    
        if len(lny) > 1:
            lny = lny - np.max(lny)
    
        y = np.exp(lny)
    
        # Normalise the distribution
        y = y/np.sum(y);
        
        #plot the pdf
        ax = plt.subplot(5, 3, i+1)
        ax.plot(F, y, label='N=%s'%toss, c='blue')
        ax.legend(loc='best')
    
        #disable y axis label
        ax.yaxis.set_visible(False)

        # Setting the x-axis major tick's label
        ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
        ax.set_xticklabels(['0','','0.5','','1'])
        plt.axvline(0.5, ls='--', c='k')     
    
        if pheads > 0.0:
            idx = np.argmax([y]);
            plt.axvline(F[idx], c='blue')

    plt.tight_layout()
    plt.show()
    
    
def vary_tosses_Gaussian(pheads=0.5):
    
    '''
    Function to compute the posterior probability of N coin tosses, where N is varied between
    1 and 4096. We assume a Gaussion prior peaked at 0.5 on the fairness F.
    
    '''
    
    fig = plt.figure(figsize = (15,15))
    n_tosses = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

    F = np.linspace(1e-6,1.-1e-6,500)
    
    X_4096, T_4096, result_4096 = simulation(N=4096, pheads=pheads)
    
    for i, toss in enumerate(n_tosses):
        
        # Get the result up to N=toss
        result = result_4096[0:toss]
        
        # Get the number of heads
        X = result.count(1)
        
        # Get the number of tails
        T = toss - X
        
        # Calculate the posterior probability of F using a uniform prior:
        lny = X*np.log(F) + T*np.log(1-F)
    
        if len(lny) > 1:
            lny = lny - np.max(lny)
    
        y = np.exp(lny)
    
        # Normalise the distribution
        y = y/np.sum(y);
        
        
        # Calculate the posterior probability of F using a Gaussian prior:
        prior = stats.norm.pdf(F, loc=0.5, scale=0.05)
        
        lnyG = X*np.log(F) + T*np.log(1-F) + np.log(prior)
    
        if len(lnyG) > 1:
            lnyG = lnyG - np.max(lnyG)
    
        yG = np.exp(lnyG)
    
        # Normalise the distribution
        yG = yG/np.sum(yG);
        
        
        #plot the pdf
        ax = plt.subplot(5, 3, i+1)
        ax.plot(F, y, label='N=%s'%toss, c='blue')
        ax.plot(F, yG, ls='--', c='red')
        ax.legend(loc='best')
    
        #disable y axis label
        ax.yaxis.set_visible(False)

        # Setting the x-axis major tick's label
        ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
        ax.set_xticklabels(['0','','0.5','','1'])
        plt.axvline(0.5, ls='--', c='k')     
    
        if pheads > 0.0:
            idx = np.argmax([y]);
            idxG = np.argmax([yG]);
            plt.axvline(F[idx], c='blue')
            plt.axvline(F[idxG], ls='--', c='red')

    plt.tight_layout()
    plt.show()

