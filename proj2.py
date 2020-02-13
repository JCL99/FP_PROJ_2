             ###################################################
             #                Joao Carlos Lopes                #
             #                   Num: 90732                    #
             #                   2º projeto                    #
             ###################################################

################################## Codigo ######################################
#from Projeto_pt1 import e_palavra
from parte1 import e_palavra
import itertools
################################ Constantes ####################################

########################### TAD palavra_potencial ##############################
def cria_palavra_potencial(string, tuplo):
    """
    Cadeia de caracteres x tuplo de letras --> palavra_potencial
    """
    if not(isinstance(string, str)) or not(isinstance(tuplo, tuple)):
        raise ValueError("cria_palavra_potencial:argumentos invalidos.")

    if tuplo == ("",):
        return ""

    for i in string:
        if not(ord("A") <= ord(i) <= ord("Z")):
            raise ValueError("cria_palavra_potencial:argumentos invalidos.")
    for i in tuplo:
        if not(ord("A") <= ord(i) <= ord("Z")):
            raise ValueError("cria_palavra_potencial:argumentos invalidos.")

    if (string == "" and tuplo == ()) or (string == "" and tuplo != ()):
        return ""

    if len(string) > len(tuplo):
        raise ValueError("cria_palavra_potencial:a palavra nao e valida.")
    for i in string:
        if not(i in tuplo):
            raise ValueError("cria_palavra_potencial:a palavra nao e valida.")

    aux_lst = list(tuplo) #Ja e mutavel

    #Verifica se há mais elementos na string do que no tuplo
    for i in range(len(string)):
        if string[i] not in aux_lst:
            raise ValueError("cria_palavra_potencial:a palavra nao e valida.")
        for j in range(len(aux_lst)):
            if string[i] == aux_lst[j]:
                del(aux_lst[j])
                break

    return string

def palavra_tamanho(palavra_potencial):
    """
    palavra_potencial --> inteiro
    """
    return len(palavra_potencial)

def e_palavra_potencial(arg):
    """
    universal --> logico
    """
    if not(isinstance(arg, str)):
        return False
    if not(arg):
        return True

    for i in arg:
        if not(ord("A") <= ord(i) <= ord("Z")):
            return False
    return True

def palavras_potenciais_iguais(palavra_potencial_1, palavra_potencial_2):
    """
    palavra_potencial x palavra_potencial --> logico
    """
    return palavra_potencial_1 == palavra_potencial_2

def palavras_potencial_menor(palavra_potencial_1, palavra_potencial_2):
    """
    palavra_potencial x palavra_potencial --> logico
    """
    return palavra_potencial_1 < palavra_potencial_2

def palavra_potencial_para_cadeia(palavra_potencial):
    """
    palavra_potencial --> cadeia caracteres
    """
    return palavra_potencial

########################### TAD conjunto_palavras ##############################
def cria_conjunto_palavras():
    """
    --> conjunto palavras
    """
    aux_lst = []
    return aux_lst

def numero_palavras(conjunto_palavras):
    """
    conjunto_palavras -->  inteiro
    """
    return len(conjunto_palavras)

def subconjunto_por_tamanho(conjunto_palavras, num_int):
    """
    conjunto_palavras x inteiro --> lista
    """
    aux_lst = []

    for i in conjunto_palavras:
        #Se o tamanho da palavra for igual ao inteiro
        if len(i) == num_int:
            #Entao adiciona a lista
            aux_lst.append(i)

    return aux_lst

def acrescenta_palavra(conjunto_palavras, palavra_potencial):
    """
    conjunto_palavras x palavra_potencial -->
    """
    if not(isinstance(conjunto_palavras, list)) or not(isinstance(palavra_potencial, str)):
        raise ValueError("acrescenta_palavra:argumentos invalidos.")
    for i in conjunto_palavras:
        for j in i:
            if not (ord("A") <= ord(j) <= ord("Z")):
                raise ValueError("acrescenta_palavra:argumentos invalidos.")
    for i in palavra_potencial:
        if not (ord("A") <= ord(i) <= ord("Z")):
            raise ValueError("acrescenta_palavra:argumentos invalidos.")

    if not(palavra_potencial in conjunto_palavras):
        #Caso não esteja, acrescenta
        conjunto_palavras.append(palavra_potencial)

