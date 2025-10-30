from manim import *
 
class GraphWorldPopulation(Scene):
    def construct(self):
        ax = Axes(x_range=[0,10,1], y_range=[0,12,1])
        #set the x range to be the range of pop project x range
        f1 =  ax.plot(lambda x: 2*x, color = GREEN)
        
        self.add(ax,f1)
class AnimatedLogisticCurve(Scene):
    def construct(self):
        vt = ValueTracker(0)

        ax = Axes(x_range=[0,3500,400],y_range=[0,12,1],tips=False,
            axis_config={"include_numbers": True})

        f1 = always_redraw(lambda: ax.plot(lambda x: 11/(1+(3.981072*10**11)*(0.9867**x)),color=BLUE,x_range=[0,vt.get_value()]))

        f1_dot = always_redraw(lambda: Dot( 
            point=ax.c2p(vt.get_value(), f1.underlying_function(vt.get_value())),color=BLUE
        ))
        labels = ax.get_axis_labels(
            Tex("Years scene 1 AD").scale(0.7), Text("Population in Billions").scale(0.45))

        Logistic_Label = MathTex(r"f(x) = \frac{11}{1+3.98*10^{11}*0.987^x}").shift(LEFT*2.6).shift(UP*1).scale(.8)
        Name_Curve = Text("Logistic model").shift(RIGHT*3).shift(DOWN*1).scale(.8)
        self.play(Write(ax))
        self.add(labels)
        self.play(Write(Name_Curve),run_time = 2)
        self.play(Write(Logistic_Label))

        self.add(f1,f1_dot)
        self.play(vt.animate.set_value(3500), run_time=4)
        self.play(FadeOut(f1_dot))
        self.wait(2)
class AnimatedExponentalCurve(Scene):
    def construct(self):
        vt = ValueTracker(0)

        ax = Axes(x_range=[0,3500,400],y_range=[0,12,1],tips=False,
            axis_config={"include_numbers": True})

        f1 = always_redraw(lambda: ax.plot(lambda x: (6.112934*10**-13)*(1.015**x),color=BLUE,x_range=[0,vt.get_value()]))

        f1_dot = always_redraw(lambda: Dot( 
            point=ax.c2p(vt.get_value(), f1.underlying_function(vt.get_value())),color=BLUE
        ))
        labels = ax.get_axis_labels(
            Tex("Years scene 1 AD").scale(0.7), Text("Population in Billions").scale(0.45))

        Logistic_Label = MathTex(r"f(x) = {6.1*{10^{-13}}}*{1.015^x} ").shift(LEFT*2.6).shift(UP*1).scale(.8)
        Name_Curve = Text("Exponental model").shift(RIGHT*3.4).shift(DOWN*1).scale(.8)
        self.play(Write(ax))
        self.add(labels)
        self.play(Write(Name_Curve),run_time = 2)
        self.play(Write(Logistic_Label))

        self.add(f1,f1_dot)
        self.play(vt.animate.set_value(2065), run_time=4)
        self.play(FadeOut(f1_dot))
        self.wait(2)
        

      
        

            