
def Nf(z,f,df):
    return z - f(z)/df(z)

def runNewton(z, f, df, maxiter, epsilon):
    for i in range(maxiter):
        if(df(z)==0): return (False,z)
        z = Nf(z,f,df)
        if abs(f(z))<=epsilon : return (True,z)
    return (False,z)

print(runNewton(1+3j,lambda x : x**3 - 1, lambda x : 3*x**2, 100, 0.001))