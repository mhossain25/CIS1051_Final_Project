choice = input("Type 'D' to manually insert your own cash flows or type 'S' to insert a type of series.")
choice = choice.upper()
if choice == 'D':
    import DCF
elif choice == 'S':
    import seriesCF
else:
    print("You didn't select an option.")