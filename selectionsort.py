sList=[9,8,6,3,5,1]
n = len(sList)
print("Start: ", sList)
# 바깥 반복문, 리스트의 마지막 인덱스 -1 까지 반복
for i in range(n):
    # 최소값 인덱스를 저장할 변수 선언. 인덱스 i 부터 시작. 
    minIndex = i
    # 안쪽 반복문, i+1부터 리스트의 마지막 인덱스 까지 반복
    for j in range(i+1, n):
        # 리스트[j] (다음값 혹은 오른쪽값) 이 리스트[minIndex](이전값 혹은 왼쪽값) 보다 작다면 minIndex에 인덱스 값을 저장
        if sList[j] < sList[minIndex]:
                minIndex = j
    # 리스트의 가장 왼쪽자리의 값과 minIdex에 위치한 값을 서로 바꿔준다.
    sList[i], sList[minIndex] = sList[minIndex], sList[i]

print("Sorted: ", sList)