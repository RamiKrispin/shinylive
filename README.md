This repo provides an example of a [Shinylive](https://shiny.rstudio.com/py/docs/shinylive.html) app. Shinylive enables to create q serverless Shiny applications with Python. Leveraging [WebAssembly](https://webassembly.org/), it can run the Shiny app on the web browser without a server on the backend.


### Example

Inspired by Prop. Richard McElreath's explanation about why normal distribution is normal in [Statistical Rethinking](https://xcelab.net/rm/statistical-rethinking/) chapter 3, created the following app:

<img src="images/app screenshot.png" width="100%" align="center"/></a>
### Why normal distributions are normal
Chapter 3 illustrates how to generate a normal distribution using the soccer field experiment:
Place a bunch of people at the center line of a soccer field
Each person flips a coin and moves one step to the right or left according to the outcome (head or tail)
Repeat this process multiple times
After a couple of iterations, you will notice the distribution of the people's distances across the field will become Gaussian or normal (e.g., bell-curved shape).

The app above simulates this experience by setting the sample size (i.e., number of people) and number of iterations. Where on each iteration, we draw a random number between -1 and 1 (can choose between float integer steps with the Step Type drop-down). The plot above shows the cumulative sum of each experiment across each step of the experience. You can notice how the distribution becomes more Gaussin as the number of steps increases.
