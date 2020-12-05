import time

current_milli_time = lambda: int(round(time.time() * 1000))


def sum2020(data):
    print('start data scan')
    for i in data:
        for j in data:
            for k in data:
                if i + j + k == 2020:
                    return i, j, k
    return None


if __name__ == "__main__":
    start = current_milli_time()

    file1 = open('in', 'r')
    Lines = file1.readlines()

    data = [int(i) for i in Lines]

    data.sort()
    j, i, k = sum2020(data)
    print(i * j * k)
    end = current_milli_time() - start