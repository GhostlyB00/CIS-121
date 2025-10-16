# question5 
#not sure why this isnt working
'''
def hailstone_seq(n):
    output_list = []
    while n >=1:
        if n % 2 == 0:
            n /= 2
        else:
            n = (3 * n) +1 
        print(n)
        output_list.append(n)
    return output_list

print(f" {hailstone_seq(25)}")
'''

def hailstone_seq(n):
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3*n + 1
        seq.append(n)
    return seq



