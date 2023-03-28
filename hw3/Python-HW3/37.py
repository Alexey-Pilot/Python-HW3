
def revert(n):
    x = input()
    if n == 1:
        return x
    return revert(n - 1) + " " + x

print(revert(5))