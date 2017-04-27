from simplex import Simplex
objective = ('max', '50x_1 + 80x_2')
constraints = ['1x_1 + 2x_2 <= 120', '1x_1 + 1x_2 <= 90', '1x_1 + 1x_2 >= 0']
Lp_system = Simplex(num_vars=2, constraints=constraints, objective_function=objective)
print(Lp_system.solution)
print(Lp_system.optimize_val)
