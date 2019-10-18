import pygame,random as ran,time
import os
ran.seed()
pygame.init()

music_list=['eshgh.mp3','ghamar.mp3','heidar.mp3','Ashegh.mp3']
def music_choice():
    r=ran.randint(0,len(music_list)-1)
    pygame.mixer.music.load(music_list[r])

class static_variable:
    pass
def stuff(stuff_x,stuff_y,stuff_w,stuff_h,stuff_c):
    pygame.draw.rect(gamedisplay,stuff_c,[stuff_x,stuff_y,stuff_w,stuff_h])
def exit1():
    pygame.quit()
    quit()
def score(badge,kind,color,font_width,point):
    font=pygame.font.SysFont(None,font_width)
    text=font.render(kind+' :'+str(badge),True,color)
    gamedisplay.blit(text,point)
def record(recoord):
    font=pygame.font.Font('freesansbold.ttf',30)
    text=font.render('Record ='+str(recoord),True,(130,145,201))
    gamedisplay.blit(text,(0,yw-30))
def paint(x,y):
    gamedisplay.blit(picture,(x,y))
def text_object(text,font):
    textsurface=font.render(text,True,colorrandom(),colorrandom())
    return textsurface,textsurface.get_rect()
def massage_display(text):
    largetext=pygame.font.SysFont(None,130)
    textsurface,textrect=text_object(text,largetext)
    textrect.center=(xw/2,yw/2)
    gamedisplay.blit(textsurface,textrect)
    pygame.display.update()
    time.sleep(3)
def crash():
    pygame.mixer.music.stop()

    massage_display("You Crashed")
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit1()
        button('Try again',220,380,125,40,(0,255,0),(50,200,60),gameloop)
        button('Quit',480,380,99,40,(255,0,0),(200,50,60),exit1)
        pygame.display.update()
picture=pygame.image.load('testpic.png')
car_width=48
def colorrandom():
     randomcolor=(ran.randint(0,255),ran.randint(0,255),ran.randint(0,255))
     return randomcolor
#if you use the button you need to pygame.surface.update
def button(text,x,y,x_width,y_height,color_front,color_back,active=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x<mouse[0]<x+x_width and y<mouse[1]<y+y_height:
        pygame.draw.rect(gamedisplay,color_front,(x,y,x_width,y_height))
        if click[0]==1:
            if active!=None:
                active()
    else:
        pygame.draw.rect(gamedisplay,color_back,(x,y,x_width,y_height))
    font=pygame.font.SysFont(None,30)
    txt=font.render(text,True,(0,0,0))
    gamedisplay.blit(txt,(x+(x_width/4),y+(y_height/4)))
def game_intro():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit1()
        gamedisplay.fill((255,255,50))
        pygame.draw.circle(gamedisplay,(40,150,200),(400,340),200)
        font=pygame.font.SysFont(None,100)
        text=font.render('lets play !',True,(0,0,0))
        gamedisplay.blit(text,(xw/2-150,yw/2-75))
        button('play',220,380,99,40,(0,255,0),(50,200,60),gameloop)
        button('Quit',480,380,99,40,(255,0,0),(200,50,60),exit1)

        pygame.display.update()


xw=800
yw=600
gamedisplay=pygame.display.set_mode((xw,yw))
pygame.display.set_caption('python Game')
clock=pygame.time.Clock()
staticvariable=static_variable()
staticvariable.record_keep=0
class d:
    i=0
f=d()
f.i=0
def gameloop():
    f.i+=1
    if f.i>3:
        return
    heart=3
  #  music_choice()
 #   pygame.mixer.music.play(-1)
    stuff_height=10
    stuff_startx1=-10
    stuff_startx,stfx=ran.randint(0,xw),-700
    stuff_starty,stfy=-1000,ran.randint(0,yw-stuff_height)
    stuff_width=10
    stuff_speed=10
    gameExit=False
    x,y=.45*xw,.8*yw
    badge=0
    one=1
    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit1()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                            x-=30
                if event.key==pygame.K_RIGHT:
                            x+=30
                elif event.key==pygame.K_UP:
                            y-=30
                elif event.key==pygame.K_DOWN:
                            y+=30
            #pygame.draw.rect(gamedisplay,colorrandom(),[xw/2,20,60,40])
        gamedisplay.fill((0,0,0))
        stuff(stuff_startx,stuff_starty,stuff_width,stuff_height,colorrandom())
        stuff(stuff_startx1,stuff_starty,stuff_width,stuff_height,colorrandom())
        stuff_starty+=stuff_speed
        stuff(stfx,stfy,stuff_height,stuff_width,(255,255,255))
        if one ==1:
            stfx+=stuff_speed
        elif one==0:
            stfx-=stuff_speed
        score(badge,'score',(40,150,210),25,(10,20))
        score(int(heart),'heart',(255,0,0),35,(10,35))
        record(staticvariable.record_keep)
        paint(x,y)
        pygame.display.update()
        clock.tick(30)
        if stuff_starty>yw:
            stuff_starty=0-stuff_height
            stuff_startx=ran.randint(0,xw)
            stuff_startx1=ran.randint(0,xw)
            badge+=2
            if badge> staticvariable.record_keep:
                staticvariable.record_keep=badge
            if badge%5==0:
                if stuff_speed<80:
                    stuff_speed+=1
                if stuff_width<70:
                    stuff_width+=2
                    stuff_height+=1
        if x<0 or x>xw-car_width:
            crash()
        if (stfx>xw and one==1) or (stfx<0 and one==0):
            if one==1:
                stfx=xw+stuff_width
                one=0
            elif one==0:
                stfx=0-stuff_width
                one=1
            stfy=ran.randint(0,yw)
            # this if for save record to display us
            if badge>staticvariable.record_keep:
                staticvariable.record_keep=badge
        if y<stuff_starty+stuff_height:
            for x_test in range(int(x)+1,int(x+car_width)):
                if stuff_startx < x_test <stuff_startx+stuff_width or stuff_startx1<x_test<stuff_startx1+stuff_width:
                    if not  y+car_width<stuff_starty:
                        heart-=.1
                    
        if x<stfx+stuff_width:
            for y_test in range(int(y)+1,int(y+car_width)):
                if (stfy <y_test< stfy+stuff_width):
                    if not x+car_width<stfx:
                        heart+=.1
        
        if heart <0:
            score(0,'heart',(0,0,0),50,(20,50))
            crash()
game_intro()
gameloop()