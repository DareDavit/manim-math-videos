from manim import *
import numpy as np

class Reductions(Scene):
    def construct(self):
        # Title
        title = Text(
            "Բերման Բանաձևերը",
            font_size=36,
        )
        self.play(Write(title), run_time=4)
        self.wait(1)
        self.play(FadeOut(title))
        self.wait(1)

        # +-
        x_axis = Arrow(start=LEFT * 3, end=RIGHT * 3, buff=0, stroke_width=2)
        y_axis = Arrow(start=DOWN * 3, end=UP * 3, buff=0, stroke_width=2)
        uc = Circle(radius=2, color=BLUE)
        self.play(Create(x_axis), Create(y_axis), Create(uc))


        radius = 2
        alpha = 60 * DEGREES


        alpha_tracker = ValueTracker(0)


        dot_alpha = always_redraw(
            lambda: Dot(radius * np.array([
                np.cos(alpha_tracker.get_value()),
                np.sin(alpha_tracker.get_value()), 0]), color=ORANGE)
        )
        line_alpha = always_redraw(lambda: Line(ORIGIN, dot_alpha.get_center(), color=ORANGE))
        arc_alpha = always_redraw(
            lambda: Arc(
                start_angle=0,
                angle=alpha_tracker.get_value(),
                radius=0.4,
                arc_center=ORIGIN,
                color=ORANGE,
            )
        )
        label_alpha = always_redraw(
            lambda: MathTex(r"\alpha", font_size=24, color=ORANGE).move_to(
                arc_alpha.point_from_proportion(0.5) + 0.2 * UR
            )
        )


        alpha_line_static = Line(ORIGIN, radius * RIGHT, color=ORANGE)
        alpha_arc_static = Arc(start_angle=0, angle=0.001, radius=0.4, arc_center=ORIGIN, color=ORANGE)
        alpha_label_static = MathTex(r"\alpha", font_size=24, color=ORANGE).move_to(alpha_arc_static.point_from_proportion(0.5) + 0.2 * UR)
        alpha_dot_static = Dot(radius * np.array([
                    np.cos(alpha_tracker.get_value()),
                    np.sin(alpha_tracker.get_value()), 0]), color=ORANGE)


        self.play(FadeIn(alpha_line_static), FadeIn(alpha_arc_static), FadeIn(alpha_label_static))
        self.play(FadeIn(alpha_dot_static))
        self.wait(1)


        self.remove(alpha_line_static, alpha_arc_static, alpha_label_static, alpha_dot_static)
        self.add(dot_alpha, line_alpha, arc_alpha, label_alpha)
        self.play(alpha_tracker.animate.set_value(alpha), run_time=4)
        self.wait(1)


        alpha_coords = always_redraw(
            lambda: MathTex(r"(\cos\alpha,\ \sin\alpha)", font_size=32).next_to(dot_alpha, 0.5 * UR)
        )
        self.play(Write(alpha_coords))
        self.wait(2)

        dashed_x = DashedLine(
            start=dot_alpha.get_center(),
            end=np.array([dot_alpha.get_center()[0], -dot_alpha.get_center()[1], 0]),
        )
        dashed_y = DashedLine(
            start=dot_alpha.get_center(),
            end=np.array([0, dot_alpha.get_center()[1], 0]),
        )

        x_dot = Dot(np.array([dot_alpha.get_center()[0], 0, 0]))
        x_dot_label = MathTex(r"\cos\alpha", font_size=24).move_to(x_dot.get_center() + 0.4*RIGHT + 0.2*DOWN)
        y_dot = Dot(np.array([0, dot_alpha.get_center()[1], 0]))
        y_dot_label = MathTex(r"\sin\alpha", font_size=24).move_to(y_dot.get_center() + 0.4*LEFT + 0.1*DOWN)
        y1_dot = Dot(np.array([0, -dot_alpha.get_center()[1], 0]))
        y1_dot_label = MathTex(r"-\sin\alpha", font_size=24).move_to(y1_dot.get_center() + 0.4*LEFT + 0.2*UP)
        dot_alpha1 = Dot(np.array([dot_alpha.get_center()[0], -dot_alpha.get_center()[1], 0]), color=GREEN)

        self.play(Create(dashed_x, run_time=3), Create(dashed_y, run_time=1.5))
        self.play(Create(x_dot), Create(y_dot), Create(dot_alpha1), Create(x_dot_label), Create(y_dot_label))

        dashed_y1 = DashedLine(
            start=dot_alpha1.get_center(),
            end=np.array([0, -dot_alpha.get_center()[1], 0]),
        )

        line_alpha1 = Line(ORIGIN, dot_alpha1.get_center(), color=GREEN)
        arc_alpha1 = Arc(
                start_angle=0,
                angle=-alpha,
                radius=0.4,
                arc_center=ORIGIN,
                color=GREEN,
            )
        label_alpha1 = MathTex(r"-\alpha", font_size=24, color=GREEN).move_to(
                arc_alpha1.point_from_proportion(0.5) + 0.2 * DR)

        self.play(Create(line_alpha1), Create(arc_alpha1), Create(label_alpha1))
        self.play(Create(dashed_y1, run_time=1.5))
        self.play(Create(y1_dot), Create(y1_dot_label))

        alpha1_coords = MathTex(r"(\cos(-\alpha),\ \sin(-\alpha))", font_size=32).next_to(dot_alpha1, 0.5 * DR)
        self.play(Write(alpha1_coords))
        self.wait(2)

        cosm = alpha1_coords[0][1:8].copy()
        cosm1 = x_dot_label.copy()

        self.play(Indicate(alpha1_coords[0][1:8], scale_factor=1.5))
        self.play(cosm.animate.move_to(ORIGIN + 3*UP + 6*LEFT).scale(1.5))
        equal = MathTex(r'=').next_to(cosm, RIGHT)
        self.play(Indicate(x_dot_label, scale_factor=2))
        self.play(Write(equal), cosm1.animate.next_to(equal, 2.1*RIGHT).scale(2.05))
        self.wait(2)

        sinm = alpha1_coords[0][9:-1].copy()
        sinm1 = y1_dot_label.copy()

        self.play(Indicate(alpha1_coords[0][9:-1], scale_factor=1.5))
        self.play(sinm.animate.move_to(ORIGIN + 2*UP + 6*LEFT).scale(1.5))
        equal1 = MathTex(r'=').next_to(sinm, RIGHT)
        self.play(Indicate(y1_dot_label, scale_factor=2))
        self.play(Write(equal1), sinm1.animate.next_to(equal1, 2.1*RIGHT).scale(2.05))
        self.wait(2)

        tgm = MathTex(r'\tan(-\alpha) = \frac{\sin(-\alpha)}{\cos(-\alpha)}').next_to(equal1, 12*DOWN)
        self.play(Write(tgm))
        self.wait(2)
        tgm1 = MathTex(r'\frac{-\sin\alpha}{\cos\alpha}').next_to(tgm[0][7], RIGHT)
        self.play(Indicate(VGroup(cosm, cosm1, equal, sinm, sinm1, equal1), scale_factor=1.1))
        self.play(ReplacementTransform(tgm[0][8:], tgm1))
        self.wait(2)
        tgm2 = MathTex(r'-\tan\alpha').next_to(tgm[0][7], RIGHT)
        self.play(ReplacementTransform(tgm1, tgm2))
        self.wait(2)

        ctgm = MathTex(r'\cot(-\alpha) = \frac{1}{\tan(-\alpha)}').next_to(tgm, 2*DOWN)
        self.play(Write(ctgm))
        self.wait(2)
        self.play(Indicate(VGroup(tgm[0][:8], tgm2), scale_factor=1.1))
        ctgm1 = MathTex(r'-\tan\alpha').move_to(ctgm[0][10:].get_center())
        self.play(ReplacementTransform(ctgm[0][10:], ctgm1))
        ctgm2 = MathTex(r'-\cot\alpha').next_to(ctgm[0][7], RIGHT)
        self.wait(2)
        self.play(ReplacementTransform(ctgm1, ctgm2), FadeOut(ctgm[0][8:10]))

        self.wait(4)

        self.play(FadeOut(VGroup(x_axis, y_axis, uc, dot_alpha, line_alpha, arc_alpha, label_alpha, alpha_coords, ctgm2, tgm2, ctgm[0][:8], tgm[0][:8],
                                 dot_alpha1, line_alpha1, arc_alpha1, label_alpha1, alpha1_coords, equal, equal1, x_dot, y_dot,
                                 y1_dot, x_dot_label, y_dot_label, y1_dot_label, cosm, cosm1, sinm, sinm1, dashed_x, dashed_y, dashed_y1)))
        self.wait(3)



       #------------------------------------------------------------------------------------------------ 
       #------------------------------------------------------------------------------------------------ 
       #------------------------------------------------------------------------------------------------ 
       #------------------------------------------------------------------------------------------------ 
       #------------------------------------------------------------------------------------------------ 
       #------------------------------------------------------------------------------------------------ 
       #------------------------------------------------------------------------------------------------ 


        # 90
        A = 6 * LEFT + 2 * DOWN
        B = A + 4 * RIGHT
        C = A + 3 * UP

        side_a = Line(C, A, color=BLUE)       # vertical side
        side_b = Line(A, B, color=GREEN)      # horizontal side
        side_c = Line(B, C, color=RED)        # hypotenuse
        triangle = VGroup(side_a, side_b, side_c)
        label_a = MathTex("a", color=BLUE).next_to(side_a, LEFT)
        label_b = MathTex("b", color=GREEN).next_to(side_b, DOWN)
        label_c = MathTex("c", color=RED).move_to(side_c.get_center() + 0.3*UR)
        right_angle = Square(0.3, color=WHITE).move_to(A + 0.15*RIGHT + 0.15*UP)

        self.play(Create(triangle))
        self.play(FadeIn(right_angle))
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait(1)

        arc = Arc(
            radius=0.5,
            start_angle=PI - np.arcsin(0.6),
            angle=np.arcsin(0.6),
            color=YELLOW
        )
        arc.move_arc_center_to(B)
        alpha = MathTex(r"\alpha", color=YELLOW, font_size=36).move_to(B + 0.2 * UP + 0.7 * LEFT)
        self.play(Create(arc), Write(alpha))

        arc1 = Arc(
            radius=0.5,
            start_angle= -PI/2,
            angle=np.arcsin(0.8),
            color=ORANGE
        )
        arc1.move_arc_center_to(C)
        alpha1 = MathTex(r"90^\circ - \alpha", color=ORANGE, font_size=26).move_to(C + 0.8 * DOWN + 0.5 * RIGHT)

        sin90 = MathTex(r'\sin\alpha = \frac{a}{c} = \cos(\frac{\pi}{2} - \alpha)').move_to(ORIGIN + 3*UP)
        self.play(Write(sin90[0][:5]), Write(sin90[0][6]))
        
        self.play(Indicate(label_a, scale_factor=2))
        a = label_a.copy()
        self.add(a)
        self.play(a.animate.move_to(sin90[0][5].get_center()))
        self.play(Indicate(label_c, scale_factor=2))
        c = label_c.copy()
        self.add(c)
        self.play(c.animate.move_to(sin90[0][7].get_center()))

        self.play(Create(arc1), Write(alpha1))
        self.play(Write(sin90[0][8:]))

        cos90 = MathTex(r'\cos\alpha = \frac{b}{c} = \sin(\frac{\pi}{2} - \alpha)').move_to(ORIGIN + 1.5*UP)
        self.play(Write(cos90[0][:5]), Write(cos90[0][6]))
        
        self.play(Indicate(label_b, scale_factor=2))
        b = label_b.copy()
        self.add(b)
        self.play(b.animate.move_to(cos90[0][5].get_center()))
        self.play(Indicate(label_c, scale_factor=2))
        c = label_c.copy()
        self.add(c)
        self.play(c.animate.move_to(cos90[0][7].get_center()))
        self.play(Write(cos90[0][8:]))

        tg90 = MathTex(r'\tan\alpha = \frac{a}{b} = \cot(\frac{\pi}{2} - \alpha)').move_to(ORIGIN + 1.5*DOWN + 2*RIGHT)
        self.play(Write(tg90[0][:5]), Write(tg90[0][6]))
        
        self.play(Indicate(label_a, scale_factor=2))
        a = label_a.copy()
        self.add(a)
        self.play(a.animate.move_to(tg90[0][5].get_center()))
        self.play(Indicate(label_b, scale_factor=2))
        b = label_b.copy()
        self.add(b)
        self.play(b.animate.move_to(tg90[0][7].get_center()))
        self.play(Write(tg90[0][8:]))

        ctg90 = MathTex(r'\cot\alpha = \frac{b}{a} = \tan(\frac{\pi}{2} - \alpha)').move_to(ORIGIN + 3*DOWN + 2*RIGHT)
        self.play(Write(ctg90[0][:5]), Write(ctg90[0][6]))
        
        self.play(Indicate(label_b, scale_factor=2))
        b = label_b.copy()
        self.add(b)
        self.play(b.animate.move_to(ctg90[0][5].get_center()))
        self.play(Indicate(label_a, scale_factor=2))
        a = label_a.copy()
        self.add(a)
        self.play(a.animate.move_to(ctg90[0][7].get_center()))
        self.play(Write(ctg90[0][8:]))

        self.play(FadeOut(VGroup(triangle, arc, arc1, alpha, alpha1, label_a, label_b, label_c, right_angle)))
        
        self.clear()
        self.play(ReplacementTransform(cos90, MathTex(r'\sin(\frac{\pi}{2}-\alpha)=\cos\alpha').move_to(cos90.get_center())),
                  ReplacementTransform(sin90, MathTex(r'\cos(\frac{\pi}{2}-\alpha)=\sin\alpha').move_to(sin90.get_center())),
                  ReplacementTransform(ctg90, MathTex(r'\tan(\frac{\pi}{2}-\alpha)=\cot\alpha').move_to(ctg90.get_center())),
                  ReplacementTransform(tg90, MathTex(r'\cot(\frac{\pi}{2}-\alpha)=\tan\alpha').move_to(tg90.get_center()))
                  )
        trig90 = VGroup(cos90, sin90, ctg90, tg90)
        self.clear()
        self.play(trig90.animate.arrange(DOWN, buff=1).to_edge(LEFT))
        self.wait(3)


        sin900 = MathTex(r'\sin(\frac{\pi}{2}+\alpha)', r'=', r'\sin(\frac{\pi}{2}-(-\alpha))', r'=', r'\cos(-\alpha)=\cos\alpha', font_size=36).next_to(cos90, 4.5*RIGHT)
        sin901 = MathTex(r'\sin(\frac{\pi}{2}+\alpha)', r'=', r'\cos\alpha', font_size=36).move_to(sin900.get_center())
        self.play(Write(sin900))
        self.wait(2)
        self.play(TransformMatchingTex(sin900, sin901))
        self.play(sin901.animate.scale(1.33))
        self.wait(2)
        
        cos901 = MathTex(r'\cos(\frac{\pi}{2}+\alpha)', r'=', r'-\sin\alpha')
        tg901 = MathTex(r'\tan(\frac{\pi}{2}+\alpha)', r'=', r'-\cot\alpha')
        ctg901 = MathTex(r'\cot(\frac{\pi}{2}+\alpha)', r'=', r'-\tan\alpha')
        trig901 = VGroup(cos901, tg901, ctg901).arrange(DOWN, buff=1, aligned_edge=LEFT)
        trig901.next_to(sin901, DOWN, buff=1)

        for text in trig901:
            self.play(Write(text))
        self.wait(2)
        
        self.play(FadeOut(trig90), FadeOut(trig901), FadeOut(sin901))

        self.wait(3)



        #------------------------------------------------------------------------------------------------ 
        #------------------------------------------------------------------------------------------------ 
        #------------------------------------------------------------------------------------------------ 
        #------------------------------------------------------------------------------------------------ 
        #------------------------------------------------------------------------------------------------ 
        #------------------------------------------------------------------------------------------------ 
        #------------------------------------------------------------------------------------------------ 


        # 360
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

        angle = 60 * DEGREES
        point = np.array([radius * np.cos(angle), radius * np.sin(angle), 0])
        radius_line = Line(ORIGIN, point, color=BLUE)
        alpha_dot = Dot(point, color=BLUE)

        arc = Arc(start_angle=0, angle=angle, radius=0.4, color=BLUE)
        arc_label = MathTex(r"\alpha", font_size = 28).next_to(arc, RIGHT * 0.2)

        self.play(Create(radius_line), Create(arc), Write(arc_label), Create(alpha_dot))
        self.wait(1)

        angle_tracker = ValueTracker(angle)

        rotating_dot = always_redraw(lambda: 
            Dot(
                radius * np.array([
                    np.cos(angle_tracker.get_value()),
                    np.sin(angle_tracker.get_value()),
                    0
                ]),
                color=ORANGE
            )
        )

        rotating_line = always_redraw(lambda: 
            Line(ORIGIN, rotating_dot.get_center(), color=ORANGE)
        )
        path = TracedPath(rotating_dot.get_center, stroke_color=YELLOW, stroke_width=4)
        self.add(path, rotating_dot, rotating_line)

        self.play(angle_tracker.animate.set_value(angle + 2 * PI), run_time=5, rate_func=linear)
        self.wait()

        sin360 = MathTex(r'\sin(2\pi+\alpha) = \sin\alpha').to_edge(UL)
        cos360 = MathTex(r'\cos(2\pi+\alpha) = \cos\alpha').next_to(sin360, DOWN)
        self.play(Write(sin360), Write(cos360))
        self.wait(2)
        self.play(FadeOut(VGroup(sin360, cos360, rotating_line, rotating_dot, path)), run_time=2)




        #------------------------------------------------------------------------------------------------ 
        #------------------------------------------------------------------------------------------------ 
        #------------------------------------------------------------------------------------------------ 
        #------------------------------------------------------------------------------------------------ 
        #------------------------------------------------------------------------------------------------ 
        #------------------------------------------------------------------------------------------------ 
        #------------------------------------------------------------------------------------------------ 



        # 180
        alpha_coords = MathTex(r'(\cos\alpha, \ \sin\alpha)').next_to(alpha_dot, 0.2*UR)
        self.play(Write(alpha_coords))
        self.wait(2)

        angle_tracker = ValueTracker(angle)

        rotating_dot = always_redraw(lambda: 
            Dot(
                radius * np.array([
                    np.cos(angle_tracker.get_value()),
                    np.sin(angle_tracker.get_value()),
                    0
                ]),
                color=ORANGE
            )
        )

        rotating_line = always_redraw(lambda: 
            Line(ORIGIN, rotating_dot.get_center(), color=ORANGE)
        )
        path = TracedPath(rotating_dot.get_center, stroke_color=YELLOW, stroke_width=4)
        self.add(path, rotating_dot, rotating_line)

        self.play(angle_tracker.animate.set_value(angle + PI), run_time=5, rate_func=linear)
        arc1 = Arc(start_angle=0, angle=angle+PI, radius=0.8, color=ORANGE)
        arc1_label = MathTex(r"\pi+\alpha", font_size = 28).next_to(arc1, UL * 0.05)
        self.remove(path)
        self.play(Create(arc1), Write(arc1_label))
        self.wait(2)

        alpha1_coords = MathTex(r'(-\cos\alpha, \ -\sin\alpha)').next_to(rotating_dot, 0.2*DL)
        self.play(Write(alpha1_coords))
        self.wait(2)

        sin180 = MathTex(r'\sin(\pi+\alpha) = -\sin\alpha').to_edge(UL)
        cos180 = MathTex(r'\cos(\pi+\alpha) = -\cos\alpha').next_to(sin180, 2*DOWN)
        self.play(Write(sin180), Write(cos180))
        self.wait(2)
        self.play(FadeOut(VGroup(rotating_line, rotating_dot, axes, circle, arc, arc_label, alpha_dot, radius_line, alpha1_coords, alpha_coords, arc1, arc1_label)), run_time=2)
        self.wait(2)

        tg1801 = MathTex(r'\tan(\pi+\alpha) =', r'\frac{\sin(\pi+\alpha)}{\cos(\pi+\alpha)} = \frac{-\sin\alpha}{-\cos\alpha} = \frac{\sin\alpha}{\cos\alpha} =', r'\tan\alpha').move_to(ORIGIN + 2*DOWN)
        tg180 = MathTex(r'\tan(\pi+\alpha) =', r'\tan\alpha').move_to(tg1801.get_center())

        self.play(Write(tg1801), run_tim=3)
        self.wait(2)
        self.play(TransformMatchingTex(tg1801, tg180))
        self.play(tg180.animate.move_to(sin180.get_center()+5*DOWN))
        self.wait(2)

        ctg180 = MathTex(r'\cot(\pi+\alpha) = \cot\alpha').next_to(tg180, 2*DOWN)
        self.play(Write(ctg180))
        self.wait(2)

        sin1801 = MathTex(r'\sin(\pi-\alpha) = \sin\alpha').next_to(cos180, 2*DOWN)
        cos1801 = MathTex(r'\cos(\pi-\alpha) = -\cos\alpha').next_to(sin1801, 2*DOWN)
        self.play(Write(sin1801), Write(cos1801))
        self.wait(2)
        self.play(FadeOut(sin180, cos180, sin1801, cos1801, tg180, ctg180))


        self.wait(3)
