from manim import *
#virtualenv venv
#.\venv\Scripts\activate
#manim .\Tutorial\tut_3.py -pqh --show_in_file_browser
class tut_3(MovingCameraScene):
	def construct(self):
		t1 = Text(r"Metrische tensor $g_{\mu\nu}$").move_to(3*UP).set_color(RED)
		t2 = Tex(r"Metrische tensor $g_{\mu\nu}$").set_color(YELLOW)
		t3 = MathTex(r"\text{Metrische tensor }g_{\mu\nu}").move_to(3*DOWN).set_color("#31FA05")
		t4 = MathTex(r"g_{",r"\mu",r"\nu}").move_to(5*LEFT)
		t4[0].set_color(RED)
		t4[1].set_color(YELLOW)
		t4[2].set_color(GREEN)
		t5 = MathTex(r"\frac{a+b}{c-d}").move_to(5*RIGHT+1*UP)
		t6 = MathTex(r"{{a",r"+",r"b}",r"\over",r"{c",r"-",r"d}}").next_to(t5,DOWN)
		lista = ["#FA1005",ORANGE,YELLOW,"#31FA05",TEAL,BLUE,"#2061EC"]
		for i in range(len(lista)):
			t6[i].set_color(lista[i])
		grid = NumberPlane()
		self.add(t1,t2,t3,t4,t5,t6,grid)
