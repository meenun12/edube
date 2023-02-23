def read_int(prompt, min, max):

    v = input(prompt)

    try:
        assert int(v) >= min and int(v) <= max
    except AssertionError:
        print(f"Error: the value is not within permitted range ({min}..{max})")
    except Exception:
        print(f"Error: wrong input")
    else:
        print("The number is:", v)

v  = read_int("Enter a number from -10 to 10: ", -10, 10)



