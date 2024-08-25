import numpy as np


def differentiate(u, dt):
    # t=0
    d = np.zeros(len(u))
    d0 = (u[1] - u[0]) / dt
    d[0] = d0

    # t=n
    for n in range(1, len(u) - 1):
        dn = (u[n + 1] - u[n - 1]) / (2*dt)
        d[n] = dn

    # t=Nt
    dN = (u[-1] - u[-2]) / dt
    d[-1] = dN

    return d

def differentiate_vector(u, dt):
    # t=0
    d = np.zeros(len(u))
    d0 = (u[1] - u[0]) / dt
    d[0] = d0

    # t=n
    d[1:-1] = (u[2:] - u[0:-2]) / (2*dt)

    # t=Nt
    dN = (u[-1] - u[-2]) / dt
    d[-1] = dN

    return d

def test_differentiate():
    t = np.linspace(0, 10, 11)
    dt = t[1] - t[0]
    u = t**2
    du = differentiate(u, dt)
    ru = 2*t
    ru[0] = 1
    ru[-1] = 19
    assert np.allclose(du, ru)

def test_differentiate_vector():
    t = np.linspace(0, 1, 10)
    dt = t[1] - t[0]
    u = t**2
    du1 = differentiate(u, dt)
    du2 = differentiate_vector(u, dt)
    assert np.allclose(du1, du2)

if __name__ == '__main__':
    test_differentiate()
    