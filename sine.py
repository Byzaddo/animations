from manim import *
import numpy as np
import math

class SineTaylorApproximation(Scene):
    def construct(self):
        # Set up axes (no coordinates to avoid cluttered x-axis labels)
        axes = Axes(
            x_range=[-4 * math.pi, 4 * math.pi, math.pi],
            y_range=[-2, 2, 1],
            x_length=10,
            y_length=6,
            axis_config={"color": WHITE},
            tips=False,
        )

        # Labels for axes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        self.add(axes, x_label, y_label)

        # Sine graph
        sine_graph = axes.plot(
            lambda x: np.sin(x),
            color=BLUE,
            x_range=[-4 * math.pi, 4 * math.pi],
        )
        sine_label = MathTex(r"y = \sin(x)").next_to(axes, UP, buff=0.5).set_color(BLUE)

        # Add sine graph and label
        self.play(Create(sine_graph), Write(sine_label))
        self.wait(1)

        # Taylor series approximation function
        taylor_series = lambda x, n: sum(
            (-1) ** k * x ** (2 * k + 1) / math.factorial(2 * k + 1) for k in range(n + 1)
        )

        # Animate Taylor series approximation
        taylor_graph = None
        taylor_label = None
        for n in range(1, 11):  # Increase the degree of the polynomial
            new_taylor_graph = axes.plot(
                lambda x: taylor_series(x, n),
                color=RED,
                x_range=[-4 * math.pi, 4 * math.pi],
            )
            new_taylor_label = MathTex(
                f"y = \\sum_{{k=0}}^{{{n}}} \\frac{{(-1)^k x^{{2k+1}}}}{{(2k+1)!}}"
            ).to_corner(UR).set_color(RED)

            if taylor_graph:
                self.play(
                    Transform(taylor_graph, new_taylor_graph),
                    Transform(taylor_label, new_taylor_label),
                )
            else:
                taylor_graph = new_taylor_graph
                taylor_label = new_taylor_label
                self.play(Create(taylor_graph), Write(taylor_label))

            self.wait(1)

        self.wait(2)
