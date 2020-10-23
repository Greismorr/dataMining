import pandas as pd

csv_file = pd.read_csv("data/mercadinho.csv")
file = open("naive.txt", "a")

csv_count_rows = len(csv_file.index)
csv_file.set_index('TID', inplace=True)

count = 0
number_of_rows = len(csv_file.index)
list_of_columns = csv_file.columns.values.tolist()

for index, column in csv_file.iteritems():
    instances = 0
    instances_antecedent_column = 0
    position = 0

    first_column = csv_file[list_of_columns[count]]
    second_column = csv_file[list_of_columns[count+1]]

    list_first_column = list(first_column)
    list_second_column = list(second_column)

    print("Checando suporte entre " + list_of_columns[count] + " e " + list_of_columns[count + 1])

    for element in list_first_column:
        if list_first_column[position] == 'sim':
            instances_antecedent_column += 1

            if list_second_column[position] == 'sim':
                instances += 1

        position += 1

    print("Suporte entre " + list_of_columns[count] + " e " + list_of_columns[count + 1] + " é de " + str(instances/number_of_rows)
          + "(" + str((instances/number_of_rows) * 100) + "%)")
    file.write("Suporte entre " + list_of_columns[count] + " e " + list_of_columns[count + 1] + " é de " + str(instances/number_of_rows)
          + "(" + str((instances/number_of_rows) * 100) + "%)\n")

    print("Confiança entre " + list_of_columns[count] + " e " + list_of_columns[count + 1] + " é de " + str(instances/instances_antecedent_column)
          + "(" + str((instances/number_of_rows) * 100) + "%)")
    file.write("Confiança entre " + list_of_columns[count] + " e " + list_of_columns[count + 1] + " é de " + str(instances/instances_antecedent_column)
          + "(" + str((instances/number_of_rows) * 100) + "%)\n")
    print("\n\n\n")
    file.write("\n")
    
    if count < (len(list_of_columns) - 2):
        count += 1

file.close()