import pygame, sys
from pygame.locals import*
from tkinter import*

def openas() :
    global nn
    global e1
    global window
    nn=e1.get()
    window.destroy()

def blackbanthing(i, j, k) : #검정색 클러스터를 만들 때 필요한 함수(클러스터 : 상하좌우로 연결된 돌. 즉, '뭉친' 돌들)
    global blackban
    blackban[i][j]=k

def whitebanthing(i, j, k) : #위 함수의 하얀색 버전
    global whiteban
    whiteban[i][j]=k

def makeblackcluster(k,i,j) : #실제로 클러스터를 형성하는 검정돌을 모아서 블랙클러스터1, 블랙클러스터2 이런식으로 묶음. 재귀함수로, 대마 중 한 돌이 걸리면 캐스케이드로 붙은 돌들에 대해 검사하고, 그 검사한 돌을 중심으로 또 검사하고,..
    global blackban
    global stat
    global Blackcluster
    global tt
    if i<19 and j<19 :
        Blackcluster[k][tt]=[i,j]
        blackbanthing(i,j,1)
        tt+=1
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

def blacksahwal() : #흑돌이 따였는지 그대로 있으면 되는지를 판단하는 함수. 마지막 줄에 ttemp==0일 때의 경우를 보면 흑돌을 들어내는 경우, 즉 클러스터를 둘러싸는 좌표에 공배가 없는 경우 드러낸다.
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
                for [i, j] in Blackcluster[k] :
                    if i!=20 and j!=20 :
                        stat[i][j]=0
                        deadblack+=1 # 돌 하나를 들어낼 때마다 사석을 한 개씩 추가한다.
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
        

