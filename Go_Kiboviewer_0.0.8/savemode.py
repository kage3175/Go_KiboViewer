import pygame, sys
from pygame.locals import *
from tkinter import*
import os

def search() :
    global filenames
    filenames=os.listdir('./doc')

def saveas() : #기보 저장을 할 때 실행되는 함수. tkinter로 기보 이름과 대국자, 승자 등의 정보를 입력받는다.
    global e1
    global sequence
    global nn
    global e2
    global e3
    global e4 #승자 누군지
    global e5 #승리 방식
    global window
    global n
    window=Tk()
    window.title('기보 저장')
    frm=Frame(window, width=345, height=250, bg='gray89')
    '''frm=Frame(window, width=340, height=250, bg='black')'''
    frm.pack()

    l1=Label(window, text='기보 이름을 입력하세요.', bg='gray89', fg='black')
    l1.place(x=10, y=10)
    l2=Label(window, text='흑번 대국자', bg='gray89', fg='black')
    l2.place(x=10, y=50)
    l3=Label(window, text='백번 대국자', bg='gray89', fg='black')
    l3.place(x=10, y=90)
    l4=Label(window, text='승자(흑 or 백 or 빅)', bg='gray89', fg='black')
    l4.place(x=10, y=130)
    l5=Label(window, text='승리방식', bg='gray89', fg='black')
    l5.place(x=10, y=170)
    l6=Label(window, text='승(빅)', bg='gray89', fg='black')
    l6.place(x=306,y=170)
    '''l1=Label(window, text='기보 이름을 입력하세요.', bg='black', fg='white')
    l1.place(x=10, y=10)
    l2=Label(window, text='흑번 대국자', bg='black', fg='white')
    l2.place(x=10, y=50)
    l3=Label(window, text='백번 대국자', bg='black', fg='white')
    l3.place(x=10, y=90)
    l4=Label(window, text='승자(흑 or 백 or 빅)', bg='black', fg='white')
    l4.place(x=10, y=130)
    l5=Label(window, text='승리방식', bg='black', fg='white')
    l5.place(x=10, y=170)
    l6=Label(window, text='승', bg='black', fg='white')
    l6.place(x=310,y=170)'''
    e1=Entry(window)
    e1.place(x=160, y=10)
    e2=Entry(window)
    e2.place(x=160, y=50)
    e3=Entry(window)
    e3.place(x=160, y=90)
    e4=Entry(window)
    e4.place(x=160, y=130)
    e5=Entry(window)
    e5.place(x=160, y=170)
    enter=Button(window, text='      저장      ',bg='white', command=checksave) # 저장 버튼
    enter.place(x=55, y=210)
    cancel=Button(window, text='      취소      ',bg='white', command=Cancel) # 취소 버튼
    cancel.place(x=190, y=210)
    window.mainloop()
    '''createfile = open('./doc/'+nn+'.hgf', 'w')
    createfile.write(str(n)+'\n')
    for i in range(n):
        data = str((i+1))+' '+str(sequence[i][0])+' '+str(sequence[i][1])+' '
        createfile.write(data)
    createfile.write('\n')
    createfile.write(blackplayer+' '+whiteplayer+'\n')
    createfile.write(winner+',')
    createfile.write(method)
    createfile.close()''' # 0.0.4까지 썼던 코드. 해당 코드는 아래쪽의 save 함수로 대체하였다.

def checksave() :
    global filenames
    global nn
    global e1
    global window
    global win

    search()
    ztt=0
    nn=e1.get()
    for filename in filenames :
        if filename==(nn+'.hgf') :
            ztt=1
    if ztt==1 :
        win=Tk()
        frm=Frame(win, width=290, height=90)
        frm.pack()
    
        l1=Label(win, text='이미 존재하는 이름입니다. 덮어씌우시겠습니까?', bg='white', fg='black')
        l1.place(x=10, y=10)
        enter=Button(win, text='       예       ', command=savein) # 저장 버튼
        enter.place(x=50, y=50)
        cancel=Button(win, text='    아니오    ', command=Cancelwin) # 취소 버튼
        cancel.place(x=150, y=50)
    else :
        save()

def Cancel(): #취소를 누르면 그냥 저장하는 창이 꺼지고 기보 만들기 모드가 계속 이어진다.
    global window
    window.destroy()

def Cancelwin() :
    global win
    win.destroy()

