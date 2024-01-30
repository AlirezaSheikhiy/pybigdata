from pybigdata import optimization as OPT

x_0 = 1
df = lambda x: 5 * (x + 3)

OPT.simple_gradient_descent(df, x_0)
