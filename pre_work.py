import numpy as np

a = np.array([[1, 2, 3], [4 ,5 ,6]])
b = np.array([2, 3, 4])
c = np.array(
    [
        [
        [1, 2],
        [3, 4]
        ],
        [
        [5, 6],
        [7, 8]
        ]
    ]
)

d = np.zeros(5)
print(d)
f = np.zeros((2, 3, 4))
print(f'{f.ndim} Dimensions')