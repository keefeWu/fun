class Number:
    def __init__(self, min_, max_):
        self.min = min_
        self.max = max_
        self.val = min_

A = Number(1, 9)
B = Number(1, 9)
C = Number(1, 9)
D = Number(1, 9)
E = Number(0, 9)
F = Number(0, 9)
G = Number(0, 9)
H = Number(1, 9)
I = Number(1, 9)
J = Number(1, 9)
K = Number(1, 9)


numberList = [A, B, C, D, E, F, G, H, I, J, K]

def check():
    for i in range(len(numberList)):
        print(numberList[i].val, end=' ')
    print('\n')

    status = True
    if not (A.val * C.val == H.val):
        status = False
    if not (D.val * 10 + E.val - H.val == I.val):
        status = False
    if not (B.val * C.val == J.val):
        status = False
    if not (I.val * 10 + F.val - J.val == K.val):
        status = False
    if not (3 * C.val == 10 * K.val + G.val):
        status = False
    if not (3 * C.val == 10 * K.val + G.val):
        status = False
    return status

def run(id):
    #最后一位了
    if id == len(numberList) - 1:
        for i in range(numberList[id].min, numberList[id].max):
            numberList[id].val = i
            if check():
                print('find the answer!!')
                exit(0)
        return 
    for i in range(numberList[id].min, numberList[id].max):
        numberList[id].val = i
        run(id+1)

for i in range(numberList[0].min, numberList[0].max):
    run(1)
    