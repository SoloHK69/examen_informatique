#coding:utf-8

def display_sum_of_products(truth_table, variable_names):

    number_of_variables = len(truth_table[0]) - 1
    true_rows = [i for i in range(len(truth_table)) if truth_table[i][-1] == 1]

    canonical_form = ""
    for row in true_rows:
        canonical_form += "("
        for i in range(number_of_variables):
            value = truth_table[row][i]
            if value == 1:
                canonical_form += variable_names[i]
            else:
                canonical_form += f" NOT({variable_names[i]})"
        canonical_form += ") OR "

    canonical_form = canonical_form[:-3]
    print(f"The sum of products is:\n{canonical_form}")

def display_product_of_sums(truth_table, variable_names):

    number_of_variables = len(truth_table[0]) - 1
    false_rows = [i for i in range(len(truth_table)) if truth_table[i][-1] == 0]

    canonical_form = ""
    for row in false_rows:
        canonical_form += "("
        for i in range(number_of_variables):
            value = truth_table[row][i]
            if value == 0:
                canonical_form += variable_names[i]
            else:
                canonical_form += f" NOT({variable_names[i]})"
        canonical_form += ") AND "

    canonical_form = canonical_form[:-3]
    print(f"The product of sums is:\n{canonical_form}")

def get_user_input():

    try:
        num_variables = int(input("Enter the number of variables: "))
    except ValueError:
        print("Invalid input. Please enter an integer for the number of variables.")
        return None, None, None

    variable_names = []
    for i in range(num_variables):
        variable_names.append(input("Enter the name of variable {}: ".format(i + 1)))

    logic_function = input("Enter the logical function (e.g., a and b or not c): ")
    function_python = logic_function.replace("et", "and").replace("ou", "or").replace("non", "not")
    return num_variables, variable_names, function_python

def power_of_two(n):
  return 1 if n == 0 else 2 * power_of_two(n-1)

def create_truth_table(num_variables):

    values = [0, 1]
    truth_table = []

    for i in range(power_of_two(num_variables)):
        combination = []
        for j in range(num_variables):
            combination.append(values[i % 2])
            i //= 2
        truth_table.append(combination)
    return truth_table

def evaluate_function(function_python, variable_values):

    try:
        function_result = eval(function_python, variable_values)
    except (NameError, SyntaxError) as e:
        print("Error evaluating expression:", e)
        return None
    return function_result

def print_header(variable_names):

    print("=" * (14 + 5 * len(variable_names)))
    print("| ", end="")
    for name in variable_names:
        print(f"{name:^5}", end="")
    print("| F({})".format(", ".join(variable_names)))
    print("=" * (14 + 5 * len(variable_names)))

def print_row(row):

    print("| ", end=" ")
    for value in row:
        print(f"{value:^5}", end="")
    print("| ")

def main():
    num_variables, variable_names, function_python = get_user_input()
    if num_variables is None:
        return

    truth_table = create_truth_table(num_variables)

    for i in range(len(truth_table)):
        variable_values = dict(zip(variable_names, truth_table[i]))
        result = evaluate_function(function_python, variable_values)
        if result is not None:
            truth_table[i].append(result)

    print_header(variable_names)

    for row in truth_table:
        print("| ", end="")
        for value in row:
            print(f"{value:^4}", end=" ")
        print("|")

    display_sum_of_products(truth_table.copy(), variable_names)
    display_product_of_sums(truth_table.copy(), variable_names)

if __name__ == "__main__":
	main()                                                                               