def savein() : #실제로 txt 파일을 만들어 저장하는 함수. 첫줄에는 총 수순이, 둘째 줄에는 수순의 진행정보가, 셋째 줄에는 대국자 이름, 마지막 줄에는 승자와 승리방식이 기록된다.
    global nn
    global e1
    global window
    global e2
    global e3
    global e4
    global e5
    global blackplayer
    global whiteplayer
    global winner
    global method
    global n
    global win
    blackplayer=e2.get()
    whiteplayer=e3.get()
    winner = e4.get()
    method = e5.get()
    createfile = open('./doc/'+nn+'.hgf', 'w')
    createfile.write(str(n)+'\n')
    for i in range(n):
        data = str((i+1))+' '+str(sequence[i][0])+' '+str(sequence[i][1])+' '+str(sequence[i][2])+' '
        createfile.write(data)
    createfile.write('\n')
    createfile.write(blackplayer+' '+whiteplayer+'\n')
    createfile.write(winner+',')
    createfile.write(method)
    createfile.close()
    window.destroy()
    win.destroy()

def save() : #실제로 txt 파일을 만들어 저장하는 함수. 첫줄에는 총 수순이, 둘째 줄에는 수순의 진행정보가, 셋째 줄에는 대국자 이름, 마지막 줄에는 승자와 승리방식이 기록된다.
    global nn
    global e1
    global window
    global e2
    global e3
    global e4
    global e5
    global blackplayer
    global whiteplayer
    global winner
    global method
    global n
    blackplayer=e2.get()
    whiteplayer=e3.get()
    winner = e4.get()
    method = e5.get()
    createfile = open('./doc/'+nn+'.hgf', 'w')
    createfile.write(str(n)+'\n')
    for i in range(n):
        data = str((i+1))+' '+str(sequence[i][0])+' '+str(sequence[i][1])+' '+str(sequence[i][2])+' '
        createfile.write(data)
    createfile.write('\n')
    createfile.write(blackplayer+' '+whiteplayer+'\n')
    createfile.write(winner+',')
    createfile.write(method)
    createfile.close()
    window.destroy()

def blackbanthing(i, j, k) : #검정색 클러스터를 만들 때 필요한 함수(클러스터 : 상하좌우로 연결된 돌. 즉, '뭉친' 돌들)
    global blackban
    blackban[i][j]=k

def whitebanthing(i, j, k) : #위 함수의 하얀색 버전
    global whiteban
    whiteban[i][j]=k

def makeblackcluster(k,i,j) : #실제로 클러스터를 형성하는 검정돌을 모아서 블랙클러스터1, 블랙클러스터2 이런식으로 묶음
    global blackban
    global stat
    global Blackcluster
    global tt
    if i<19 and j<19 :
        Blackcluster[k][tt]=[i,j]
        blackbanthing(i,j,1)
        tt+=1 # 해당 클러스터의 몇 번째 돌인지를 카운트하기 위한 변수.
        if i<18 and stat[i+1][j]==1 and blackban[i+1][j]==0 :
            makeblackcluster(k,i+1,j)
        if i>0 and stat[i-1][j]==1 and blackban[i-1][j]==0 :
            makeblackcluster(k,i-1,j)
        if j<18 and stat[i][j+1]==1 and blackban[i][j+1]==0 :
            makeblackcluster(k,i,j+1)
        if j>0 and stat[i][j-1]==1 and blackban[i][j-1]==0 :
            makeblackcluster(k,i,j-1)

def makewhitecluster(k,i,j) : #위 함수의 하얀색 버전
    global whiteban
    global stat
    global Whitecluster
    global zz
    if i<19 and j<19 :
        Whitecluster[k][zz]=[i,j]
        whitebanthing(i,j,1)
        zz+=1
        if i<18 and stat[i+1][j]==2 and whiteban[i+1][j]==0 :
            makewhitecluster(k,i+1,j)
        if i>0 and stat[i-1][j]==2 and whiteban[i-1][j]==0 :
            makewhitecluster(k,i-1,j)
        if j<18 and stat[i][j+1]==2 and whiteban[i][j+1]==0 :
            makewhitecluster(k,i,j+1)
        if j>0 and stat[i][j-1]==2 and whiteban[i][j-1]==0 :
            makewhitecluster(k,i,j-1)

def blackbanthingko(i,j,k) :
    global blackbanko
    blackbanko[i][j]=k

