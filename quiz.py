# testing
# 202100796 김승진 컴퓨터공학과

from random import shuffle

majorList = ['컴퓨터공학과', '경영학과', '영어영문학과']
nameList = ['김승진', '김승철', '김승연']

print('이제부터 제 소개를 얼마나 주의깊게 들었는지 확인하겠습니다.')

while True:
  shuffle(majorList)

  majorAns = majorList.index('컴퓨터공학과') + 1
  print('\n1단계 문제입니다.\n저의 학과에 해당하는 번호를 고르십시오.')
  
  for i in range(len(majorList)):
    print(i + 1, '. ', majorList[i], sep = '')

  if input() == str(majorAns):
    print('정답입니다. 1단계를 통과하셨습니다.')
    break
  else:
    print('오답입니다. 다시 시도하십시오.')
    
while True:
  shuffle(nameList)
  
  nameAns = nameList.index('김승진') + 1
  print('\n2단계 문제입니다.\n저의 이름에 해당하는 번호를 고르십시오.')
  
  for i in range(len(nameList)):
    print(i + 1, '. ', nameList[i], sep = '')

  if input() == str(nameAns):
    print('정답입니다. 2단계를 통과하셨습니다.')
    break
  else:
    print('오답입니다. 다시 시도하십시오.')
    
while True:
  numAns = 202100796
  print('\n마지막 3단계 문제입니다.\n저의 학번에 해당하는 번호를 고르십시오.')
  
  for i in range(10):
    print(i + 1, '. ', numAns - i + 2, sep = '')

  if input() == '3':
    print('정답입니다. 저에게 관심이 많으시군요.')
    break
  else:
    print('오답입니다. 다시 시도하십시오.')
