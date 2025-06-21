def ok(n):
    if n == 0:
        print("nombre paire")
    elif n == 1:
        print("nombre impaire")
    else:
        ok(n-2)

print("choose a number")
my_var=int(input())
ok(my_var)
