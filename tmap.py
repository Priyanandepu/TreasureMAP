row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = str(input("Where do you want to put the treasure? "))
p=int(position[0])
q=int(position[1])
E='X'
map[q-1].pop(p-1)
map[q-1].insert(p-1,E)
print(f"{row1}\n{row2}\n{row3}")
