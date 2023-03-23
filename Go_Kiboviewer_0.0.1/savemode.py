import pygame, sys
from pygame.locals import *

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
    n=0 # 돌의 수순을 알기 위한 상수. 돌이 하나 놓일 때마다 1씩 증가한다.
    cnt=0 # 마찬가지로 수순을 알기 위한 상수. sequecne에 값을 저장할 때 쓰인다.
    tmp=0
    LEFT=1
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
    deadwhite=0
    deadblack=0
    now1 = 0
    now2 = 0
    stat=[[0 for i in range(19)] for j in range(19)] 
    sequence=[[0, 0] for i in range(600)]
    Blackcluster=[[[20,20] for i in range(361)] for i in range(361)]
    Whitecluster=[[[20,20] for i in range(361)] for i in range(361)]
    blackban=[[0 for i in range(19)] for i in range(19)] #0이면 ban이 안 된것이고(클러스터를 이루지 않음) 1 이상이면 밴 된 것
    whiteban=[[0 for i in range(19)] for i in range(19)] #0이면 ban이 안 된것이고(클러스터를 이루지 않음) 1 이상이면 밴 된 것
    cntt=0
    name='  '
    data='  '
    temp=0
    bjg1=27.5 # 좌표 보정을 위한 상수
    bjgx=4 # x좌표 보정을 위한 상수
    bjgy=0 # y좌표 보정을 위한 상수
    fps=20
    fpsClock=pygame.time.Clock()

    imgBaduk=pygame.image.load('./image/pan.png')
    imgBlackstone=pygame.image.load('./image/blackstone.png')
    imgWhitestone=pygame.image.load('./image/whitestone.png')

    pygame.init()
    screen=pygame.display.set_mode((700,700))
    pygame.display.set_caption('기보')

    fps=20
    fpsClock=pygame.time.Clock()

    while 1 :
        blackban=[[0 for i in range(19)] for i in range(19)]
        Blackcluster=[[[20,20] for i in range(361)] for i in range(361)]
        whiteban=[[0 for i in range(19)] for i in range(19)]
        Whitecluster=[[[20,20] for i in range(361)] for i in range(361)]
        tt=0
        zz=0
        for event in pygame.event.get() :
            if event.type==QUIT :
                pygame.quit()
                sys.exit()
            if event.type==MOUSEBUTTONDOWN and event.button==LEFT :
                position=pygame.mouse.get_pos()
                pos[n][0]=position[0]
                pos[n][1]=position[1]
                www=1
            if event.type==KEYDOWN :
                if event.key==K_s :
                    name=input("저장할 파일의 이름을 입력하세요.: ")
                    createfile = open('./doc/'+name+'.txt', 'w')
                    createfile.write(str(n)+'\n')
                    for i in range(n):
                        data = str((i+1))+' '+str(sequence[i][0])+' '+str(sequence[i][1])+' '
                        createfile.write(data)
                    createfile.close()
            if www==1 :
                for i in range(19) :
                    for j in range(19) :
                        if pos[n][0]>=i*bjg1+70+bjgx and pos[n][0]<=i*bjg1+90+bjgx :
                            if pos[n][1]>=j*bjg1+70+bjgy and pos[n][1]<=j*bjg1+90+bjgy :
                                xt=i
                                yt=j
                                tmp=1
                if stat[xt][yt]==0 and tmp==1 :
                    if n%2==0 :
                        stat[xt][yt]=1
                        sequence[cnt][0]=xt
                        sequence[cnt][1]=yt
                        now1=xt
                        now2=yt
                        cnt+=1
                    else :
                        stat[xt][yt]=2
                        sequence[cnt][0]=xt
                        sequence[cnt][1]=yt
                        now1=xt
                        now2=yt
                        cnt+=1
                    n+=1   
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
            blacksahwal()
            whitesahwal()
            www=0
        screen.fill(WHITE)
        screen.blit(imgBaduk, (50,50))
        for i in range(19) :
            for j in range(19) :
                if stat[i][j]==1 :
                    screen.blit(imgBlackstone, (i*bjg1+65+bjgx,j*bjg1+65+bjgy))
                if stat[i][j]==2 :
                    screen.blit(imgWhitestone, (i*bjg1+65+bjgx,j*bjg1+65+bjgy))
        fontObj = pygame.font.Font(None, 26)
        textSurfaceObj1 = fontObj.render('White Dead(by Black) : '+str(deadblack), True, BLACK)
        textRectObj1=textSurfaceObj1.get_rect();
        textRectObj1.center =(170,650)
        textSurfaceObj2 = fontObj.render('Black Dead(by White) : '+str(deadwhite), True, BLACK)
        textRectObj2=textSurfaceObj2.get_rect();
        textRectObj2.center =(490,650)
        screen.blit(textSurfaceObj1, textRectObj1)
        screen.blit(textSurfaceObj2, textRectObj2)
        pygame.display.flip()
