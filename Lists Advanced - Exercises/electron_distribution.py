electrons_quantity = int(input())
electrons_shells = []
counter = 0
while 0 < electrons_quantity:
    counter += 1
    shell = 2 * counter ** 2
    if electrons_quantity >= shell:
        electrons_shells.append(shell)
        electrons_quantity -= shell
    else:
        electrons_shells.append(electrons_quantity)
        electrons_quantity = 0
print(electrons_shells)
