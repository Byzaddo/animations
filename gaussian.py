from manim import *

class GaussianIntegralFinalUpdated(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # Axes setup
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            axis_config={"include_numbers": False, "include_ticks": True, "color": WHITE},
            tips=False
        )
        self.play(Create(axes))

        # Plot curve and area under e^{-x^2}
        curve = axes.plot(lambda x: np.exp(-x**2), color=BLUE)
        area = axes.get_area(curve, x_range=[-4, 4], color=BLUE, opacity=0.3)
        curve_label = MathTex(r"y = e^{-x^2}", color=BLUE).scale(0.9).next_to(curve, UP).shift(RIGHT * 2)
        self.play(Create(curve), FadeIn(area), Write(curve_label))
        self.wait(1)

        # Original integral
        integral = MathTex(r"\int_{-\infty}^\infty e^{-x^2} dx").to_corner(UR).shift(DOWN * 0.5 + LEFT * 0.5)
        self.play(Write(integral))
        self.wait(1)

        # Remove graph
        self.play(FadeOut(axes), FadeOut(curve), FadeOut(area), FadeOut(curve_label))

        # Step-by-step transformation
        steps = [
            r"I = \int_{-\infty}^\infty e^{-x^2} dx",
            r"I^2 = \left(\int_{-\infty}^\infty e^{-x^2} dx\right)^2",
            r"= \int_{-\infty}^\infty \int_{-\infty}^\infty e^{-(x^2+y^2)} dx\,dy",
        ]
        current = MathTex(steps[0]).scale(1.2)
        self.play(Write(current))
        self.wait(1)

        for step in steps[1:]:
            next_step = MathTex(step).scale(1.2)
            self.play(Transform(current, next_step))
            self.wait(1)

        # Jacobian derivation — move to top-left
        self.wait(0.5)
        jacobian_parts = VGroup(
            MathTex(r"x = r\cos\theta,\quad y = r\sin\theta").scale(0.9),
            MathTex(r"\mathbf{J}(r,\theta) = \begin{bmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{bmatrix}").scale(0.9),
            MathTex(r"\Rightarrow |\mathbf{J}(r,\theta)| = r").scale(0.9),
            MathTex(r"dx\,dy = r \, dr \, d\theta").scale(0.9)
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)

        for part in jacobian_parts:
            self.play(Transform(part))
            self.wait(1)

        self.play(*[Write(mob) for mob in jacobian_parts])
        self.wait(2)

        # Fade out Jacobian stuff and show substituted integral
        self.play(FadeOut(jacobian_parts))

        polar = MathTex(
            r"= \int_0^{2\pi} \int_0^\infty e^{-r^2} \cdot r \, dr \, d\theta"
        ).scale(1.2)
        self.play(Transform(current, polar))
        self.wait(1)

        factor_out = MathTex(
            r"= 2\pi \int_0^\infty e^{-r^2} r \, dr"
        ).scale(1.2)
        self.play(Transform(current, factor_out))
        self.wait(1)

        eval = MathTex(
            r"= 2\pi \cdot \frac{1}{2}"
        ).scale(1.2)
        self.play(Transform(current, eval))
        self.wait(1)

        result = MathTex(
            r"I^2 = \pi \Rightarrow I = \sqrt{\pi}"
        ).scale(1.2)
        self.play(Transform(current, result))
        self.wait(2)

        final = MathTex(
            r"\int_{-\infty}^\infty e^{-x^2} dx = \sqrt{\pi}"
        ).scale(1.2)
        box = SurroundingRectangle(final, color=RED, buff=0.1)
        self.play(Transform(current, final))
        self.add(final)  # Ensure 'final' is added to the scene
        self.play(Create(box))
        self.wait(3)
        