def kiboopen() :
    pos=[[0,0] for i in range(600)] # 마우스 클릭 위치를 받기 위한 리스트. 이게 특정값 이내여야 클릭으로 인정되고, 돌이 놓인다
    global stat # 이차원 리스트로, i행 j열이 비어있는지, 흑돌인지, 백돌인지에 따라 리스트의 i행 j열에 0, 1, 2가 들어간다. 가장 중요한 변수.
    xt=0 # 밑에서 클릭을 했을 때 stat이 비어있으면 1 또는 2를, 차 있으면 스킵할 때 필요한 상수
    yt=0 # xt와 같음
    n=0 # 돌의 수순을 알기 위한 상수. 돌이 하나 놓일 때마다 1씩 증가한다.
    cnt=0 # 마찬가지로 수순을 알기 위한 상수. sequecne에 값을 저장할 때 쓰인다.
    tmp=0 # 마우스로 눌렀을 때 얘가 1로 바뀌고, 그래야만 다음의 if문을 실행한다.
    LEFT=1#마우스 왼쪽 버튼을 인식하기 위한 상수
    www=0
    WHITE=(255,255,255) # 판을 하얀색으로 채우기 위한 상수
    BLACK=(0,0,0)
    global sequence # 이차원 리스트. 만약 100수째에 돌이 12행 12열에 놓인다면, sequence[100]에 [11,11]이 저장된다.
    global Blackcluster
    global Whitecluster
    global blackban
    global whiteban
    global tt
    global zz
    global now1
    global now2
    global deadwhite
    global deadblack
    global nn
    global e1
    global window
    Players=['a', 'a']
    anothertmp=0
    deadwhite=0 #죽은 백돌(사석)을 세기 위한 변수
    deadblack=0
    now1 = 0 # 방금 놓인 수(수순이 100수라면, 100번째에 놓인 그 수)의 x좌표를 저장하는 변수
    now2 = 0 # y좌표
    stat=[[0 for i in range(19)] for j in range(19)]
    sequence=[[0, 0] for i in range(600)]
    opensequence=[[-1, -1] for i in range(600)]
    tmpseq=[[0, 0, 0] for i in range(600)]
    another=[0 for i in range(1200)]
    Blackcluster=[[[20,20] for i in range(361)] for i in range(361)] # 흑돌의 클러스터(뭉친 돌, 즉 대마)를 저장하기 위한 변수. 제1클러스터에 [x,y]의 흑돌이 속한다는 식으로 표현. 한 개짜리 돌도 하나의 클러스터를 이룬다.
    Whitecluster=[[[20,20] for i in range(361)] for i in range(361)] # 백돌의 클러스터
    blackban=[[0 for i in range(19)] for i in range(19)] #0이면 ban이 안 된것이고(클러스터를 이루지 않음) 1 이상이면 밴 된 것
    whiteban=[[0 for i in range(19)] for i in range(19)] #0이면 ban이 안 된것이고(클러스터를 이루지 않음) 1 이상이면 밴 된 것
    blackdeadcount=[0 for i in range(600)] # n번째 수순에서의 흑 사석이 몇 개인지 알기 위한 변수. 만약 100번째 수가 두어진 직후 죽은 흑돌이 2개면, blackdeadcount[99]=2 이런식으로 저장된다.
    whitedeadcount=[0 for i in range(600)]
    statundo=[[[0 for i in range(19)] for j in range(19)] for k in range(600)] # 무르기(뒤로가기, undo)를 위한 리스트. statundo[0]에는 첫 번째 수를 둔 직후 판의 전체 상태가 저장되는 식이다. 0,0부터 18,18까지의 0, 1, 2 전부를 저장한다.
    cntt=0
    temp=0
    position=[0,0]
    soosoon='' # 기보의 총 수순을 저장하기 위한 변수
    bjg1=27.5 # 좌표 보정을 위한 상수
    bjgx=4 # x좌표 보정을 위한 상수
    bjgy=0 # y좌표 보정을 위한 상수
    fps=20
    fpsClock=pygame.time.Clock()

    imgBaduk=pygame.image.load('./image/pan.png')
    imgBlackstone=pygame.image.load('./image/blackstone.png')
    imgWhitestone=pygame.image.load('./image/whitestone.png')
    imgMainbutton=pygame.image.load('./image/mainbutton.png')

    pygame.init()
    screen=pygame.display.set_mode((750,750))
    pygame.display.set_caption('기보')

    fps=20
    fpsClock=pygame.time.Clock()

    window=Tk() #여기부터 아래 몇 줄은 tkinter를 이용하여 기보의 이름을 입력받기 위한 코드이다.
    frm=Frame(window, width=400, height=200)
    frm.pack()
    l1=Label(window, text='기보 이름을 입력하세요.', bg='white', fg='black')
    l1.place(x=150, y=20)
    e1=Entry(window)
    e1.place(x=50, y=110)
    enter=Button(window, text='열기', command=openas)
    enter.place(x=250, y=110)
    window.mainloop()
    
    openkibo=open('./doc/'+nn+'.txt', 'r') # 입력받은 기보의 이름을 토대로 기보를 불러온다.
    lines=openkibo.readlines()
    soosoon=int(lines[0]) #기보 txt 파일의 가장 첫 줄은 총 수순이다.
    another=lines[1].split() # 2번째 줄은 [돌이 놓인 순서, x 좌표, y 좌표] 순으로 기보가 저장되어 있다. 띄어쓰기로 구분되어 있으므로 split으로 나눠서 저장한다.
    Players=lines[2].split()
    openkibo.close()
    print(Players)
    
    for i in range(soosoon) : # 총 수순의 수만큼
        for j in range(3) :
            tmpseq[i][j]=another[i*3+j] #tmpseq에 다시 저장해주고
    for i in range(soosoon) :
        for j in range(2) :
            opensequence[i][j]=tmpseq[i][j+1] #opensequence라는 변수에는 이게 몇 번째 수인지에 대한 정보가 그냥 리스트의 순서이기 때문에 tmpseq에서 편집해서 넣어준다.

    while 1 :
        
        blackban=[[0 for i in range(19)] for i in range(19)]
        Blackcluster=[[[20,20] for i in range(361)] for i in range(361)]
        whiteban=[[0 for i in range(19)] for i in range(19)]
        Whitecluster=[[[20,20] for i in range(361)] for i in range(361)] # 매 수마다 초기화가 필요한 변수들은 이렇게 초기화해준다.
        tt=0
        zz=0
        
        for event in pygame.event.get() :
            
            if event.type==QUIT :
                pygame.quit()
                sys.exit()
            if event.type==MOUSEBUTTONUP and event.button==LEFT :
                position=pygame.mouse.get_pos()
                if position[0]>=632 and position[0]<=732 and position[1]>=179 and position[1]<=225 :
                    return 0
            if event.type==KEYUP :
                if event.key==K_RIGHT or event.key==K_UP : #수순 진행 버튼
                    if int(opensequence[n][0])!=-1 :
                        www=1 # 수순 진행은 www를 1로 만든다.
                if event.key==K_m or event.key==K_DOWN or event.key==K_LEFT : # 무르기 버튼
                    if n>=1 :
                        www=2 # 무르기는 www를 2로 만든다.
            if www==1 : #수순 진행
                if n%2==0 :
                    stat[int(opensequence[n][0])][int(opensequence[n][1])]=1 #opensequence 안에는 char형으로 리스트가 되어있으므로 이를 int로 바꿔야 한다.
                    now1=int(opensequence[n][0])
                    now2=int(opensequence[n][1])
                else :
                    stat[int(opensequence[n][0])][int(opensequence[n][1])]=2
                    now1=int(opensequence[n][0])
                    now2=int(opensequence[n][1])
                n+=1 #n이 여기서 커짐에 주의
            if www==2 : # 뒤로 가기(undo)
                n-=1
                for i in range(19) :
                    for j in range(19) :
                        stat[i][j]=statundo[n-1][i][j]
                deadblack=blackdeadcount[n-1]
                deadwhite=whitedeadcount[n-1]
                blackdeadcount[n]=0
                whitedeadcount[n]=0
                www=0
        cntt=0 # 클러스터를 만들기 위한 변수
        if www==1 : 
            for i in range(19) : #검정 클러스터
                for j in range(19) :
                    if stat[i][j]==1 and blackban[i][j]==0 : #흑돌이 밴 목록에 없다면
                        tt=0
                        makeblackcluster(cntt,i,j) # 클러스터를 만들고
                        cntt+=1 # 클러스터 번호를 1 늘린다.
            cntt=0
            for i in range(19) : #하양 클러스터
                for j in range(19) :
                    if stat[i][j]==2 and whiteban[i][j]==0 :
                        zz=0
                        makewhitecluster(cntt,i,j)
                        cntt+=1
            blacksahwal() # 죽는 흑돌이 있는지, 있다면 들어내기 위한 함수
            whitesahwal() # 위와 같음. 다만 백돌
            for i in range(19) :
                for j in range(19) :
                    statundo[n-1][i][j]=stat[i][j] # undo를 위해 statundo에 stat의 값을 저장해 놓는다.
            blackdeadcount[n-1]=deadblack
            whitedeadcount[n-1]=deadwhite
            www=0
        screen.fill(WHITE)
        screen.blit(imgBaduk, (50,50)) # 바둑 판
        for i in range(19) : #stat에 따라 흑돌 또는 백돌을 판 위에 놓는다.
            for j in range(19) :
                if stat[i][j]==1 :
                    screen.blit(imgBlackstone, (i*bjg1+65+bjgx,j*bjg1+65+bjgy))
                if stat[i][j]==2 :
                    screen.blit(imgWhitestone, (i*bjg1+65+bjgx,j*bjg1+65+bjgy))
        fontObj = pygame.font.Font(None, 26)
        pygame.draw.rect(screen, BLACK, (50,620,235,120))
        pygame.draw.rect(screen, BLACK, (370,620,235,120), 1)
        textSurfaceObj1 = fontObj.render('White Dead(by Black) : '+str(deadwhite), True, WHITE)
        textRectObj1=textSurfaceObj1.get_rect();
        textRectObj1.center =(165,646)
        textSurfaceObj2 = fontObj.render('Black Dead(by White) : '+str(deadblack), True, BLACK)
        textRectObj2=textSurfaceObj2.get_rect();
        textRectObj2.center =(485,646)
        textSurfaceObj3 = fontObj.render(Players[0], True, WHITE)
        textRectObj3=textSurfaceObj3.get_rect();
        textRectObj3.center =(165,705)
        textSurfaceObj4 = fontObj.render(Players[1], True, BLACK)
        textRectObj4=textSurfaceObj4.get_rect();
        textRectObj4.center =(485,705)
        screen.blit(textSurfaceObj1, textRectObj1)
        screen.blit(textSurfaceObj2, textRectObj2)
        screen.blit(textSurfaceObj3, textRectObj3)
        screen.blit(textSurfaceObj4, textRectObj4)
        screen.blit(imgMainbutton, (628, 175))
        pygame.draw.line(screen, WHITE, (50,675),(285,675), 1)
        pygame.draw.line(screen, BLACK, (370,675),(605,675), 1)
        pygame.display.flip()
