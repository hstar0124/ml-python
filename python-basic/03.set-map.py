#######################################################
### 시퀀스, 집합형 자료구조
#######################################################

## 세트(set)
# 세트는 순서가 보장 되지 않습니다.
# 세트는 요소의 중복을 허용하지 않습니다.
# 세트는 {}를 활용하여 생성할 수 있습니다.

mySet = set([1, 1, 1, 3, 4, 6, 10])
print(mySet)

# 요소를 중복하여 추가하였지만, 중복을 허용하지 않는 set의 특성상 {1, 2, 3} 으로 중복이 제거된 요소만 출력됩니다.

mySet.add(1)
mySet.add(2)
mySet.add(3)

print(mySet)

## update() : 여러개 값 추가
# 여러개의 값을 한꺼번에 추가하고자 할 때는 update() 메서드를 사용합니다.

mySet.update({1, 2, 3, 10, 11, 12})
print(mySet)

## remove() : 값 제거
# 단일 요소를 제거합니다.
mySet.remove(2)
print(mySet)

## 교집합 (intersection)
# 교집합은 집합 A와 B가 주어졌을 때 공통된 요소를 말합니다.
# & 기호나 intersection() 메서드를 활용하여 교집합을 구할 수 있습니다.

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
  
print(a & b)  # = a.intersection(b)


## 합집합 (union)
# 합집합은 집합 A와 B가 주어졌을 때 집합 A, B 요소 모두를 포함하는 것을 말합니다.
# |기호나 union() 메서드를 활용하여 합집합을 구할 수 있습니다.

print(a | b)  # = a.union(b)


## 차집합 (difference)
# 두 집합에서, 하나의 집합에 포함되고 다른 집합에는 포함되지 않는 모든 원소의 집합.
# -연산자를 활용하거나 difference() 메서드를 활용하여 구할 수 있습니다.

print(a - b)  # = a.difference(b)


## 집합의 타입 변환

## set를 list로 변환

a = {1, 2, 3, 4, 5}
b = list(a)
print(type(b))


## list를 set로 변환
# 중복을 제거할 때 많이 활용합니다.

a = [1, 1, 1, 2, 2, 2, 3, 3, 3]
b = set(a)
print(b)
print(type(b))


print('-----------------------------------------------')
#######################################################
### 딕셔너리(dictionary)
#######################################################

# 순서를 가지지 않습니다.
# 키(key)와 값(value)의 쌍으로 이루어져 있습니다.
# type은 dict로 표시 됩니다.
# key를 사용하여 값을 조회할 수 있습니다.
# 딕셔너리는 수정, 삭제, 추가가 가능합니다.

myDict = dict()
print(type(myDict))
print(myDict)

myDict = {'a': 1, 'b': 2, 'c': 3}
print(type(myDict))
print(myDict)

# key를 지정하여 값을 조회할 수 있습니다.
print(myDict['a'])

## get() 메서드를 활용하여 값을 조회할 수 있습니다.
print(myDict.get('b'))

## keys() : 모든 key 조회
# [참고] dict_keys
# dict_keys는 리스트(list)가 아닙니다.
# 객체(object)로 생성되는데, 이를 list로 변경하기 위해서는 list()로 타입 변환을 하면 됩니다.

myDict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}
print(myDict.keys())

## values() : 모든 value 조회
print(myDict.values())

## items() : 모든 key, value 조회
# key, value가 튜플로 묶여서 조회됩니다.
print(myDict.items())
print(list(myDict.items()))

## key 값의 존재 유무 확인
print('a' in myDict)
print('f' in myDict)

## 값을 추가하기
# 새로운 key에 값을 대입하여 추가
myDict = dict()
myDict['apple'] = 123
myDict['apple']

print(myDict)

## update() : 다중 업데이트
# 값을 한꺼번에 업데이트 합니다.
myDict = {'파인애플': 1500, '망고': 3500, '배': 1000}
fruit = {
    '사과': 2000, 
    '딸기': 3000, 
    '수박': 5000, 
}
myDict.update(fruit)

print(myDict)

## 제거하기 / key 제거

## del 값을 제거할 수 있습니다.
# del에 딕셔너리 key를 지정합니다.
myDict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}
del myDict['a']

print(myDict)

## pop() 에 key를 지정하여 값을 제거할 수 있습니다.
# 제거되는 값의 value를 반환합니다.

print(myDict.pop('b'))
print(myDict)

## len() : 요소의 개수 파악
print(len(myDict))

## clear() - 전부 삭제
myDict.clear()
print(myDict)