# WAP to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

amount = int(input("Enter the amount: "))
notes = [500, 100, 50, 20, 10, 5, 1]
for note in notes:
    count = amount // note
    amount = amount % note
    print(note, "=", count)
