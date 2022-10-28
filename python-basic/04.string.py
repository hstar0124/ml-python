#######################################################
### 문자열
#######################################################

## 데이터 분석에 있어서 문자열(텍스트) 데이터의 중요성
# 자연어처리 데이터는 대부분이 텍스트 데이터로 이루어져 있습니다.
# 우리가 흔히 접하는 Excel 혹은 Table 데이터안에도 수많은 텍스트 데이터가 존재합니다.
# 게다가 우리나라는 영어와 더불어 한글까지 추가로 처리 할 수 있어야 합니다!!

## 특성
# 문자열 역시 리스트(list), 튜플(tuple)과 마찬가지로 sequence 형 자료구조를 가집니다.
# 문자열은 불변(immutable) 객체입니다.


## 문자열의 생성
# 파이썬의 문자열은 작은 따옴표(') 나 큰 따옴표(") 모두 구분없이 사용하여 문자열을 생성할 수 있습니다
# 작은 따옴표 3개 혹은 큰 따옴표 3개를 써서 여러 줄의 문자열을 생성할 수 있습니다.

sample = '''안녕하세요? 
반가워요
내이름은 
파이썬 입니다.'''

print(sample)


## 문자열 출력 (포맷팅)

# print() : 출력
print('문자열 첫째', '그리고, 둘째')

# end 옵션으로 출력될 마지막 글자를 변경할 수 있습니다. (기본값: \n)
# [참고] : \n 은 개행을 의미하는 특수 문자입니다.

print('여기까지!', end='end출력!')

# sep 옵션으로 출력될 문자열 사이에 출력될 글자를 변경할 수 있습니다. (기본값: 공백)

print('문자1', '문자1', '문자3', sep=' <구분> ')


## %를 사용한 출력

print("안녕하세요? %s" % ('반갑습니다.'))
print('안녕하세요? %d' % (12345))
print('안녕하세요? %c' % ('a'))

## {} 와 format를 사용한 출력
print('웰컴투? {}'.format('파이썬.'))
print('비밀번호 {}'.format(486))
print('원주율? {:.2f}'.format(3.141592))

## f 문자열 포맷팅 (python 3.6 이상만 지원)
name = '펭수'
age = 10
print(f'나의 이름은 {name}입니다. 나이는 {age} 살입니다.')
print(f'내년에 저는 {age+1} 살입니다.')

d = {'name':'펭수', 'age':10}
print(f"반가워요. 저는 {d['name']}입니다. 저의 나이는 {d['age']} 살입니다.")


## 문자열 길이
# 공백은 길이에 포함됩니다.
print(len('한글 킹왕짱'))

## 인덱싱 (indexing)
# 문자열에서 한 개의 글자(char)를 조회하기 위해서는 []를 활용한 인덱싱으로 조회할 수 있습니다.

a = 'Python is my life'
print(a[0])

## 슬라이싱 (Slicing)
# 슬라이싱의 활용: [start:stop:step] 을 명시하여 부분을 추출할 수 있습니다.

# [:]을 활용하여 전체를 추출할 수 있습니다.
print(a[:])

# [start:]는 시작 index 부터 끝까지 추출합니다.
print(a[3:])
print(a[-4:])

# [:end]는 처음부터 end 전까지 추출합니다.
print(a[:6])
print(a[:-3])

# [start:end]는 start부터 end 전까지 추출합니다.
print(a[3:6])

# [start:stop:step]에서 step 지정시 step만큼 건너 뛰면서 추출합니다.
print(a[::2])


## 문자열의 덧셈과 곱셈

# 연결: 문자열의 덧셈
# 덧셈은 문자열을 연결합니다.
a = '반갑습니다!'
b = '웰컴 투 파이썬'
print(a + b)

# 복제: 문자열의 곱셈
# 문자열을 곱한 숫자 만큼 반복하여 생성합니다.
print('abc ' * 5)
print('===' * 7)



## 문자열의 list, set

# 리스트(list)
# 문자열을 리스트(list)로 타입 변환이 가능합니다.
# 타입 변환시 한 글자를 요소로 갖는 리스트가 생성됩니다.

print(list('ABCDE'))


# 세트(set)
# 한 글자를 요소로 갖는 세트가 생성됩니다.
# 세트의 특성상 요소를 생성한 후 중복된 글자는 제거됩니다.

print(set('AAABBBCCC'))

# 중복이 제거된 리스트로 생성하기 위해서는 list로 다시 타입 변환합니다.

print(list(set('AAABBBCCC')))



## 문자열(텍스트)을 다루는 다양한 기능, 메서드(method)
# 문자열만 가지고 있는 고유의 편한 기능들이 있습니다.
# 우리는 이들 중 몇 가지를 배워 앞으로 유용하게 활용할 예정입니다.

## split() : 분리
# split은 문장을 특정 규칙에 의해 쪼개 주는 기능을 합니다.
# 분리한 결과는 list 형식으로 값을 return 받습니다.
a = 'This is a pen'
print(a.split())

# 기본 값인 공백에서 특정 문자로 지정할 수 있습니다.
a = 'This-is-a-pen'
print(a.split('-'))

## join() : 합치기
# 결합하고자 하는 문자에 .join() 안에 리스트를 지정하여 결합할 수 있습니다.
print('-'.join(['010',  '1234', '5678']))
print('-'.join('ABCDE'))


## lower(), upper() : 소문자 / 대문자로 만들기
a = 'My name is Teddy'
print(a.lower())
print(a.upper())


## startswith, endswith
# 시작과, 끝이 맞는지 결과를 bool로 반환합니다.

## startswith() : 시작하는
# 지정한 문자열로 시작하면 True, 그렇지 않다면 False를 반환합니다.
a = '01-sample.png'
print(a.startswith('01'))
print(a.startswith('012'))

## endswith() : 끝나는
# 지정한 문자열로 끝나면 True, 그렇지 않다면 False를 반환합니다.
print(a.endswith('.png'))
print(a.endswith('.jpg'))


## replace() : 문자열 바꾸기
# 문자열에 replace(바꿀 대상, 바꾸려는 문자열) 지정하여 문자열을 변경합니다.
# 결과는 복사본이 만들어져 반환됩니다.

a = '01-sample.png'
b = a.replace('.png', '.jpg')
print(a)
print(b)


## 불필요한 공백 제거
# lstrip() : 왼쪽 공백 제거
# rstrip() : 오른쪽 공백 제거
# strip() : 양쪽 공백 제거


a = '    01-sample.png                '
print(a.lstrip())
print(a.rstrip())
print(a.strip())