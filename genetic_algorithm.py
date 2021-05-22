import numpy as np


def fitness(population, n):
   ans = [] # list declaration
   for i in range(0,len(population)):
       count = 0
       for j in range(0,n):
           count = count + direction(population[i],j) # eikhane hocche ekta row jabe , idx 8 ta jabe
       fitnessValue = n * ( n-1 )
       fitnessValue = fitnessValue / 2
       fitnessValue = fitnessValue - count
       ans.append(fitnessValue)
   return ans

def direction(arr,idx):
   count = 0
   count = count + straightDirection(arr,idx)
   count = count + upperDirection(arr,idx)
   count = count + lowerDirection(arr,idx)
   return count;

def lowerDirection(arr, idx):
   count = 0
   pos = 0
   for i in range (0,8):
       if(i > idx):
           pos = pos - 1
           if(arr[idx] + pos == -1 ):
               break
           if(arr[idx] + pos == arr[i]):
               count = count + 1
   return count

def upperDirection(arr, idx):
   count = 0
   pos = 0
   for i in range(0,8):
       if( i > idx ):
           pos = pos + 1
           if(arr[idx] + pos == 8 ):
               break
           if(arr[idx] + pos == arr[i]):
               count = count + 1
   return count

def straightDirection(arr, idx):
   count = 0
   for i in range (0,8):
       if( i > idx ):
           if(arr[idx] == arr[i]):
               count = count + 1
   return count





def select(population, fit):
   selectIndex = np.random.randint(0, 5)
   fiittest = np.sort(fit)
   fiittest = np.flip(fiittest)
   val = fiittest[selectIndex]
   pos = 0
   for i in range (0,len(fit)):
       if val == fit[i]:
           pos = i
           break
   return population[pos]

def crossover(x, y):
   crossoverPoint = np.random.randint(1, n-1)
   child = []
   for i in range(0,n):
       if(i<crossoverPoint):
           child.append(x[i])
       else:
           child.append(y[i])
   return child


def mutate(child):
   randomInd = np.random.randint(0, n)
   randomQueen = np.random.randint(0, n)
   child[randomInd] = randomQueen
   return child


def GA(population, n, mutation_threshold=0.3):
   fit = fitness(population, n)
   x = select(population,fit)
   y = select(population,fit)
   child = crossover(x,y)
   newthreshold = np.random.randint(0, 11)
   if (newthreshold < mutation_threshold*10):
       child = mutate(child)
   count = 0
   for j in range(0, n):
       count = count + direction(child, j)  # eikhane hocche ekta row jabe , idx 8 ta jabe
   child_fit = n * (n - 1)
   child_fit = child_fit / 2
   child_fit = child_fit - count
   child = np.ndarray(child)
   new_population = population
   print(new_population)
   return population

'''for 8 queen problem, n = 8'''
n = 8

'''start_population denotes how many individuals/chromosomes are there
 in the initial population n = 8'''
start_population = 10

'''if you want you can set mutation_threshold to a higher value,
  to increase the chances of mutation'''
mutation_threshold = 0.3

'''creating the population with random integers between 0 to 7 inclusive
  for n = 8 queen problem'''
population = np.random.randint(0, n, (start_population, n))

'''calling the GA function'''
ans = GA(population, n, mutation_threshold)


