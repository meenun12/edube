def read_int(prompt, max):

    v = input(prompt)

    try:
        assert int(v) != 0
    except AssertionError:
        print(f"Error: the value is not within permitted range ({max})")
    except Exception:
        print(f"Error: wrong input")
    else:
        print("The number is:", v)

v  = read_int("Enter a number from -10 to 10: ", max)



