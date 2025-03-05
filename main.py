print("Welcome to the Mariik Restaurant Table Finder!!")

table_chart = [
    ['T1(2)', 'T2(4)', 'T3(2)', 'T4(6)', 'T5(4)', 'T6(2)'],
    ['x', 'o', 'o', 'o', 'o', 'x'],
    ['o', 'x', 'o', 'o', 'x', 'o'],
    ['x', 'x', 'o', 'x', 'o', 'o'],
    ['o', 'o', 'o', 'x', 'o', 'x'],
    ['o', 'x', 'o', 'x', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'x', 'o']
]

free_tables = []
for col in range(len(table_chart[0])):
    for row in range(1, len(table_chart)):
        if table_chart[row][col] == 'o':
            free_tables.append(table_chart[0][col])
            break

print("These are our available tables (free tables):")
for table in free_tables:
    print("-", table)
print()

party_size = int(input("What is the size of your party? [enter a number 1 to 6]: "))
selected_table = None
for col in range(len(table_chart[0])):
    table_id = table_chart[0][col]
    capacity = int(table_id[table_id.index('(')+1:table_id.index(')')])
    for row in range(1, len(table_chart)):
        if table_chart[row][col] == 'o' and capacity >= party_size:
            selected_table = table_id
            break
    if selected_table:
        break

if selected_table:
    print(f"{selected_table} is available.")
else:
    print("")
print()

suitable_tables = []
for col in range(len(table_chart[0])):
    table_id = table_chart[0][col]
    capacity = int(table_id[table_id.index('(')+1:table_id.index(')')])
    for row in range(1, len(table_chart)):
        if table_chart[row][col] == 'o' and capacity >= party_size:
            suitable_tables.append(table_id)
            break

if suitable_tables:
    print("Tables for your party size:")
    for table in suitable_tables:
        print("-", table)
else:
    print("No suitable tables found for your party size.")