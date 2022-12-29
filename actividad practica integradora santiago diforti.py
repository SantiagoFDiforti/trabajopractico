#Tu desafío es desarrollar un programa que permita realizar diferentes operaciones en base a
#las opciones que el usuario vaya ingresando por línea de comandos:
#● Jugar a “piedra, papel, tijera” compitiendo contra la computadora.
#● Adivinar un número compitiendo contra la computadora.
#● Tirar un dado.
#● Graficar una función matemática.

import random
dicc_ascii={}
diccionario={}
dic_grafico={}

#codigo ascii
spock=("MMMMMMMMMMMMMMMWNK00000KNWMMMMMMMMMMMMMM\nMMMMMMMMMMWXko:;,'.....',,:lxKWMMMMMMMMM\nMMMMMMMMXx:....',;;;;;;;,''...;oKWMMMMMM\nMMMMMMXd'..,;::;;;,,,,;;;;;:;,'..lKWMMMM\nMMMMWk,..;:;;:;,;;lkkc';:;,,,,;;'..dNMMM\nMMMNo..,;;;:;;';0OkNMk,,:';kx;,;;;..:KMM\nMMWo..;:;;:;;;'cXKxKMK;',,kW0c,,;;;'.:XM\nMMO..;:;;;;;;:':KNk0MNl.'oNKk0o';::;..lW\nMNc ':;;;;;;;:';0WOOWWx.:KNkOK:';;;:;.'0\nMK,.,:;::;;;;:';0WOx0X0lONkkNk,,:;;;;..k\nM0'.;:;,,,,;;:',OWXXXWWWWXOXNl';;;;:;..x\nMX: ,;'ckxo:,,';0MMMMMMMMMMM0;,:;;;;;..k\nMMd..;,;o0WNko:oXWNXNWMMMMMMk,,:;;;:,.:X\nMMX:.';;,,lKWWWWMWXOxkXMMMMMx,,:;;:;..kM\nMMM0,.';;;';kNMMMMMWWOOWMMMNl';;;:;..dNM\nMMMMK:..,;;,,l0WMMMMMXKWMMNd,,;;;'.,kWMM\nMMMMMNx,..,;;,,oXMMMMWWMMNo',:;'..lKMMMM\nMMMMMMMNk:...,,'xMMMMMMMMK;.'...lKWMMMMM\nMMMMMMMMMWKdc;'.,ldddddoc;..;lxXWMMMMMMM\nMMMMMMMMMMMMMWKOxdolllodxkOKWMMMMMMMMMMM").replace(';',' ').replace(':',' ').replace('.',' ').replace(',',' ').replace("'"," ").replace("o",".").replace('l','.')
piedra=("MMMMMMMMMMMWXOxdocccccooxOXWMMMMMMMMMMMM\nMMMMMMMMW0o:,....'''''....';lONMMMMMMMMM\nMMMMMMXx;..',;:;;;;;;;;::;,..;:dXMMMMMMM\nMMMMWk,.';;;;::;;;;,,,;;,,cxKNOc;xNMMMMM\nMMMNo..;:;;;,;:clodddddddONMMMMWx,lXMMMM\nMMWo..;:;;,;dOKNWMMMMMMMMMMMMMMMWk'cNMMM\nMMk..;;;:;,dKXMMMMMMMMMMMMMMMMMMMNc.xWMM\nMWc ':;;:,;O0KNNMMMMMMMMMMMMMMWKxl, :NMM\nMX;.,:;;:,cOKX0KWWMMMMMMMMMMM0l;,;,.,KMM\nMNc.,:;;:,;c0K0X0XMWWKOOONMMNo,:;:' :XMM\nMMx..:;;;:;,lx0KONMX0xkKOKMMKc,:;;..dMMM\nMMNc.':;;;;;,,oxOWWXKXNK0NW0l,;;;'.:XMMM\nMMMX:.';;;;;;;,,:xOkkOkdddl:;;:;'.;KMMMM\nMMMMXo..,;;;;;;;;,,,,;;;,;;;;;,..lXMMMMM\nMMMMMW0c..',;;;;;;;;;;::;;;,'..cOWMMMMMM\nMMMMMMMWKx:,...'',,,,,''...':dKWMMMMMMMM\nMMMMMMMMMMMXOdl::;;;;;::ldOXWMMMMMMMMMMM").replace(';',' ').replace(':',' ').replace('.',' ').replace(',',' ').replace("'"," ").replace("o",".").replace('l','.')
papel=("MMMMMMMMMMMMN0kxolccccodxOKWMMMMMMMMMMMM\nMMMMMMMMWKd:,.....'.......',ckXMMMMMMMMM\nMMMMMMNkc'..';;::;::;;;::;;'..'l0WMMMMMM\nMMMMWO:,o0ko:,,;;::;;;;;;;;;:;'..lKWMMMM\nMMMNo'cKWMMWXOdl:,,,;;;;;;;;;;;;'.'xWMMM\nMMXc'xNMMMMMMMMWN0xlc:,,;;;;;;:;:,..dWMM\nMNc.cNMMMMMMMMMMMMMWWXOo;,;:;;;;;;;..xWM\nMk..,cOWMMMMMMMMMMMMMW000d:,;;;;;;:,.,KM\nNc ':,,dNMMMMMMMMMMNKKKOk00d;,;;;;;;..dM\nK;.,::,,kMMMMMMMMMWNK0kO0OOOkc,;::;:' cW\nK,.,:;;'cXMMMNXWMWXOO0K0OOO0Oo,,:;;:' cW\nN: ':;;;,:ONMXxoxXWNK0OOKK0OOd,,:;;;. oW\nMx..;;;;;,,lOWNd',o0XNWKOO0X0c';:;:,..OM\nMX: ';;;;;;,,l0Xl.',;cx0X0l::,,;;:;..oWM\nMMK;.';;;;;;;,;:;,;;;;,,::,,;::;;;..lNMM\nMMMK:..,;;;;;;;;;:;;;;:;;;:;;;;;,..oNMMM\nMMMMNx,.';;;;;;;;;;;;;;;;;;:;;,..;OWMMMM\nMMMMMMXd,..';;::;;;;;;;;::;,'..:kNMMMMMM\nMMMMMMMMNOl;....'''''''....';o0WMMMMMMMM\nMMMMMMMMMMMWKkdlc:;::::coxOXWMMMMMMMMMMM").replace(';',' ').replace(':',' ').replace('.',' ').replace(',',' ').replace("'"," ").replace("o",".").replace('l','.')
tijeras=("MMMMMMMMMMMMMWNKOkkkxkOKXWMMMMMMMMMMMMMM\nMMMMMMMMMWKxc;,'........';:okXMMMMMMMMMM\nMMMMMMMXd;...',;;;;:::;;,'...'cOWMMMMMMM\nMMMMMXo'..,;;;;;;;:;;;;;;;:;;'..:OWMMMMM\nMMMWk,.';;;;;;;;:;;;;;;;;;;;;;;,..cKMMMM\nMMNd..;;;;;:;;;::;;;;;;;;,,;;:;;;..,0MMM\nMWd..;;,:lc;,,,;::;:;;,;lddl:,,;:;' ,0MM\nMO..;:;,l0KKOxol:;,,';oKWMMWXkl;,,,. cN\nWl ':;:;,;cokKNWX0kl;xWWKkKWMMWX0OOO;.kM\nX;.;:;;;;;;;,;cokKNOlOWKxoOWMMMMMMMMd.oM\nK,.;:;;;,,,,,,,,,c0X0kkkkkONMMMMMMMMx.oM\nX:.,;,:odxxkOO0KXNWMMXOOXNKKXWMMMMMMo.dM\nWd..;,ckOOOOkkkOOOO0000Ox0WWWWMMMMMX;'0M\nMK;.,;,,,,,,,',xKXNNNX0kxdONMMWKdol;.dWM\nMMO'.,;;;;;:;;,:ok0OOO0XXkxXNKd;,,..lNMM\nMMW0;.';;;;;;::;':dOOOxoc;:lc;,;,..lXMMM\nMMMMXl..';;;;;:;;,,,,,,,;;;;;:;..,kNMMMM\nMMMMMW0l'..,;::;;;;;;;;;::;;'..;xXMMMMMM\nMMMMMMMWXx:'...'',,,,,''....,lONMMMMMMMM\nMMMMMMMMMMWXOxl:;;,,,,;:ldkKWMMMMMMMMMMM").replace(';',' ').replace(':',' ').replace('.',' ').replace(',',' ').replace("'"," ").replace("o",".").replace('l','.')
lagarto=("MMMMMMMMMMMMMNKkxoollodxk0NMMMMMMMMMMMMM\nMMMMMMMMMWKd:,............':dKWMMMMMMMMM\nMMMMMMMNk:...';;;:::::;;;,'...:kNMMMMMMM\nMMMMMW0;..,;:;;;;;;;;;;:;;;:;'..;0WMMMMM\nMMMMWd..,;:;;:;;,;loooc,,;;:;;;'..dNMMMM\nMMMNo..;:;;;,,:ldkO00Oxolc:,,;;;,..lNMMM\nMMWd..;;;;,:dOKKKKXNWWX0OOxl::;,;;..dWMM\nMMO..;;;;'lXMWWWMMWNXXXNWWNKOd;';:,..kMM\nMNc ':;:;,kMMMMW0oc:::::cloxkl,;;;;. cNM\nMK,.;:;:,:0MMMMWd',,,,,:loo;',;;;;:,.,KM\nMO..;:;;,oNMMMMMNOdddxOXWNOc,;:;;;;;..OM\nMO..;;:;;kMMMMMMMMMMMMMNkc,,;;;;;;:,..OM\nMK;.,::,:KMMMMMMMMMMMNk:,;::;;;;;;:' ;XM\nMWo..;:,cXMMMMMMMMNOdl,,;;:;;;;;;:;. oWM\nMMX;.,:,:0MMMMMMM0c,,,;;;;;:;;;;;;' ;XMM\nMMM0'.,;,xMMMMMMNo';;;;;;;;:;;;;;' 'OMMM\nMMMMO,.''oNMMMMMNl,;;;;;;;;:;;;;. 'OMMMM\nMMMMMKc..:KMMMMMWo,;;;;;;;;;;;'..:0MMMMM\nMMMMMMNk;.:OWMMMWd,;:;;;;;;,...,kNMMMMMM\nMMMMMMMMNOc;;cdOKd,,;,,'.....ckNMMMMMMMM\nMMMMMMMMMMWXkoc::;.....';cokXWMMMMMMMMMM").replace(';',' ').replace(':',' ').replace('.',' ').replace(',',' ').replace("'"," ").replace("o",".").replace('l','.')

