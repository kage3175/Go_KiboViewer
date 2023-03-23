import os

def main() :
    another=[0 for i in range(1600)]
    anothernum=[-1 for i in range (1600)]
    sequence=[[-1,-1,-1] for i in range(600)]
    n=0
    strtmp=' '
    filename=[' ' for i in range(100)]
    
    filenames=os.listdir('./whattochange')
    for k in range(len(filenames)) :
        filename=os.path.splitext(filenames[k])[0]
        openx=open('./whattochange/'+filename+'.hgf', 'r')
        lines=openx.readlines()
        another=lines[1].split()
        openx.close()
        for i in range(len(another)) :
            anothernum[i]=int(another[i])
        while anothernum[4*n]!=-1:
            sequence[n]=[anothernum[4*n+3],anothernum[4*n+2],anothernum[4*n+1]]
            n+=1
        n=0
        createfile=open('./result/'+filename+'.sgf', 'w')
        createfile.write('(;GM[1]FF[4]CA[UTF-8]AP[Sabaki:0.50.1]KM[6.5]SZ[19]DT[1900-01-01]')
        while sequence[n][0]!=-1:
            if sequence[n][0]==1:
                strtmp=';B['+chr(sequence[n][2]+97)+chr(sequence[n][1]+97)+']'
            elif sequence[n][0]==2:
                strtmp=';W['+chr(sequence[n][2]+97)+chr(sequence[n][1]+97)+']'
            createfile.write(strtmp)
            n+=1
        createfile.write(')')
        createfile.close()
        os.remove('./whattochange/'+filename+'.hgf')

main()
