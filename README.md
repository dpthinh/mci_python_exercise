# mci_python_exercise
This repo contains source code for Python exercise 01, 02, 03.

Problem 1, a simple user-defined function is required. I show the source code for this function

Problem 2, require to calculate winning probablity. 
To solve this problem, i try to simulate this game. Specifically, I try to play 1000000 times and count how many times i win in these trial. Then the winning probablity is simple the ratio of number of winning over 1000000. There some misunderstanding point in the problem. Here as my understanding, winning probablity is that we can reach the stair 60 or over and the moving up time is maximum is 100. That means if we move up more than 100 and still not reach stair 60, we have to stop and lose in that trial. It's surprising that the winning probability is 0.99996 is very close to 1. This let me wondering there are some errors in my coding or my understanding. I try to increase the difficulty level in winning the game such as the person has to reach step 90, the winning probablity is now 0.997 still very close to 1. It seems that person can move-up up to 100 times is quite ease condition. If I restrict this condition, such that the person has to finish the game up to move-up times 50 times (note that there is no restriction in number of move-down times), the winning probability to reach stair 60 is 0.834. You can use my code and reset some parameters to check the winning probability

Problem 3, i use jupyter notebook to demonstrat my data analysis skills. It includes some query skills with dataframe and visualization skills with matplotlib.
