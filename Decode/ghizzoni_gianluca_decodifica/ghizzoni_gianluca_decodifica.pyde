a='carattere'                                          
b='carattere'                                          
c='carattere'                                          
i=0                                                
j=0 #indice per indicare il pixel
                                           
def setup():
    global img
    size(500,500)
    img=loadImage("Mistery.tiff")                      
    img.loadPixels()                               
    decodifica()                                         
    
def decodifica():
    global i,a,b,c,img,frase,j
    frase=""
    lettura1=red(img.pixels[j])
    lettura2=green(img.pixels[j])
    lettura3=blue(img.pixels[j])  
    while lettura1 != 0 or lettura2 != 0 or lettura3 != 0:
        for i in range (10):                      
            lettura1=red(img.pixels[j])               
            lettura2=green(img.pixels[j])             
            lettura3=blue(img.pixels[j])              
            if lettura1 >128:                      
                lettura1=0
            if lettura2>128:                        
                lettura2=0
            if lettura3 == 0 and lettura2 == 0 and lettura1 == 0 : 
                break                    
            letturaintero1 = int(lettura1) #cambio il valore da float a int
            letturaintero2 = int(lettura2)                  
            letturaintero3 = int(lettura3)                                  
            a=chr(letturaintero1) #cambio il valore da int a char
            b=chr(letturaintero2)                     
            c=chr(letturaintero3)                     
            frase+=a+b+c                        
            j+=50 #aggiungo a j 50 per spostarsi di quadrato                             
        j+=500*49 #aggiungo a j 500*49 per spostarsi di riga
    print(frase)                                  
    
