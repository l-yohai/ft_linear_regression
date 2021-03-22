import pandas as pd


def check_number(f, n):
    try:
        n = f(n)
    except:
        exit("Value error")
    return n


if __name__ == '__main__':
    try:
        with open('output.txt', 'r') as f:
            if f.mode == 'r':
                theta = []
                lines = f.readlines()
                for x in lines:
                    theta.append(check_number(float, x))
    except:
        theta = [0, 0]
    print('Theta:', theta)

    d = input('차량의 주행거리를 입력하세요.\n')
    d = check_number(float, d)
    p = theta[0] + theta[1] * d
    print('입력하신 차량의 예측 가격:', p)