def e_conjunto_palavras(arg):
    """
    universal --> logico
    """
    if not(isinstance(arg, list)):
        return False
    if arg == []:
        return True
    for i in arg:
        if not(isinstance(i, str)):
            return False
        for j in i:
            if not (ord("A") <= ord(j) <= ord("Z")):
                return False
    return True

def conjuntos_palavras_iguais(conjunto_palavras_1, conjunto_palavras_2):
    """
    conjunto_palavras x conjunto_palavras --> universal
    """
    return sorted(conjunto_palavras_1) == sorted(conjunto_palavras_2)

def conjunto_palavras_para_cadeia(conjunto_palavras):
    """
    conjunto_palavras --> cadeia caracteres
    """
    #Ordenar as palavras
    sorted_lst = sorted(conjunto_palavras)
    aux_dic = {}
    aux_str = ""

    #Para cada palavra, se nao estiver no dicionario cria uma chave
    #com o seu tamanho e adiciona a palavra
    for i in sorted_lst:
        if not(str(len(i)) in aux_dic):
            aux_dic[str(len(i))] = []
        aux_dic[str(len(i))].append(i)

    for key in sorted(aux_dic.keys()):
        aux_str = aux_str + key + "->" + str(aux_dic[key]) + ";"

    aux_str = aux_str[:len(aux_str)-1] #Tira o ultimo ;

    return ("[" + aux_str.replace("'", "") + "]")

################################## TAD Jogador #################################
def cria_jogador(string):
    """
    cadeia caracteres --> jogador
    """
    if not(isinstance(string, str)) or string == "":
        raise ValueError("cria_jogador:argumento invalido.")

    return {"nome": string, "pontos": 0, "validas": [], "invalidas": []}

def jogador_nome(jogador):
    """
    jogador --> cadeia caracteres
    """
    return jogador["nome"]

def jogador_pontuacao(jogador):
    """
    jogador --> inteiro
    """
    return jogador["pontos"]

def jogador_palavras_validas(jogador):
    """
    jogador --> conjunto_palavras
    """
    return jogador["validas"]

def jogador_palavras_invalidas(jogador):
    """
    jogador --> conjunto_palavras
    """
    return jogador["invalidas"]

def adiciona_palavra_valida(jogador, palavra_potencial):
    """
    jogador x palavra_potencial -->
    """
    if not(isinstance(jogador, dict)) or not(e_palavra_potencial(palavra_potencial)):
        raise ValueError("adiciona_palavra_valida:argumentos invalidos.")
    if not("nome" in jogador and "pontos" in jogador and "validas" in jogador and "invalidas" in jogador):
        raise ValueError("adiciona_palavra_valida:argumentos invalidos.")

    #Adiciona a palavra as validas
    jogador["validas"].append(palavra_potencial)
    #Incrementa os pontos com o tamanho dessa palavra
    jogador["pontos"] += len(palavra_potencial)

def adiciona_palavra_invalida(jogador, palavra_potencial):
    """
    jogador x palavra_potencial -->
    """
    if not(isinstance(jogador, dict)) or not(e_palavra_potencial(palavra_potencial)):
        raise ValueError("adiciona_palavra_invalida:argumentos invalidos.")
    if not("nome" in jogador and "pontos" in jogador and "validas" in jogador and "invalidas" in jogador):
        raise ValueError("adiciona_palavra_invalida:argumentos invalidos.")

    #Adiciona a palavra as invalidas
    jogador["invalidas"].append(palavra_potencial)
    #Decrementa os pontos com o tamanho dessa palavra
    jogador["pontos"] -= len(palavra_potencial)

def e_jogador(arg):
    """
    universal --> logico
    """
    if not(isinstance(arg, dict)):
        return False
    if not("nome" in arg and "pontos" in arg and "validas" in arg and "invalidas" in arg):
        return False
    if len(arg) > 4:
        return False
    return True

def jogador_para_cadeia(jogador):
    """
    jogador --> cadeia caracteres
    """
    return ("JOGADOR " + jogador["nome"] + " PONTOS=" + str(jogador["pontos"]) + " VALIDAS=" + conjunto_palavras_para_cadeia(jogador["validas"]) + " INVALIDAS=" + conjunto_palavras_para_cadeia(jogador["invalidas"]))

