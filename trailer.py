from manim import *

class Quantum8LinesTrailer(MovingCameraScene):
    def construct(self):
        title = Text("Quantum8Lines", font_size=72, weight=BOLD)
        subtitle = Text("Visual Intuition in Motion", font_size=36)
        subtitle.next_to(title, DOWN)
        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=DOWN))
        self.wait(1)

        equation = MathTex(r"\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}", font_size=48)
        equation.to_edge(UP)
        self.play(Write(equation))
        self.wait(1)

        circle = Circle(radius=1.0, color=BLUE).shift(LEFT*3)
        square = Square(side_length=2.0, color=GREEN).shift(RIGHT*3)
        triangle = Triangle(color=YELLOW).scale(1.5)
        triangle.move_to(UP*2)
        self.play(Create(circle), Create(square), Create(triangle))
        self.wait(1)

        self.play(circle.animate.shift(RIGHT*3), square.animate.shift(LEFT*3), triangle.animate.shift(DOWN*2))
        self.wait(1)

        self.play(self.camera.frame.animate.move_to(UP*1.5).scale(0.8))
        self.wait(1)

        highlight_text = Text("Explore, Animate, Understand", font_size=48, color=ORANGE)
        highlight_text.move_to(DOWN*2)
        self.play(FadeIn(highlight_text))
        self.wait(1)

        outro_text = Text("Quantum8Lines", font_size=72, weight=BOLD)
        outro_text.set_color_by_gradient(BLUE, PURPLE)
        self.play(Transform(title, outro_text))
        self.play(FadeOut(subtitle), FadeOut(equation), FadeOut(circle), FadeOut(square), FadeOut(triangle))
        self.play(title.animate.scale(1.2))
        self.wait(2)
