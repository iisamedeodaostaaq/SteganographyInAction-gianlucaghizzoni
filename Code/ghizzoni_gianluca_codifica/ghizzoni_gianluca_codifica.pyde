lunghezzaimmagine=500
altezzaimmagine=500
nquadrati=0          # numero di quadrati in una riga
fine=0               #fine della lunghezza 
    
img=createImage(lunghezzaimmagine,altezzaimmagine,RGB)   #creo l immagine
img.loadPixels()                #carico i pixel                                                      
 
def setup():
    size(lunghezzaimmagine,altezzaimmagine)                                                     
    crea_Immagine()   
        
def crea_Immagine():
    global lunghezzaimmagine,altezzaimmagine,nquadrati,i,a,y,j,fine    #y=dimensione quadrato,j=dimensione quadrato
    input=createInput("Input")                                                                           
    i=0        #inserisco un indice per i pixel    
    while nquadrati<=10:                                                                                                  
        lettura1=input.read()                                             
        lettura2=input.read()                                             
        lettura3=input.read()                                             
        if lettura1==-1:                                                    
            lettura1=255                                                    
        if lettura2==-1:                                                    
            lettura2=255                                                    
        if lettura3==-1:                                                    
            if nquadrati==0:
                break
            else:
                for a in range (10-nquadrati):
                    for y in range (50):
                        for j in range (50):
                            img.pixels[i+y+(lunghezzaimmagine*j)]=color(0,0,0) #faccio il colore nero al pixel
                            fine=1
        else:                                                          
            nquadrati+=1
            for y in range (50):
                for j in range (50):
                    img.pixels[i+y+(lunghezzaimmagine*j)]=color(lettura1,lettura2,lettura3)        
        i=i+50                                                                
        if(i%lunghezzaimmagine==0):
            i=i+lunghezzaimmagine*49                                                       
            nquadrati=0                                                             
            if fine==1:       #quando incontra il colore nero finisce tutta la funzione
                break
    img.updatePixels()                                                       
    image(img,0,0)                                                            
    save("Mistery.tiff")                                                          
