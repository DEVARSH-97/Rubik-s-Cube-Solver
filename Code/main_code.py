import cv2 
import numpy as np
from trial_code import predict_class


cap=cv2.VideoCapture(0)

state=  {
            'up':['white','white','white','white','green','white','white','white','white',],
            'right':['white','white','white','white','orange','white','white','white','white',],
            'front':['white','white','white','white','white','white','white','white','white',],
            'down':['white','white','white','white','blue','white','white','white','white',],
            'left':['white','white','white','white','red','white','white','white','white',],
            'back':['white','white','white','white','yellow','white','white','white','white',]
        }
cv2.namedWindow('frame')
cv2.namedWindow('prevalue')
cv2.namedWindow('preview')
stickers={
        'new_pop': [
            [20, 20], [70, 20], [120, 20],
            [20, 70], [70, 70], [120, 70]
        ],
      'main': [
            [200, 120], [300, 120], [400, 120],
            [200, 220], [300, 220], [400, 220],
            [200, 320], [300, 320], [400, 320]
        ],
        'current': [
            [20, 20], [54, 20], [88, 20],
            [20, 54], [54, 54], [88, 54],
            [20, 88], [54, 88], [88, 88]
        ],
        'left': [
            [50, 280], [94, 280], [138, 280],
            [50, 324], [94, 324], [138, 324],
            [50, 368], [94, 368], [138, 368]
        ],
        'front': [
            [188, 280], [232, 280], [276, 280],
            [188, 324], [232, 324], [276, 324],
            [188, 368], [232, 368], [276, 368]
        ],
        'right': [
            [326, 280], [370, 280], [414, 280],
            [326, 324], [370, 324], [414, 324],
            [326, 368], [370, 368], [414, 368]
        ],
        'up': [
            [188, 128], [232, 128], [276, 128],
            [188, 172], [232, 172], [276, 172],
            [188, 216], [232, 216], [276, 216]
        ],
        'down': [
            [188, 434], [232, 434], [276, 434],
            [188, 478], [232, 478], [276, 478],
            [188, 522], [232, 522], [276, 522]
        ], 
        'back': [
            [464, 280], [508, 280], [552, 280],
            [464, 324], [508, 324], [552, 324],
            [464, 368], [508, 368], [552, 368]
        ],
}
sign_conv={
            'green'  : 'F',
            'white'  : 'U',
            'blue'   : 'B',
            'red'    : 'R',
            'orange' : 'L',
            'yellow' : 'D'
          }
color = {
        'red'    : (0,0,255),
        'orange' : (0,165,255),
        'blue'   : (255,0,0),
        'green'  : (0,255,0),
        'white'  : (255,255,255),
        'yellow' : (0,255,255)
        }
RED    = (0,0,255)
ORANGE = (0,165,255)
BLUE   = (255,0,0)
GREEN  = (0,255,0)
WHITE  = (255,255,255)
YELLOW = (0,255,255)
'''color = {
        'red'    : RED,
        'orange' : ORANGE,
        'blue'   : BLUE,
        'green'  : GREEN,
        'white'  : WHITE,
        'yellow' : YELLOW
        }'''
def fill_stickers(frame,stickers,sides):    
    for side,colors in sides.items():
        num=0
        for x,y in stickers[side]:
            cv2.rectangle(frame,(x,y),(x+40,y+40),color[colors[num]],-1)
            num+=1

color_dict = {
    'RED': RED,
    'ORANGE': ORANGE,
    'BLUE': BLUE,
    'GREEN': GREEN,
    'WHITE': WHITE,
    'YELLOW': YELLOW
}
def fill_stickers_select(frame, stickers, side):    
    for (x, y), (color_name, color_values) in zip(stickers[side], color.items()):
        cv2.rectangle(frame, (x, y), (x + 50, y + 50), color_values, -1)


set_co=-1       

def click_event(event, x, y, flags, param):
    global kpop
    kpop=0
    def click_new_pop(event,x,y,flags, param):
        if event==cv2.EVENT_LBUTTONDOWN:
            if(x>19 and x<20+50):
                if(y>19):
                    if(y<19+50):
                        poll= ['red']
                    if(y<19+50+50):
                        poll= ['green']
            if(x>20+50 and x<20+50+50):
                if(y>19):
                    if(y<19+50):
                        poll= ['orange']
                    if(y<19+50+50):
                        poll= ['white']
                    
            if(x>20+100 and x<20+150):
                if(y>19):
                    if(y<19+50):
                        poll= ['blue']
                    if(y<19+50+50):
                        poll= ['yellow']
            cv2.rectangle(prevalue,(x,y),(x+30,y+30),color.get(poll[0]),-1)
            kpop=1
    if event == cv2.EVENT_LBUTTONDOWN:
        
        print(x)
        print(y)
        set_co=-1
        if(x<19 and x>19+34):
            if(y<19 and y>19+34):
                set_co=0
            if(y<19 and y>19+34):
                set_co=3
            if(y<19 and y>19+34):
                set_co=6
        if(x<19+34 and x>19+34+34):
            if(y<19 and y>19+34):
                set_co=1
            if(y<19 and y>19+34):
                set_co=4
            if(y<19 and y>19+34):
                set_co=7
        if(x<19+34+34 and x>19+34+34+34):
            if(y<19 and y>19+34):
                set_co=2
            if(y<19 and y>19+34):
                set_co=5
            if(y<19 and y>19+34):
                set_co=8            
        if((x<89+34 and x>19) and (y<89+34 and y>19) ):
            
            
            new_pop = np.zeros((150,200,3), np.uint8) 
            while True:
                
                fill_stickers_select(new_pop,stickers,'new_pop')
                cv2.imshow('new_pop',new_pop)
                cv2.setMouseCallback('new_pop', click_new_pop)
                
                    
                    
                k = cv2.waitKey(5) & 0xFF
    
                if k == 27 or kpop==1:
                    kpop=0
                    cv2.destroyWindow('new_pop')
                    break



        
        
        
            


