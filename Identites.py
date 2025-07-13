from manim import *
import numpy as np

class Trig_Basics(Scene):
    def construct(self):
        # Title
        title = Text(
            "Հիմնական\n\nԵռանկյունաչափական\n\nՆույնությունները",
            font_size=36,
        )
        self.play(Write(title), run_time=4)
        self.wait(1)
        self.play(FadeOut(title))
        self.wait(1)

        # Identity 1
        i1 = MathTex(r'\tan x \cdot \cot x = \frac{\sin x}{\cos x} \cdot \frac{\cos x}{\sin x}')
        self.play(Write(i1[0][:10], run_time = 2))
        self.play(Indicate(i1[0][:4], run_time = 4), Write(i1[0][10:19], run_time = 3))
        self.play(Indicate(i1[0][5:9], run_time = 4), Write(i1[0][19:29], run_time = 3))

        sin_top = i1[0][10:14]
        sin_bot = i1[0][25:29]

        sline1 = Line(sin_top.get_corner(DL), sin_top.get_corner(UR), color=RED)
        sline2 = Line(sin_bot.get_corner(DL), sin_bot.get_corner(UR), color=RED)

        self.play(Create(sline1), Create(sline2))
        self.wait(1)

        cos_top = i1[0][15:19]
        cos_bot = i1[0][20:24]

        cline1 = Line(cos_top.get_corner(DL), cos_top.get_corner(UR), color=BLUE_E)
        cline2 = Line(cos_bot.get_corner(DL), cos_bot.get_corner(UR), color=BLUE_E)

        self.play(Create(cline1), Create(cline2))
        self.wait(1)
        one = MathTex(r'1').next_to(i1[0][:10], RIGHT)
        self.play(
            ReplacementTransform(i1[0][10:29], one, run_time=2),
            FadeOut(VGroup(sline1, sline2, cline1, cline2), run_time=1)
        )

        self.play(i1.animate.set_color(YELLOW).to_corner(UL), FadeOut(one, run_time=0.1))
        self.wait(3)


        # Identity 2
        axes = Axes(
            x_range=[-1, 1],
            y_range=[-1, 1],
            axis_config={"include_numbers": False},
        )

        radius = 2
        circle = Circle(radius=radius, color=BLUE)
        circle.move_to(ORIGIN)

        self.play(Create(axes), Create(circle))
        self.wait(1)

        angle = 40 * DEGREES
        point = np.array([radius * np.cos(angle), radius * np.sin(angle), 0])
        radius_line = Line(ORIGIN, point, color=YELLOW)

        arc = Arc(start_angle=0, angle=angle, radius=0.4, color=BLUE)
        arc_label = MathTex("x", font_size = 28).next_to(arc, RIGHT * 0.2)

        self.play(Create(radius_line), Create(arc), Write(arc_label))
        self.wait(1)

        foot = np.array([point[0], 0, 0])
        perp_line = Line(point, foot, color=GREEN)
        base_line = Line(foot, ORIGIN, color=RED)

        self.play(Create(perp_line), Create(base_line))
        self.wait()

        cos_label = MathTex(r"\cos x", font_size = 36).next_to(base_line, DOWN, buff=0.2)
        sin_label = MathTex(r"\sin x", font_size = 36).next_to(perp_line, RIGHT, buff=0.2)
        hyp_label = MathTex("1").move_to(radius_line.get_center() + 0.5 * UP)

        self.play(Write(cos_label), Write(sin_label), Write(hyp_label))
        self.wait(3)

        i2 = MathTex(r'\sin^2 x', r'+', r'\cos^2 x', r'=', r'1').to_edge(UR)
        self.play(Write(i2, run_time = 3))
        self.wait(2)

        self.play(Indicate(i2, color=YELLOW))
        self.play(i2.animate.set_color(YELLOW).next_to(i1, DOWN))

        self.wait(1)
        self.play(FadeOut(VGroup(axes, circle, cos_label, sin_label, hyp_label, radius_line, perp_line, base_line, arc, arc_label)))
        self.wait(3)

        # Identity 3
        i31 = i2.copy()
        i32 = MathTex(r'\frac{\sin^2x}{\cos^2x}' r'+' r'\frac{\cos^2x}{\cos^2x}' r'=' r'\frac{1}{\cos^2x}')
        i3 = MathTex(r'\tan^2x' r'+' r'1' r'=' r'\frac{1}{\cos^2x}')
        self.add(i31)
        self.play(i31.animate.set_color(WHITE).move_to(ORIGIN))
        self.wait(2)
        self.play(ReplacementTransform(i31, i32, run_time = 2))
        self.wait(2)
        self.play(ReplacementTransform(i32, i3, run_time = 2))
        self.wait(2)
        self.play(i3.animate.set_color(YELLOW).next_to(i2, DOWN))
        self.wait(2)

        # Identity 4
        i40 = i2.copy()
        i41 = MathTex(r'\cos^2 x', r'+', r'\sin^2 x', r'=', r'1')
        i42 = MathTex(r'\frac{\cos^2x}{\sin^2x}' r'+', r'\frac{\sin^2x}{\sin^2x}', r'=', r'\frac{1}{\sin^2x}')
        i4 = MathTex(r'\cot^2x', r'+', r'1', r'=', r'\frac{1}{\sin^2x}')
        self.add(i40)
        self.play(i40.animate.set_color(WHITE).move_to(ORIGIN))
        self.wait(2)
        self.play(TransformMatchingTex(i40, i41, path_arc = PI/2, run_time = 2))
        self.wait(2)
        self.play(ReplacementTransform(i41, i42), run_time = 2)
        self.wait(2)
        self.play(ReplacementTransform(i42, i4), run_time = 2)
        self.play(i4.animate.set_color(YELLOW))
        self.wait(2)

        # Final
        group = VGroup(i1, i2, i3, i4)
        self.play(
            group.animate.arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.6).move_to(ORIGIN),
            run_time=2
        )
        self.wait(3)


class test(Scene):
    def construct(self):
        e1 = MathTex(r'a', r'+', r'b', r'=', r'c', font_size = 30)
        e2 = MathTex(r'b', r'+', r'a', r'=', r'c')
        self.add(e1)
        self.play(TransformMatchingTex(e1, e2, path_arc = PI/2, run_time = 2))
        self.wait(3)