def makeblackclusterko(k,i,j) :
    global blackbanko
    global statko
    global Blackclusterko
    global ttko
    if i<19 and j<19 :
        Blackclusterko[k][ttko]=[i,j]
        blackbanthingko(i,j,1)
        ttko+=1 # 해당 클러스터의 몇 번째 돌인지를 카운트하기 위한 변수.
        if i<18 and statko[i+1][j]==1 and blackbanko[i+1][j]==0 :
            makeblackclusterko(k,i+1,j)
        if i>0 and statko[i-1][j]==1 and blackbanko[i-1][j]==0 :
            makeblackclusterko(k,i-1,j)
        if j<18 and statko[i][j+1]==1 and blackbanko[i][j+1]==0 :
            makeblackclusterko(k,i,j+1)
        if j>0 and statko[i][j-1]==1 and blackbanko[i][j-1]==0 :
            makeblackclusterko(k,i,j-1)

def blacksahwalko():
    global Blackclusterko
    global statko
    global deadblackko
    temp=0
    ttemp=0
    x=0
    y=0
    for k in range(361) :
        ttemp=0
        temp=0
        if Blackclusterko[k][0][0] != 20 :
            while temp<361 :
                if Blackclusterko[k][temp][0] == 20 :
                    break
                else :
                    x=Blackclusterko[k][temp][0]
                    y=Blackclusterko[k][temp][1]
                    if x<=17 and statko[x+1][y] == 0 : #한쪽이라도 공배가 있으면 살아있는 돌이기 때문에 이렇게 처리해준다.
                        ttemp=1
                        break
                    if x>=1 and statko[x-1][y] == 0 :
                        ttemp=1
                        break
                    if y<=17 and statko[x][y+1] == 0 :
                        ttemp=1
                        break
                    if y>=1 and statko[x][y-1] == 0 :
                        ttemp=1
                        break
                    temp+=1
            temp=0
            if ttemp==0 :
                for [i, j] in Blackclusterko[k] :
                    if i!=20 and j!=20 :
                        deadblackko+=1
        else :
            break

def whitebanthingko(i,j,k) :
    global whitebanko
    whitebanko[i][j]=k

def makewhiteclusterko(k,i,j) :
    global whitebanko
    global statko
    global Whiteclusterko
    global ttko
    if i<19 and j<19 :
        Whiteclusterko[k][ttko]=[i,j]
        whitebanthingko(i,j,1)
        ttko+=1 # 해당 클러스터의 몇 번째 돌인지를 카운트하기 위한 변수.
        if i<18 and statko[i+1][j]==2 and whitebanko[i+1][j]==0 :
            makewhiteclusterko(k,i+1,j)
        if i>0 and statko[i-1][j]==2 and whitebanko[i-1][j]==0 :
            makewhiteclusterko(k,i-1,j)
        if j<18 and statko[i][j+1]==2 and whitebanko[i][j+1]==0 :
            makewhiteclusterko(k,i,j+1)
        if j>0 and statko[i][j-1]==2 and whitebanko[i][j-1]==0 :
            makewhiteclusterko(k,i,j-1)

def whitesahwalko():
    global Whiteclusterko
    global statko
    global deadwhiteko
    temp=0
    ttemp=0
    x=0
    y=0
    for k in range(361) :
        ttemp=0
        temp=0
        if Whiteclusterko[k][0][0] != 20 :
            while temp<361 :
                if Whiteclusterko[k][temp][0] == 20 :
                    break
                else :
                    x=Whiteclusterko[k][temp][0]
                    y=Whiteclusterko[k][temp][1]
                    if x<=17 and statko[x+1][y] == 0 : #한쪽이라도 공배가 있으면 살아있는 돌이기 때문에 이렇게 처리해준다.
                        ttemp=1
                        break
                    if x>=1 and statko[x-1][y] == 0 :
                        ttemp=1
                        break
                    if y<=17 and statko[x][y+1] == 0 :
                        ttemp=1
                        break
                    if y>=1 and statko[x][y-1] == 0 :
                        ttemp=1
                        break
                    temp+=1
            temp=0
            if ttemp==0 :
                for [i, j] in Whiteclusterko[k] :
                    if i!=20 and j!=20 :
                        deadwhiteko+=1
        else :
            break

