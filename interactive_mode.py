def get_valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value == 0 and prompt == 'a = ':
                print("Error. a cannot be 0")
                continue
            return value
        except ValueError:
            print(f"Error. Expected a valid real number, got {input} instead")
