def countdown_range_recursive(start,end):
    print(end)
    if start==end:
        return
    else:
        countdown_range_recursive(start,end-1)

start = int(input("Enter the first number in the range: "))
end = int(input("Enter the Last number in the range: "))

countdown_range_recursive(start,end)