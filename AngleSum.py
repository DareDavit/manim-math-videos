from manim import *
import numpy as np


class AngleSum(Scene):
   def construct(self):
       # Title
       title = Text(
           "Երկու անկյունների\n\nգումարի և տարբերության\n\nեռանկյունաչափական ֆունկցիաների\n\nբանաձևերը",
           font_size=36,
       )
       self.play(Write(title), run_time=4)
       self.wait(1)
       self.play(FadeOut(title))
       self.wait(1)


       # Axes and unit circle
       x_axis = Arrow(start=LEFT * 3, end=RIGHT * 3, buff=0, stroke_width=2)
       y_axis = Arrow(start=DOWN * 3, end=UP * 3, buff=0, stroke_width=2)
       uc = Circle(radius=2, color=BLUE)
       self.play(Create(x_axis), Create(y_axis), Create(uc))


       # "1" labels on axes
       x_one = MathTex("1", font_size=32).next_to([1, 0, 0], DOWN)
       y_one = MathTex("1", font_size=32).next_to([0, 1, 0], LEFT)
       self.play(Write(x_one), Write(y_one))


       radius = 2
       alpha = 60 * DEGREES
       beta = 20 * DEGREES


       alpha_tracker = ValueTracker(0)
       beta_tracker = ValueTracker(0)


       # Alpha components
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


       # Beta components
       dot_beta = always_redraw(
           lambda: Dot(radius * np.array([
               np.cos(beta_tracker.get_value()),
               np.sin(beta_tracker.get_value()), 0]), color=GREEN)
       )
       line_beta = always_redraw(lambda: Line(ORIGIN, dot_beta.get_center(), color=GREEN))
       arc_beta = always_redraw(
           lambda: Arc(
               start_angle=0,
               angle=beta_tracker.get_value(),
               radius=0.6,
               arc_center=ORIGIN,
               color=GREEN,
           )
       )
       label_beta = always_redraw(
           lambda: MathTex(r"\beta", font_size=24, color=GREEN).move_to(
               arc_beta.point_from_proportion(0.5) + 0.2 * RIGHT
           )
       )


       # --- New part: Static alpha elements fade in at 0 angle ---
       alpha_line_static = Line(ORIGIN, radius * RIGHT, color=ORANGE)
       alpha_arc_static = Arc(start_angle=0, angle=0.001, radius=0.4, arc_center=ORIGIN, color=ORANGE)
       alpha_label_static = MathTex(r"\alpha", font_size=24, color=ORANGE).move_to(alpha_arc_static.point_from_proportion(0.5) + 0.2 * UR)
       alpha_dot_static = Dot(radius * np.array([
                np.cos(alpha_tracker.get_value()),
                np.sin(alpha_tracker.get_value()), 0]), color=ORANGE)


       self.play(FadeIn(alpha_line_static), FadeIn(alpha_arc_static), FadeIn(alpha_label_static))
       self.play(FadeIn(alpha_dot_static))
       self.wait(1)


       # Switch to dynamic alpha and animate angle
       self.remove(alpha_line_static, alpha_arc_static, alpha_label_static, alpha_dot_static)
       self.add(dot_alpha, line_alpha, arc_alpha, label_alpha)
       self.play(alpha_tracker.animate.set_value(alpha), run_time=4)
       self.wait(1)


       alpha_coords = always_redraw(
           lambda: MathTex(r"(\cos\alpha,\ \sin\alpha)", font_size=32).next_to(dot_alpha, 0.5 * UR)
       )
       self.play(Write(alpha_coords))
       self.wait(2)


       # --- New part: Static beta elements fade in at 0 angle ---
       beta_line_static = Line(ORIGIN, radius * RIGHT, color=GREEN)
       beta_arc_static = Arc(start_angle=0, angle=0.001, radius=0.6, arc_center=ORIGIN, color=GREEN)
       beta_label_static = MathTex(r"\beta", font_size=24, color=GREEN).move_to(beta_arc_static.point_from_proportion(0.5) + 0.2 * RIGHT)
       beta_dot_static = Dot(radius * np.array([
                np.cos(beta_tracker.get_value()),
                np.sin(beta_tracker.get_value()), 0]), color=GREEN)


       self.play(FadeIn(beta_line_static), FadeIn(beta_arc_static), FadeIn(beta_label_static))
       self.play(FadeIn(beta_dot_static))
       self.wait(1)


       # Switch to dynamic beta and animate angle
       self.remove(beta_line_static, beta_arc_static, beta_label_static, beta_dot_static)
       self.add(dot_beta, line_beta, arc_beta, label_beta)
       self.play(beta_tracker.animate.set_value(beta), run_time=4)
       self.wait(1)


       beta_coords = always_redraw(
           lambda: MathTex(r"(\cos\beta,\ \sin\beta)", font_size=32).next_to(dot_beta, 0.5 * UR)
       )
       self.play(Write(beta_coords))
       self.wait(2)


       # Line d and its label (animated)
       d_line = always_redraw(lambda: Line(dot_alpha.get_center(), dot_beta.get_center(), color=YELLOW, stroke_width=4))
       d_label = always_redraw(lambda: MathTex("d", font_size=28, color=YELLOW).next_to(d_line.get_center(), 0.5*DL))
       self.play(Create(d_line), Write(d_label))
       self.wait(2)


       # Add general distance formula in top-right corner (semi-transparent)
       general_d_formula = MathTex(
           r"d^2 = (x_1 - x_2)^2 + (y_1 - y_2)^2",
           font_size=28,
           color=YELLOW
       ).to_corner(UR).set_opacity(0.8)
       self.play(FadeIn(general_d_formula))
       self.play(Indicate(general_d_formula))


       # First distance formula
       distance_formula1 = MathTex(
           r"d^2 = (\cos\alpha - \cos\beta)^2 + (\sin\alpha - \sin\beta)^2",
           font_size=32,
       ).to_corner(UL)
       self.play(Write(distance_formula1))
       self.wait(3)


       # Arc between alpha and beta
       arc_alpha_minus_beta_initial = Arc(
           start_angle=beta,
           angle=alpha - beta,
           radius=0.8,
           arc_center=ORIGIN,
           color=PURPLE,
       )
       label_alpha_minus_beta_initial = MathTex(
           r"\alpha - \beta", font_size=24, color=PURPLE
       ).move_to(arc_alpha_minus_beta_initial.point_from_proportion(0.5) + 0.25 * UR)
       self.play(Create(arc_alpha_minus_beta_initial), Write(label_alpha_minus_beta_initial))
       self.wait(3)


       # Remove initial arcs, labels, and coordinate labels
       self.play(
           FadeOut(arc_alpha),
           FadeOut(label_alpha),
           FadeOut(arc_beta),
           FadeOut(label_beta),
           FadeOut(alpha_coords),
           FadeOut(beta_coords),
       )
       self.wait(1)


       # Move alpha and beta to new positions (alpha−beta, 1,0)
       self.play(
           beta_tracker.animate.set_value(0),
           alpha_tracker.animate.set_value(alpha - beta),
           Rotate(arc_alpha_minus_beta_initial, angle=-beta, about_point=ORIGIN),
           label_alpha_minus_beta_initial.animate.move_to(ORIGIN + 1.1*RIGHT + 0.4*UP),
           run_time=6,
       )
       self.wait(1)


       # Final coordinates
       alpha_minus_beta_coords = always_redraw(
           lambda: MathTex(
               r"(\cos(\alpha - \beta),\ \sin(\alpha - \beta))", font_size=28
           ).next_to(dot_alpha, 0.5*UR)
       )
       beta_coords_final = always_redraw(
           lambda: MathTex(r"(1,\ 0)", font_size=28).next_to(dot_beta, 0.5*DR)
       )


       self.play(Write(alpha_minus_beta_coords), Write(beta_coords_final))
       self.wait(2)


       # Second distance formula
       distance_formula2 = MathTex(
           r"d^2 = (\cos(\alpha - \beta) - 1)^2 + (\sin(\alpha - \beta) - 0)^2",
           font_size=32,
       ).next_to(distance_formula1, DOWN, aligned_edge=LEFT)
       self.play(Write(distance_formula2))
       self.wait(4)


        # --- New part: remove geometry, center formulas, derive cos(alpha-beta) ---


       # 1. Fade out all dots, arcs, lines, coords except the two distance formulas
       objects_to_fade = [
           dot_alpha, line_alpha, arc_alpha, label_alpha,
           dot_beta, line_beta, arc_beta, label_beta,
           d_line, d_label,
           alpha_minus_beta_coords, beta_coords_final,
           general_d_formula,
       ]
       self.play(*[FadeOut(mob) for mob in self.mobjects if mob not in [distance_formula1, distance_formula2]])
       self.wait(1)


       # 2. Move the two distance formulas to center, stacked vertically
       distance_formula1.generate_target()
       distance_formula2.generate_target()
       distance_formula1.target.move_to(UP * 1)
       distance_formula2.target.next_to(distance_formula1.target, DOWN, buff=0.7)
       self.play(
           MoveToTarget(distance_formula1),
           MoveToTarget(distance_formula2),
       )
       self.wait(1)


       # 3. Write combined distance formula underneath
       combined_formula = MathTex(
           r"(\cos\alpha - \cos\beta)^2", r"+", r"(\sin\alpha - \sin\beta)^2", r"=", r"(\cos(\alpha - \beta) - 1)^2", r"+", r"(\sin(\alpha - \beta) - 0)^2",
           font_size=30
       ).next_to(distance_formula2, DOWN, buff=0.8)
       self.play(Write(combined_formula))
       self.wait(2)


       # 4. Fade out original formulas
       self.play(FadeOut(distance_formula1), FadeOut(distance_formula2))
       self.wait(0.5)


       # 5. Move combined formula to center
       self.play(combined_formula.animate.move_to(ORIGIN))
       self.wait(1)


       # 6. Show (a+b)^2 identity in corner
       binomial_identity = MathTex(
           r"(a+b)^2 = a^2 + 2ab + b^2",
           font_size=24,
           color=YELLOW
       ).to_corner(UR).set_opacity(0.8)
       self.play(FadeIn(binomial_identity))
       self.play(Indicate(binomial_identity))
       self.wait(1)


       #7. Transforming to formula
       lp1 = MathTex(
           r"(\cos\alpha - \cos\beta)^2", r"+", r"(\sin\alpha - \sin\beta)^2", r"=", r"(\cos(\alpha - \beta) - 1)^2", r"+", r"\sin^2(\alpha - \beta)",
           font_size=30
       )
       lp2 = MathTex(r"\cos^2\alpha", r"-", r"2", r"\cos\alpha\cos\beta", r"+", r"\cos^2\beta", r"+", r"(\sin\alpha - \sin\beta)^2", r"=", r"(\cos(\alpha - \beta) - 1)^2", r"+", r"\sin^2(\alpha - \beta)",
                     font_size=30)
       lp3 = MathTex(r"\cos^2\alpha", r"-", r"2", r"\cos\alpha\cos\beta", r"+", r"\cos^2\beta", r"+", r"\sin^2\alpha", r"-", r"2", r"\sin\alpha\sin\beta", r"+", r"\sin^2\beta", r"=", r"(\cos(\alpha - \beta) - 1)^2", r"+", r"\sin^2(\alpha - \beta)",
                     font_size=30)
       lp4 = MathTex(r"\cos^2\alpha", r"+", r"\sin^2\alpha", r"-", r"2\cos\alpha\cos\beta", r"+", r"\cos^2\beta", r"+", r"\sin^2\beta", r"-", r"2", r"\sin\alpha\sin\beta", r"=", r"(\cos(\alpha - \beta) - 1)^2", r"+", r"\sin^2(\alpha - \beta)",
                     font_size=30)
       self.play(TransformMatchingTex(combined_formula, lp1, run_time=2))
       self.wait(2)
       self.play(TransformMatchingTex(lp1,lp2,run_time=2))
       self.wait(2)
       self.play(TransformMatchingTex(lp2,lp3,run_time=2))
       self.wait(2)
       self.play(TransformMatchingTex(lp3,lp4,run_time=2))


       trig_identity = MathTex(
           r"sin^2x + cos^2x = 1",
           font_size=24,
           color=YELLOW
       ).next_to(binomial_identity, DOWN).set_opacity(0.8)
       self.play(FadeIn(trig_identity))
       self.play(Indicate(trig_identity))
       self.wait(1)


       self.play(Circumscribe(*VGroup(lp4[:3]), color=YELLOW, fade_out=True))
       self.wait(2)


       lp5 = MathTex(r"1", r"-", r"2", r"\cos\alpha\cos\beta", r"+", r"\cos^2\beta", r"+", r"\sin^2\beta", r"-", r"2", r"\sin\alpha\sin\beta", r"=", r"(\cos(\alpha - \beta) - 1)^2", r"+", r"\sin^2(\alpha - \beta)",
                     font_size=30)
       self.play(TransformMatchingTex(lp4,lp5,run_time=2))
       self.wait(2)


       self.play(Circumscribe(*VGroup(lp5[5:8]), color=YELLOW, fade_out=True))
       self.wait(2)


       lp6 = MathTex(r"1", r"-", r"2", r"\cos\alpha\cos\beta", r"+", r"1", r"-", r"2", r"\sin\alpha\sin\beta", r"=", r"(\cos(\alpha - \beta) - 1)^2", r"+", r"\sin^2(\alpha - \beta)",
                     font_size=30)
       self.play(TransformMatchingTex(lp5,lp6,run_time=2))
       self.wait(2)


       lp7 = MathTex(r"2", r"-", r"2", r"\cos\alpha\cos\beta", r"-", r"2", r"\sin\alpha\sin\beta", r"=", r"(\cos(\alpha - \beta) - 1)^2", r"+", r"\sin^2(\alpha - \beta)",
                     font_size=30)
       lp8 = MathTex(r"2", r"-2", r"(", r"\cos\alpha\cos\beta", r"+", r"\sin\alpha\sin\beta", r")", r"=", r"(\cos(\alpha - \beta) - 1)^2", r"+", r"\sin^2(\alpha - \beta)",
                     font_size=30)
       self.play(TransformMatchingTex(lp6,lp7,run_time=2))
       self.wait(2)
       self.play(TransformMatchingTex(lp7,lp8,run_time=2))
       self.wait(2)


       rp1 = MathTex(r"2", r"-2", r"(\cos\alpha\cos\beta", r"+", r"\sin\alpha\sin\beta)", r"=", r"\cos^2(\alpha - \beta)", r"-", r"2\cos(\alpha - \beta)", r"+" r"1", r"+", r"\sin^2(\alpha - \beta)",
                     font_size=30)
       rp2 = MathTex(r"2", r"-2", r"(\cos\alpha\cos\beta", r"+", r"\sin\alpha\sin\beta)", r"=", r"\cos^2(\alpha - \beta)", r"+", r"\sin^2(\alpha - \beta)", r"+", r"1", r"-", r"2\cos(\alpha - \beta)",
                     font_size=30)
       self.play(TransformMatchingTex(lp8,rp1,run_time=2))
       self.wait(2)
       self.play(TransformMatchingTex(rp1,rp2,run_time=2))
       self.wait(2)


       self.play(Circumscribe(*VGroup(rp2[6:9]), color=YELLOW, fade_out=True))
       self.wait(2)
      
       rp3 = MathTex(r"2", r"-2", r"(\cos\alpha\cos\beta", r"+", r"\sin\alpha\sin\beta)", r"=", r"1", r"+", r"1", r"-", r"2\cos(\alpha - \beta)",
                     font_size=30)
       rp4 = MathTex(r"2", r"-2", r"(\cos\alpha\cos\beta", r"+", r"\sin\alpha\sin\beta)", r"=", r"2", r"-", r"2\cos(\alpha - \beta)",
                     font_size=30)
       self.play(TransformMatchingTex(rp2,rp3,run_time=2))
       self.wait(2)
       self.play(TransformMatchingTex(rp3,rp4,run_time=2))
       self.wait(2)


       rp5 = MathTex(r"(\cos\alpha\cos\beta", r"+", r"\sin\alpha\sin\beta)", r"=", r"\cos(\alpha - \beta)",
                     font_size=30)
       self.play(TransformMatchingTex(rp4,rp5,run_time=2))
       self.play(FadeOut(rp5))
       self.play(FadeOut(binomial_identity), FadeOut(trig_identity))
      
       fe1 = MathTex(r"\cos(\alpha - \beta)", r"=", r"\cos\alpha\cos\beta", r"+", r"\sin\alpha\sin\beta",
                     font_size=40, color=YELLOW).to_corner(UP)
       self.play(Write(fe1))


       fe21 = MathTex(r"\cos(\alpha - (-\beta)) = \cos\alpha\cos(-\beta) + \sin\alpha\sin(-\beta)", font_size=30)
       fe2 = MathTex(r"\cos(\alpha + \beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta", font_size=30).next_to(fe21,DOWN)


       sinm = MathTex(r"\sin(-x) = -\sin x", font_size=24, color=YELLOW).to_corner(UR).set_opacity(0.8)
       cosm = MathTex(r"\cos(-x) = \cos x", font_size=24, color=YELLOW).next_to(sinm, DOWN).set_opacity(0.8)


       self.play(Write(fe21, run_time=2))
       self.play(Write(sinm), Write(cosm))
       self.play(Indicate(sinm), Indicate(cosm))
       self.wait(2)
       self.play(Write(fe2))
       self.wait(2)
       self.play(FadeOut(fe21), FadeOut(sinm), FadeOut(cosm))
       self.wait(1)


       self.play(
           fe2.animate.set_color(YELLOW).scale(1.33).shift(UP*3)
       )


       cssn = MathTex(r"\cos\left(\frac{\pi}{2} - x\right) = \sin x", font_size=24, color=YELLOW).to_corner(UR).set_opacity(0.8)
       sncs = MathTex(r"\sin\left(\frac{\pi}{2} - x\right) = \cos x", font_size=24, color=YELLOW).next_to(cssn, DOWN).set_opacity(0.8)


       fe31 = MathTex(
           r"\sin(\alpha \pm \beta) = \cos\left(\frac{\pi}{2} - \alpha \mp \beta\right)"
           r" = \cos\left(\frac{\pi}{2} - \alpha\right)\cos\beta \pm \sin\left(\frac{\pi}{2} - \alpha\right)\sin\beta",
           font_size=30
       )


       fsin = MathTex(
           r"\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \sin\beta\cos\alpha",
           font_size=30
       ).next_to(fe31, DOWN)


       self.play(Write(cssn), Write(sncs), Write(fe31), run_time=2)
       self.play(Indicate(sncs), Indicate(cssn))
       self.wait(2)
       self.play(Write(fsin))
       self.wait(2)
       self.play(FadeOut(sncs), FadeOut(cssn), FadeOut(fe31))
       self.wait(2)
       self.play(
           fsin.animate.set_color(YELLOW).scale(1.33)
       )


       fcos = MathTex(r"\cos(\alpha \pm \beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta", font_size=40, color=YELLOW).next_to(fe1, DOWN)
       self.play(FadeOut(fe1), ReplacementTransform(fe2,fcos))
       self.wait(2)
       self.play(FadeOut(fsin), FadeOut(fcos))


       final = VGroup(fsin, fcos).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
       final.move_to(2*UL)


       self.play(Write(final))


       # Tanges
       tg1 = MathTex(r"\tan(\alpha \pm \beta)", r"=", r"\frac{\sin(\alpha\pm\beta)}{\cos(\alpha\pm\beta)}", r"=", r"\frac{\sin\alpha\cos\beta\pm\sin\beta\cos\alpha}{\cos\alpha\cos\beta\mp\sin\alpha\sin\beta}", font_size=30)
       tan_frac = MathTex(r"\tan x = \frac{\sin x}{\cos x}", font_size=24, color=YELLOW).to_corner(UR).set_opacity(0.8)


       tg2 = MathTex(r"\tan(\alpha \pm \beta)", r"=", r"\frac{\frac{\sin\alpha\cos\beta}{\cos\alpha\cos\beta}\pm\frac{\sin\beta\cos\alpha}{\cos\alpha\cos\beta}}{\frac{\cos\alpha\cos\beta}{\cos\alpha\cos\beta}\mp\frac{\sin\alpha\sin\beta}{\cos\alpha\cos\beta}}", font_size=30).next_to(tg1, DOWN)
       tg3 = MathTex(r"\tan(\alpha \pm \beta)", r"=", r"\frac{\tan\alpha\pm\tan\beta}{1\mp\tan\alpha\tan\beta", font_size=30).next_to(tg1, DOWN)


       self.play(Write(tg1, run_time=2), Write(tan_frac, run_time=1))
       self.play(Indicate(tan_frac))
       self.wait(2)
       self.play(Write(tg2), run_time=2)
       self.wait(2)
       self.play(ReplacementTransform(tg2,tg3), run_time=2)
       self.wait(2)
       self.play(FadeOut(tan_frac), FadeOut(tg1))
       self.play(
           tg3.animate.set_color(YELLOW).scale(1.33)
       )
       self.wait(2)
       self.play(FadeOut(final), FadeOut(tg3))

       ctg = MathTex(r"\cot(\alpha \pm \beta) = \frac{\cot\alpha\cot\beta \mp 1}{\cot\alpha \pm \cot\beta}", color=YELLOW, font_size=40)


       FINAL = VGroup(fsin, fcos, tg3, ctg).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
       FINAL.move_to(ORIGIN)


       self.play(Write(FINAL))






       self.wait(5)