uno=("                                        \n                                        \n                                        \n                                        \n                                        \n                                        \n                'okOOko'                \n               ;KMMMMMMK;               \n               lNMMMMMMNl               \n               .l0NWWN0l.               \n                 .',,'.                 \n                                        \n                                        \n                                        \n                                        \n                                        \n                                        ")
dos=("O,                                    ,O\nc                             .'.      c\nc                          .cOXNXOc.   c\nc                          cNMMMMMNc   c\nc                          :XMMMMMX:   c\nc                           ,dO00d,    c\nc                              .       c\nc                                      c\nc                                      c\nc                                      c\nc                                      c\nc                                      c\nc                                      c\nc    ,oOOko'                           c\nc   cXMMMMMK,                          c\nc   oWMMMMMX:                          c\nc   .oKNWN0c.                          c\nc     .','.                            c\no.                                    .o\nKc.                                  .cX")
tres=("'                                      '\n     ..                                 \n   ;kKKx,                               \n  .xMMMWd.                              \n   'dOko.                               \n                                        \n                                        \n                                        \n                .cxkkd,                 \n                cNMMMMO.                \n                'xKXX0c.                \n                  ....                  \n                                        \n                                        \n                                        \n                                ,odo,   \n                               ,KMMMK;  \n                               .dXNXd.  \n                                 .'.    \n:.                                     :")
cuatro=("WWWNKkxxxdxxxxxxdxxdxxddxxddxxxdxdxxddxxxxxdxxdxOKNW\nWXo.                                            .oXW\nWd.     .';,'.                        .';;'.     .dW\nNo    'd0NNNX0o.                    .o0XNNX0d'    oN\nNo   'OWWWWWWWWk.                  .kWWWWWWWWO'   oN\nNl   cXWWWWWWWWX;                  ;KWWWWWWWWXc   oN\nNl   .kWWWWWWWNx.                  .xNWWWWWWWk.   oN\nNo    .ckKXXKkc.                    .:kKXXKkc.    lN\nNo       ....                          ....       oN\nNo                                                oN\nNl                                                lN\nNo                                                oN\nNo                                                lN\nNo                                                lN\nNl                                                oN\nNl                                                lN\nNo                                                oN\nNo     .;lool;.                      .;lool;.     oN\nNl    c0NWWWWNO:                    :ONWWWWN0c.   lN\nNo   ;KWWWWWWWW0,                  ,0WWWWWWWWK;   lN\nNl   :XWWWWWWWWK;                  ;KWWWWWWWWX:   lN\nNo   .oXWWWWWWKc.                   cKWWWWWWXl.   oN\nNo     'ldxkdc.                      .cdxxxc'     oN\nWO'                                              'OW\nWN0o;,,,,,,,,,,,,,,,',,',,,,,,,,,,,,,',,,,,,',,;o0NW\nWWWWWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNWWWW")
cinco=("o.                                    .o\n,      .,;'.                .';,.      ,\n,    ,kXWWNO:              :ONWWXk,    ,\n,   .kMMMMMMK,            ,KMMMMMMk.   ,\n,   .oNMMMMWk.            .kWMMMMNo.   ,\n,    .;dkkxc.              .cxkkd;.    ,\n,                                      ,\n,               .,cllc,.               ,\n,              'kNMMMMNk'              ,\n,              lWMMMMMMWl              ,\n,              'OWMMMMWO'              ,\n,               .;lool;.               ,\n,                                      ,\n,     .;cc:.                .;cc;.     ,\n,    ;0WMMWKl.            .lKWMMW0;    ,\n,   .kMMMMMMK,            ,KMMMMMMk.   ,\n,    cXMMMMNd.            .dNMMMMXc    ,\n,     'codl,                ,ldoc'     ,\n:                                      ;\nx.                                    .x")
seis=("k;.                                  .;O\n.   .;ldo:.                  .:odl,.   .\n   .dNWMMWO'                '0WMMMNd.   \n   '0WWMMMNc                cNMMMWWO'   \n    :OXWN0l.                .oKNWXO;    \n     ..,'.                    .',.      \n                                        \n      .''.                    .''.      \n    ,xXNN0o.                .l0XNXk;    \n   .kMMMMMWl                cNMMMMM0'   \n   .oNMMMMK;                ,0WMMMWx.   \n     ,lddc.                  .codo;.    \n                                        \n      .''.                    .,;'.     \n    ,kKNNKo.                .oKWWNO:    \n   .OWWMMMWl                :NMMMMM0'   \n   .oNWMMWK;                'OWMMWNd.   \n    .,lddc'                  .:lol,     \n:.                                     :\nXo.                                  .oX")

