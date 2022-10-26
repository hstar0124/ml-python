#######################################################
### 리스트(List), 튜플(Tuple)
#######################################################

# 시퀀스, 집합형 자료구조
# 시퀀스(sequence)	리스트(list)	        순서가 있고, 가변(mutable)	            [1, 2, 3]
# 시퀀스(sequence)	튜플(tuple)	            순서가 있고, 불변(immutable)	        (1, 2, 3)
# 세트(set)	        세트(set)	            순서가 없고, 중복을 허용하지 않음	     {1, 2, 3}
# 맵(map)	        딕셔너리(dictionary)	순서가 없고, key/value 쌍으로 이루어짐	 {'a': 1, 'b': 2, 'c': 3}


#######################################################
### 리스트(List)
#######################################################

# 리스트는 데이터의 요소를 순차적으로 파악하는데 용이한 자료형 입니다.
# 리스트는 다양한 메서드(method) 혹은 함수를 지원하며 메서드를 활용하여 요소를 추가, 삭제 및 변경할 수 있습니다.
# 메서드(method): 객체(object)가 포함하는 함수 혹은 기능입니다. 함수에 대한 내용은 추후에 다룹니다.

from typing import List


list1 = []
print(list1)

list2 = list()
print(list2)

list3 = [1, 6, 3, 2, 10]
print(list3)

print('----------------------------------------------------')
## 규칙
# list는 다양한 type의 데이터를 집합으로 가집니다.
# list안에 list도 허용합니다.
# list는 순서(order)의 개념이 존재합니다.

a = [1, 'hello', 3, 10.22, True]
print(a)

b = [1, 'hello', 3, 10.22, True, [1, 9, '12']]
print(b)

print('----------------------------------------------------')
## 관련함수
# . 점 연산자로 함수를 실행할 수 있습니다.
# 함수는 어떤 작업을 수행하는 코드를 모아 이름을 붙인 것입니다.
# 중복된 값을 추가할 수 있으며, 순서가 유지됩니다.

listAppend = []
listAppend.append(10)
listAppend.append(7)
listAppend.append(7)
listAppend.append(7)
listAppend.append(3)
listAppend.append(5)
listAppend.append(2)
print(listAppend.append(2))


print('----------------------------------------------------')
## sort() : 정렬
# 요소를 순서대로 정렬합니다 (오름차순)
# sort()는 내부적으로 정렬 합니다.

listAppend.sort()
print(listAppend)

# 역정렬(reverse order)도 가능합니다. (reverse=True를 지정합니다.)

listAppend.sort(reverse=True)
print(listAppend)


print('----------------------------------------------------')
## sorted() : 정렬
# 요소를 순서대로 정렬합니다.
# 내부적으로 정렬하지 않고 정렬된 복사본을 반환합니다.
# 즉 원본 데이터는 정렬되지 않습니다.
# 마찬가지로, reverse=True를 지정하여 역정렬할 수 있습니다.

myList = [1, 6, 3, 2, 7, 5, 4]
sortedList = sorted(myList)
reverseList = sorted(myList, reverse=True)
print(myList)
print(sortedList)
print(reverseList)

print('----------------------------------------------------')
## len() : 전체 항목의 개수 세기
print(len(sortedList))


print('----------------------------------------------------')
## insert() : 값 추가
# 지정한 index에 값 추가

## remove() : 값 제거
# 리스트에서 첫 번째 나오는 해당 값 삭제

## pop() : 요소 꺼내기
# x번째 요소를 돌려주고 해당 요소는 삭제

## count() : 갯수 세기

## extend() : 리스트 확장
# + 연산자는 extend()와 동일한 기능을 수행합니다.

cudList = [10, 20, 30, 40, 1, 6, 2, 1, 1, 1]
print(cudList)

cudList.insert(1, 200)
print(cudList)

cudList.remove(10)
print(cudList)

x = cudList.pop(1)
print(x)
print(cudList)

print(cudList.count(1))

plusList = [10, 10, 10]

cudList.extend(plusList)
print(cudList)

print('----------------------------------------------------')
#######################################################
### 인덱싱(Indexing), 슬라이싱(Slicing)
#######################################################

## 인덱싱(indexing): 색인
# 인덱스는 0번 부터 시작 합니다.

myList = ['P', 'Y', 'T', 'H', 'O', 'N']
print(myList[0])

## 역순 인덱싱
# 파이썬은 음수 인덱싱을 지원합니다.

print(myList[-1])

## 중첩된 리스트 인덱싱
# 중첩된 리스트에 대한 리스트는 중첩 인덱싱으로 접근합니다. 값을 변경하는 것도 가능합니다.

myList = [['가', '나', '다'], [4, 5, 6], 7, 8, 9]

print(myList[1])
print(myList[1][1])


print('----------------------------------------------------')
## 슬라이싱(Slicing): 범위 추출
# 슬라이싱의 활용: [start:stop:step] 을 명시하여 부분을 추출할 수 있습니다.
# [start:end]는 start부터 end 전까지 추출합니다.

myList = [100, 200, 300, 400, 500]
print(myList[:])
print(myList[:3])
print(myList[1:3])


## indexing 에 step 활용하기
# list[start:stop:step]

myList = [100, 200, 300, 400, 500]
print(myList[::2])
print(myList[::-1])
print(myList[::-2])


print('----------------------------------------------------')
#######################################################
### 인덱싱(Indexing), 슬라이싱(Slicing)
#######################################################

## 튜플(Tuple)
# 리스트(list)는 가변(mutable)하는 객체(object)이지만, 튜플(tuple)은 불변(immutable)한 객체입니다.
# 가변 객체는 요소에 대한 수정, 삭제, 변경 등이 가능하지만, 불변 객체는 요소에 대한 수정, 삭제, 변경이 불가합니다.
# 튜플 자료형은 요소의 추가, 삭제, 변경등을 허용하지 않습니다.

## 생성
# tuple(), () 로 생성합니다.
# 혹은 , 로 생성할 수 있습니다.

myTuple = (1, 2, 3)
print(myTuple)

myTuple = 4, 5, 6
print(myTuple)

# 단일 요소를 생성할 때는 반드시 ,를 붙여 줍니다.
# (1,)과 (1)은 다른 자료구조임을 꼭 알고 있어야 합니다.

myTuple = 1,
print(type(myTuple))

myTuple = 1
print(type(myTuple))


## 튜플 언패킹(unpacking)
# 튜플로 한 번에 여러 변수에 값을 한 번에 할당할 수 있습니다.

a, b, c = 1, 2, 3

print(a)
print(b)
print(c)

myTuple = (1, 2, 3)
print(myTuple)

# 에러남
# myTuple[1] = 100
# print(myTuple)

# 길이 확인
print(len(myTuple))


# list -> tuple

a = [1, 2, 3, 4]
b = tuple(a)
print(type(b))

# tuple -> list

x = (1, 4, 6, 8)
y = list(x)
y.append(100)
print(y)
print(type(y))
