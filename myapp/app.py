# Dependencies
from shiny import App, render, ui
from numpy import random 
import pandas as pd
import matplotlib.pyplot as plt

# Functions
def random_steps(steps = 16, type = "float", low = -1, high = 1):
    if type == "int":
        r = random.randint(low = low, high=high, size= steps, dtype=int).tolist()
        r = [high if i == 0 else i for i in r]
    elif type == "float":
        r = (high - low) * random.random_sample(size = steps) + low
    else:
        print("The type argument is not valid")
        return
    return r

def cumsum(l):
    c = []
    t = 0
    for i in range(0, len(l)):
        t += l[i]
        c.append(t)
    return(c)

def sim_steps(sim_number = 10, steps = 16, type = "float"):
    s = []
    d = pd.DataFrame()
    for i in range(0, sim_number):
        v1 = [0]
        v2 = random_steps(steps = steps, type = type)
        if not isinstance(v2, list):
            v2 = v2.tolist()
        v = cumsum(v1 + v2)
        d_temp = pd.DataFrame({"sim": i, "step": range(0, len(v)), "y": v})
        d = pd.concat([d, d_temp])
    return d


# UI
app_ui = ui.page_fluid(
        ui.layout_sidebar(
            ui.panel_sidebar(
                ui.h2("Why normal distributions are normal"),
                ui.input_slider("sample_size", "Sample Size", 1, 1000, 500),
                ui.input_slider("steps", "Number of Steps", 1, 20, 16),
                ui.input_select("step", "Step Type", {"float": "Float", "int": "Integer"}),
                ui.input_slider("alpha", "Color Opacity", 0, 1, 0.2)
            ),
        ui.panel_main(
            ui.output_plot("plot"),
            ui.markdown(
        """
        ### Why normal distributions are normal

        Chapter 3 of [Statistical Rethinking's](https://xcelab.net/rm/statistical-rethinking/) by Prof. Richard McElreath focuses on normal distribution
        and its characteristics. It illustrates how to generate a normal distribution using the soccer field experiment:

        - Place a bunch of people at the center line of a soccer field
        - Each person flips a coin and moves one step to the right or left according to the outcome (head or tail)
        - Repeat this process multiple times
        After a couple of iterations, you will notice the distribution of the people's distances across the field will become Gaussian or normal (e.g., bell-curved shape).

        The app above simulates this experience by setting the sample size (i.e., number of people) and number of iterations. Where on each iteration, we draw a random number between -1 and 1 (can choose between float integer steps with the `Step Type` drop-down). The plot above shows the cumulative sum of each experiment across each step of the experience. You can notice how the distribution becomes more Gaussian as the number of steps increases.

        Code available [here](https://github.com/RamiKrispin/shinyelive).

        """
    ),
        )
    )
)

# Server
def server(input, output, session):
    @output
    @render.plot(alt="A simulation plot")
    def plot():
        type = input.step()
        color = "lightblue"
        alpha = input.alpha()
        sim_number = input.sample_size()
        steps = input.steps()
        sim_df = sim_steps(sim_number = sim_number, steps = steps, type = type)
        fig, ax = plt.subplots()
        for i in sim_df.sim.unique():
            df = sim_df[sim_df["sim"] == i]
            ax.plot(df["step"], df["y"], color = color, alpha= alpha)

        ax.set_title(label = "Simulation of Random Walk")
        ax.set_xlabel("Number of Steps")
        ax.set_ylabel("Position")
        return fig


app = App(app_ui, server)
