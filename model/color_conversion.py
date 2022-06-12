def RGB_to_HSL(r,g,b):
    r/=255
    g/=255
    b/=255

    #Find greatest and smallest channel values
    min_rgb = min(r,g,b)
    max_rgb = max(r,g,b)

    delta = max_rgb - min_rgb
    h = 0
    s = 0
    l = 0

    #Calculate hue
    #No difference
    if(delta == 0):
        h  = 0
    #Red is max    
    elif (max_rgb == r):
        h = ((g - b) / delta) % 6
    #Green is max    
    elif (max_rgb == g):
        h = (b - r) / delta + 2
    #Blue is max    
    else:
        h = (r - g) / delta + 4
    
    h = round(h*40)

    #// Make negative hues positive (Paint) 
    if(h<0):
        h += 240
    
    #Calculate lightness
    l = (max_rgb + min_rgb)/2

    # Calculate saturation
    if(delta == 0):
        s = 0
    else:
        s = delta/(1-abs(2*l-1))
  
    #Multiply l and s by 240 (Paint)
    s = round(s*240) 
    l = round(l*240) 

    return h, s, l



def HSL_to_RGB(h,s,l):
    s/=240
    l/=240

    c = (1-abs(2*l-1)) * s
    x = c * (1 - abs((h/40) % 2-1))

    m = l - c/2
    r = 0
    g = 0
    b = 0
    
    if(h<=0 and h<40):
        r = c
        g = x
        b = 0

    elif (h<=40 and h<80):
        r = x
        g = c
        b = 0
    
    elif(h<=80 and h<120):
        r = 0
        g = c
        b = x
    
    elif(h<=120 and h<160):
        r = 0
        g = x
        b = c
    
    elif(h<=160 and h<200):
        r = x
        g = 0
        b = c
    
    elif(h<=200 and h<240):
        r = c
        g = 0
        b = x

    r = round((r+m)*255)
    g = round((g+m)*255)
    b = round((b+m)*255)

    return b, g, r



"""
print("RGB to HSL (paint): (196, 63, 224) -> (193, 174, 135)")

h, s, l = RGB_to_HSL(196, 63, 224)
#h, s, l = RGB_to_HSL(0, 0, 0)
print(h,s,l)

r, g, b = HSL_to_RGB(h,s,l)
print(r, g, b)
"""

