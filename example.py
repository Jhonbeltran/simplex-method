from simplex import Simplex
objective = ('minimize', '4x_1 + 1x_2')
constraints = ['3x_1 + 1x_2 = 3', '4x_1 + 3x_2 >= 6', '1x_1 + 2x_2 <= 4']
Lp_system = Simplex(num_vars=2, constraints=constraints, objective_function=objective)
print(Lp_system.solution)
print(Lp_system.optimize_val)
