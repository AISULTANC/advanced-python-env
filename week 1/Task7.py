a = int(input())
op = input()
b = int(input())
print(a / b if op == '/' and b != 0 else
      "Error" if op == '/' and b == 0 else
      a + b if op == '+' else
      a - b if op == '-' else
      a * b)
