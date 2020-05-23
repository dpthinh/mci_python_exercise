# mci_python_exercise
This repo contains the source codes for Python exercises 01, 02, and 03.

Problem 1, a simple user-defined function is required. I show the source code for this function in file mci_ex01.py

Problem 2, requires to calculate the winning probablity of a game.
To solve this problem, I try to simulate this game by Python (see my code in mci_ex02.py for details).
Specifically, I try to simulate this game 1000000 times and count how many times I win in these trials. The winning probablity is the ratio of number of times I win over 1000000. To have more accurate winning probablity, we can increase number of trials.
There are some uncler points in the problem's statment. Here is my understanding, the winning condition is that we can reach the stair 60-th or higher and the moving up times is limit at 100. That means I can move-up up to 100 times (of course during this process there's probability we move down several times but we do not care how many times we move down, we just care how many times we move up and it limits at 100). During that process, we we can reach the stair 60-th or over we stop the game and win otherwise we lose.
It's suprising that the winning probability is 0.99996 that is very close to 1 or we almost win this game. 
This let me wonder there are some errors in my coding or my understanding. I try to increase the difficulty level in winning game such as the person has to reach the stair 90th or higher, the winning probablity from my code is now 0.997 is still very close to 1. If I go back to the original problem, but limit the move-up times is 50, the winning probability when reaching stair 60th or over is 0.834. This result is quite reasonable since I restrict the winning condition so the winning probability is lower than that of original case.
You can use my code and change the parameter to investigate the winning probablity variations.

Problem 3, I use jupyter notebook to demonstrate my data analysis skills. It includes some queries with dataframe and visualizations with matplotlib library.
