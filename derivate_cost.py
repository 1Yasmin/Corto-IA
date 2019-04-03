def derivate_cost(theta, X, y):
    m,n = X.shape
    h= np.matmul(X, theta)
    resta = (y - h)
    total = resta * X
    return resta.sum/m
