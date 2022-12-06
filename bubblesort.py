import random

def BubbleSort(sList):
# 마지막 아이템의 인덱스를 저장
  lastidx = len(sList) - 1

# 모든 패스를 위한 바깥쪽 for loop
  for j in range (lastidx, 0, -1):

# 샘플리스트의 길이만큼 interation을 실행.
    for i in range(j):

# 왼쪽의 숫자가 오른쪽의 숫자보다 크다면 서로 값을 바꿔줌.
      if sList[i] > sList[i+1]:
        sList[i], sList[i+1] = sList[i+1], sList[i]


if __name__ == '__main__':
    # 1 패스 코드, 리스트 안에 가장 큰 숫자를 맨 오른쪽으로 옮김
    # 버블 정렬을 실행할 sampleList를 선언
    sList = [67,1,27,4,36,65,35,70,28,11]
    lastidx= len(sList) - 1

    # 샘플리스트의 길이만큼 interation을 실행.
    for i in range(lastidx):

    # 왼쪽의 숫자가 오른쪽의 숫자보다 크다면 서로 값을 바꿔줌.
        if sList[i] > sList[i+1]:
            sList[i], sList[i+1] = sList[i+1], sList[i]

        # 매 Iteration을 출력함으로써 가장 큰 숫자가 어떻게 옮겨지는지 확인.
        print(i+1, sList)

# 버블 정렬을 실행할 sampleList를 선언
    sList = [ random.randint(1,40) for i in range(1,10) ]
# 정렬전 리스트를 출력  
    print(sList)
# 버블 정렬 함수를 호출
    BubbleSort(sList)
# 정렬 후 리스트를 출력
    print(sList)


