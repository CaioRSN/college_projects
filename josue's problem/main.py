quantidade_cidades = int(input()) #numero de cidades

print ("Pega a sua trouxa, moleque. O ônibus pro sertão já vai sair.")
print (f"Se ajeita nesse banco, menino, que o chacoalho vai ser grande. A gente tem {quantidade_cidades} cidade(s) de poeira pela frente até achar o tal do teu pai. Presta atenção no que o povo fala...")

for k in range (quantidade_cidades): #vai repetir de acordo com o numero de cidades

    acumulador = "" #vai ser usado pra juntar todas as informacoes JA CONVERTIDAS em () , {} ou []

    r = True #condicao do while que vai ser usado

    #variavel gambiarra pra ser usada nos pares
    contador_nome_jesus = 0 
    contador_nome_isaias = 0
    contador_nome_moises = 0
    contador_end_sertao = 0
    contador_end_bom_jesus = 0
    contador_lembranca = 0


    print (f"Atenção, {k + 1}ª cidade! Carta de graça! A gente só quer informação da minha família em troca!")

    while r:
     informacao = str(input().lower())
    
     if informacao == "fim": #recebe informacao ate a informacao ser: "fim"
         r = False

    #parte de converter em identidade, endereco e lembrança yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy

    #endereço:
    #endereço; tem "sertao" ou "bom jesus": resulta em chaves {}

    #sertao
     elif ("sertao" in informacao) and (contador_end_sertao == 0):
         acumulador = acumulador + "{"
         contador_end_sertao = contador_end_sertao + 1
     elif ("sertao" in informacao) and (contador_end_sertao == 1):
         acumulador = acumulador + "}"
         contador_end_sertao = contador_end_sertao - 1

    #bom jesus
     elif ("bom jesus" in informacao) and (contador_end_bom_jesus == 0):
         acumulador = acumulador + "{"
         contador_end_bom_jesus = contador_end_bom_jesus + 1
     elif ("bom jesus" in informacao) and (contador_end_bom_jesus == 1):
         acumulador = acumulador + "}"
         contador_end_bom_jesus = contador_end_bom_jesus - 1

    #identidade:
    #identidade; tem que ter "jesus" "isaias" ou "moises" : resulta em parenteses

    #jesus
     elif ("jesus" in informacao) and (contador_nome_jesus == 0):
         acumulador = acumulador + "("
         contador_nome_jesus = contador_nome_jesus + 1
     elif ("jesus" in informacao) and (contador_nome_jesus == 1): #
         acumulador = acumulador + ")"
         contador_nome_jesus = contador_nome_jesus - 1 # pra zerar o contador do nome jesus e ser possivel repetir o processo quantas vezes necessario

    #isaias
     elif ("isaias" in informacao) and (contador_nome_isaias == 0):
         acumulador = acumulador + "("
         contador_nome_isaias = contador_nome_isaias + 1
     elif ("isaias" in informacao) and (contador_nome_isaias == 1):
         acumulador = acumulador + ")"
         contador_nome_isaias = contador_nome_isaias - 1

    #moises
     elif ("moises" in informacao) and (contador_nome_moises == 0):
         acumulador = acumulador + "("
         contador_nome_moises = contador_nome_moises + 1
     elif ("moises" in informacao) and (contador_nome_moises == 1):
         acumulador = acumulador + ")"
         contador_nome_moises = contador_nome_moises - 1

    

    #lembranca:
    #lembranca; se nenhum dos acima : resulta em colchetes []

     elif ("jesus" not in informacao) and ("isaias" not in informacao) and ("moises" not in informacao) and ("sertao" not in informacao) and ("bom jesus" not in informacao) and (contador_lembranca == 0):
         acumulador = acumulador + "["
         contador_lembranca = contador_lembranca + 1
     elif ("jesus" not in informacao) and ("isaias" not in informacao) and ("moises" not in informacao) and ("sertao" not in informacao) and ("bom jesus" not in informacao) and (contador_lembranca == 1):
         acumulador = acumulador + "]"
         contador_lembranca = contador_lembranca - 1
    
    #yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy

     #ver se recebeu informacao
    if acumulador == "":
        print ("Ô cidadezinha morta, Josué. Ninguém abriu a boca pra dar um pio do teu pai. Dobra essa mesa que aqui a gente só gastou saliva à toa.")

    else:
     #algoritimo pra verificar o acumulador hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
     pilha = "" #criacao da pilha que vai usar
     g = len(acumulador) % 2 == 0 #verifica logo se é par, se nn for... nem comeca o algoritimo
     tem_par = False #fechou identidade?
     tem_col = False #fechou endereco?
     tem_cha = False #fechou lembranca?

     if g:
      for simbolo in acumulador: #percorrer a variavel com os simbolos
        if simbolo == "(" or simbolo == "[" or simbolo == "{": #se for de abertura empilha
            pilha = pilha + simbolo
        else:
            if pilha == "": #se nn comecou com um de abertura é falso. nem e possivel isso kkkkkk   
                g = False
            else:
                ultimo = "" #vai ser o simbolo de abertura que acabou de ser empilhado
                nova_pilha = "" #CRIACAO DA NOVA PILHA SEM OQ EMPILHOU 
                 
                tamanho = 0 
                for c in pilha: #for so pra contar quantos simbolos tem na nova pilha
                    tamanho = tamanho + 1
                
                cont = 1 #pra saber em que posicao ta
                for c in pilha:
                    if cont == tamanho: #chegou no ultimo?
                        ultimo = c #entao e o topo do empilamento
                    else:
                        nova_pilha = nova_pilha + c #copia tudo igual da antiga variavel menos oq acabou de empilhar
                    cont = cont + 1
                
                #se tiver achado o par
                if simbolo == ")" and ultimo == "(": #se fechou com o simbolo que ta guardado no ultimo
                    pilha = nova_pilha
                    tem_par = True #ja confirma que conseguiu fechar identidade 
                elif simbolo == "]" and ultimo == "[":#se fechou com o simbolo que ta guardado no ultimo
                    pilha = nova_pilha
                    tem_col = True #ja confirma que conseguiu fechar endereco
                elif simbolo == "}" and ultimo == "{":#se fechou com o simbolo que ta guardado no ultimo
                    pilha = nova_pilha
                    tem_cha = True #ja confirma que conseguiu fechar a lembranca
                else:
                    g = False

     if pilha != "" or not (tem_par and tem_col and tem_cha): #se sobrou coisa na pilha ouuuuu se nao fechou as pistas: é invalido
        g = False

    #hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
     if g == True:
       print ("A história bateu, Josué. O povo falou a mesma coisa. Pega tuas coisas que a gente achou o caminho do teu pai.")
       print ("------------------------------------------------------------")
       print("✅ Pistas confirmadas. Josué encontrou os irmãos e uma carta de seu pai.")
       print ("A missão de Dora terminou. Pela janela do ônibus, ela escreve para o menino que deixou para trás:")
       print("✉️ Dora: 'Você tem razão. Seu pai ainda vai aparecer e, com certeza, ele é tudo aquilo que você diz que ele é.'")
       print("✉️ Dora: 'Quando você estiver cruzando as estradas no seu caminhão enorme, espero que você lembre que fui eu a primeira pessoa a te fazer botar a mão no volante.'")
       print("✉️ Dora: 'No dia que você quiser lembrar de mim, dá uma olhada no retratinho que a gente tirou junto... Tenho medo que um dia você também me esqueça. Tenho saudade de tudo.'")

     elif (g == False) and (k != quantidade_cidades - 1):
       print ("Essa conversa tá toda torta, um fala uma coisa, outro fala outra. Vamos embora, menino, a busca continua.")
    
     elif (g == False) and (k == quantidade_cidades - 1):
        print("Não achamos eles nessas cidades, Dona Dora... Mas amanhã a gente bota a mesinha de novo, né? O Brasil é grande, uma hora a gente encontra.")
    