############################### Funcoes adicionais #############################
def gera_todas_palavras_validas(tuplo):
    """
    tuplo de letras --> conjunto_palavras
    """
    aux_lst = []

    #Para todos os tamanhos possiveis de gerar
    for i in range(1, len(tuplo)+1):
        #Para todas as permutacoes com cada um desses tamanhos
        for j in list(itertools.permutations(list(tuplo))):
            #Para cada combinacao dessas permutacoes
            for k in list(itertools.combinations(j, i)):
                #Se a juncao das letras da lista for uma palavra
                if e_palavra(cria_palavra_potencial("".join(k), tuplo)):
                    #Entao junta as palavras validas
                    aux_lst.append("".join(k))

    #No final apresenta a lista de pal. validas sem repeticoes usando o set()
    return list(set(aux_lst))

def guru_mj(tuplo):
    """
    tuplo de letras -->
    """
    #Nomes dos jogadores
    aux_jogadores = []
    #Jogadores criados pela cria_jogador()
    jogadores = []
    #Gerar as palavras validas
    palavras_validas = gera_todas_palavras_validas(tuplo)
    palavras_validas_copy = list(palavras_validas)

    aux_pal_usadas = []

    print("Descubra todas as palavras geradas a partir das letras:\n" + str(tuplo))
    print("Introduza o nome dos jogadores (-1 para terminar)...")

    #Enquanto o input nao for -1 continuar a pedir nomes de jogadores
    #e escrever esses nomes no aux_jogadores
    aux_jogador = 1
    aux_input = ""
    while aux_input != "-1":
        aux_input = input("JOGADOR " + str(aux_jogador) + " -> ")
        if aux_input != "-1":
            aux_jogadores.append(aux_input)
            aux_jogador += 1

    #Para cada nome de jogador criar um jogador
    for i in aux_jogadores:
        jogadores.append(cria_jogador(i))

    #Enquanto houver palavras validas
    aux_jogador = 1
    aux_jogada = 1
    aux_input = ""
    while palavras_validas:
        print("JOGADA " + str(aux_jogada) + " - Falta descobrir " + str(len(palavras_validas)) + " palavras")
        aux_input1 = input("JOGADOR " + aux_jogadores[aux_jogador - 1] + " -> ")
        aux_input = cria_palavra_potencial(aux_input1, tuplo)
        if aux_input in palavras_validas_copy:
            print(str(aux_input) + " - palavra VALIDA")
            #Se ainda nao tiver sido escolhida
            if not(aux_input in aux_pal_usadas):
                adiciona_palavra_valida(jogadores[aux_jogador-1], aux_input)
                palavras_validas.remove(aux_input)
                aux_pal_usadas.append(aux_input)
        else:
            print(str(aux_input) + " - palavra INVALIDA")
            #Se ainda nao tiver sido escolhida
            if not(aux_input in aux_pal_usadas):
                adiciona_palavra_invalida(jogadores[aux_jogador-1], aux_input)
                aux_pal_usadas.append(aux_input)
        aux_jogador += 1
        aux_jogada += 1
        #Se por acaso o ultimo jogador jogar e necessario depois disso referir
        #ao programa que o jogador seguinte deve ser o primeiro
        if aux_jogador == len(aux_jogadores) + 1:
            aux_jogador = 1

    #Ver o maior numero de pontos em todos os jogadores
    mais_pontos = -1 * 9999
    melhores_jogadores = []
    for i in jogadores:
        if i["pontos"] > mais_pontos:
            mais_pontos = i["pontos"]
    #Se um jogador tiver o mesmo que o maior numero de pontos entao deve
    #ser adicionado a lista de melhores jogadores, sobrando assim so os
    #jogadores que têm o maior numero de pontos
    for i in jogadores:
        if i["pontos"] == mais_pontos:
            melhores_jogadores.append(i)

    #Se so houver um jogador nos melhores jogadores
    if len(melhores_jogadores) == 1:
        print("FIM DE JOGO! O jogo terminou com a vitoria do jogador " + jogador_nome(melhores_jogadores[0]) + " com " + str(jogador_pontuacao(melhores_jogadores[0])) + " pontos.")
    #Caso contrario, se houver mais
    else:
        print("FIM DE JOGO! O jogo terminou em empate.")

    for i in jogadores:
        print(jogador_para_cadeia(i))
