import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

START = int(input("start:"))
END = int(input("end:"))
STEP = 100  
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)

x = np.linspace(START,END,STEP)
l, = ax.plot(x, np.zeros_like(x), lw=2)


def submit(expression):
    """
    Update the plotted function to the new math *expression*.

    *expression* is a string using "x" as its independent variable, e.g.
    "x ** 3".
    """
    ydata = eval(expression)
    l.set_ydata(ydata)
    ax.relim()
    ax.autoscale_view()
    plt.draw()


axbox = fig.add_axes([0.1, 0.05, 0.8, 0.075])
ax.spines['left'].set_position(('data', 0))
text_box = TextBox(axbox, "Evaluate")
text_box.on_submit(submit)
text_box.set_val("x ** 2")  # Trigger `submit` with the initial string.

plt.show()