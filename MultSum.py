from manim import *
import numpy as np

class MultSum(Scene):
    def construct(self):
        # Title
        title = Text(
            "Եռանկյունաչափական ֆունկցիաների\n\nգումարի և արտադրյալի բանաձևերը",
            font_size=36,
        )
        self.play(Write(title), run_time=4)
        self.wait(1)
        self.play(FadeOut(title))
        self.wait(1)

        # Mult 
        cangsum = MathTex(r'\cos(\alpha+\beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta').to_edge(UP)
        cangsub = MathTex(r'\cos(\alpha-\beta) = \cos\alpha\cos\beta + \sin\alpha\sin\beta').next_to(cangsum, DOWN)
        self.play(Write(cangsum), Write(cangsub), run_time=2)
        self.wait(2)


        eq = MathTex(r'\cos(\alpha+\beta)+\cos(\alpha-\beta)', r'=', r'\cos\alpha\cos\beta', r'-\sin\alpha\sin\beta', r'+', r'\cos\alpha\cos\beta', r'+\sin\alpha\sin\beta', font_size=40)
        self.play(Write(eq, run_time=4))
        self.wait(2)
        self.play(Indicate(eq[3]), Indicate(eq[6]), run_time=2)
        self.wait(2)
        eq1 = MathTex(r'\cos(\alpha+\beta)+\cos(\alpha-\beta)', r'=', r'\cos\alpha\cos\beta', r'+', r'\cos\alpha\cos\beta')
        self.play(TransformMatchingTex(eq, eq1, run_time=2))
        self.wait(2)
        eq2 = MathTex(r'\cos(\alpha+\beta)+\cos(\alpha-\beta)', r'=', r'2', r'\cos\alpha\cos\beta')
        self.play(TransformMatchingTex(eq1, eq2, run_time=2))
        self.wait(2)
        eq3 = MathTex(r'\frac{1}{2}(', r'\cos(\alpha+\beta)+\cos(\alpha-\beta)', r')', r'=', r'\cos\alpha\cos\beta')
        self.play(TransformMatchingTex(eq2, eq3, run_time=2))
        self.wait(2)
        coscos = MathTex(r'\cos\alpha\cos\beta', r'=', r'\frac{1}{2}(', r'\cos(\alpha+\beta)+\cos(\alpha-\beta)', r')')
        sinsin = MathTex(r'\sin\alpha\sin\beta', r'=', r'\frac{1}{2}', r'(', r'\cos(\alpha-\beta)', r'-', r'\cos(\alpha+\beta)', r')')
        sincos = MathTex(r'\sin\alpha\cos\beta', r'=', r'\frac{1}{2}', r'(', r'\sin(\alpha+\beta)', r'+', r'\sin(\alpha-\beta)', r')').move_to(ORIGIN + 2*DOWN)
        self.play(TransformMatchingTex(eq3, coscos, run_time=2))
        self.wait(2)
        self.play(FadeOut(VGroup(cangsum, cangsub), run_time=1), coscos.animate.move_to(ORIGIN + 2*UP))
        self.play(Write(VGroup(sinsin, sincos), run_tim=3))
        self.wait(2)
        self.play(Circumscribe(VGroup(sinsin, sincos, coscos)), run_time=2)
        self.wait(4)

        coscos1 = MathTex(r'\frac{1}{2}(', r'\cos(\alpha+\beta)+\cos(\alpha-\beta)', r')', r'=', r'\cos\alpha\cos\beta').move_to(ORIGIN + 2*UP)
        sinsin1 = MathTex(r'\frac{1}{2}', r'(', r'\cos(\alpha-\beta)', r'-', r'\cos(\alpha+\beta)', r')', r'=', r'\sin\alpha\sin\beta')
        sincos1 = MathTex(r'\frac{1}{2}', r'(', r'\sin(\alpha+\beta)', r'+', r'\sin(\alpha-\beta)', r')', r'=', r'\sin\alpha\cos\beta').move_to(ORIGIN + 2*DOWN)
        self.play(TransformMatchingTex(sinsin, sinsin1, run_time=2),
                  TransformMatchingTex(sincos, sincos1, run_time=2),
                  TransformMatchingTex(coscos, coscos1, run_time=2))
        self.wait(2)
        
        coscos2 = MathTex(r'\cos(\alpha+\beta)+\cos(\alpha-\beta)', r'=', r'2', r'\cos\alpha\cos\beta').move_to(ORIGIN + 2*UP)
        sinsin2 = MathTex(r'\cos(\alpha-\beta)', r'-', r'\cos(\alpha+\beta)', r'=', r'2', r'\sin\alpha\sin\beta')
        sincos2 = MathTex(r'\sin(\alpha+\beta)', r'+', r'\sin(\alpha-\beta)', r'=', r'2', r'\sin\alpha\cos\beta').move_to(ORIGIN + 2*DOWN)
        self.play(TransformMatchingTex(sinsin1, sinsin2, run_time=2),
                  TransformMatchingTex(sincos1, sincos2, run_time=2),
                  TransformMatchingTex(coscos1, coscos2, run_time=2))
        self.wait(2)
        
        alpha = MathTex(r'\alpha = \frac{x+y}{2}', font_size=36).move_to(coscos2.get_center() + 1.2*UP + 3*LEFT)
        beta = MathTex(r'\beta = \frac{x-y}{2}', font_size=36).next_to(alpha, 10*RIGHT)
        self.play(Write(alpha), Write(beta), run_time=2)
        self.wait(2)

        coscos3 = MathTex(r'\cos x', r'+', r'\cos y', r'=', r'2', r'\cos\frac{x+y}{2}', r'\cdot', r'\cos\frac{x-y}{2}').move_to(ORIGIN + 2*UP)
        sinsin31 = MathTex(r'\cos y', r'-', r'\cos x', r'=', r'2', r'\sin\frac{x+y}{2}', r'\cdot', r'\sin\frac{x-y}{2}')
        sincos3 = MathTex(r'\sin x', r'+', r'\sin y', r'=', r'2', r'\sin\frac{x+y}{2}', r'\cdot', r'\cos\frac{x-y}{2}').move_to(ORIGIN + 2*DOWN)
        self.play(TransformMatchingShapes(sinsin2, sinsin31),
                  TransformMatchingShapes(sincos2, sincos3),
                  TransformMatchingShapes(coscos2, coscos3),
                  run_time=2)
        self.wait(1)
        sinsin3 = MathTex(r'\cos x', r'-', r'\cos y', r'=', r'-', r'2', r'\sin\frac{x+y}{2}', r'\cdot', r'\sin\frac{x-y}{2}')
        self.play(TransformMatchingShapes(sinsin31, sinsin3))
        self.wait(2)
        self.play(FadeOut(alpha), FadeOut(beta), run_time=2)
        self.play(sinsin3.animate.move_to(ORIGIN + 1.5*UP),
                  coscos3.animate.move_to(ORIGIN + 3*UP),
                  sincos3.animate.move_to(ORIGIN + 1.5*DOWN))
        self.wait(1)
        
        f = sincos3.copy()
        self.play(f.animate.move_to(ORIGIN + 3*DOWN))
        f1 = MathTex(r'\sin x', r'+', r'\sin (-y)', r'=', r'2', r'\sin\frac{x+(-y)}{2}', r'\cdot', r'\cos\frac{x-(-y)}{2}').move_to(ORIGIN + 3*DOWN)
        f2 = MathTex(r'\sin x', r'-', r'\sin y', r'=', r'2', r'\sin\frac{x-y}{2}', r'\cdot', r'\cos\frac{x+y}{2}').move_to(ORIGIN + 3*DOWN)
        self.play(ReplacementTransform(f, f1), run_time=2)
        self.wait(1)
        self.play(ReplacementTransform(f1, f2, run_time=2))
        self.wait(2)
        self.play(FadeOut(sinsin3, sincos3, coscos3, f2), run_time=2)
        
        
    
        self.wait(3)





