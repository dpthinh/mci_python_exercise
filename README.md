# mci_python_exercise
This repo contains the source codes for Python exercises 01, 02, and 03.

Problem 1, a sipmle user-defined function is required. I show the source code for this function in file mci_ex01.py

Problem 2, requires to calculate winning probability of a game.
To solve this problem, I try to simulate this game by Python (see my code in mci_ex02.py for details). Specifically, I try to simulate this game 1000000 times and count how many times I win in these trials. The winning probablity is then simply the ratio of number of times I win over 1000000. To have more accurate winning probability, we can increase number of trials.
There are some unclear points in the statement of the problem. Here is my understanding, wining probability that we can reach the stair >= 60 and the moving up times is limit at 100. That means, I can move-up up to 100 times (during this process there's probability we move down several times but we do not care how many we move down, we just care how many we move up and maximum of move up is limit at 100). During that process, if can can reach the stair 60th or over I win the game otherwise I lose.
It's suprising that the winning probability is 0.99996 that is very close to 1 or we almost win this game. 
This let me wonder there are some errors in my coding or my understanding. I try to increase the difficulty level in winning game such as the person has to reach the stair 90th or higher, the winning probablity from my code is now 0.997 is still very close to 1. If I go back to the original problem, but limit the move-up times is 50, the winning probability when reaching stair 60th or over is 0.834. This result is quite reasonable since i restrict the winning condition so the winning probability is lower than condition stated in the original problem.
You can use my code and changing the parameter to investigate the winning probablity variations.

Problem 3, I use jupyter notebook to demonstrat my data analysis skills. It includes some query skills with dataframe and visualization skills with matplotlib.
