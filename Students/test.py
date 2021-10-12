l1 = [1,[2,3],4]
def deepReverse(L):
  if L == []:
    return []
  if not isinstance(L[0], list):
    return deepReverse(L[1:]) + [L[0]]
  else:
    return deepReverse(L[1:]) + [deepReverse(L[0])]
answer = deepReverse(l1)
print(answer)