dicc_ascii={'spock':spock,'piedra':piedra,'papel':papel,'tijeras':tijeras,'lagarto':lagarto,1:uno,2:dos,3:tres,4:cuatro,5:cinco,6:seis}
diccionario={('spock','piedra'):"GANASTE, SPOCK VAPORIZA PIEDRA",("spock","tijeras"):"GANASTE, SPOCK ROMPE TIJERAS",("spock","spock"):"EMPATE",("spock","lagarto"):"PERDISTE, LAGARTO ENVENENA SPOCK",("spock","papel"):"PERDISTE, PAPEL DESAUTORIZA SPOCK",("papel","piedra"):"GANASTE, PAPEL TAPA PIEDRA",("papel","spock"):"GANASTE, PAPEL DESAUTORIZA SPOCK",("papel","papel"):"EMPATE",("papel","tijeras"):"PERDISTE, TIJERAS CORTAN PAPEL",("papel","lagarto"):"PERDISTE, LAGARTO DEVORA PAPEL",("piedra","tijeras"):"GANASTE, PIEDRA APLASTAN TIJERAS",("piedra","lagarto"):"GANASTE, PIEDRA APLASTA LAGARTO",("piedra","piedra"):"EMPATE",("piedra","papel"):"PERDISTE, PAPEL TAPA PIEDRA",("piedra","spock"):"PERDISTE, SPOCK VAPORIZA PIEDRA",("tijeras","papel"):"GANASTE, TIJERAS CORTAN PAPEL",("tijeras","lagarto"):"GANASTE, TIJERAS DESCAPITAN LAGARTO",("tijeras","tijeras"):"EMPATE",("tijeras","piedra"):"PERDISTE, PIEDRA APLASTA TIJERAS",("tijeras","spock"):"PERDISTE, SPOCK ROMPE TIJERAS",("lagarto","spock"):"GANASTE, LAGARTO ENVENENA SPOCK",("lagarto","papel"):"GANASTE, LAGARTO DEVORA PAPEL",("lagarto","lagarto"):"EMPATE",("lagarto","tijeras"):"PERDISTE, TIJERAS DECAPITAN LAGARTO",("lagarto","piedra"):"PERDISTE, PIEDRA APLSTA LAGARTO"}
dic_grafico_Y={5:0,4:1,3:2,2:3,1:4,0:5,-1:6,-2:7,-3:8,-4:9,-5:10}
dic_grafico_X={5:10,4:9,3:8,2:7,1:6,0:5,-1:4,-2:3,-3:2,-4:1,-5:0}

