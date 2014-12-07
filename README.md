queue_simulation
================

Simulation of a simple M/M/1 queue using uniform RV's

to run:
```
./queue.sh <lambda> <mu> <n> <T>
```
- lambda is the input (arrival) rate for the queue
- mu is the output (departure) reate for the queue
- n is the initial size of the queue
- T is the total time to simulate the queue for

The output of the script is a png file named hist.png which is a histogram of 1000 trials of Xt, the total number
of people in the queue at time T.

The image is automatically opened in google chrome.


