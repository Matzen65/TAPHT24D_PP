
def pretty_print(list):

    if len(list) > 0:
        print(f"Listan har {len(list)} element:")

        for element in list:
            i = list.index(element) + 1
            print(f"{i}: {element}")
    else:
        print("Listan är tom")