def blacksahwal() : #흑돌이 따였는지 그대로 있으면 되는지를 판단하는 함수 마지막 줄에 ttemp==0일 때의 경우를 보면 흑돌을 드러내는 경우, 즉 클러스터를 둘러싸는 좌표에 공배가 없는 경우 드러낸다.
    global Blackcluster
    global stat
    global now1
    global now2
    global deadblack
    temp=0
    ttemp=0
    x=0
    y=0
    for k in range(361) :
        ttemp=0
        temp=0
        if Blackcluster[k][0][0] != 20 :
            while temp<361 :
                if Blackcluster[k][temp][0] == 20 :
                    break
                else :
                    x=Blackcluster[k][temp][0]
                    y=Blackcluster[k][temp][1]
                    if x==now1 and y==now2 : # 방금 놓여진 돌은 따이지 않기 때문에 이렇게 처리해준다.
                        ttemp=1
                        break
                    if x<=17 and stat[x+1][y] == 0 : #한쪽이라도 공배가 있으면 살아있는 돌이기 때문에 이렇게 처리해준다.
                        ttemp=1
                        break
                    if x>=1 and stat[x-1][y] == 0 :
                        ttemp=1
                        break
                    if y<=17 and stat[x][y+1] == 0 :
                        ttemp=1
                        break
                    if y>=1 and stat[x][y-1] == 0 :
                        ttemp=1
                        break
                    temp+=1
            temp=0
            if ttemp==0 :
                for [i, j] in Blackcluster[k] :
                    if i!=20 and j!=20 :
                        stat[i][j]=0
                        deadblack+=1
        else :
            break

def whitesahwal() : #위와 마찬가지
    global Whitecluster
    global stat
    global now1
    global now2
    global deadwhite
    temp=0
    ttemp=0
    x=0
    y=0
    for k in range(361) :
        ttemp=0
        temp=0
        if Whitecluster[k][0][0] != 20 :
            while temp<361 :
                if Whitecluster[k][temp][0] == 20 :
                    break
                else :
                    x=Whitecluster[k][temp][0]
                    y=Whitecluster[k][temp][1]
                    if x==now1 and y==now2 :
                        ttemp=1
                        break
                    if x<=17 and stat[x+1][y] == 0 :
                        ttemp=1
                        break
                    if x>=1 and stat[x-1][y] == 0 :
                        ttemp=1
                        break
                    if y<=17 and stat[x][y+1] == 0 :
                        ttemp=1
                        break
                    if y>=1 and stat[x][y-1] == 0 :
                        ttemp=1
                        break
                    temp+=1
            temp=0
            if ttemp==0 :
                for [i, j] in Whitecluster[k] :
                    if i!=20 and j!=20 :
                        stat[i][j]=0
                        deadwhite+=1
        else :
            break


