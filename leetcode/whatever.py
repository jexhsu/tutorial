import itertools

# 相当于嵌套循环
result = list(itertools.product([1, 2], ['a', 'b']))
print(result)  # [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

# 多个序列
result = list(itertools.product([1, 2], ['a', 'b'], ['x', 'y']))
print(result)  # [(1, 'a', 'x'), (1, 'a', 'y'), (1, 'b', 'x'), ...]

# 重复自身
result = list(itertools.product([0, 1], repeat=3))
print(result)  # [(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), ...]
