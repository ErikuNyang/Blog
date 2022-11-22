i = 0

def MergeSort(list):
    global i
    if len(list)>1:
        # 리스트를 반으로 나눕니다.
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]

        # 나뉜 부분의 크기가 1이 될때까지 반복합니다.
        MergeSort(left)
        MergeSort(right)

        a,b,c, = 0,0,0

        # 왼쪽과 오른쪽의 길이가 0 보다 클 경우
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                list[c] = left[a]
                a = a + 1
            else:
                list[c] = right[b]
                b = b + 1
            c = c + 1
        
        while a < len(left):
            list[c] = left[a]
            a = a + 1
            c = c + 1

        while b < len(right):
            list[c] = right[b]
            b = b + 1
            c = c + 1
    print(f"{i} 리스트", list)
    i = i + 1
    return list

i = 0
list = [44, 16, 83, 7, 67, 21, 34, 45, 10]
MergeSort(list)
print(list)
