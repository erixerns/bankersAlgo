import numpy as np

# numProcecsses = int(input("Enter number of processes: "))
# numResources = int(input("Enter number of resources: "))
numProcesses=5
finished = [0 for x in range(numProcesses)]
need = []
alloc = []

# for i in range(numProcecsses):
#   temp = input("Enter allocation for process {}: ".format(i)).split(' ')
#   temp = [int(x) for x in temp]
#   alloc.append(temp)


# for i in range(numProcecsses):
#   temp = input("Enter need for process {}: ".format(i)).split(' ')
#   temp = [int(x) for x in temp]
#   need.append(temp)


# work = input("Enter availale: ").split(' ')
# work = [int(x) for x in work]

work = [2, 1, 0]
need = [[7, 2, 3],
        [0, 2, 0],
        [6, 0, 0],
        [0, 1, 1],
        [4, 3, 1],]

alloc = [[0, 3, 0],
        [3, 0, 2],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2],]

work = np.asarray(work)
need = np.asarray(need)
alloc = np.asarray(alloc)

print(work)
print(need)
print(alloc)

while not all(finished):
  i = 0
  flag = False
  for i in range(numProcesses):
    # print(i, need[i], work, np.less_equal(need[i], work))
    if not finished[i] and all(np.less_equal(need[i], work)):
      print("P", i, end='\n', sep='')
      work = np.add(work, alloc[i])
      finished[i]=True
      flag = True
  if not flag:
    break

print(finished)