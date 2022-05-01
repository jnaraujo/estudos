from collections import deque

def main():
    qnt = int(input())

    for i in range(qnt):
        entrada = input()
        r = resolve(entrada)
        print("{:.2f}".format(r))

def formatInput(line):
    return line.strip().split(",")

def resolve(conta):
    queue = deque(formatInput(conta))

    stack = deque()
    
    index = 0
    while len(queue) > 0:
        atual = queue[index]

        if str(atual) not in "#-*/":
            stack.append(atual)
            queue.popleft()
        else:
            operacao = atual
            queue.popleft()

            value1 = float(stack.pop()) # ultimo valor
            value2 = float(stack.pop()) # penultimo valor

            res = 0

            if operacao == "#": # adicao
                res = value2 + value1
            elif operacao == "-": # subtracao
                res = value2 - value1
            elif operacao == "*": # multiplicacao
                res = value2 * value1
            elif operacao == "/": # divisao
                res = value2 / value1

            stack.append(res)

    return float(stack[0])

if __name__ == "__main__":
    main()