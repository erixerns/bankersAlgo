# bankersAlgo
### Implementation of Banker's Algorithm in python. This algorithm is used to test if a system is in deadlocked state or not.
1. Let Work and Finish be vectors of length m and n, respectively. 

   Initialize Work = Available and Finish[i] = false for i = 0, 1, ..., n − 1.
   
2. Find an index i such that both

  a. Finish[i] == false
  
  b. Need i ≤ Work332
  
If no such i exists, go to step 4.

3. Work = Work + Allocation i

   Finish[i] = true
   
   Go to step 2.
   
4. If Finish[i] == true for all i, then the system is in a safe state.
