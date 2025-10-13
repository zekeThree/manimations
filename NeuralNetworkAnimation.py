from manim import *
 
class NeuralNetworkAnimation(Scene):
    def construct(self):
        inputNeuronList = []
        numberOfInputNeurons = 5
        for i in range(numberOfInputNeurons):
            inputNeuronList.append(Circle(radius=.2,color=BLUE))
        for i in range(len(inputNeuronList)):
            inputNeuronList[i].shift(DOWN * i)
            self.play(Create(inputNeuronList[i]))
        
        #add hidden layer and graph
        circ = Circle(color=RED).shift(4*LEFT)
        dot = Dot(color=RED).move_to(circ.get_start())
        #rolling_circle = VGroup(circ, dot)
        trace = TracedPath(circ.get_start)
        #rolling_circle.add_updater(lambda m: m.rotate(-0.1))
        #self.add(trace, rolling_circle)
        self.play(circ.animate.shift(8*RIGHT).shift(DOWN*3), run_time=4, rate_func=linear)
        self.add(trace)   
        self.play(circ.animate.shift(UP*3),run_time = 3,rate_func = linear )
        self.wait(2)
        

            