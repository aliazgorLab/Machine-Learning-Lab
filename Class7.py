import numpy as np 
from scipy.spatial.distance import euclidean, cityblock, cosine 
from sklearn.metrics import pairwise_distances 

A = np.array([1, 2, 3]) 
B = np.array([2, 4, 6]) 
C = np.array([3, 2, 1]) 

print("A-B Euclidean:", euclidean(A, B)) 
print("A-B Manhattan:", cityblock(A, B)) 
print("A-B Cosine similarity:", 1 - cosine(A, B)) 

X = np.array([A, B, C]) 
D_euclidean = pairwise_distances(X, metric="euclidean") 
D_manhattan = pairwise_distances(X, metric="manhattan") 
D_cosine = pairwise_distances(X, metric="cosine") 

print("Euclidean distance matrix:\n", D_euclidean) 
print("Manhattan distance matrix:\n", D_manhattan) 
print("Cosine distance matrix:\n", D_cosine)
