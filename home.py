import kivy
import subprocess
import os
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QMessageBox, QLabel
from PySide6.QtCore import QTimer, Qt
import pyqtgraph as pg
from constants import wireshark_file_path
from random import randint
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QProgressBar, QLabel, QListWidgetItem
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import Qt
from securitycheck import get_packets_and_entropy
from scapy.all import *
from scapy.layers.inet import IP  # Add this line to import the IP class
import math

class Home(App):
    def build(self):
        root = FloatLayout()  # Switch this to whatever png we need
        
        # Background Image
        bg_image = Image(source='Project-NetProbeX/background.png', allow_stretch=True, keep_ratio=False)
        root.add_widget(bg_image)

        # Sidebar
        sidebar = BoxLayout(orientation='vertical', size_hint=(None, 1), width=200)
        sidebar_button = Button(text='≡', size_hint=(None, None), size=(50, 50))
        sidebar_button.bind(on_release=self.show_sidebar)
        sidebar.add_widget(sidebar_button)
        
        root.add_widget(sidebar)
        return root
    
    def show_sidebar(self, instance):
        # Popup for Sidebar
        content = BoxLayout(orientation='vertical')
        task1_label = Button(text='Task 1')
        task2_label = Button(text='Task 2')
        task3_label = Button(text='Task 3')
        task4_label = Button(text='Task 4')
        task5_label = Button(text='Task 5')
        
        task2_label.bind(on_press=self.open_visualaid)  # Binding the function to Task 2
        task5_label.bind(on_press=self.filter_analysis_win)
        
        content.add_widget(task1_label)
        content.add_widget(task2_label)
        content.add_widget(task3_label)
        content.add_widget(task4_label)
        content.add_widget(task5_label)
        
        popup = Popup(title='Sidebar', content=content, size_hint=(None, 1), width=200)
        popup.open()
    
    def open_visualaid(self, instance):
       try:
            subprocess.Popen(['python', 'Project-NetProbeX/visualaid.py'])  # Launch visualaid.py script
       except Exception as e:
            print(f"Error occurred while launching visualaid.py: {e}")
    
    def filter_analysis_win(self, instance):
        try:
            subprocess.Popen(['python','Project-NetProbeX/filter_analysis_win.py'])
        except Exception as e:
            print(f"Error occured while launching filter_analysis_win.py: {e}")

if __name__ == "__main__":
    Home().run()
