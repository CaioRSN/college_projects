#regular show problem XD

#variaveis dos ingredientes
carne_misteriosa = float(input (""))
queijo_radioativo = float(input (""))
molho_especial = float(input (""))

#condicao sobre quantidade de ingredientes
if carne_misteriosa <= 0 or queijo_radioativo <=0 or molho_especial <=0 :
    print ("Vocês destruíram o parque! ESTÃO DESPEDIDOS!")
elif carne_misteriosa == queijo_radioativo == molho_especial:
     print ("A receita não explodiu!")
     print ("Todas as medidas são iguais. Vocês criaram o Hambúrguer Supremo do Caos!")
     print ("OOOOOOOH! Mandaram bem, caras!")
elif carne_misteriosa > queijo_radioativo and carne_misteriosa > molho_especial:
     print ("A receita não explodiu!")
     print("Havia muita carne! O Musculoso vai adorar esse Bifão de Dinossauro!")
     print ("OOOOOOOH! Mandaram bem, caras!")
elif queijo_radioativo > carne_misteriosa and queijo_radioativo > molho_especial:
     print ("A receita não explodiu!")
     print ("Tem queijo pra todo lado! Criamos uma Lasanha Dimensional!")
     print ("OOOOOOOH! Mandaram bem, caras!")
elif molho_especial > carne_misteriosa and molho_especial > queijo_radioativo:
     print ("A receita não explodiu!")
     print ("Panela cheia de molho e sorriso no rosto, criamos o Strogonoff da Paz!")
     print ("OOOOOOOH! Mandaram bem, caras!")
elif carne_misteriosa == queijo_radioativo or carne_misteriosa == molho_especial or queijo_radioativo == molho_especial:
    print ("Tá tudo girando! Acabamos de criar um Buraco Negro Culinário!")
    print ("OOOOOOOH! Mandaram bem, caras!")