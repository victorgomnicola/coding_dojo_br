name = input()
base_salary = float(input())
total_sold = float(input())
final_salary = base_salary + 0.15*total_sold
print('TOTAL = R$', '{0:.2f}'.format(final_salary))
