
def myreverse(data):
    str_len = len(data)
    half_len = str_len//2
    first_half = data[0:half_len]
    second_half = data[half_len:]
    first_list = list(first_half)
    second_list = list(second_half)

    while True:
        remover = second_list[-1]
        if remover != first_list[0]:
            break
        second_half_len = len(second_list)
        for i in range(-1, -second_half_len, -1):
            if second_list[-1] == remover:
                second_list.pop(-1)
            else:
                break
        my_len = len(first_list)
        for i in range(my_len):
            if first_list[0] == remover:
                first_list.pop(0)
            else:
                break

    final_str = "".join(second_list)+"".join(first_list)
    print(final_str)
    return len(final_str)

print(myreverse('aabcccabba'))