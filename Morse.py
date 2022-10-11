from tkinter import*
root=Tk()
root.title("Translator")
root.geometry("900x900")
root.config(background="#ffffe0")
l2=Label(root,text="Morse Code Translator..", bg="#ffffe0", fg="#E74C3C",font="verdana 12 bold")
l2.place(relx=0.5,rely=0.3,anchor=CENTER)
var=IntVar()
var1=StringVar()
def txt():
    global h
def mor():
    global m

def sub():
    pay=str(var.get())
    pay=int(pay)
    root1=Tk()
    root1.geometry("900x900")
    root1.config(background="#ffffe0")
    
    if(pay==1):
        root1.title("Morse code generator")
        l5=Label(root1,text="Translate Message", bg="#ffffe0", fg="#E74C3C",font="verdana 12 bold")
        l5.place(relx=0.3,rely=0.16,anchor=CENTER)
        e=Text(root1,height=10,width=25)
        e.place(relx=0.3,rely=0.3,anchor=CENTER)
        l3=Label(root1,text="Translated Message", bg="#ffffe0", fg="#E74C3C",font="verdana 12 bold")
        l3.place(relx=0.7,rely=0.16,anchor=CENTER)
        e1=Text(root1,height=10,width=25)
        e1.place(relx=0.7,rely=0.3,anchor=CENTER)
        def subm():
            t=e.get("1.0", "end-1c")
            p=t.split(" ")
            l=[]
            for i in p:
                i=i.lower()
                l.append(i)
                
            s=""
            mo={"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
            for i in l:
                for j in i:
                    s=s+mo[j]+"  "
                s=s+" /n "
       
            e1=Text(root1,height=10,width=25)
            e1.place(relx=0.7,rely=0.3,anchor=CENTER)
            e1.insert(END, s)
        def cl():
            e.delete("1.0", "end-1c")
            e1=Text(root1,height=10,width=25)
            e1.place(relx=0.7,rely=0.3,anchor=CENTER)
        Button(root1,text="Submit",bg="#fdde6c", fg="#000", font="verdana 12 bold ",command=subm).place(relx=0.3,rely=0.6,anchor=CENTER)
        Button(root1,text="Clear",bg="#fdde6c", fg="#000", font="verdana 12 bold ",command=cl).place(relx=0.6,rely=0.6,anchor=CENTER)
        l6=Label(root1,text="Note : Make sure the text does not contain any special symbols or digits", bg="#ffffe0", fg="#E74C3C",font="verdana 12 bold")
        l6.place(relx=0.5,rely=0.8,anchor=CENTER)
    elif(pay==2):
        root1.title("Text generator")
        l5=Label(root1,text="Translate Message", bg="#ffffe0", fg="#E74C3C",font="verdana 12 bold")
        l5.place(relx=0.3,rely=0.16,anchor=CENTER)
        l3=Label(root1,text="Translated Message", bg="#ffffe0", fg="#E74C3C",font="verdana 12 bold")
        l3.place(relx=0.7,rely=0.16,anchor=CENTER)
        e=Text(root1,height=10,width=25)
        e.place(relx=0.3,rely=0.3,anchor=CENTER)
        e1=Text(root1,height=10,width=25)
        e1.place(relx=0.7,rely=0.3,anchor=CENTER)
        def subm():
            t=e.get("1.0", "end-1c")
            p=t.split("/n")
            l=[]
            for i in p:
                i=i.lower()
                l.append(i)
                
            s=""
            mo={"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
            ko=list(mo.keys())
            lo=list(mo.values())
            for i in l:
                f=""
                for j in i:
                    if(j==" "):
                        if(len(f)>1):
                            po=lo.index(f)
                            s=s+ko[po]
                            f=""
                        if(len(f)==1 and f!=" "):
                            po=lo.index(f)
                            s=s+ko[po]
                            f=""
                        f=""
                    else:
                        
                        f=f+j
                s=s+" "
           
            e1=Text(root1,height=10,width=25)
            e1.place(relx=0.7,rely=0.3,anchor=CENTER)
            e1.insert(END, s)
        def cl():
            e.delete("1.0", "end-1c")
            e1=Text(root1,height=10,width=25)
            e1.place(relx=0.7,rely=0.3,anchor=CENTER)
            
            
        Button(root1,text="Submit",bg="#fdde6c", fg="#000", font="verdana 12 bold ",command=subm).place(relx=0.3,rely=0.6,anchor=CENTER)
        Button(root1,text="Clear",bg="#fdde6c", fg="#000", font="verdana 12 bold ",command=cl).place(relx=0.6,rely=0.6,anchor=CENTER)
        l6=Label(root1,text="Note : Use space after completing the notation of character and use ( /n ) after completing the word ", bg="#ffffe0", fg="#E74C3C",font="verdana 12 bold")
        l6.place(relx=0.5,rely=0.8,anchor=CENTER)
        
e1=Radiobutton(root,text="Text to Morse Code",variable=var,value=1,command=txt)
e1.place(relx=0.4,rely=0.4,anchor=CENTER)
e2=Radiobutton(root,text="Morse Code to Text",variable=var,value=2,command=mor)
e2.place(relx=0.6,rely=0.4,anchor=CENTER)

Button(root,text="Submit",bg="#fdde6c", fg="#000", font="verdana 12 bold ",command=sub).place(relx=0.5,rely=0.6,anchor=CENTER)
