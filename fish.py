# 두개의 비지 않은 배열 A,B를 받을거야
# 정수 N 으로 이루어져 있지
# N 들은 탐욕스러운 물고기들을 의미하지
# 강을따라 배치돼있지
# 물고기들은 0 ~ N-1 까지 있지
# P, Q 가 두 물고기라고 치면  P < Q 의 관계를 가져
# P 는 Q 보다 윗물에 있을거야
# 그래서 각각의 물고기들은 다른 위치를 가지지
# A 는 물고기의 사이즈를 결정하고 B 는 물고기의 방향을 가지고 0,1만 가질 수 있어
# 서로 방향이 반대일경우 언젠가 만나지


def fish(A: list, B: list) -> int:
    if len(A) == 1:
        return 1

    arr = list()

    for i in range(len(A)):
        arr.append((A[i], B[i]))

    res = list()
    res.append(arr[0])

    for i in range(1, len(arr)):
        while True:
            if arr[i][1] == 0 and res[-1][1] == 1:
                if arr[i][0] < res[-1][0]:
                    break
                else:
                    del res[-1]
                    if len(res) == 0:
                        res.append(arr[i])
                        break
            else:
                res.append(arr[i])
                break

    return len(res)


if __name__ == '__main__':
    print(fish([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]))
