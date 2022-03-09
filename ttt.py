#CodeWithHN

from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.button import MDRoundFlatButton
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.tab import MDTabs
from kivy.lang import Builder
from kivymd.uix.toolbar import MDToolbar
from kivy.core.text import LabelBase
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.label import Label,MDIcon
from kivy.properties import ObjectProperty
from kivymd.uix.label import MDLabel


LabelBase.register(name='font',fn_regular='my_font.ttf')

class tictac(FloatLayout):
	
	screen_mngr = ObjectProperty(None)
	
	def check1(self):
		lebelTxt = self.screen_mngr.home.lebel.text
		firstTxt = self.screen_mngr.home.first.text
		
		if (lebelTxt == "Player : O" and firstTxt == " "):
			self.screen_mngr.home.first.text = "o"
			self.screen_mngr.home.lebel.text = "Player : X"
		
		elif (lebelTxt == "Player : X" and firstTxt != "o"):
			self.screen_mngr.home.first.text = "×"
			self.screen_mngr.home.lebel.text = "Player : O"
		
		else:
			pass

	def check2(self):
		lebelTxt = self.screen_mngr.home.lebel.text
		secondTxt = self.screen_mngr.home.second.text
		
		if (lebelTxt == "Player : O" and secondTxt == " "):
			self.screen_mngr.home.second.text = "o"
			self.screen_mngr.home.lebel.text = "Player : X"
		
		elif (lebelTxt == "Player : X" and secondTxt != "o"):
			self.screen_mngr.home.second.text = "×"
			self.screen_mngr.home.lebel.text = "Player : O"
		
		else:
			pass
	
	def check3(self):
		lebelTxt = self.screen_mngr.home.lebel.text
		thirdTxt = self.screen_mngr.home.third.text
		
		if (lebelTxt == "Player : O" and thirdTxt == " "):
			self.screen_mngr.home.third.text = "o"
			self.screen_mngr.home.lebel.text = "Player : X"
		
		elif (lebelTxt == "Player : X" and thirdTxt != "o"):
			self.screen_mngr.home.third.text = "×"
			self.screen_mngr.home.lebel.text = "Player : O"
		
		else:
			pass
		
	def check4(self):
		lebelTxt = self.screen_mngr.home.lebel.text
		fourthTxt = self.screen_mngr.home.fourth.text
		
		if (lebelTxt == "Player : O" and fourthTxt == " "):
			self.screen_mngr.home.fourth.text = "o"
			self.screen_mngr.home.lebel.text = "Player : X"
		
		elif (lebelTxt == "Player : X" and fourthTxt != "o"):
			self.screen_mngr.home.fourth.text = "×"
			self.screen_mngr.home.lebel.text = "Player : O"
		
		else:
			pass
	
	def check5(self):
		lebelTxt = self.screen_mngr.home.lebel.text
		fifthTxt = self.screen_mngr.home.fifth.text
		
		if (lebelTxt == "Player : O" and fifthTxt == " "):
			self.screen_mngr.home.fifth.text = "o"
			self.screen_mngr.home.lebel.text = "Player : X"
		
		elif (lebelTxt == "Player : X" and fifthTxt != "o"):
			self.screen_mngr.home.fifth.text = "×"
			self.screen_mngr.home.lebel.text = "Player : O"
		
		else:
			pass

	
	def check6(self):
		lebelTxt = self.screen_mngr.home.lebel.text
		sixthTxt = self.screen_mngr.home.sixth.text
		
		
		if (lebelTxt == "Player : O" and sixthTxt == " "):
			self.screen_mngr.home.sixth.text = "o"
			self.screen_mngr.home.lebel.text = "Player : X"
		
		elif (lebelTxt == "Player : X" and sixthTxt != "o"):
			self.screen_mngr.home.sixth.text = "×"
			self.screen_mngr.home.lebel.text = "Player : O"
		
		else:
			pass
	
	def check7(self):
		lebelTxt = self.screen_mngr.home.lebel.text
		seventhTxt = self.screen_mngr.home.seventh.text
		
		
		if (lebelTxt == "Player : O" and seventhTxt == " "):
			self.screen_mngr.home.seventh.text = "o"
			self.screen_mngr.home.lebel.text = "Player : X"
		
		elif (lebelTxt == "Player : X" and seventhTxt != "o"):
			self.screen_mngr.home.seventh.text = "×"
			self.screen_mngr.home.lebel.text = "Player : O"
		
		else:
			pass
	
	def check8(self):
		lebelTxt = self.screen_mngr.home.lebel.text
		eighthTxt = self.screen_mngr.home.eighth.text
		
		if (lebelTxt == "Player : O" and eighthTxt == " "):
			self.screen_mngr.home.eighth.text = "o"
			self.screen_mngr.home.lebel.text = "Player : X"
		
		elif (lebelTxt == "Player : X" and eighthTxt != "o"):
			self.screen_mngr.home.eighth.text = "×"
			self.screen_mngr.home.lebel.text = "Player : O"
		
		else:
			pass
	
	def check9(self):
		lebelTxt = self.screen_mngr.home.lebel.text
		ninthTxt = self.screen_mngr.home.ninth.text
		
		if (lebelTxt == "Player : O" and ninthTxt == " "):
			self.screen_mngr.home.ninth.text = "o"
			self.screen_mngr.home.lebel.text = "Player : X"
		
		elif (lebelTxt == "Player : X" and ninthTxt != "o"):
			self.screen_mngr.home.ninth.text = "×"
			self.screen_mngr.home.lebel.text = "Player : O"
		
		else:
			pass
	
	def reset(self):
		self.screen_mngr.home.lebel.text = "Player : O"
		self.screen_mngr.home.first.text = " "
		self.screen_mngr.home.second.text = " "
		self.screen_mngr.home.third.text = ' '
		self.screen_mngr.home.fourth.text = ' '
		self.screen_mngr.home.fifth.text = ' '
		self.screen_mngr.home.sixth.text = ' '
		self.screen_mngr.home.seventh.text = ' '
		self.screen_mngr.home.eighth.text = ' '
		self.screen_mngr.home.ninth.text = ' '
		
		#RESET COLOR
		self.screen_mngr.home.ninth.text_color=0.12941176470588237, 0.5882352941176471, 0.9529411764705882, 1.0
		
		self.screen_mngr.home.eighth.text_color=0.12941176470588237, 0.5882352941176471, 0.9529411764705882, 1.0
		
		self.screen_mngr.home.seventh.text_color=0.12941176470588237, 0.5882352941176471, 0.9529411764705882, 1.0
		
		self.screen_mngr.home.sixth.text_color=0.12941176470588237, 0.5882352941176471, 0.9529411764705882, 1.0
		
		self.screen_mngr.home.fifth.text_color=0.12941176470588237, 0.5882352941176471, 0.9529411764705882, 1.0
		
		self.screen_mngr.home.fourth.text_color=0.12941176470588237, 0.5882352941176471, 0.9529411764705882, 1.0
		
		self.screen_mngr.home.third.text_color=0.12941176470588237, 0.5882352941176471, 0.9529411764705882, 1.0
		
		self.screen_mngr.home.second.text_color=0.12941176470588237, 0.5882352941176471, 0.9529411764705882, 1.0
		
		self.screen_mngr.home.first.text_color=0.12941176470588237, 0.5882352941176471, 0.9529411764705882, 1.0
	
	def winner(self):
		lebelTxt = self.screen_mngr.home.lebel.text
		firstTxt = self.screen_mngr.home.first.text
		secondTxt = self.screen_mngr.home.second.text
		thirdTxt = self.screen_mngr.home.third.text
		fourthTxt = self.screen_mngr.home.fourth.text
		fifthTxt = self.screen_mngr.home.fifth.text
		sixthTxt = self.screen_mngr.home.sixth.text
		seventhTxt = self.screen_mngr.home.seventh.text
		eighthTxt = self.screen_mngr.home.eighth.text
		ninthTxt = self.screen_mngr.home.ninth.text
		
		#Horizontal.....
		
		if (firstTxt=="o" and secondTxt=="o" and thirdTxt=="o"):
			self.screen_mngr.home.lebel.text="O : Wins"
			self.screen_mngr.home.first.text_color = 1,0,0,1
			self.screen_mngr.home.second.text_color = 1,0,0,1
			self.screen_mngr.home.third.text_color = 1,0,0,1
		
		elif (fourthTxt=="o" and fifthTxt=="o" and sixthTxt=="o"):
			self.screen_mngr.home.lebel.text="O : Wins"
			
			self.screen_mngr.home.fourth.text_color = 1,0,0,1
			self.screen_mngr.home.fifth.text_color = 1,0,0,1
			self.screen_mngr.home.sixth.text_color = 1,0,0,1
		
		elif (seventhTxt=="o" and eighthTxt=="o" and ninthTxt=="o"):
			self.screen_mngr.home.lebel.text="O : Wins"
			self.screen_mngr.home.seventh.text_color = 1,0,0,1
			self.screen_mngr.home.eighth.text_color = 1,0,0,1
			self.screen_mngr.home.ninth.text_color = 1,0,0,1
		
		elif (firstTxt=="×" and secondTxt=="×" and thirdTxt=="×"):
			self.screen_mngr.home.lebel.text="X : Wins"
			self.screen_mngr.home.first.text_color = 1,0,0,1
			self.screen_mngr.home.second.text_color = 1,0,0,1
			self.screen_mngr.home.third.text_color = 1,0,0,1
		
		elif (fourthTxt=="×" and fifthTxt=="×" and sixthTxt=="×"):
			self.screen_mngr.home.lebel.text="X : Wins"
			self.screen_mngr.home.fourth.text_color = 1,0,0,1
			self.screen_mngr.home.fifth.text_color = 1,0,0,1
			self.screen_mngr.home.sixth.text_color = 1,0,0,1
		
		elif (seventhTxt=="×" and eighthTxt=="×" and ninthTxt=="×"):
			self.screen_mngr.home.lebel.text="X : Wins"
			self.screen_mngr.home.seventh.text_color = 1,0,0,1
			self.screen_mngr.home.eighth.text_color = 1,0,0,1
			self.screen_mngr.home.ninth.text_color = 1,0,0,1
		
		#Vertical....
		
		elif (firstTxt=="o" and fourthTxt=="o" and seventhTxt=="o"):
			self.screen_mngr.home.lebel.text="O : Wins"
			
			self.screen_mngr.home.first.text_color = 1,0,0,1
			self.screen_mngr.home.fourth.text_color = 1,0,0,1
			self.screen_mngr.home.seventh.text_color = 1,0,0,1
		
		elif (secondTxt=="o" and fifthTxt=="o" and eighthTxt=="o"):
			self.screen_mngr.home.lebel.text="O : Wins"
			self.screen_mngr.home.second.text_color = 1,0,0,1
			self.screen_mngr.home.fifth.text_color = 1,0,0,1
			self.screen_mngr.home.eighth.text_color = 1,0,0,1
		
		elif (thirdTxt=="o" and sixthTxt=="o" and ninthTxt=="o"):
			self.screen_mngr.home.lebel.text="O : Wins"
			self.screen_mngr.home.third.text_color = 1,0,0,1
			self.screen_mngr.home.sixth.text_color = 1,0,0,1
			self.screen_mngr.home.ninth.text_color = 1,0,0,1
		
		elif (firstTxt=="×" and fourthTxt=="×" and seventhTxt=="×"):
			self.screen_mngr.home.lebel.text="X : Wins"
			
			self.screen_mngr.home.first.text_color = 1,0,0,1
			self.screen_mngr.home.fourth.text_color = 1,0,0,1
			self.screen_mngr.home.seventh.text_color = 1,0,0,1
		
		elif (secondTxt=="×" and fifthTxt=="×" and eighthTxt=="×"):
			self.screen_mngr.home.lebel.text="X : Wins"
			self.screen_mngr.home.second.text_color = 1,0,0,1
			self.screen_mngr.home.fifth.text_color = 1,0,0,1
			self.screen_mngr.home.eighth.text_color = 1,0,0,1
		
		elif (thirdTxt=="×" and sixthTxt=="×" and ninthTxt=="×"):
			self.screen_mngr.home.lebel.text="X : Wins"
			self.screen_mngr.home.third.text_color = 1,0,0,1
			self.screen_mngr.home.sixth.text_color = 1,0,0,1
			self.screen_mngr.home.ninth.text_color = 1,0,0,1
		
		#Cross......
		
		elif (firstTxt=="×" and fifthTxt=="×" and ninthTxt=="×"):
			self.screen_mngr.home.lebel.text="X : Wins"
			self.screen_mngr.home.first.text_color = 1,0,0,1
			self.screen_mngr.home.fifth.text_color = 1,0,0,1
			self.screen_mngr.home.ninth.text_color = 1,0,0,1
		
		elif (thirdTxt=="×" and fifthTxt=="×" and seventhTxt=="×"):
			self.screen_mngr.home.lebel.text="X : Wins"
			self.screen_mngr.home.third.text_color = 1,0,0,1
			self.screen_mngr.home.fifth.text_color = 1,0,0,1
			self.screen_mngr.home.seventh.text_color = 1,0,0,1
			
		elif (firstTxt=="o" and fifthTxt=="o" and ninthTxt=="o"):
			self.screen_mngr.home.lebel.text="O : Wins"
			self.screen_mngr.home.first.text_color = 1,0,0,1
			self.screen_mngr.home.fifth.text_color = 1,0,0,1
			self.screen_mngr.home.ninth.text_color = 1,0,0,1
		
		elif (thirdTxt=="o" and fifthTxt=="o" and seventhTxt=="o"):
			self.screen_mngr.home.lebel.text="O : Wins"
		
			self.screen_mngr.home.fifth.text_color = 1,0,0,1
			self.screen_mngr.home.seventh.text_color = 1,0,0,1
			self.screen_mngr.home.third.text_color = 1,0,0,1
		
		
		else:
			pass
		
		
	

class ticgame(MDApp):
	def build(self):
		screen = Screen()
		return Builder.load_file("tictoe.kv")

if __name__=="__main__":
	ticgame().run()