def juego (): #juego 'PIEDRA','PAPEL','TIJERAS','LAGARTO','SPOCK'

    def corroborar(x,y): #verifica que la opcion dada este en la lista 
        vari=False
        for i in x:
            if i.lower() == y:
                vari = True
        return vari

    mano=['PIEDRA','PAPEL','TIJERAS','LAGARTO','SPOCK']
    print('VAMOS A JUGAR PIEDRA, PAPEL, TIJERAS, LAGARTO, SPOCK. "FIN" PARA TERMINAR')
    semi_ia = open("semi_ia.txt",'w')
    semi_ia.close
    list_jugadas=0

    while True: #dice quien gana y lo guarda en una lista en un archivo 
        opcionj=input('TU OPCION?').lower()
        npc=random.choice(mano).lower()
        if corroborar(mano,opcionj)==True:
            print(opcionj,npc)
            print(dicc_ascii[opcionj],'\n                Versus\n',dicc_ascii[npc])
            print(diccionario[opcionj,npc])
            semi_ia = open("semi_ia.txt",'a')
            semi_ia.write(opcionj+',')
            semi_ia.flush()
            semi_ia= open("semi_ia.txt",'r')
            p=semi_ia.read()
            list_jugadas=p.rstrip(p[-1])
            semi_ia.close
        elif opcionj =='fin':
            print('BAZZINGA')
            print('tus jugadas fueron: '+list_jugadas)
            break
        else:
            print('OPCION INVALIDA')

