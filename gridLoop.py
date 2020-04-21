
# Turn the grid  a quarter turn on the right :

grid =[['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
print('Loop to see the grid :\n')
for donnee in grid:
	print(donnee)

print('\n------------\n')


print('Solution : \n')

cols = len(grid)

if cols:
	rows = len(grid[1])

print('Loop to see the "turn right" grid :\n')
for j in range(rows):
	for i in range(cols):
		print(grid[i][j], end = ' ')
	print()
