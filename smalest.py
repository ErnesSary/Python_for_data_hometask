largest = None
smallest = None

while True:
    s = input("Enter a number (or 'done' to finish): ")
    if s == "done":
        print("Done")
        break

    try:
        num = int(s)
    except:
        print("Error. Enter a valid number")
        continue

    if largest is None or num > largest:
        largest = num

    if smallest is None or num < smallest:
        smallest = num
print("Largest:", largest)
print("Smallest:", smallest)