def adivinar(): #adivina el numero
    num=int(random.randrange(1,20))
    def pista(x,y): #da pistas sobre el numero a adivinar 
        if x < y:
           print('INTENTA UN NUMERO MAS GRANDE')
        else:
            print('MAS CHICO \n')

    num_per=int(input('ESTOY PENSANDO EN UN NUMERO DEL 1 AL 20\nTENES TRES INTENTOS.\n'))
    if num_per == num:
        print('INCREIBLE ADIVINASTE EN EL PRIMER INTENTO\n')
    else:
        pista(num_per,num)
        num_per=int(input('INCORRECTO, SEGUNDO INTENTO\n'))
        if num_per==num:
            print('DOS DE TRES NO ESTA MAL, MUY BIEN\n')
        else:
            pista(num_per,num)
            num_per=int(input('NO NO,ULTIMA\n'))
            if num_per==num:
                print('MUY BIEN\n')
            else:
                print('NOPE, PERDISTE EL NUMERO ERA ',num,'\n')
            
def Dado(): #genera e imprime un dado
    dado=random.randrange(1,6)
    print(dicc_ascii[dado])

def funcion():
    Grafico = [[5 ,'  ','  ','  ','  ','|','  ','  ','  ','  ','  '], #grafico de la funcion
               [4 ,'  ','  ','  ','  ','|','  ','  ','  ','  ','  '], 
               [3 ,'  ','  ','  ','  ','|','  ','  ','  ','  ','  '],
               [2 ,'  ','  ','  ','  ','|','  ','  ','  ','  ','  '],
               [1 ,'  ','  ','  ','  ','|','  ','  ','  ','  ','  '],
               [0 ,'- ','- ','- ','- ','|','- ','- ','- ','- ','- '],
               [-1,'  ','  ','  ','  ','|','  ','  ','  ','  ','  '],
               [-2,'  ','  ','  ','  ','|','  ','  ','  ','  ','  '],
               [-3,'  ','  ','  ','  ','|','  ','  ','  ','  ','  '],
               [-4,'  ','  ','  ','  ','|','  ','  ','  ','  ','  '],
               ['','-4','-3','-2','-1','|','1 ','2 ','3 ','4 ','5 ']]

    rango=[-5,-4,-3,-2,-1,0,1,2,3,4,5]
    print('EJEMPLO Y = M X + B\n')
    VAL_B= int(input('INGRESA VALOR DE "B"\n'))
    VAL_M= int(input('INGRESA VALOR DE "M"\n'))
    cont=0
    Y=0
    for I in rango: #dibuja la funcion
        Y=(VAL_M*I)+VAL_B
        if (Y<=5 and Y>=-5):      
            Grafico[dic_grafico_Y[Y]][dic_grafico_X[I]]='O '
    for I in rango:
        print(Grafico[cont])
        cont=cont+1

def menu ():#llama a todas
    while True:
        opcion=input('Bienvenido al menu\nIngrese "juego" para jugar piedra, papel, tijera, lagarto spock\n"adivinar" para una adivinanza numerica\n"Dado" para generar un dado\ny "Funcion" para graficar una funcion\n finalmente "fin" para terminar\n').lower()
        if opcion == 'juego':
            juego()
        elif opcion == 'adivinar':
            adivinar()
        elif opcion == 'dado':
            Dado()
        elif opcion == 'funcion':
            funcion()
        elif opcion == 'fin':
            break
        else:
            print('No es un opcion correcta\n')

menu()