def draw_preview_stickers(frame,stickers):
        stick=['front','back','left','right','up','down']
        for name in stick:
            for x,y in stickers[name]:
                cv2.rectangle(frame, (x,y), (x+40, y+40), (255,255,255), 2)
def draw_stickers(frame,stickers,name,pop=100):
        for x,y in stickers[name]:
            cv2.rectangle(frame, (x,y), (x+pop, y+pop), (255,255,255), 2)
def get_color(h, s, v):
    predicted_color=predict_class(np.array([h,s,v]))    
    print(predicted_color)
    if(predicted_color==0):
        return ['white']
    if(predicted_color==1):
        return ['yellow']
    if(predicted_color==2):
        return ['red']
    if(predicted_color==3):
        return ['green']
    if(predicted_color==4):
        return ['blue']
    if(predicted_color==5):
        return ['orange']
    
  # Assuming the model returns a single prediction
def solve(state):
    raw=''
    for i in state:
        for j in state[i]:
            raw+=sign_conv[j]
    print("RAW")
    print(raw)


def change_colors(side,current_state,list_to,list_from):
    for pos,lapp in zip(list_to,list_from):
            state[side][pos] = current_state[lapp]

current_state=[]     
if __name__=='__main__':
     preview = np.zeros((700,800,3), np.uint8)
     draw_preview_stickers(preview,stickers)
     prevalue = np.zeros((300,300,3), np.uint8)
     cv2.setMouseCallback('prevalue', click_event)
     count=0
     
     while True:
            ret,img=cap.read()

            draw_stickers(img,stickers,'main')
            draw_stickers(prevalue,stickers,'current',30)
            fill_stickers(preview,stickers,state)
            frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break
            elif k==ord('s'):
                current_state=[]
                for (x,y),(a,b) in zip(stickers['main'],stickers['current']):
                        h, s, v = frame[y+50, x+50]
                        colort=get_color(h,s,v)
                        print("colort")
                        print(colort)
                        #print(color_dict.get(colort[0]))
                        cv2.rectangle(prevalue,(a,b),(a+30,b+30),color.get(colort[0]),-1)
                        print(color.get(colort[0]))
                        current_state.append(colort[0])
                        
            elif k==ord('d'):
                if(count==0):
                    #state['front']=current_state
                    change_colors('front',current_state,[0,1,2,3,5,6,7,8],[0,1,2,3,5,6,7,8]) 
                    count=1
                elif(count==1):
                    #right motor
                    change_colors('up',current_state,[2,5,8],[2,5,8])
                    count=2
                elif(count==2):
                    #right motor
                    change_colors('back',current_state,[6,3,0],[2,5,8])
                    count=3
                elif(count==3):
                    #right motor
                    change_colors('down',current_state,[2,5,8],[2,5,8])
                    count=4
                elif(count==4):
                    #left motor
                    change_colors('up',current_state,[0,3,6],[0,3,6])
                    count=5
                elif(count==5):
                    #left motor
                    change_colors('back',current_state,[8,5,2],[0,3,6])
                    count=6                
                elif(count==6):
                    #right motor
                    change_colors('down',current_state,[0,3,6],[0,3,6])
                    count=7
                elif(count==7):
                    #upper motor
                    change_colors('left',current_state,[0,1,2],[0,1,2])
                    count=8
                elif(count==8):
                    #upper motor
                    change_colors('back',current_state,[1],[1])
                    count=9
                elif(count==9):
                    #upper motor
                    change_colors('right',current_state,[0,1,2],[0,1,2])
                    count=10
                elif(count==10):
                    #down motor
                    change_colors('left',current_state,[6,7,8],[6,7,8])
                    count=11
                elif(count==11):
                    #down motor
                    change_colors('back',current_state,[7],[7])
                    count=12
                elif(count==12):
                    #down motor
                    change_colors('right',current_state,[6,7,8],[6,7,8])
                    count=13
                elif(count==13):
                    #combined motor upper face
                    change_colors('up',current_state,[1,7],[3,5])
                    count=14
                elif(count==14):
                    #combined right face
                    change_colors('right',current_state,[3,5],[1,7])
                    count=15
                elif(count==15):
                    #combined left face
                    change_colors('left',current_state,[3,5],[1,7])
                    count=16
                elif(count==16):
                    #combined down face
                    change_colors('down',current_state,[1,7],[3,5])
                    count=17                     
            
                      
                 
            cv2.imshow('preview',preview)
            cv2.imshow('frame',img[0:700,0:700])
            cv2.imshow('prevalue',prevalue)
