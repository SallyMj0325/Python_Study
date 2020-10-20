#
a = "김민정"
print(a)

#이건 또 뭐에요
name = "hi "
name2 = "hello "
name3 = "my name is min jung kim"
print(name + name2 + name3)

#이건 저런 거에요
d = 2
f = 3
print(d * f)
w = 6
e = 3
print(w / e)
q= 7
r= 4
print(q // r)
b= 3
c= 4
print(b ** c)
z= """Hello world """
x= 'python is fun '
v= "Life is too short, you need python "
print(z + x + v)
food = "Python's favorite food is peal"
print(food)
k = "Python"
print( k * 2)
y = "Life is too short, You need Python"
print( y[3] )
print( y[-9] )
print( y[0] + y[1] + y[2] + y[3] )
print( y[0:4] )
print( y[19:] )

# 숫자 바로 대입
h = "I eat %d apples" %3
print( h )

# 문자열 바로 대입
j = "I eat %s apples" % "five"
print( j )

# 숫자 값을 나타내는 변수로 대입
number = 3
meat = "I eat %d apples" % number
print( meat )

# 2개 이상의 값 넣기
number = 10
day = "three"
good = "I ate %d apples. so I was sick for %s days." % ( number, day )
print( good )

# 정렬과 공백
rt = "%10s" % "hi"
print( rt )

qw = "%-10s jane" % 'hi'
print( qw )

# 소수점 표현하기
sd = "%0.4f" % 3.24134234
print( sd )

df = "%10.4f" %3.24134234
print( df )

# 숫자 바로 대입하기
qs = "I eat {0} apples".format(3)
print( qs )

# 문자열 바로 대입하기
gg = "I eat {0} apples".format("five")
print( gg )

# 숫자 값을 가진 변수로 대입하기
number = 4
fg = "I wat {0} apples".format(number)
print( fg )

# 2개 이상의 값 넣기
number = 11
day = "six"
ff = "I ate {0} apples. so I was sick for {1} days.".format(number, day)
print( ff )

# 이름으로 넣기
fh = "I ate {number} apples. so I was sick for {day} days.".format(number=12, day=3)
print( fh )

# 인덱스와 이름을 혼용해서 넣기
jh = "I ate {0} apples. so I was sick for {day} days.".format(10, day=5)
print( jh )

# 왼쪽 정렬
pp = "{0:>10}".format("hi")
print( pp )

# 오른쪽 정렬
kk = "{0:^10}".format("hi")
print( kk )

# 공백 채우기
jw = "{0:=^10}".format("hi")
print( jw )

# 소수점 표현하기
y = 3.42134234
gq=  "{0:0.4f}".format(y)
print( gq )

# { 또는 } 문자 표현하기
do = "{{ and }}".format()
print( do )

# 문자 개수 세기
a = "hobby"
a = a.count('b')
print( a )

# 위치 알려주기 1(find)
a = "Python is the best choice"
a = a.find('b')
print( a )
a = "PYthon is the best choice"
a = a.find('k')
print( a )

# 위치 알려주기 2(index)
a = "Life is too short"
a = a.index('t')
print( a )

# 문자열 삽입(join)
a = ",".join('abcd')
print( a )
a = ",".join(['a', 'b', 'c', 'd'])
print( a )

# 소문자를 대문자로 바꾸기(upper)
a = "hi"
a = a.upper()
print( a )

# 대문자를 소문자로 바꾸기(lower)
a = "Hi"
a = a.lower()
print( a )

# 왼쪽 공백 지우기(lstrip)
a = " hi "
a = a.lstrip()
print( a )

# 오른쪽 공백 지우기(rstrip)
a = " hi "
a = a.rstrip()
print( a )

# 양쪽 공백 지우기(strip)
a = " hi "
a = a.strip()
print( a )

# 문자열 바꾸기(replace)
a = "Life is too short"
a = a.replace("Life", "Your leg")
print( a )

# 문자열 나누기(split)
a = "Life is too short"
a = a.split()
print( a )
b = "a:b:c:d"
b = b.split(':')
print( b )

