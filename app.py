import time
from tkinter import *
from tkinter import scrolledtext
import chatBot

master = Tk()
master.title("Symptoms ChatBot")
master.geometry("400x500")

def sendMessage():
    userEntry = entry.get()
    #print(userEntry.strip())
    symptoms = userEntry.split(",")
    symptoms = [symptom.strip().replace(" ","_") for symptom in symptoms]
    normalInput = " ".join(symptoms)
    if normalInput.strip():
        chatDisplay.config(state="normal")
        chatDisplay.insert(END, f"\nYou: {normalInput}\n\n")

        if userEntry.lower() == "yes":
            # Reset prompt for new symptoms
            chatDisplay.insert(END, "Please type your symptoms below and press 'Send' to continue.\n")
            chatDisplay.config(state="disabled")
            entry.delete(0, END)
            return
        elif userEntry.lower() == "no":
            # Exit the chatbot
            chatDisplay.insert(END, "Thank you. Shutting down now.\n")
            master.quit()  # Stop the Tkinter main loop
            return
        else:
            # Process the user's symptoms
            chatDisplay.insert(END, "Scanning our database for your symptoms. Please wait...\n")
            chatDisplay.config(state="disabled")
            master.update()  # Refresh GUI
            entry.delete(0, END)

            try:
                response = chatBot.calling_the_bot(userEntry.strip())
                chatDisplay.config(state="normal")
                chatDisplay.insert(END, f"\nDoc: {response}\n")
            except Exception as e:
                chatDisplay.config(state="normal")
                chatDisplay.insert(END, "Sorry, an error occurred. Please try again.\n")
                chatDisplay.insert(END, f"Error: {e}\n")
            finally:
                chatDisplay.insert(END, "Do you want to continue? Type 'yes' to continue or 'no' to exit.\n")
                chatDisplay.config(state="disabled")



chatDisplay = scrolledtext.ScrolledText(master, wrap=WORD, state="normal", height=10,font=("Times New Roman", 16))
chatDisplay.pack(padx=10,pady=10,fill=BOTH,expand=True)
chatDisplay.insert(END,"Bot is running\n")
chatDisplay.insert(END,"Hello, I am Doc, your personal Talking Symptoms ChatBot\n")
chatDisplay.insert(END,"Type your symptoms below and press 'Send' to get started.\n")
chatDisplay.config(state="disabled")


entry = Entry(master,font=("Times New Roman", 16))
entry.pack(padx=10, pady =10, fill = X)

send = Button(master,text="Send", command=sendMessage, font=("Times Nes Roman", 16))
send.pack(padx=0,pady=0)

#master.bind("<Return>",lambda event: sendMessage())

master.mainloop()

