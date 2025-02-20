from manim import *
#virtualenv venv
#.\venv\Scripts\activate
#Calidades: [l|m|h|p|k]
#Preview de baja calidad: manim .\Tutorial\tut_2.py -pql
#Preview de media calidad: manim .\Tutorial\tut_2.py -pqm
#Preview de alta calidad: manim .\Tutorial\tut_2.py -pqh
#Preview 4K: manim .\Tutorial\tut_2.py -pqk
#Último frame de alta calidad: manim .\Tutorial\tut_2.py -sqh
#Asignar nombre: manim .\Tutorial\tut_2.py -pqh -o Textito
#Renderizar algunas animaciones: manim .\Tutorial\tut_2.py -pqh -n 2,4
#Exportar con formato personalizado [png|gif|mp4|webm|mov]: manim .\Tutorial\tut_2.py -pql --format gif
#Abrir el directorio del archivo renderizado: manim .\Tutorial\tut_2.py -qh --show_in_file_browser
#Resolución personalizada: manim .\Tutorial\tut_2.py -pqh -r 1080,1920
#FPS: manim .\Tutorial\tut_2.py -pqh --fps 20
#Transparente: manim .\Tutorial\tut_2.py -pqh -t
#Renderiza todas las escenas: manim .\Tutorial\tut_2.py -pqh -a
class tut_2(MovingCameraScene):
	def construct(self):
		title = Tex(r"Texto estilo \LaTeX")
		basilea = MathTex(r"\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}").next_to(title,DOWN)
		self.play(Write(title),FadeIn(basilea,shift=DOWN))
		self.wait()
		transform_title = Tex("Transformación de texto").to_corner(UP+LEFT)
		self.play(Transform(title,transform_title),FadeOut(basilea,shift=DOWN))
		self.wait()
		grid = NumberPlane()
		grid_title = Tex("Plano numérico").to_edge(DOWN).scale(1.5).set_color(YELLOW)
		self.play(Create(grid),Write(grid_title))
		self.wait()
