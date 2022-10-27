def InsertionSort(sList):
# 샘플 리스트의 길이 만큼 interation
    for i in range(1, len(sList)):
        # 정렬 전 리스트
        print('Begin', sList)
        # j 변수에는 왼쪽 아이템을 할당
        j = i - 1
        # nextItem 변수에는 오른쪽 아이템을 할당
        nextItem = sList[i]
        # 왼쪽 아이템 > 오른쪽 아이템 and 왼쪽 인덱스가 >= 0
        # 오른쪽에서 자리를 잃은 아이템이 왼쪽의 아이템보다 작을 수 있기때문에
        # 왼쪽 < 오른쪽의 조건을 만족할때까지 비교해줘야함
        while (sList[j] > nextItem) and (j >= 0):
            # 왼쪽 > 오른쪽 일 경우, 위치를 바꿔줌
            sList[j+1] = sList[j]
            # 자리를 잃은 아이템을 다른 왼쪽 아이템과 비교하기위해 j를 줄여줌
            j = j - 1
            # 왼쪽 > 오른쪽 일 경우 왼쪽 아이템이 오른쪽으로 옮겨갔음을 보여줌
            print("while", sList)
        # 자리를 잃은 아이템을 올바른 위치로 옮김
        sList[j+1] = nextItem
        # 자리를 잃은 아이템이 옮겨졌음을 보여줌
        print("for", sList)
    return sList

if __name__ == '__main__':
    sList = [67,1,27,4,36,65,35,70,28,11]
    print("result", InsertionSort(sList))