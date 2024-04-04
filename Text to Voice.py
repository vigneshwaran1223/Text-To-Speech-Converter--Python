from gtts import gTTS

s = input("Enter a file Name : ")

f = open(s)
text = f.read()

obj = gTTS(text= text, lang='en', slow=False)
f1 = input("Enter the Audio name to be saved : ")
 
obj.save(f1)

