# the values must be sorted
pos = -1


def search(list, n):
    l = 0
    u = len(list) - 1
    while l <= u:
        mid = (l + u) // 2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    # return False

list = [4, 7, 8, 9, 15, 45, 99]
key = 999

if search(list, key):
    print("Found at ", pos + 1)
else:
    print("Not Found")
