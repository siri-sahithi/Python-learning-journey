import numpy as np
#without seed the elements changes when we execute again and again
print(np.random.rand(9).reshape(3,3))

#with seed
np.random.seed(42)
print("with seed \n", np.random.rand(9).reshape(3,3))


