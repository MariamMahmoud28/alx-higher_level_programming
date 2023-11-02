#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    
    a = 10
    b = 5
    
    result_add = add(a, b)
    result_sub = sub(a, b)
    result_mul = mul(a, b)
    result_div = div(a, b)
    
    print(f"10 + 5 = {result_add}")
    print(f"10 - 5 = {result_sub}")
    print(f"10 * 5 = {result_mul}")
    print(f"10 / 5 = {result_div}")

