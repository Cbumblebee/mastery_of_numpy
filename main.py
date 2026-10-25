import numpy as np

print(np.__version__) #2.5.4


# ~~~~~~~~~~~list vs array~~~~~~~~~~~~~~~~~
# python list
my_list = [1,2,3,4]
my_list = my_list * 2
print(my_list) # [1, 2, 3, 4, 1, 2, 3, 4]

# numpy ndarray
array = np.array([1,2,3,4])
print(array)
print(type(array))
array = array * 2
print(array) # [2 4 6 8]


# ~~~~~~~~~~~~~~~~~~ Arrays ~~~~~~~~~~~~~~~~~~~~
arrayA = np.array('A')
print(array.ndim) # 1

arrayABC = np.array([['A', 'B', 'C'], 
                    ['D', 'E', 'F'], 
                    ['G', 'H', 'I']])
print(arrayABC.ndim) # 2

# it's important to have arrays that are all the same size (homogeneus shape)
array3dim = np.array([[['A', 'B', 'C'], ['A', 'B', 'C']],
                    [['A', 'B', 'C'], ['A', 'B', 'C']], 
                    [['A', 'B', 'C'], ['A', 'B', '']]])
print(array3dim.ndim) # 3
print(array3dim.shape) # (3, 2, 3)
print(f"chain indexing {array3dim[0][0][0]} looks the same as multidimensional indexing {array3dim[0,0,0]}")


word = array3dim[0,0,0] + array3dim[0,1,2]
print(word)


# ~~~~~~~~~~~~~~~~~~ slicing ~~~~~~~~~~~~~~~~~~~~~~~~~
# row selection
array2 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
# array[start:end (exclusive):step]
print(array2[0:3:2])
"""gives u:
[[ 1  2  3  4]
 [ 9 10 11 12]]"""
print(array2[::-1]) # all the rows, reversed
print(array2[:2:])

# column selection
print(array2[:,0]) #[1 5 9] are all 0-columns
print(array2[:,-2]) # [ 3  7 11]
print(array2[:, 0:3]) # prints all the first three columns
print(array2[::3, :])   # every 3rd row, all columns
print(array2[:, 1:]) # prints all the columns after the first one
print(array2[:, ::2]) # gives us every second column

# ~~~~~~~~~~~~~~~~~~~~~~~~~arithmetic~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# vectorized math functions
radii = np.array([1,2,3])
# np.sqrt(array)
# np.round(array) or .floor or .ceil
# np.pi
print(np.pi * radii ** 2)

# element-wise arithmetic
array3 = np.array([1,2,3])
array4 = np.array([4,5,6])
print(array3 ** array4) # = 1**4, 2**5, 3**6

# comparison operators
scores = np.array([91,95,100,74,82,64])
print(scores == 100) # [False False  True False False False]
scores[scores < 70] = 0
print(scores) # [ 91  95 100  74  82   0]


# ~~~~~~~~~~~~~~~~~~~~~~~~broadcasting~~~~~~~~~~~~~~~~~~~~~~~~~
# as soon as there is a "1" in the shape, we can broadcast it
array_1 = np.array([[1,2,3,4]])
array_2 = np.array([[1],[2],[3],[4]])
print(f"shape of 1 {array_1.shape}=(1,4) and shape of 2 {array_2.shape} = (4,1)")

print(array_1 * array_2)
"""[[ 1  2  3  4] basically [1] * [1,2,3,4] 
 [ 2  4  6  8]
 [ 3  6  9 12]
 [ 4  8 12 16]]"""


arr1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
arr2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
print(f"shape of 1 {arr1.shape}=(1,10) and shape of 2 {arr2.shape}=(10,1)")
print(arr1 * arr2)
# ~~~~~~~~~~~~~~~~~~~~~~~~aggregate functions~~~~~~~~~~~~~~~~~~~~~~~~~
# they summarize dta and return a single value
array = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])
# np.sum(array)
print(np.sum(array, axis=0)) # [ 7  9 11 13 15], sums over all the columns
print(np.sum(array, axis=1)) # [15 40], sums over all the rows
# np.mean(array)
# np.std(array) is the standard deviation
# np.var(array)
# np.min(array) and max
# np.argmin gives the index of the array
print(np.argmax(array)) # gives 9
# ~~~~~~~~~~~~~~~~~~~~~~~~filtering~~~~~~~~~~~~~~~~~~~~~~~~~
ages = np.array([[21,27,49,3],
                 [5,4,33,5]])

teenargers = ages[ages < 18] 
print(teenargers)# [3 5 4 5] flattens your array with boolean indexing and is one-dim
adults = ages[(ages >= 18) & (ages < 60)]
print(adults)
seniors= ages[ages >= 60]
print(seniors)

adults = np.where(ages >= 18, ages, np.nan) # keeps previous shape, but is slower than boolean indexing
print(adults)
"""[[21. 27. 49. nan]
 [nan nan 33. nan]]"""
# ~~~~~~~~~~~~~~~~~~~~~~~~random numbers~~~~~~~~~~~~~~~~~~~~~~~~~
rng = np.random.default_rng()
# if setting a seed, you'll get the same numbers again by re-running
rng_seeded = np.random.default_rng(seed=1)
print(rng.integers(low=1, high=101, size=(3,2)))
"""[[35 69]
 [14 25]
 [77 11]]"""
# np.random.seed(seed=1) # everything below that will always reproduce the same thing with this seed
print(np.random.uniform(low=-1,high=1,size=2))

# shuffle an array
array = np.array([[21,27,49,3],
                 [5,4,33,5]])
rng.shuffle(array)
print(array)
# take a random sample from array
number = rng.choice(array[0])
print(array[0].shape, number)