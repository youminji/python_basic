'''
Stack과 Queue를 List로 작성한다.
'''

stack_list = [1,2,3, ]
stack_list.append(5)
stack_list.extend([10, 20])
print(stack_list)

# LIFO
stack_list.pop()
print(stack_list)
stack_list.pop()
print(stack_list)

# FIFO
queue_list =[10,20,30]
queue_list.pop(0)
print(queue_list)

# tuple => 튜플과 리스트가 다른 점은 값변경이 안된다는거
my_tuple = tuple([10, 30, 40])
my_tuple2 = (20, 30, 40)
print(type(my_tuple), type(my_tuple2))
print(my_tuple[2], my_tuple2[0:2], my_tuple*2)

my_int = (10)
my_tuple3 = (10,)
print(type(my_int), type(my_tuple3))

# set - 값의 중복을 허용하지 않는 list
my_set = set([1, 2, 3, 1, 2, 3])
print(type(my_set), my_set)
my_set.add(1)
print(my_set)
my_set.remove(1)
print(my_set)
my_set.update([1, 4, 5, 6, 7])
print(my_set)
my_set.discard(3)
print(my_set)
my_set.clear()
print(my_set)

s1 = set([1, 2, 3, 4, 5])
s2 = set([3, 4, 5, 6, 7])
print('합집합: ', s1.union, s1|s2)