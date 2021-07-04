from numpy import cos, linspace
import matplotlib.pyplot as plt
import string, random, os, glob
# the model

def plot(A,B,C,D):
    fname = "static/" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8)) + ".png"

    x = linspace(-50, 50, 500)
    y = A*x**3 + B*x**2 + C*x + D

    plt.figure()
    plt.plot(x,y)
    plt.title(f"Cubic Function: {A}*x**3 + {B}*x**2 + {C}*x + {D}")

    if not os.path.isdir('static'):
        os.mkdir('static')
    else: # Remove oldplotfiles
        for filename in glob.glob(os.path.join('static', '*.png')):
            os.remove(filename)

    plt.savefig(fname)
    return fname