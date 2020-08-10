# Do you have a fair coin? - A first introduction to Bayesian inference

Before you get started, get:
 * A coin
 * Blu Tack or some other form of “weight” that can stick to a coin
 * Pen & paper or some modern technology to record your counts sequentially; denote each head as a 1 and each tail as a 0


In many data analysis problems across all disciplines, we are often concerned with estimating the values of parameters based on measured empirical data that has a random component: In politics, one may wish to estimate the winner of an election based on exit polls; in physics, Millikan sought to measure the value of the charge of the electron; in medical research, one may wish to estimate the effectiveness of a drug by designing an adaptive trial which, at each stage, takes the results from the previous stage into account. To do so, we require an estimator to approximate the unknown parameters using the measurements. The common approach to this is probability theory, which allows us to determine the probability distribution of a parameter given a statistical sample, i.e. measurements/data. 

Probability theory comes in different flavours and you are most likely already familiar with the frequentist statistic, where the goal is to assign a probability P to the data given a model or hypothesis H, $P(data|H)$

A different view is presented by Bayesian probability theory named after Rev Thomas Bayes FIG. Here, we seek to determine the (posterior) probability $P$ of a model/hypothesis given some data and any prior information I on the model we have $P(H|data,I)$

While in the frequentist approach we seek to rule out models/hypotheses, in Bayesian statistics we seek to determine their relative probabilities. 

At the very heart of Bayesian probability theory lies Bayes’ theorem: ADD FORMULA

It tells us that the posterior probability of a model (hypothesis) is proportional to the product of the likelihood of measuring the data given the hypothesis and its prior probability distribution. The prior represents any form of knowledge or information we already have about the parameter we wish to measure, for example FILL IN.

Let’s look at an elementary example of parameter estimation and the application of Bayesian statistics: **The fair coin**. 

Every cricket match begins with the toss of a coin and the winner gets to choose between batting and fielding. If the coin is fair, then the chance or probability $P$ that the outcome of the toss is either a head or a tail is equal at 50%. 

## DIY Experiment:
Take a coin and flip it ten times. Record how many heads and tails you counted sequentially.
Now, let’s stick some Blu Tack or some other form of “weight” to one side of the coin and repeat the experiment. How man heads and tails did you count this time?

We can now analyse our results statistically using Bayesian probability theory and determine whether or not our coin is fair (Activity 1). In this example, the parameter we want to measure or the hypothesis we wish to test is the “fairness” F of the coin and the data we have are the results of our N tosses; in our case $N=10$. If our coin is totally fair, $F = 0.5$: In ten flips, you get five heads and five tails. If our coin was totally biased towards tails, then $F = 0$ (you never get a head) and, conversely, if it was only ever giving heads and never a tail then $F = 1$. To determine the posterior probability of $F$ we now use Bayes’ theorem Eq. (), which requires a likelihood and a prior. 


The most conservative prior for our coin flip experiment that we can choose is to assume that any value of $F$ between 0 and 1 is equally as probable. This is called a uniform prior:
FORMULA

The second ingredient is the likelihood. If we assume that our coin flips are independent of one another, which is a pretty reasonable assumption, then the probability of obtaining the data such that we have “X heads in N tosses” is given by the binomial distribution:
FORMULA

You now have everything to determine how fair your coin is. To do this, open this [![interactive notebook](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PatriciaSchmidt/Fair_Coin_Example.ipynb)
 in a new tab and proceed with **Activity 1**. 

 * Is your original coin fair?
 * Did you bias your coin by adding the weight to it? 

## Sample size:
In our experiment, we have tossed the coin only ten times, i.e. our statistical sample is relatively small. The posterior probability distribution of the fairness $F$ we have obtained, represents our state of knowledge about the fairness of the coin in the light of our ten tosses. We should ask ourselves how robust this measurement of $F$ is: Would it change if I did 100, 1000 tosses? To find out, head back to the interactive notebook and process with **Activity 2**, in which you will generate simulated data to see how the posterior probability distribution of $F$ is evolving as we increase the size of our statistical sample. 

 * What do you observe for $N=0$?
 * If you have only flipped your coin once, what can you say about it?
 * As you increase the number of tosses N, how does the shape of the resulting posterior probability distribution change?
 * Does the best estimate of $F$ ultimately converge to the value you expect?


## Prior:
So far, we have only considered a uniform prior. We should ask ourselves whether this is actually a good representation of our knowledge of the coin. Regular coins are minted to be fair, i.e. $F$ should have a peak at 0.5. To incorporate this additional information when determining the posterior probability of $F$, we exchange our uniform prior for a prior that is narrowly peaked at 0.5 using a normal (or Gaussian) distribution with a mean of 0.5 and a variance of 0.05. To see how our inference of the fairness of the coin changes under this alternative prior, head back to the interactive notebook and proceed with **Activity 3**. 

 * Do you notice any significant differences, especially when you have a small sample size?
 * s you have more data points, do the resulting posteriors lead to the same conclusion irrespective of our prior knowledge?
 * If your results converge, do they converge at the same rate or does one prior choice lead to a slower convergence than the other?


This is the end of our elementary example. The key takeaway points are:
 1. Bayesian probability theory allows us to estimate the most likely value of a parameter given a statistical sample (empirical data) and prior knowledge on the parameter
 1. The estimation of the most likely value depends sensitively on the size of the statistical sample. Small sample sizes can lead to incorrect inferences.
 1. The prior can dominate our inference if the same size is too small or of the data are uninformative. It can also improve or slow down convergence.


## Outlook: 
Next time, we will look at the reliability of our inferences, define the best estimate and error measures.



## Further reading:
D. S. Sivia, “Data Analysis - A Bayesian Tutorial”, Oxford Science Publications



