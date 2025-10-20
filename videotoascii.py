import cv2
import tkinter
import threading
import keyboard

#Transformer un nombre (0-255) en ascii
def number_to_ascii(number):
    color_Palette = ['..',':','!','*','%','$','@','&','#','S','B']
    color_list = [23, 46, 69, 92, 115, 138, 161, 184, 207, 230, 255]
    for i in range(len(color_list)):
        if number <= color_list[i]:
            return(color_Palette[i])

#code principal
def main():
    VideoPath = "choose your file directory"
    cap = cv2.VideoCapture(VideoPath)
    run = True
    while (cap.isOpened() and run):
        _, frame = cap.read() 
        grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #on le convertit en tableau à 2 dimensions, en rendant l'image en noir et blanc
        result = ""
        for i in range(len(grayImage)):
            for j in range(grayImage.shape[1]):
                result += number_to_ascii(int(grayImage[i,j]))
            result += "\n"
        my_label.config(text = result)
        if keyboard.is_pressed("escape"):
            app.destroy()
            run = False
            exit()

#Partie tkinter
if __name__ == "__main__":
    th1 = threading.Thread(target=main)
    th1.start()
    app = tkinter.Tk()
    my_label = tkinter.Label(app)
    my_label.pack()
    app.title("title")
    app.mainloop()