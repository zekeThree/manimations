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

        ax = Axes(x_range=[0,3500,200],y_range=[0,12,1])

        f1 = always_redraw(lambda: ax.plot(lambda x: 11/(1+(3.981072*10**11)*(0.9867**x)),color=BLUE,x_range=[0,vt.get_value()]))

        f1_dot = always_redraw(lambda: Dot( 
            point=ax.c2p(vt.get_value(), f1.underlying_function(vt.get_value())),color=BLUE
        ))

        self.play(Write(ax))
        self.wait()

        self.add(f1,f1_dot)
        self.play(vt.animate.set_value(3500), run_time=4)

        

      
        

            