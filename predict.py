import pandas as pd


def check_number(f, n):
    try:
        n = f(n)
    except:
        exit("올바른 값이 아닙니다.")
    return n


if __name__ == '__main__':
    try:
        with open('output.txt', 'r') as f:
            if f.mode == 'r':
                theta = []
                lines = f.readlines()
                for x in lines:
                    check_number(float, x)
    except FileNotFoundError:
        theta = [0, 0]
    except:
        exit('output 파일에 올바르지 않은 값이 포함되어 있습니다.')
    else:
        for x in lines:
            theta.append(check_number(float, x))
    print('Theta:', theta)

    d = input('차량의 주행거리를 입력하세요.\n')
    if (d.isnumeric() is False or int(d) < 0):
        exit('양의 정수만 입력해주세요.')
    d = check_number(float, d)
    p = theta[0] + theta[1] * d
    print('입력하신 차량의 예측 가격:', p)
