list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

print(f"The original list 1 : {list1}")
print(f"The original list 2 : {list2}")

temp = list(zip(list1, list2))
random.shuffle(temp)
res1, res2 = zip(*temp)

res1, res2 = list(res1), list(res2)
 
print(f"List 1 after shuffle :  {res1}")
print(f"List 2 after shuffle :  {res2}")
