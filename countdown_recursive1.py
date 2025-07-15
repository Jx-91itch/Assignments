def countdown(n):

    print(n)

    if n == 1:
        return

    else:
        countdown(n - 1)#method must call itself
countdown(10)