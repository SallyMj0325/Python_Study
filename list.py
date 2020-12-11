odd = [1, 3, 5, 7, 9]
print(odd)

print(odd[0])

# 리스트 인덱싱
a = [1, 2, 3]
print( a )

# 리스트의 슬라이싱
a = [1, 2, 3, 4, 5]
b = a[0:2]
print( a[0:2] )

a = "12345"
b = a[0:2]
print( a[0:2] )

a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]
print( a[:2] )
print( a[2:] )

a = [1, 2, 3, 4, 5]
b = a[1:3]
print( a[1:3])

# 리스트 더하기(+)
a = [1, 2, 3]
b = [4, 5, 6]
print( a + b )

# 리스트 반복하기(*)
a = [1, 2, 3]
print( a * 3 )

# 리스트 길이 구하기
a = [1, 2, 3]
b = len(a)
print( len(a) )

# 리스트에서 값 수정하기
a = [1,2,3]
a[2] = 4
print( a )

# del 함수 사용해 리스트 요소 삭제하기
a = [1, 2, 3]
del  a[1]
print( a )

a = [1, 2, 3, 4, 5]
del a[2:]
print( a )

# 리스트에 요소 추가(append)
a = [1, 2, 3]
a.append(4)
print( a )

a.append([5,6])
print( a )

# 리스트 정렬(sort)

a = [1, 4, 3, 2]
a.sort()
print( a )

a = ['a', 'c', 'b']
a.sort()
print( a )
# 리스트 뒤집기(reverse)
a = ['a', 'c', 'b']
a.reverse()
print( a )

# 위치 변환(index)
a = [1,2,3]
a = a.index(3)
print( a )

a = [1,2,3]
a = a.index(1)
print( a )

# 리스트에 요소 산입(insert)
a = [1, 2, 3]
a.insert(0, 4)
print( a )