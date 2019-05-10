from tkinter import *
from tkinter import ttk
import webbrowser
from tkinter.filedialog import askopenfilename
import sys
import sparkx_fellows_students_matching


global filepathFellows
global filepathXLab

def teammate_matching_fellows():
    global filepathFellows
    filepathFellows = askopenfilename()

def teammate_matching_xlab():
    global filepathXLab
    filepathXLab = askopenfilename()

def generateOptimalMatches():
    global filepathFellows
    global filepathXLab
    sparkx_fellows_students_matching.main(sys.argv[1:], filepathFellows, filepathXLab)

def openTeammateMatchingFellows(event):
    webbrowser.open('http://google.com')

def openTeammateMatchingXLab(event):
    webbrowser.open('http://google.com')

def main():
    root = Tk()
    root.title("Teammate Matching Algorithm")

    hyper_text = Label(root, text="Teammate Matching - Fellows", fg="blue", cursor="hand2")
    hyper_text.pack(side=LEFT, padx=5, pady=5)
    hyper_text.bind("<Button-1>", openTeammateMatchingFellows)

    hyper_text = Label(root, text="Teammate Matching - X-Lab", fg="blue", cursor="hand2")
    hyper_text.pack(side=LEFT, padx=5, pady=5)
    hyper_text.bind("<Button-1>", openTeammateMatchingXLab)

    buttonTTK = ttk.Button(root, text='Import Fellowship Preferences', command=(lambda: teammate_matching_fellows() )).pack(side=LEFT)
    buttonTTK2 = ttk.Button(root, text='Import Teammate Preferences', command=(lambda: teammate_matching_xlab() )).pack(side=LEFT)
    buttonTTK3 = ttk.Button(root, text='Generate Optimal Matches', command=(lambda: generateOptimalMatches() )).pack(side=LEFT)
    
    root.mainloop()

main()

