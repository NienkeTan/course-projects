import numpy as np
#import plotly.express as px


def mesh_function(f, t):
    result = np.array([])
    for time in t:
        result = np.append(result, f(time))
    #fig = px.line(x=t, y=result)
    #fig.show()
    return result

def func(t):
    if 0 <= t <= 3:
        return np.exp(-t)
    elif 3 < t <= 4:
        return np.exp(-3*t)

def test_mesh_function():
    t = np.array([1, 2, 3, 4])
    f = np.array([np.exp(-1), np.exp(-2), np.exp(-3), np.exp(-12)])
    fun = mesh_function(func, t)
    assert np.allclose(fun, f)