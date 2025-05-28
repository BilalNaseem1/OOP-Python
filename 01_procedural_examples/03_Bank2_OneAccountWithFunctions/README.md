- As a general programming tenet, functions should never modify global variables. 

- A function should only use data that is passed into it, make calculations based on that data, and potentially return a result or results. 

- The withdraw() function in this program does work, but it violates this rule by modifying the value of the global variable accountBalance 6 (in addition to
accessing the value of the global variable accountPassword).