def kibosave() :
    pos=[[0,0] for i in range(600)] # 마우스 클릭 위치를 받기 위한 리스트. 이게 특정값 이내여야 클릭으로 인정되고, 돌이 놓인다
    global stat # 이차원 리스트로, i행 j열이 비어있는지, 흑돌인지, 백돌인지에 따라 리스트의 i행 j열에 0, 1, 2가 들어간다.
    xt=0 # 밑에서 클릭을 했을 때 stat이 비어있으면 1 또는 2를, 차 있으면 스킵할 때 필요한 상수
    yt=0 # xt와 같음
    cnt=0 # 마찬가지로 수순을 알기 위한 상수. sequecne에 값을 저장할 때 쓰인다.
    tmp=0
    LEFT=1
    www=0 #매우 중요한 변수이다. 이벤트를 입력받을 때 이 변수를 변화시켜서 다른 실행이 일어나게 만든다. 0이면 아무 일도 없고, 1이면 돌을 수순에 맞게 놓으며 2이면 무르기이다.
    yolo=0
    WHITE=(255,255,255) # 판을 하얀색으로 채우기 위한 상수
    BLACK=(0,0,0)
    global sequence # 이차원 리스트. 만약 100수째에 돌이 12행 12열에 놓인다면, sequence[100]에 [11,11]이 저장된다.
    global Blackcluster
    global Whitecluster
    global blackban
    global whiteban
    global undosequence
    global tt
    global zz
    global now1
    global now2
    global deadwhite
    global deadblack
    global nn
    global e1
    global n
    global blackbanko
    global Blackclusterko
    global ttko
    global statko
    global deadblackko
    global whitebanko
    global Whiteclusterko
    global deadwhiteko
    deadblackko=0
    statko=[[0 for i in range(19)] for i in range(19)]
    ttko=0
    blackbanko=[[0 for i in range(19)] for i in range(19)]
    Blackclusterko=[[[20,20] for i in range(361)] for j in range(361)]
    deadwhiteko=0
    whitebanko=[[0 for i in range(19)] for i in range(19)]
    Whiteclusterko=[[[20,20] for i in range(361)] for j in range(361)]
    n=0 # 돌의 수순을 알기 위한 상수. 돌이 하나 놓일 때마다 1씩 증가한다.
    forsaveconst=0
    deadwhite=0
    deadblack=0
    now1 = 0
    now2 = 0
    noww1=0
    noww2=0
    stat=[[0 for i in range(19)] for j in range(19)] 
    sequence=[[-1, -1, 0] for i in range(600)]
    Blackcluster=[[[20,20] for i in range(361)] for i in range(361)]
    Whitecluster=[[[20,20] for i in range(361)] for i in range(361)]
    blackban=[[0 for i in range(19)] for i in range(19)] #0이면 ban이 안 된것이고(클러스터를 이루지 않음) 1 이상이면 밴 된 것
    whiteban=[[0 for i in range(19)] for i in range(19)] #0이면 ban이 안 된것이고(클러스터를 이루지 않음) 1 이상이면 밴 된 것
    blackdeadcount=[0 for i in range(600)]
    whitedeadcount=[0 for i in range(600)]
    statundo=[[[0 for i in range(19)] for j in range(19)] for k in range(600)]
    cntt=0
    fornow=[[-1,-1] for i in range(600)]
    bjg1=27.5 # 좌표 보정을 위한 상수
    bjgx=4 # x좌표 보정을 위한 상수
    bjgy=0 # y좌표 보정을 위한 상수
    sogur=0
    ktwiz=0
    fps=20
    fpsClock=pygame.time.Clock()

    pygame.init()
    pygame.mixer.init()
    imgBaduk=pygame.image.load('./image/pan.png')
    imgBlackstone=pygame.image.load('./image/blackstone.png')
    imgWhitestone=pygame.image.load('./image/whitestone.png')
    imgBlacknew=pygame.image.load('./image/blackstone_new.png') #빨간색 삼각형이 표시된 흑돌
    imgWhitenew=pygame.image.load('./image/whitestone_new.png')
    imgSavebutton=pygame.image.load('./image/savebutton.png')
    imgMainbutton=pygame.image.load('./image/mainbutton.png')
    imgAlternateu=pygame.image.load('./image/alternate_unpressed.png')
    imgAlternatep=pygame.image.load('./image/alternate_pressed.png')
    imgBlackonlyu=pygame.image.load('./image/onlyblack_unpressed.png')
    imgBlackonlyp=pygame.image.load('./image/onlyblack_pressed.png')
    imgWhiteonlyu=pygame.image.load('./image/onlywhite_unpressed.png')
    imgWhiteonlyp=pygame.image.load('./image/onlywhite_pressed.png')

    soundObjChaksu = pygame.mixer.Sound('./audio/chaksu.wav')


    screen=pygame.display.set_mode((750,700))
    pygame.display.set_caption('기보 만들기')
    fontObj = pygame.font.Font(None, 26)
    fonthan = pygame.font.Font('./font/NanumGothic.ttf', 16) #한글 출력을 위한 나눔 글꼴

    fps=10 #프레임이 높을 필요가 없기 때문에 프레임은 10으로 설정하였다. 낮은 사양의 컴퓨터에서는 이를 5 정도로 낮춰서 사용해도 문제가 없다.
    fpsClock=pygame.time.Clock() 

    while 1 : # 기보 만들기 종료시까지 계속 실행하도록
        blackban=[[0 for i in range(19)] for i in range(19)]
        Blackcluster=[[[20,20] for i in range(361)] for i in range(361)]
        whiteban=[[0 for i in range(19)] for i in range(19)]
        Whitecluster=[[[20,20] for i in range(361)] for i in range(361)]
        blackbanko=[[0 for i in range(19)] for i in range(19)]
        Blackclusterko=[[[20,20] for i in range(361)] for i in range(361)]
        whitebanko=[[0 for i in range(19)] for i in range(19)]
        Whiteclusterko=[[[20,20] for i in range(361)] for i in range(361)]
        tt=0
        zz=0
        tmp=0
        deadblackko=0
        deadwhiteko=0
        forsaveconst=0 # 매번 초기화해줘야 하는 변수들은 이렇게 초기화해준다.
        for event in pygame.event.get() :
            if event.type==QUIT : #우상단 X버튼을 눌렀을 경우
                pygame.quit()
                sys.exit()
            if event.type==MOUSEBUTTONDOWN and event.button==LEFT : # 마우스 좌클릭
                position=pygame.mouse.get_pos()
                pos[n][0]=position[0]
                pos[n][1]=position[1]
                www=1
                if position[0]>=62 and position[0]<=102 and position[1]>=11 and position[1]<=39 and yolo!=0 :
                    yolo=0
                if position[0]>=118 and position[0]<=144 and position[1]>=11 and position[1]<=39 and yolo!=1 :
                    yolo=1
                if position[0]>=157 and position[0]<=183 and position[1]>=11 and position[1]<=39 and yolo!=2 :
                    yolo=2
                if position[0]>=632 and position[0]<=732 and position[1]>=179 and position[1]<=225 : #메뉴 버튼을 눌렀을 경우
                    return 0 # 0을 리턴해서 HamGo.py에서 메인메뉴가 실행되도록 한다.
            if event.type==MOUSEBUTTONUP and event.button==LEFT : # 마우스 좌클릭
                position=pygame.mouse.get_pos()
                pos[n][0]=position[0]
                pos[n][1]=position[1]
                if position[0]>=632 and position[0]<=732 and position[1]>=104 and position[1]<=153 : #저장 버튼을 눌렀을 경우
                    forsaveconst=1 # 이 변수가 1이 되면 saveas가 실행된다.
            if event.type==KEYUP :
                if event.key==K_s :
                    forsaveconst=1
                if event.key==K_m or event.key==K_UP :
                    if n>=1 :
                        www=2
        if forsaveconst==1 :
            saveas()
            forsaveconst=0
        if www==1 : #마우스 좌클릭을 한 경우 www=1이 되므로 이게 실행된다.
            tmp=0
            for i in range(19) :
                for j in range(19) :
                    if pos[n][0]>=i*bjg1+68+bjgx and pos[n][0]<=i*bjg1+92+bjgx :
                        if pos[n][1]>=j*bjg1+68+bjgy and pos[n][1]<=j*bjg1+92+bjgy :
                            xt=i
                            yt=j
                            tmp=1 #바둑판 위에, 인식하는 범위를 클릭했을 경우 일단 tmp=1로 만든다.
            if stat[xt][yt]==0 and tmp==1 : #여기서부터 아래의 코드는 패인지 아닌지를 판단한다. 만약 패인 경우, 따인 이후 바로 되따내는 것은 금수이므로 tmp=0으로 만들어 착수가 되지 않는다.
                if sogur%2==0 :
                    if xt>=1 and xt<=17 and yt>=1 and yt<=17 :
                        if stat[xt+1][yt]==2 and stat[xt-1][yt]==2 and stat[xt][yt+1]==2 and stat[xt][yt-1]==2 :
                            if statundo[n-2][xt][yt]==1 :
                                tmp=0
                    if xt==18 and yt>=1 and yt<=17 :
                        if stat[xt-1][yt]==2 and stat[xt][yt+1]==2 and stat[xt][yt-1]==2 :
                            if statundo[n-2][xt][yt]==1 :
                                tmp=0
                    if xt==0 and yt>=1 and yt<=17 :
                        if stat[xt+1][yt]==2 and stat[xt][yt+1]==2 and stat[xt][yt-1]==2 :
                            if statundo[n-2][xt][yt]==1:
                                tmp=0
                    if xt>=1 and xt<=17 and yt==18 :
                        if stat[xt+1][yt]==2 and stat[xt-1][yt]==2 and stat[xt][yt-1]==2 :
                            if statundo[n-2][xt][yt]==1:
                                tmp=0
                    if xt>=1 and xt<=17 and yt==0 :
                        if stat[xt+1][yt]==2 and stat[xt-1][yt]==2 and stat[xt][yt+1]==2 :
                            if statundo[n-2][xt][yt]==1:
                                tmp=0
                    if xt==0 and yt==0 :
                        if stat[xt+1][yt]==2 and stat[xt][yt+1]==2 :
                            if statundo[n-2][xt][yt]==1:
                                tmp=0
                    if xt==0 and yt==18 :
                        if stat[xt+1][yt]==2 and stat[xt][yt-1]==2 :
                            if statundo[n-2][xt][yt]==1:
                                tmp=0
                    if xt==18 and yt==0 :
                        if stat[xt-1][yt]==2 and stat[xt][yt+1]==2 :
                            if statundo[n-2][xt][yt]==1:
                                tmp=0
                    if xt==18 and yt==18 :
                        if stat[xt-1][yt]==2 and stat[xt][yt-1]==2 :
                            if statundo[n-2][xt][yt]==1:
                                tmp=0
                    if tmp==0 :
                        if stat[xt][yt]==0 :
                            statko[xt][yt]=1
                            cntt=0
                            for i in range(19) : #검정 클러스터
                                for j in range(19) :
                                    if statko[i][j]==2 and whitebanko[i][j]==0 :
                                        ttko=0
                                        makewhiteclusterko(cntt,i,j)
                                        cntt+=1
                            cntt=0
                            whitesahwalko()
                            if deadwhiteko>1:
                                tmp=1
                            statko[xt][yt]=0
                else :
                    if xt>=1 and xt<=17 and yt>=1 and yt<=17 :
                        if stat[xt+1][yt]==1 and stat[xt-1][yt]==1 and stat[xt][yt+1]==1 and stat[xt][yt-1]==1 :
                            if statundo[n-2][xt][yt]==2 :
                                tmp=0
                    if xt==18 and yt>=1 and yt<=17 :
                        if stat[xt-1][yt]==1 and stat[xt][yt+1]==1 and stat[xt][yt-1]==1 :
                            if statundo[n-2][xt][yt]==2 :
                                tmp=0
                    if xt==0 and yt>=1 and yt<=17 :
                        if stat[xt+1][yt]==1 and stat[xt][yt+1]==1 and stat[xt][yt-1]==1 :
                            if statundo[n-2][xt][yt]==2:
                                tmp=0
                    if xt>=1 and xt<=17 and yt==18 :
                        if stat[xt+1][yt]==1 and stat[xt-1][yt]==1 and stat[xt][yt-1]==1 :
                            if statundo[n-2][xt][yt]==2:
                                tmp=0
                    if xt>=1 and xt<=17 and yt==0 :
                        if stat[xt+1][yt]==1 and stat[xt-1][yt]==1 and stat[xt][yt+1]==1 :
                            if statundo[n-2][xt][yt]==2:
                                tmp=0
                    if xt==0 and yt==0 :
                        if stat[xt+1][yt]==1 and stat[xt][yt+1]==1 :
                            if statundo[n-2][xt][yt]==2:
                                tmp=0
                    if xt==0 and yt==18 :
                        if stat[xt+1][yt]==1 and stat[xt][yt-1]==1 :
                            if statundo[n-2][xt][yt]==2:
                                tmp=0
                    if xt==18 and yt==0 :
                        if stat[xt-1][yt]==1 and stat[xt][yt+1]==1 :
                            if statundo[n-2][xt][yt]==2:
                                tmp=0
                    if xt==18 and yt==18 :
                        if stat[xt-1][yt]==1 and stat[xt][yt-1]==1 :
                            if statundo[n-2][xt][yt]==2:
                                tmp=0
                    if tmp==0 :
                        if stat[xt][yt]==0 :
                            statko[xt][yt]=2
                            cntt=0
                            for i in range(19) : #검정 클러스터
                                for j in range(19) :
                                    if statko[i][j]==1 and blackbanko[i][j]==0 :
                                        ttko=0
                                        makeblackclusterko(cntt,i,j)
                                        cntt+=1
                            cntt=0
                            blacksahwalko()
                            if deadblackko>1:
                                tmp=1
                            statko[xt][yt]=0
            if stat[xt][yt]==0 and tmp==1 :#금수가 아니면서 놓인 위치에 먼저 돌이 놓여있지 않다면 해당 위치에 수순에 맞는 색의 돌을 놓는다.
                if (sogur%2==0 and yolo==0) or yolo==1 :
                    stat[xt][yt]=1 #1, 즉 흑돌을 해당 위치에 놓는다.
                    sequence[cnt][0]=xt
                    sequence[cnt][1]=yt
                    sequence[cnt][2]=1
                    if yolo==0:
                        ktwiz=1
                    now1=xt
                    now2=yt
                    fornow[n]=[xt,yt]
                    cnt+=1 #sequence에 수순을 저장하기 위한 변수
                    tmp=0
                if (sogur%2==1 and yolo==0) or yolo==2 :
                    stat[xt][yt]=2
                    sequence[cnt][0]=xt
                    sequence[cnt][1]=yt
                    sequence[cnt][2]=2
                    if yolo==0:
                        ktwiz=1
                    now1=xt
                    now2=yt
                    fornow[n]=[xt,yt]
                    cnt+=1
                    tmp=0
                soundObjChaksu.play()
                if ktwiz==1:
                    sogur+=1
                    ktwiz=0
                n+=1 # 수순을 나타내는 변수를 1 증가시킨다.
        if www==2 and n!=0 : #무르기를 실행한 경우
            n-=1
            sogur-=1
            for i in range(19) :
                for j in range(19) :
                    stat[i][j]=statundo[n][i][j] #statundo[n]에는 n번째 수순이 놓아진 이후의 바둑판의 상태가 고스란이 저장되어 있다. 즉, stat에 바로 직전 수순의 바둑판을 다시 입력한다.
                    statundo[n+1][i][j]=0 #무르기를 진행한 이후 그 뒷 수순에 해당하는 statundo는 초기화해준다.
            deadblack=blackdeadcount[n-1] #흑 사석을 한 수 이전으로 되돌린다. blackdeadcount[n]은 n번째 수순이 진행되었을 때 흑 사석의 개수를 의미한다.
            deadwhite=whitedeadcount[n-1] 
            blackdeadcount[n]=0 #초기화
            whitedeadcount[n]=0
            now1=fornow[n-1][0] #'이번 수순에 놓여진 돌의 x좌표'도 당연히 한 수 전으로 바꿔줘야 오류가 생기지 않는다.
            now2=fornow[n-1][1]
            sequence[n]=[-1,-1,0] #기보 저장을 위한 sequence에서 n번째 수순은 초기화해주어야 한다. 그래야 기보 저장 시 오류가 발생하지 않는다.
            cnt-=1
            www=0 #아래쪽 www==1을 실행하지 않기 위하여 0으로 초기화
        cntt=0
        if www==1 : 
            for i in range(19) : #검정 클러스터
                for j in range(19) :
                    if stat[i][j]==1 and blackban[i][j]==0 :
                        tt=0
                        makeblackcluster(cntt,i,j)
                        cntt+=1
            cntt=0
            for i in range(19) : #하양 클러스터
                for j in range(19) :
                    if stat[i][j]==2 and whiteban[i][j]==0 :
                        zz=0
                        makewhitecluster(cntt,i,j)
                        cntt+=1
            blacksahwal() #사활 판단
            whitesahwal()
            for i in range(19) : # statundo에 이번 수순의 바둑판 전체 상태를 저장한다.
                for j in range(19) :
                    statundo[n][i][j]=stat[i][j]
                    statko[i][j]=stat[i][j]
            blackdeadcount[n-1]=deadblack
            whitedeadcount[n-1]=deadwhite
            www=0
        screen.fill(WHITE)
        screen.blit(imgBaduk, (52,49)) #바둑판
        for i in range(19) : #바둑판에 실제로 돌을 출력해주는 코드
            for j in range(19) :
                if stat[i][j]==1 :
                    if i==now1 and j==now2 :
                        screen.blit(imgBlacknew, (i*bjg1+65+bjgx,j*bjg1+65+bjgy)) #이번에 놓여진 돌이면 빨간색 삼각형을 표시해준다.
                    else :
                        screen.blit(imgBlackstone, (i*bjg1+65+bjgx,j*bjg1+65+bjgy))
                if stat[i][j]==2 :
                    if i==now1 and j==now2 :
                        screen.blit(imgWhitenew, (i*bjg1+65+bjgx,j*bjg1+65+bjgy))
                    else :
                        screen.blit(imgWhitestone, (i*bjg1+65+bjgx,j*bjg1+65+bjgy))
        pygame.draw.rect(screen, BLACK, (50,620,235,50))
        pygame.draw.rect(screen, BLACK, (370,620,235,50), 1)
        textSurfaceObj1 = fonthan.render('백 사석(흑이 잡은 돌) : '+str(deadwhite), True, WHITE)
        textRectObj1=textSurfaceObj1.get_rect();
        textRectObj1.center =(165,646)
        textSurfaceObj2 = fonthan.render('흑 사석(백이 잡은 돌) : '+str(deadblack), True, BLACK)
        textRectObj2=textSurfaceObj2.get_rect();
        textRectObj2.center =(485,646)
        screen.blit(textSurfaceObj1, textRectObj1)
        screen.blit(textSurfaceObj2, textRectObj2)
        screen.blit(imgSavebutton, (628, 100))
        screen.blit(imgMainbutton, (628, 175))
        if yolo==0 :
            screen.blit(imgAlternatep, (60, 10))
            screen.blit(imgBlackonlyu, (115, 10))
            screen.blit(imgWhiteonlyu, (155, 10))
        elif yolo==1 :
            screen.blit(imgAlternateu, (60, 10))
            screen.blit(imgBlackonlyp, (115, 10))
            screen.blit(imgWhiteonlyu, (155, 10))
        elif yolo==2 :
            screen.blit(imgAlternateu, (60, 10))
            screen.blit(imgBlackonlyu, (115, 10))
            screen.blit(imgWhiteonlyp, (155, 10))
        pygame.display.flip()
