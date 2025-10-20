# 🎥 Video to ASCII Art (Tkinter + OpenCV)

Ce projet est une visualisation ASCII en temps réel de vidéos, affichée dans une interface graphique Tkinter à partir d’un fichier vidéo local.  
L’application convertit chaque frame du clip en caractères ASCII selon leur niveau de luminosité, créant un rendu artistique en noir et blanc directement dans une fenêtre Python.

---

## 🚀 Fonctionnalités

- 🔢 Conversion de chaque pixel en caractères ASCII selon sa luminosité.  
- 🎬 Lecture d’une vidéo locale (`.mp4`) avec **OpenCV**.  
- 🪟 Affichage en direct du rendu ASCII avec **Tkinter**.  
- ⌨️ Fermeture rapide via la touche **Échap (Escape)**.  
- ⚙️ Multithreading pour une lecture fluide (interface Tkinter non bloquée).  

---

## 🧰 Technologies utilisées

- **Python 3.x**  
- **OpenCV** – Lecture et traitement d’images vidéo.  
- **Tkinter** – Interface graphique légère pour afficher le rendu ASCII.  
- **Keyboard** – Détection des touches clavier pour quitter l’application.  
- **Threading** – Permet de séparer la lecture vidéo de l’interface utilisateur.

---

## 📦 Installation

1. Clone le projet :
   ```bash
   git clone https://github.com/ton-utilisateur/videotoascii.git
   cd videotoascii
