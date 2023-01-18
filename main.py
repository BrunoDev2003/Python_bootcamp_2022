
from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle"])
table.add_column("Type", ["Electric", "Water"])


print(table)