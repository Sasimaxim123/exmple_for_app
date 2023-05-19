
from kivy.app import App 
from kivy.garden.joystick import Joystick
from kivy.uix.label import Label

from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


from kivy.core.window import Window
Window.size = (500, 885)

#class MyGridLayout(GridLayout):


from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout



class MyApp(App):

	def btn_press1(self, r):
		print("Работает11111")

	def build(self):
		Window.clearcolor = (38/255,38/255,38/255,1)

		fl = FloatLayout()
		#bl = BoxLayout(orientation='vertical')
		fl.padding = 50

		fl.add_widget(Button(text = "1", 
			font_size = 1, 
			on_press = self.btn_press, 
			background_normal = '1.png',
			background_down = '11.png',
			size_hint = (0.15, 0.085),
			pos_hint = {'x' : 0.05, 'y' : 0.85}
			))

		fl.add_widget(Button(text = "2", 
			font_size = 1, 
			on_press = self.btn_press, 
			#background_color = [1, 0.1, 0, 0],
			background_normal = '2.png',
			background_down = '22.png',
			size_hint = (0.15, 0.085),
			pos_hint = {'x' : 0.30, 'y' : 0.85}
			))

		fl.add_widget(Button(text = "3", 
			font_size = 1, 
			on_press = self.btn_press, 
			background_normal = '3.png',
			background_down = '33.png',
			size_hint = (0.15, 0.085),
			pos_hint = {'x' : 0.55, 'y' : 0.85}
			))

		fl.add_widget(Button(text = "4", 
			font_size = 1, 
			on_press = self.btn_press, 
			background_normal = '4.png',
			background_down = '44.png',
			size_hint = (0.15, 0.085),
			pos_hint = {'x' : 0.8, 'y' : 0.85} 
			))
		




		fl.add_widget(Button(text = "+", 
			font_size = 50, 
			on_press = self.btn_press, 
			background_color = (28/255,28/255,28/255,1),
			background_normal = '',
			size_hint = (0.15, 0.085),
			pos_hint = {'x' : 0.05, 'y' : 0.65}))
		fl.add_widget(Button(text = "mute", 
			font_size = 1, 
			on_press = self.btn_press, 
			background_normal = 'mute.png',
			background_down = 'mute_press.png',
			size_hint = (0.15, 0.085),
			pos_hint = {'x' : 0.05, 'y' : 0.565}))
		fl.add_widget(Button(text = "-", 
			font_size = 50, 
			on_press = self.btn_press, 
			background_color = (28/255,28/255,28/255,1),
			background_normal = '',
			size_hint = (0.15, 0.085),
			pos_hint = {'x' : 0.05, 'y' : 0.48}))
		

		fl.add_widget(Button(text = "up", 
			font_size = 1, 
			on_press = self.btn_press, 
			background_normal = 'up.png',
			background_down = 'up_press.png',
			size_hint = (0.15, 0.085),
			pos_hint = {'x' : 0.8, 'y' : 0.65}))
		fl.add_widget(Button(text = "s_up", 
			font_size = 1, 
			on_press = self.btn_press, 
			background_normal = 'click.png',
			background_down = 'mute_press.png',
			size_hint = (0.15, 0.085),
			pos_hint = {'x' : 0.8, 'y' : 0.565}))
		fl.add_widget(Button(text = "down", 
			font_size = 1, 
			on_press = self.btn_press, 
			background_normal = 'down.png',
			background_down = 'down_press.png',
			size_hint = (0.15, 0.085),
			pos_hint = {'x' : 0.8, 'y' : 0.48}))


		#return Label(text = "StayCool", font_size = 72)
		
		
		joystick = Joystick(
		sticky = False,
		outer_size= 0.9,
		inner_size= 0.65,
		pad_size=   0.45,
		outer_line_width= 0.01,
		inner_line_width= 0.01,
		pad_line_width=   0.01,
		outer_background_color= (30/255,30/255,30/255,1),
		outer_line_color=       (30/255,30/255,30/255,1),
		inner_background_color= (28/255,28/255,28/255,1),
		inner_line_color=       (28/255,28/255,28/255,1),
		pad_background_color = (24/255,24/255,24/255,1),
		pad_line_color = (24/255,24/255,24/255,1),
        size_hint = (0.5, 0.5),
		pos_hint = {'center_x' : 0.5, 'center_y' : 0.605}

		)

		joystick.bind(pad=self.update_coordinates)
		
		fl.add_widget(joystick)
		
		self.label = Label()

		fl.add_widget(self.label)

		return fl

	def update_coordinates(self, joystick, pad):
		x = str(pad[0])[0:5]
		y = str(pad[1])[0:5]
		
		radians = str(joystick.radians)[0:5]
		magnitude = str(joystick.magnitude)[0:5]
		angle = str(joystick.angle)[0:5]
		text = "x: {}\ny: {}\nradians: {}\nmagnitude: {}\nangle: {}"
		#self.label.text = text.format(x, y, radians, magnitude, angle)
		
		



	def btn_press(self, instance):
		print("Работает")
		print(instance.text)



if __name__ == "__main__":
	MyApp().run()

'''
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput 

from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.anchorlayout import AnchorLayout 

class BoxApp(App):
	def build (self):
		al = AnchorLayout()
		bl = BoxLayout(orientation = 'vertical', size_hint=[None, None], size= [300, 200])

		bl.add_widget( TextInput(font_size = 35) )
		bl.add_widget( TextInput(font_size = 35) ) 
		bl.add_widget( Button(text = "Войти", font_size = 35, 
			on_press = self.btn_press, 
			background_color = [1, 0.1, 0, 0.55],
			background_normal = ''))


		al. add_widget(bl)
		return al

	def btn_press(self, instance):
		pass
if __name__ == "__main__":
	BoxApp().run()

'''