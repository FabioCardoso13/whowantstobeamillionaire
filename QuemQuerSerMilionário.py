import random


class Jogo:
    def __init__(self):
        self.questoes_faceis = {
            1: {
                "pergunta": "Como é conhecido o disco compacto?",
                "respostas": {"a": "CD", "b": "COD", "c": "CDIS", "d": "COMPD"},
                "resposta_certa": "a"
            },
            2: {
                "pergunta": "Na alimentação vegetariana, qual destes alimentos não é consumido?",
                "respostas": {"a": "Carne", "b": "Lentilhas", "c": "Bolo", "d": "Fruta"},
                "resposta_certa": "a"
            },
            3: {
                "pergunta": "Qual destes países não faz parte da União Europeia?",
                "respostas": {"a": "Suíça", "b": "Grécia", "c": "França", "d": "Espanha"},
                "resposta_certa": "a"
            },
            4: {
                "pergunta": "Qual destes não é um tipo de fonte de energia renovável?",
                "respostas": {"a": "Petróleo", "b": "Eólica", "c": "Solar", "d": "Geotérmica"},
                "resposta_certa": "a"
            },
            5: {
                "pergunta": "Qual destes é um tipo de gás utilizado nos refrigerantes?",
                "respostas": {"a": "Nitrogênio", "b": "Oxigênio", "c": "Cloro", "d": "Dióxido de carbono"},
                "resposta_certa": "d"
            },
            6: {
                "pergunta": "Onde é que nasce o Rio Amazonas?",
                "respostas": {"a": "Angola", "b": "Bolívia", "c": "Brasil", "d": "Peru"},
                "resposta_certa": "c"
            },
            7: {
                "pergunta": "Qual destes é um tipo de planta medicinal?",
                "respostas": {"a": "Margarida", "b": "Violeta", "c": "Aloe vera", "d": "Rosas"},
                "resposta_certa": "c"
            },
            8: {
                "pergunta": "Qual destes é um tipo de animal que vive na água?",
                "respostas": {"a": "Elefante", "b": "Girafa", "c": "Leão", "d": "Tubarão"},
                "resposta_certa": "d"
            },
            9: {
                "pergunta": "Qual é o maior continente do mundo?",
                "respostas": {"a": "África", "b": "América", "c": "Europa", "d": "Ásia"},
                "resposta_certa": "d"
            },
            10: {
                "pergunta": "Qual é o animal mais rápido do mundo?",
                "respostas": {"a": "Elefante", "b": "Golfinho", "c": "Leão", "d": "Puma"},
                "resposta_certa": "d"
            }
        }
        self.questoes_medias = {
            1: {
                "pergunta": """"Quem pintou a obra "Guernica"?""",
                "respostas": {"a": "Rembrandt", "b": "Leonardo da Vinci", "c": "Michelangelo", "d": "Pablo Picasso"},
                "resposta_certa": "d"
            },
            2: {
                "pergunta": "Qual é a capital do Uruguai?",
                "respostas": {"a": "São Paulo", "b": "Montevidéu", "c": "Buenos Aires", "d": "Assunção"},
                "resposta_certa": "b"
            },
            3: {
                "pergunta": "Qual é o maior lago do mundo?",
                "respostas": {"a": "Lago Baikal, Rússia", "b": "Lago Superior, Canadá",
                              "c": "Lago Michigan, Estados Unidos", "d": "Lago Victoria, Tanzânia"},
                "resposta_certa": "a"
            },
            4: {
                "pergunta": "Qual era a moeda utilizada na Grécia antiga?",
                "respostas": {"a": "Euro", "b": "Dólar", "c": "Libra", "d": "Dracma"},
                "resposta_certa": "d"
            },
            5: {
                "pergunta": "Qual o elemento químico mais abundante na crosta terrestre?",
                "respostas": {"a": "Carbono", "b": "Oxigênio", "c": "Nitrogênio", "d": "Hidrogênio"},
                "resposta_certa": "b"
            },
            6: {
                "pergunta": "Onde fica o vale do rio Indo?",
                "respostas": {"a": "Ásia", "b": "África", "c": "América", "d": "Europa"},
                "resposta_certa": "a"
            },
            7: {
                "pergunta": "O que é uma órbita?",
                "respostas": {"a": "Um movimento circular", "b": "Um movimento de rotação",
                              "c": "Um movimento retilíneo", "d": "Um movimento de translação"},
                "resposta_certa": "a"
            },
            8: {
                "pergunta": """Quem foi o pintor do quadro "Girassóis"?""",
                "respostas": {"a": "Claude Monet", "b": "Vincent Van Gogh", "c": "Salvador Dalí", "d": "Pablo Picasso"},
                "resposta_certa": "b"
            },
            9: {
                "pergunta": "Quais são as 3 cores primárias?",
                "respostas": {"a": "Preto, vermelho e amarelo", "b": "Azul, verde e vermelho",
                              "c": "Amarelo, preto e branco", "d": "Azul, amarelo e vermelho"},
                "resposta_certa": "d"
            },
            10: {
                "pergunta": "De que cor é o lema da ONU?",
                "respostas": {"a": "Vermelho", "b": "Cinza", "c": "Azul", "d": "Amarelo"},
                "resposta_certa": "c"
            }
        }
        self.questoes_dificeis = {
            1: {
                "pergunta": "Quem foi o primeiro homem a pisar na lua?",
                "respostas": {"a": "Neil Armstrong", "b": "Yuri Gagarin", "c": "John Glenn", "d": "Alan Shepard"},
                "resposta_certa": "a"
            },
            2: {
                "pergunta": "Qual é a maior estrela conhecida?",
                "respostas": {"a": "Antares", "b": "Betelgeuse", "c": "Canopus", "d": "Sirius"},
                "resposta_certa": "b"
            },
            3: {
                "pergunta": """De onde vem o termo "filosofia"?""",
                "respostas": {"a": "Latim", "b": "Grego", "c": "Francês", "d": "Alemão"},
                "resposta_certa": "b"
            },
            4: {
                "pergunta": "Qual é a maior montanha do mundo?",
                "respostas": {"a": "Monte Everest", "b": "Monte Kilimanjaro", "c": "Monte Fuji", "d": "Monte Elbrus"},
                "resposta_certa": "a"
            },
            5: {
                "pergunta": "O que é a Teoria da Relatividade?",
                "respostas": {"a": "Uma teoria científica que estuda as reações químicas",
                              "b": "Uma teoria científica que estuda as leis da gravidade",
                              "c": "Uma teoria científica que estuda as leis da eletricidade",
                              "d": "Uma teoria científica que estuda as leis do espaço-tempo"},
                "resposta_certa": "d"
            },
            6: {
                "pergunta": "Que criador foi responsável pelo desenvolvimento da teoria da evolução?",
                "respostas": {"a": "Charles Darwin", "b": "Stephen Hawking", "c": "Albert Einstein",
                              "d": "Isaac Newton"},
                "resposta_certa": "a"
            },
            7: {
                "pergunta": "Onde fica a Grande Barreira de Corais?",
                "respostas": {"a": "Mar Vermelho", "b": "Oceano Índico", "c": "Oceano Atlântico", "d": "Mar do Caribe"},
                "resposta_certa": "b"
            },
            8: {
                "pergunta": "Que elemento químico é usado na fabricação da maioria das telhas?",
                "respostas": {"a": "Ouro", "b": "Ferro", "c": "Alumínio", "d": "Prata"},
                "resposta_certa": "c"
            },
            9: {
                "pergunta": "Quem foi o primeiro rei da Inglaterra?",
                "respostas": {"a": "Eduardo II", "b": "Jorge III", "c": "Henrique VII", "d": "Athelstan"},
                "resposta_certa": "d"
            },
            10: {
                "pergunta": "O que é o Cinturão de Van Allen",
                "respostas": {"a": "Um cinturão de radiação emitida pelo Sol",
                              "b": "Um cinturão de asteróides no Sistema Solar",
                              "c": "Um cinturão de radiação formado por partículas carregadas ao redor da Terra",
                              "d": "Um cinturão de luz formado por estrelas ao redor da Terra"},
                "resposta_certa": "c"
            }
        }
        self.nome = ""
        self.usado50 = False
        self.usadoTelefone = False
        self.usadoAudiencia = False
        self.ajudaRepetir = True
        self.pontuacao = 0
        self.Lpontuacao = 0
        self.niveis = [100, 200, 500, 1000, 5000, 10000, 50000, 100000, 200000, 500000, 700000, 1000000]


    def iniciar(self):
        print('Bem vindo ao "QUEM QUER SER MILIONÁRIO"')
        self.descobrir_nome()
        self.mostra_regras()
        self.novo_jogo()


    def descobrir_nome(self):
        while not self.nome.isalpha():
            nome = input("Digite o seu nome: ")
            if not nome.isalpha():
                print("Nome inválido. Por favor, digite apenas caracteres alfabéticos.")
            self.nome = nome.title()


    def mostra_regras(self):
        print(f"""\n Vamos começar o jogo, {self.nome}. \n\
            Vão-lhe ser apresentadas 12 perguntas que estão ordenadas por dificuldade. \n\
            A dificuldade vai aumentando, de acordo com o número de respostas acertadas.\n\
            Cada pergunta vai ter 4 opções de escolha sendo apenas uma delas correta. \n\
            Todas as perguntas e respostas dadas vão ser guardadas num ficheiro.
            Se conseguir responder às 12 perguntas no final ganhará 1.000.000€! \n\n\
            Lembre-se, pode usar ajudas! Basta digitar "ajuda"\n""")


    def verificadorDeRepeticao(self, lista1, numero) -> list:
        enderecosEmQueSeEncontra = list()
        for endereco in range(0, len(lista1)):
            el = lista1[endereco]
            bEncontrei = el == numero
            if (bEncontrei):
                enderecosEmQueSeEncontra.append(endereco)
            # if
        # for
        return enderecosEmQueSeEncontra


    def novo_jogo(self):
        ficheiro = open("QuemQuerSerMilionario.txt", "w")
        corresposta = False
        while not corresposta:
            snresposta = input("Deseja continuar?[s/n]: ")
            if snresposta == 's' or snresposta == 'S':
                print("\nAqui vai a primeira pergunta!\n")
                corresposta = True

                listaDeNmrsFacil = []
                listaDeNmrsMedio = []
                listaDeNmrsDificil = []

                niveis = [100, 200, 500, 1000, 5000, 10000, 50000, 100000, 200000, 500000, 700000, 1000000]
                # nivel_medio = [5000, 10000, 50000, 100000]
                # nivel_dificil = [200000, 500000, 700000, 1000000]

                while True:
                    while self.pontuacao >= 0 and self.pontuacao < 3:
                        if len(listaDeNmrsFacil) > 9:
                            listaDeNmrsFacil.clear()
                        random_nmr = random.randint(1, 10)
                        resultadoDaVerificacao = self.verificadorDeRepeticao(listaDeNmrsFacil,
                                                                        random_nmr)  # VERIFICAR SE É REPETIDO
                        encontrei = len(resultadoDaVerificacao) > 0
                        if not encontrei:
                            listaDeNmrsFacil.append(random_nmr)
                            ficheiro.write(self.questoes_faceis[random_nmr]['pergunta'] + "\n")
                            print(f"{self.questoes_faceis[random_nmr]['pergunta']}")
                            for pk, pv in self.questoes_faceis[random_nmr]["respostas"].items():
                                print(f"{pk}) {pv}")
                            resposta_user = input("Resposta: ")

                            if resposta_user == self.questoes_faceis[random_nmr]['resposta_certa']:
                                ficheiro.write(resposta_user + "\n\n")
                                print("\nResposta correta!!!")
                                self.pontuacao += 1
                                Lpontuacao = niveis[self.pontuacao]
                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")

                            elif resposta_user == "ajuda" or resposta_user == "Ajuda":
                                self.ajudaRepetir = True
                                if self.usado50 == False and self.usadoTelefone == False and self.usadoAudiencia == False:
                                    while self.ajudaRepetir:
                                        ajudaResposta = input(
                                            "Digite o tipo de ajuda que deseja[50/telefone/audiencia]: ")
                                        if ajudaResposta == '50':
                                            if self.questoes_faceis[random_nmr]["resposta_certa"] == 'a':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_faceis[random_nmr]['respostas']['a']}")
                                                    print(f"b) {self.questoes_faceis[random_nmr]['respostas']['b']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"a) {self.questoes_faceis[random_nmr]['respostas']['a']}")
                                                    print(f"c) {self.questoes_faceis[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"a) {self.questoes_faceis[random_nmr]['respostas']['a']}")
                                                    print(f"d) {self.questoes_faceis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            elif self.questoes_faceis[random_nmr]["resposta_certa"] == 'b':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_faceis[random_nmr]['respostas']['a']}")
                                                    print(f"b) {self.questoes_faceis[random_nmr]['respostas']['b']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"b) {self.questoes_faceis[random_nmr]['respostas']['b']}")
                                                    print(f"c) {self.questoes_faceis[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"b) {self.questoes_faceis[random_nmr]['respostas']['b']}")
                                                    print(f"d) {self.questoes_faceis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            elif self.questoes_faceis[random_nmr]["resposta_certa"] == 'c':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_faceis[random_nmr]['respostas']['a']}")
                                                    print(f"c) {self.questoes_faceis[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"b) {self.questoes_faceis[random_nmr]['respostas']['b']}")
                                                    print(f"c) {self.questoes_faceis[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"c) {self.questoes_faceis[random_nmr]['respostas']['c']}")
                                                    print(f"d) {self.questoes_faceis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            elif self.questoes_faceis[random_nmr]["resposta_certa"] == 'd':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_faceis[random_nmr]['respostas']['a']}")
                                                    print(f"d) {self.questoes_faceis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"b) {self.questoes_faceis[random_nmr]['respostas']['b']}")
                                                    print(f"d) {self.questoes_faceis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"c) {self.questoes_faceis[random_nmr]['respostas']['c']}")
                                                    print(f"d) {self.questoes_faceis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            self.usado50 = True
                                            self.ajudaRepetir = False
                                        elif ajudaResposta == "telefone" or ajudaResposta == "Telefone":
                                            chamada = input("Digite o nome da pessoa a quem deseja ligar: ")
                                            print(
                                                f"Trrrim-trrrim!! {chamada.title()} diz que a resposta correta é a {self.questoes_faceis[random_nmr]['resposta_certa']})!")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                            self.usadoTelefone = True
                                            self.ajudaRepetir = False

                                        elif ajudaResposta == "audiência" or ajudaResposta == "audiencia" or ajudaResposta == "Audiência" or ajudaResposta == "Audiencia":
                                            print(
                                                f"A audiência diz que a resposta certa é a {self.questoes_faceis[random_nmr]['resposta_certa']})!")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                            self.usadoAudiencia = True
                                            self.ajudaRepetir = False

                                        else:
                                            print("Inválido.")
                                            self.ajudaRepetir = True

                                elif self.usado50 == False and self.usadoTelefone == False and self.usadoAudiencia == True:
                                    ajudaResposta = input("Digite o tipo de ajuda que deseja[50/telefone]: ")
                                    while self.ajudaRepetir:
                                        ajudaResposta = input("Digite o tipo de ajuda que deseja[50/telefone]: ")
                                        if ajudaResposta == '50':
                                            if self.questoes_faceis[random_nmr]["resposta_certa"] == 'a':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_faceis[random_nmr]['respostas']['a']}")
                                                    print(f"b) {self.questoes_faceis[random_nmr]['respostas']['b']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"a) {self.questoes_faceis[random_nmr]['respostas']['a']}")
                                                    print(f"c) {self.questoes_faceis[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"a) {self.questoes_faceis[random_nmr]['respostas']['a']}")
                                                    print(f"d) {self.questoes_faceis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            elif self.questoes_faceis[random_nmr]["resposta_certa"] == 'b':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_faceis[random_nmr]['respostas']['a']}")
                                                    print(f"b) {self.questoes_faceis[random_nmr]['respostas']['b']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"b) {self.questoes_faceis[random_nmr]['respostas']['b']}")
                                                    print(f"c) {self.questoes_faceis[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"b) {self.questoes_faceis[random_nmr]['respostas']['b']}")
                                                    print(f"d) {self.questoes_faceis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            elif self.questoes_faceis[random_nmr]["resposta_certa"] == 'c':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_faceis[random_nmr]['respostas']['a']}")
                                                    print(f"c) {self.questoes_faceis[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"b) {self.questoes_faceis[random_nmr]['respostas']['b']}")
                                                    print(f"c) {self.questoes_faceis[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"c) {self.questoes_faceis[random_nmr]['respostas']['c']}")
                                                    print(f"d) {self.questoes_faceis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            elif self.questoes_faceis[random_nmr]["resposta_certa"] == 'd':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_faceis[random_nmr]['respostas']['a']}")
                                                    print(f"d) {self.questoes_faceis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"b) {self.questoes_faceis[random_nmr]['respostas']['b']}")
                                                    print(f"d) {self.questoes_faceis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"c) {self.questoes_faceis[random_nmr]['respostas']['c']}")
                                                    print(f"d) {self.questoes_faceis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            self.usado50 = True
                                            self.ajudaRepetir = False
                                        elif ajudaResposta == "telefone" or ajudaResposta == "Telefone":
                                            chamada = input("Digite o nome da pessoa a quem deseja ligar: ")
                                            print(
                                                f"Trrrim-trrrim!! {chamada.title()} diz que a resposta correta é a {self.questoes_faceis[random_nmr]['resposta_certa']})!")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                            self.usadoTelefone = True
                                            self.ajudaRepetir = False

                                        else:
                                            print("Inválido.")
                                            self.ajudaRepetir = True

                                elif self.usado50 == False and self.usadoTelefone == True and self.usadoAudiencia == False:
                                    while self.ajudaRepetir:
                                        ajudaResposta = input("Digite o tipo de ajuda que deseja[50/audiencia]: ")
                                        if ajudaResposta == '50':
                                            if self.questoes_faceis[random_nmr]["resposta_certa"] == 'a':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_faceis[random_nmr]['respostas']['a']}")
                                                    print(f"b) {self.questoes_faceis[random_nmr]['respostas']['b']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"a) {self.questoes_faceis[random_nmr]['respostas']['a']}")
                                                    print(f"c) {self.questoes_faceis[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"a) {self.questoes_faceis[random_nmr]['respostas']['a']}")
                                                    print(f"d) {self.questoes_faceis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            elif self.questoes_faceis[random_nmr]["resposta_certa"] == 'b':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_faceis[random_nmr]['respostas']['a']}")
                                                    print(f"b) {self.questoes_faceis[random_nmr]['respostas']['b']}")
                                                    opcresposta = input("Resposta: ")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"b) {self.questoes_faceis[random_nmr]['respostas']['b']}")
                                                    print(f"c) {self.questoes_faceis[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"b) {self.questoes_faceis[random_nmr]['respostas']['b']}")
                                                    print(f"d) {self.questoes_faceis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            elif self.questoes_faceis[random_nmr]["resposta_certa"] == 'c':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_faceis[random_nmr]['respostas']['a']}")
                                                    print(f"c) {self.questoes_faceis[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"b) {self.questoes_faceis[random_nmr]['respostas']['b']}")
                                                    print(f"c) {self.questoes_faceis[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"c) {self.questoes_faceis[random_nmr]['respostas']['c']}")
                                                    print(f"d) {self.questoes_faceis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            elif self.questoes_faceis[random_nmr]["resposta_certa"] == 'd':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_faceis[random_nmr]['respostas']['a']}")
                                                    print(f"d) {self.questoes_faceis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"b) {self.questoes_faceis[random_nmr]['respostas']['b']}")
                                                    print(f"d) {self.questoes_faceis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"c) {self.questoes_faceis[random_nmr]['respostas']['c']}")
                                                    print(f"d) {self.questoes_faceis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            self.usado50 = True
                                            self.ajudaRepetir = False

                                        elif ajudaResposta == "audiência" or ajudaResposta == "audiencia" or ajudaResposta == "Audiência" or ajudaResposta == "Audiencia":
                                            print(
                                                f"A audiência diz que a resposta certa é a {self.questoes_faceis[random_nmr]['resposta_certa']})!")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                            self.usadoAudiencia = True
                                            self.ajudaRepetir = False

                                        else:
                                            print("Inválido.")
                                            self.ajudaRepetir = True

                                elif self.usado50 == False and self.usadoTelefone == True and self.usadoAudiencia == True:
                                    print("Foi usada a sua única ajuda. 50/50.\n")
                                    if self.questoes_faceis[random_nmr]["resposta_certa"] == 'a':
                                        rndnumber = random.randint(1, 3)
                                        if rndnumber == 1:
                                            print(f"a) {self.questoes_faceis[random_nmr]['respostas']['a']}")
                                            print(f"b) {self.questoes_faceis[random_nmr]['respostas']['b']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                        elif rndnumber == 2:
                                            print(f"a) {self.questoes_faceis[random_nmr]['respostas']['a']}")
                                            print(f"c) {self.questoes_faceis[random_nmr]['respostas']['c']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                        elif rndnumber == 3:
                                            print(f"a) {self.questoes_faceis[random_nmr]['respostas']['a']}")
                                            print(f"d) {self.questoes_faceis[random_nmr]['respostas']['d']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                    elif self.questoes_faceis[random_nmr]["resposta_certa"] == 'b':
                                        rndnumber = random.randint(1, 3)
                                        if rndnumber == 1:
                                            print(f"a) {self.questoes_faceis[random_nmr]['respostas']['a']}")
                                            print(f"b) {self.questoes_faceis[random_nmr]['respostas']['b']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                        elif rndnumber == 2:
                                            print(f"b) {self.questoes_faceis[random_nmr]['respostas']['b']}")
                                            print(f"c) {self.questoes_faceis[random_nmr]['respostas']['c']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                        elif rndnumber == 3:
                                            print(f"b) {self.questoes_faceis[random_nmr]['respostas']['b']}")
                                            print(f"d) {self.questoes_faceis[random_nmr]['respostas']['d']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                    elif self.questoes_faceis[random_nmr]["resposta_certa"] == 'c':
                                        rndnumber = random.randint(1, 3)
                                        if rndnumber == 1:
                                            print(f"a) {self.questoes_faceis[random_nmr]['respostas']['a']}")
                                            print(f"c) {self.questoes_faceis[random_nmr]['respostas']['c']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                        elif rndnumber == 2:
                                            print(f"b) {self.questoes_faceis[random_nmr]['respostas']['b']}")
                                            print(f"c) {self.questoes_faceis[random_nmr]['respostas']['c']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                        elif rndnumber == 3:
                                            print(f"c) {self.questoes_faceis[random_nmr]['respostas']['c']}")
                                            print(f"d) {self.questoes_faceis[random_nmr]['respostas']['d']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                    elif self.questoes_faceis[random_nmr]["resposta_certa"] == 'd':
                                        rndnumber = random.randint(1, 3)
                                        if rndnumber == 1:
                                            print(f"a) {self.questoes_faceis[random_nmr]['respostas']['a']}")
                                            print(f"d) {self.questoes_faceis[random_nmr]['respostas']['d']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                        elif rndnumber == 2:
                                            print(f"b) {self.questoes_faceis[random_nmr]['respostas']['b']}")
                                            print(f"d) {self.questoes_faceis[random_nmr]['respostas']['d']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                        elif rndnumber == 3:
                                            print(f"c) {self.questoes_faceis[random_nmr]['respostas']['c']}")
                                            print(f"d) {self.questoes_faceis[random_nmr]['respostas']['d']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                    self.usado50 = True

                                elif self.usado50 == True and self.usadoTelefone == False and self.usadoAudiencia == False:
                                    while self.ajudaRepetir:
                                        ajudaResposta = input("Digite o tipo de ajuda que deseja[telefone/audiencia]: ")
                                        if ajudaResposta == "telefone" or ajudaResposta == "Telefone":
                                            chamada = input("Digite o nome da pessoa a quem deseja ligar: ")
                                            print(
                                                f"Trrrim-trrrim!! {chamada.title()} diz que a resposta correta é a {self.questoes_faceis[random_nmr]['resposta_certa']})!")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                            self.usadoTelefone = True
                                            self.ajudaRepetir = False

                                        elif ajudaResposta == "audiência" or ajudaResposta == "audiencia" or ajudaResposta == "Audiência" or ajudaResposta == "Audiencia":
                                            print(
                                                f"A audiência diz que a resposta certa é a {self.questoes_faceis[random_nmr]['resposta_certa']})!")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                            self.usadoAudiencia = True
                                            self.ajudaRepetir = False

                                        else:
                                            print("Inválido.")
                                            self.ajudaRepetir = True

                                elif self.usado50 == True and self.usadoTelefone == False and self.usadoAudiencia == True:
                                    print("Foi usada a sua única ajuda. Telefone.")
                                    chamada = input("Digite o nome da pessoa a quem deseja ligar: ")
                                    print(
                                        f"Trrrim-trrrim!! {chamada.title()} diz que a resposta correta é a {self.questoes_faceis[random_nmr]['resposta_certa']})!")
                                    opcresposta = input("Resposta: ")
                                    ficheiro.write(opcresposta + "\n\n")
                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                        print("\nResposta correta!!!")
                                        self.pontuacao += 1
                                        Lpontuacao = niveis[self.pontuacao]
                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                    else:
                                        print("\nResposta errada!")
                                        print(f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                        print("PERDEU!")
                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                        if recomecar == 's':
                                            self.pontuacao = 0
                                            print("\n")
                                            break
                                        else:
                                            quit()
                                    self.usadoTelefone = True

                                elif self.usado50 == True and self.usadoTelefone == True and self.usadoAudiencia == False:
                                    print("Foi usada a sua única ajuda. Audiência.\n")
                                    print(
                                        f"A audiência diz que a resposta certa é a {self.questoes_faceis[random_nmr]['resposta_certa']})!")
                                    opcresposta = input("Resposta: ")
                                    ficheiro.write(opcresposta + "\n\n")
                                    if opcresposta == self.questoes_faceis[random_nmr]['resposta_certa']:
                                        print("\nResposta correta!!!")
                                        self.pontuacao += 1
                                        Lpontuacao = niveis[self.pontuacao]
                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                    else:
                                        print("\nResposta errada!")
                                        print(f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                        print("PERDEU!")
                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                        if recomecar == 's':
                                            self.pontuacao = 0
                                            print("\n")
                                            break
                                        else:
                                            quit()
                                    self.usadoAudiencia = True

                                elif self.usado50 == True and self.usadoTelefone == True and self.usadoAudiencia == True:
                                    print("Já não possui ajudas!")
                                    opcresposta = input("Resposta: ")
                                    ficheiro.write(opcresposta + "\n\n")
                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                        print("\nResposta correta!!!")
                                        self.pontuacao += 1
                                        Lpontuacao = niveis[self.pontuacao]
                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                    else:
                                        print("\nResposta errada!")
                                        print(f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                        print("PERDEU!")
                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                        if recomecar == 's':
                                            self.pontuacao = 0
                                            print("\n")
                                            break
                                        else:
                                            quit()

                            else:
                                ficheiro.write(resposta_user + "\n\n")
                                print("\nResposta errada!")
                                print(f"Resposta correta: {self.questoes_faceis[random_nmr]['resposta_certa']})\n")
                                print("PERDEU!")
                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                if recomecar == 's':
                                    self.pontuacao = 0
                                    print("\n")
                                    break
                                else:
                                    quit()

                            if self.pontuacao >= 3:
                                break

                    # MEDIO
                    while self.pontuacao >= 3 and self.pontuacao < 7:
                        if len(listaDeNmrsMedio) > 9:
                            listaDeNmrsMedio.clear()
                        random_nmr = random.randint(1, 10)
                        resultadoDaVerificacao = self.verificadorDeRepeticao(listaDeNmrsMedio,
                                                                        random_nmr)  # VERIFICAR SE É REPETIDO
                        encontrei = len(resultadoDaVerificacao) > 0
                        if not encontrei:
                            listaDeNmrsMedio.append(random_nmr)
                            ficheiro.write(self.questoes_medias[random_nmr]['pergunta'] + "\n")
                            print(f"{self.questoes_medias[random_nmr]['pergunta']}")
                            for pk, pv in self.questoes_medias[random_nmr]["respostas"].items():
                                print(f"{pk}) {pv}")
                            resposta_user = input("Resposta: ")

                            if resposta_user == self.questoes_medias[random_nmr]['resposta_certa']:
                                ficheiro.write(resposta_user + "\n\n")
                                print("\nResposta correta!!!")
                                self.pontuacao += 1
                                Lpontuacao = niveis[self.pontuacao]
                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")

                            elif resposta_user == "ajuda" or resposta_user == "Ajuda":
                                self.ajudaRepetir = True
                                if self.usado50 == False and self.usadoTelefone == False and self.usadoAudiencia == False:
                                    while self.ajudaRepetir:
                                        ajudaResposta = input(
                                            "Digite o tipo de ajuda que deseja[50/telefone/audiencia]: ")
                                        if ajudaResposta == '50':
                                            if self.questoes_medias[random_nmr]["resposta_certa"] == 'a':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_medias[random_nmr]['respostas']['a']}")
                                                    print(f"b) {self.questoes_medias[random_nmr]['respostas']['b']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"a) {self.questoes_medias[random_nmr]['respostas']['a']}")
                                                    print(f"c) {self.questoes_medias[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"a) {self.questoes_medias[random_nmr]['respostas']['a']}")
                                                    print(f"d) {self.questoes_medias[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            elif self.questoes_medias[random_nmr]["resposta_certa"] == 'b':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_medias[random_nmr]['respostas']['a']}")
                                                    print(f"b) {self.questoes_medias[random_nmr]['respostas']['b']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"b) {self.questoes_medias[random_nmr]['respostas']['b']}")
                                                    print(f"c) {self.questoes_medias[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"b) {self.questoes_medias[random_nmr]['respostas']['b']}")
                                                    print(f"d) {self.questoes_medias[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            elif self.questoes_medias[random_nmr]["resposta_certa"] == 'c':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_medias[random_nmr]['respostas']['a']}")
                                                    print(f"c) {self.questoes_medias[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"b) {self.questoes_medias[random_nmr]['respostas']['b']}")
                                                    print(f"c) {self.questoes_medias[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"c) {self.questoes_medias[random_nmr]['respostas']['c']}")
                                                    print(f"d) {self.questoes_medias[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            elif self.questoes_medias[random_nmr]["resposta_certa"] == 'd':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_medias[random_nmr]['respostas']['a']}")
                                                    print(f"d) {self.questoes_medias[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"b) {self.questoes_medias[random_nmr]['respostas']['b']}")
                                                    print(f"d) {self.questoes_medias[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"c) {self.questoes_medias[random_nmr]['respostas']['c']}")
                                                    print(f"d) {self.questoes_medias[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            self.usado50 = True
                                            self.ajudaRepetir = False
                                        elif ajudaResposta == "telefone" or ajudaResposta == "Telefone":
                                            chamada = input("Digite o nome da pessoa a quem deseja ligar: ")
                                            print(
                                                f"Trrrim-trrrim!! {chamada.title()} diz que a resposta correta é a {self.questoes_medias[random_nmr]['resposta_certa']})!")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                            self.usadoTelefone = True
                                            self.ajudaRepetir = False

                                        elif ajudaResposta == "audiência" or ajudaResposta == "audiencia" or ajudaResposta == "Audiência" or ajudaResposta == "Audiencia":
                                            print(
                                                f"A audiência diz que a resposta certa é a {self.questoes_medias[random_nmr]['resposta_certa']})!")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                            self.usadoAudiencia = True
                                            self.ajudaRepetir = False

                                        else:
                                            print("Inválido.")
                                            self.ajudaRepetir = True

                                elif self.usado50 == False and self.usadoTelefone == False and self.usadoAudiencia == True:
                                    ajudaResposta = input("Digite o tipo de ajuda que deseja[50/telefone]: ")
                                    while self.ajudaRepetir:
                                        ajudaResposta = input("Digite o tipo de ajuda que deseja[50/telefone]: ")
                                        if ajudaResposta == '50':
                                            if self.questoes_medias[random_nmr]["resposta_certa"] == 'a':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_medias[random_nmr]['respostas']['a']}")
                                                    print(f"b) {self.questoes_medias[random_nmr]['respostas']['b']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"a) {self.questoes_medias[random_nmr]['respostas']['a']}")
                                                    print(f"c) {self.questoes_medias[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"a) {self.questoes_medias[random_nmr]['respostas']['a']}")
                                                    print(f"d) {self.questoes_medias[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            elif self.questoes_medias[random_nmr]["resposta_certa"] == 'b':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_medias[random_nmr]['respostas']['a']}")
                                                    print(f"b) {self.questoes_medias[random_nmr]['respostas']['b']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"b) {self.questoes_medias[random_nmr]['respostas']['b']}")
                                                    print(f"c) {self.questoes_medias[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"b) {self.questoes_medias[random_nmr]['respostas']['b']}")
                                                    print(f"d) {self.questoes_medias[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            elif self.questoes_medias[random_nmr]["resposta_certa"] == 'c':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_medias[random_nmr]['respostas']['a']}")
                                                    print(f"c) {self.questoes_medias[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"b) {self.questoes_medias[random_nmr]['respostas']['b']}")
                                                    print(f"c) {self.questoes_medias[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"c) {self.questoes_medias[random_nmr]['respostas']['c']}")
                                                    print(f"d) {self.questoes_medias[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            elif self.questoes_medias[random_nmr]["resposta_certa"] == 'd':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_medias[random_nmr]['respostas']['a']}")
                                                    print(f"d) {self.questoes_medias[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"b) {self.questoes_medias[random_nmr]['respostas']['b']}")
                                                    print(f"d) {self.questoes_medias[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"c) {self.questoes_medias[random_nmr]['respostas']['c']}")
                                                    print(f"d) {self.questoes_medias[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            self.usado50 = True
                                            self.ajudaRepetir = False
                                        elif ajudaResposta == "telefone" or ajudaResposta == "Telefone":
                                            chamada = input("Digite o nome da pessoa a quem deseja ligar: ")
                                            print(
                                                f"Trrrim-trrrim!! {chamada.title()} diz que a resposta correta é a {self.questoes_medias[random_nmr]['resposta_certa']})!")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                            self.usadoTelefone = True
                                            self.ajudaRepetir = False

                                        else:
                                            print("Inválido.")
                                            self.ajudaRepetir = True

                                elif self.usado50 == False and self.usadoTelefone == True and self.usadoAudiencia == False:
                                    while self.ajudaRepetir:
                                        ajudaResposta = input("Digite o tipo de ajuda que deseja[50/audiencia]: ")
                                        if ajudaResposta == '50':
                                            if self.questoes_medias[random_nmr]["resposta_certa"] == 'a':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_medias[random_nmr]['respostas']['a']}")
                                                    print(f"b) {self.questoes_medias[random_nmr]['respostas']['b']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"a) {self.questoes_medias[random_nmr]['respostas']['a']}")
                                                    print(f"c) {self.questoes_medias[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"a) {self.questoes_medias[random_nmr]['respostas']['a']}")
                                                    print(f"d) {self.questoes_medias[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            elif self.questoes_medias[random_nmr]["resposta_certa"] == 'b':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_medias[random_nmr]['respostas']['a']}")
                                                    print(f"b) {self.questoes_medias[random_nmr]['respostas']['b']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"b) {self.questoes_medias[random_nmr]['respostas']['b']}")
                                                    print(f"c) {self.questoes_medias[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"b) {self.questoes_medias[random_nmr]['respostas']['b']}")
                                                    print(f"d) {self.questoes_medias[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            elif self.questoes_medias[random_nmr]["resposta_certa"] == 'c':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_medias[random_nmr]['respostas']['a']}")
                                                    print(f"c) {self.questoes_medias[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"b) {self.questoes_medias[random_nmr]['respostas']['b']}")
                                                    print(f"c) {self.questoes_medias[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"c) {self.questoes_medias[random_nmr]['respostas']['c']}")
                                                    print(f"d) {self.questoes_medias[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            elif self.questoes_medias[random_nmr]["resposta_certa"] == 'd':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_medias[random_nmr]['respostas']['a']}")
                                                    print(f"d) {self.questoes_medias[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"b) {self.questoes_medias[random_nmr]['respostas']['b']}")
                                                    print(f"d) {self.questoes_medias[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"c) {self.questoes_medias[random_nmr]['respostas']['c']}")
                                                    print(f"d) {self.questoes_medias[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            self.usado50 = True
                                            self.ajudaRepetir = False

                                        elif ajudaResposta == "audiência" or ajudaResposta == "audiencia" or ajudaResposta == "Audiência" or ajudaResposta == "Audiencia":
                                            print(
                                                f"A audiência diz que a resposta certa é a {self.questoes_medias[random_nmr]['resposta_certa']})!")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                            self.usadoAudiencia = True
                                            self.ajudaRepetir = False

                                        else:
                                            print("Inválido.")
                                            self.ajudaRepetir = True

                                elif self.usado50 == False and self.usadoTelefone == True and self.usadoAudiencia == True:
                                    print("Foi usada a sua única ajuda. 50/50.\n")
                                    if self.questoes_medias[random_nmr]["resposta_certa"] == 'a':
                                        rndnumber = random.randint(1, 3)
                                        if rndnumber == 1:
                                            print(f"a) {self.questoes_medias[random_nmr]['respostas']['a']}")
                                            print(f"b) {self.questoes_medias[random_nmr]['respostas']['b']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                        elif rndnumber == 2:
                                            print(f"a) {self.questoes_medias[random_nmr]['respostas']['a']}")
                                            print(f"c) {self.questoes_medias[random_nmr]['respostas']['c']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                        elif rndnumber == 3:
                                            print(f"a) {self.questoes_medias[random_nmr]['respostas']['a']}")
                                            print(f"d) {self.questoes_medias[random_nmr]['respostas']['d']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                    elif self.questoes_medias[random_nmr]["resposta_certa"] == 'b':
                                        rndnumber = random.randint(1, 3)
                                        if rndnumber == 1:
                                            print(f"a) {self.questoes_medias[random_nmr]['respostas']['a']}")
                                            print(f"b) {self.questoes_medias[random_nmr]['respostas']['b']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                        elif rndnumber == 2:
                                            print(f"b) {self.questoes_medias[random_nmr]['respostas']['b']}")
                                            print(f"c) {self.questoes_medias[random_nmr]['respostas']['c']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                        elif rndnumber == 3:
                                            print(f"b) {self.questoes_medias[random_nmr]['respostas']['b']}")
                                            print(f"d) {self.questoes_medias[random_nmr]['respostas']['d']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                    elif self.questoes_medias[random_nmr]["resposta_certa"] == 'c':
                                        rndnumber = random.randint(1, 3)
                                        if rndnumber == 1:
                                            print(f"a) {self.questoes_medias[random_nmr]['respostas']['a']}")
                                            print(f"c) {self.questoes_medias[random_nmr]['respostas']['c']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                        elif rndnumber == 2:
                                            print(f"b) {self.questoes_medias[random_nmr]['respostas']['b']}")
                                            print(f"c) {self.questoes_medias[random_nmr]['respostas']['c']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                        elif rndnumber == 3:
                                            print(f"c) {self.questoes_medias[random_nmr]['respostas']['c']}")
                                            print(f"d) {self.questoes_medias[random_nmr]['respostas']['d']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                    elif self.questoes_medias[random_nmr]["resposta_certa"] == 'd':
                                        rndnumber = random.randint(1, 3)
                                        if rndnumber == 1:
                                            print(f"a) {self.questoes_medias[random_nmr]['respostas']['a']}")
                                            print(f"d) {self.questoes_medias[random_nmr]['respostas']['d']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                        elif rndnumber == 2:
                                            print(f"b) {self.questoes_medias[random_nmr]['respostas']['b']}")
                                            print(f"d) {self.questoes_medias[random_nmr]['respostas']['d']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                        elif rndnumber == 3:
                                            print(f"c) {self.questoes_medias[random_nmr]['respostas']['c']}")
                                            print(f"d) {self.questoes_medias[random_nmr]['respostas']['d']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                    self.usado50 = True

                                elif self.usado50 == True and self.usadoTelefone == False and self.usadoAudiencia == False:
                                    while self.ajudaRepetir:
                                        ajudaResposta = input("Digite o tipo de ajuda que deseja[telefone/audiencia]: ")
                                        if ajudaResposta == "telefone" or ajudaResposta == "Telefone":
                                            chamada = input("Digite o nome da pessoa a quem deseja ligar: ")
                                            print(
                                                f"Trrrim-trrrim!! {chamada.title()} diz que a resposta correta é a {self.questoes_medias[random_nmr]['resposta_certa']})!")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                            self.usadoTelefone = True
                                            self.ajudaRepetir = False

                                        elif ajudaResposta == "audiência" or ajudaResposta == "audiencia" or ajudaResposta == "Audiência" or ajudaResposta == "Audiencia":
                                            print(
                                                f"A audiência diz que a resposta certa é a {self.questoes_medias[random_nmr]['resposta_certa']})!")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                            self.usadoAudiencia = True
                                            self.ajudaRepetir = False

                                        else:
                                            print("Inválido.")
                                            self.ajudaRepetir = True

                                elif self.usado50 == True and self.usadoTelefone == False and self.usadoAudiencia == True:
                                    print("Foi usada a sua única ajuda. Telefone.")
                                    chamada = input("Digite o nome da pessoa a quem deseja ligar: ")
                                    print(
                                        f"Trrrim-trrrim!! {chamada.title()} diz que a resposta correta é a {self.questoes_medias[random_nmr]['resposta_certa']})!")
                                    opcresposta = input("Resposta: ")
                                    ficheiro.write(opcresposta + "\n\n")
                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                        print("\nResposta correta!!!")
                                        self.pontuacao += 1
                                        Lpontuacao = niveis[self.pontuacao]
                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                    else:
                                        print("\nResposta errada!")
                                        print(f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                        print("PERDEU!")
                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                        if recomecar == 's':
                                            self.pontuacao = 0
                                            print("\n")
                                            break
                                        else:
                                            quit()
                                    self.usadoTelefone = True

                                elif self.usado50 == True and self.usadoTelefone == True and self.usadoAudiencia == False:
                                    print("Foi usada a sua única ajuda. Audiência.\n")
                                    print(
                                        f"A audiência diz que a resposta certa é a {self.questoes_medias[random_nmr]['resposta_certa']})!")
                                    opcresposta = input("Resposta: ")
                                    ficheiro.write(opcresposta + "\n\n")
                                    if opcresposta == self.questoes_medias[random_nmr]['resposta_certa']:
                                        print("\nResposta correta!!!")
                                        self.pontuacao += 1
                                        Lpontuacao = niveis[self.pontuacao]
                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                    else:
                                        print("\nResposta errada!")
                                        print(f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                        print("PERDEU!")
                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                        if recomecar == 's':
                                            self.pontuacao = 0
                                            print("\n")
                                            break
                                        else:
                                            quit()
                                    self.usadoAudiencia = True

                                elif self.usado50 == True and self.usadoTelefone == True and self.usadoAudiencia == True:
                                    print("Já não possui ajudas!\n")
                                    opcresposta = input("Resposta: ")
                                    ficheiro.write(opcresposta + "\n\n")
                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                        print("\nResposta correta!!!")
                                        self.pontuacao += 1
                                        Lpontuacao = niveis[self.pontuacao]
                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                    else:
                                        print("\nResposta errada!")
                                        print(f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                        print("PERDEU!")
                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                        if recomecar == 's':
                                            self.pontuacao = 0
                                            print("\n")
                                            break
                                        else:
                                            quit()

                            else:
                                ficheiro.write(resposta_user + "\n\n")
                                print("\nResposta errada!")
                                print(f"Resposta correta: {self.questoes_medias[random_nmr]['resposta_certa']})\n")
                                print("PERDEU!")
                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                if recomecar == 's':
                                    self.pontuacao = 0
                                    print("\n")
                                    break
                                else:
                                    quit()

                            if self.pontuacao >= 7:
                                break

                    # DIFICIL
                    while self.pontuacao >= 7 and self.pontuacao <= 11:
                        if len(listaDeNmrsDificil) > 9:
                            listaDeNmrsDificil.clear()
                        random_nmr = random.randint(1, 10)
                        resultadoDaVerificacao = self.verificadorDeRepeticao(listaDeNmrsDificil,
                                                                        random_nmr)  # VERIFICAR SE É REPETIDO
                        encontrei = len(resultadoDaVerificacao) > 0
                        if not encontrei:
                            listaDeNmrsDificil.append(random_nmr)
                            ficheiro.write(self.questoes_dificeis[random_nmr]['pergunta'] + "\n")
                            print(f"{self.questoes_dificeis[random_nmr]['pergunta']}")
                            for pk, pv in self.questoes_dificeis[random_nmr]["respostas"].items():
                                print(f"{pk}) {pv}")
                            resposta_user = input("Resposta: ")

                            if resposta_user == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                ficheiro.write(resposta_user + "\n\n")
                                print("\nResposta correta!!!")
                                if self.pontuacao == 11:
                                    print(f"\nParabéns {self.nome}!!! Ganhou 1,000,000€!!!")
                                    recomecar2 = input("\n\nDeseja jogar novamente?[s/n]: ")
                                    if recomecar2 == 's':
                                        self.pontuacao = 0
                                        print("\n")
                                        break
                                    else:
                                        quit()

                                self.pontuacao += 1
                                if self.pontuacao <= 11:
                                    Lpontuacao = niveis[self.pontuacao]
                                    print(f"Subiu para o patamar dos {Lpontuacao}€!\n")

                            elif resposta_user == "ajuda" or resposta_user == "Ajuda":
                                self.ajudaRepetir = True
                                if self.usado50 == False and self.usadoTelefone == False and self.usadoAudiencia == False:
                                    while self.ajudaRepetir:
                                        ajudaResposta = input(
                                            "Digite o tipo de ajuda que deseja[50/telefone/audiencia]: ")
                                        if ajudaResposta == '50':
                                            if self.questoes_dificeis[random_nmr]["resposta_certa"] == 'a':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_dificeis[random_nmr]['respostas']['a']}")
                                                    print(f"b) {self.questoes_dificeis[random_nmr]['respostas']['b']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"a) {self.questoes_dificeis[random_nmr]['respostas']['a']}")
                                                    print(f"c) {self.questoes_dificeis[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"a) {self.questoes_dificeis[random_nmr]['respostas']['a']}")
                                                    print(f"d) {self.questoes_dificeis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            elif self.questoes_dificeis[random_nmr]["resposta_certa"] == 'b':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_dificeis[random_nmr]['respostas']['a']}")
                                                    print(f"b) {self.questoes_dificeis[random_nmr]['respostas']['b']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"b) {self.questoes_dificeis[random_nmr]['respostas']['b']}")
                                                    print(f"c) {self.questoes_dificeis[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"b) {self.questoes_dificeis[random_nmr]['respostas']['b']}")
                                                    print(f"d) {self.questoes_dificeis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            elif self.questoes_dificeis[random_nmr]["resposta_certa"] == 'c':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_dificeis[random_nmr]['respostas']['a']}")
                                                    print(f"c) {self.questoes_dificeis[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"b) {self.questoes_dificeis[random_nmr]['respostas']['b']}")
                                                    print(f"c) {self.questoes_dificeis[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"c) {self.questoes_dificeis[random_nmr]['respostas']['c']}")
                                                    print(f"d) {self.questoes_dificeis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            elif self.questoes_dificeis[random_nmr]["resposta_certa"] == 'd':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_dificeis[random_nmr]['respostas']['a']}")
                                                    print(f"d) {self.questoes_dificeis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"b) {self.questoes_dificeis[random_nmr]['respostas']['b']}")
                                                    print(f"d) {self.questoes_dificeis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"c) {self.questoes_dificeis[random_nmr]['respostas']['c']}")
                                                    print(f"d) {self.questoes_dificeis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            self.usado50 = True
                                            self.ajudaRepetir = False
                                        elif ajudaResposta == "telefone" or ajudaResposta == "Telefone":
                                            chamada = input("Digite o nome da pessoa a quem deseja ligar: ")
                                            print(
                                                f"Trrrim-trrrim!! {chamada.title()} diz que a resposta correta é a {self.questoes_dificeis[random_nmr]['resposta_certa']})!")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                            self.usadoTelefone = True
                                            self.ajudaRepetir = False

                                        elif ajudaResposta == "audiência" or ajudaResposta == "audiencia" or ajudaResposta == "Audiência" or ajudaResposta == "Audiencia":
                                            print(
                                                f"A audiência diz que a resposta certa é a {self.questoes_dificeis[random_nmr]['resposta_certa']})!")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                            self.usadoAudiencia = True
                                            self.ajudaRepetir = False

                                        else:
                                            print("Inválido.")
                                            self.ajudaRepetir = True

                                elif self.usado50 == False and self.usadoTelefone == False and self.usadoAudiencia == True:
                                    ajudaResposta = input("Digite o tipo de ajuda que deseja[50/telefone]: ")
                                    while self.ajudaRepetir:
                                        ajudaResposta = input("Digite o tipo de ajuda que deseja[50/telefone]: ")
                                        if ajudaResposta == '50':
                                            if self.questoes_dificeis[random_nmr]["resposta_certa"] == 'a':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_dificeis[random_nmr]['respostas']['a']}")
                                                    print(f"b) {self.questoes_dificeis[random_nmr]['respostas']['b']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"a) {self.questoes_dificeis[random_nmr]['respostas']['a']}")
                                                    print(f"c) {self.questoes_dificeis[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"a) {self.questoes_dificeis[random_nmr]['respostas']['a']}")
                                                    print(f"d) {self.questoes_dificeis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            elif self.questoes_dificeis[random_nmr]["resposta_certa"] == 'b':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_dificeis[random_nmr]['respostas']['a']}")
                                                    print(f"b) {self.questoes_dificeis[random_nmr]['respostas']['b']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"b) {self.questoes_dificeis[random_nmr]['respostas']['b']}")
                                                    print(f"c) {self.questoes_dificeis[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"b) {self.questoes_dificeis[random_nmr]['respostas']['b']}")
                                                    print(f"d) {self.questoes_dificeis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            elif self.questoes_dificeis[random_nmr]["resposta_certa"] == 'c':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_dificeis[random_nmr]['respostas']['a']}")
                                                    print(f"c) {self.questoes_dificeis[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"b) {self.questoes_dificeis[random_nmr]['respostas']['b']}")
                                                    print(f"c) {self.questoes_dificeis[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"c) {self.questoes_dificeis[random_nmr]['respostas']['c']}")
                                                    print(f"d) {self.questoes_dificeis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            elif self.questoes_dificeis[random_nmr]["resposta_certa"] == 'd':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_dificeis[random_nmr]['respostas']['a']}")
                                                    print(f"d) {self.questoes_dificeis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"b) {self.questoes_dificeis[random_nmr]['respostas']['b']}")
                                                    print(f"d) {self.questoes_dificeis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"c) {self.questoes_dificeis[random_nmr]['respostas']['c']}")
                                                    print(f"d) {self.questoes_dificeis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            self.usado50 = True
                                            self.ajudaRepetir = False
                                        elif ajudaResposta == "telefone" or ajudaResposta == "Telefone":
                                            chamada = input("Digite o nome da pessoa a quem deseja ligar: ")
                                            print(
                                                f"Trrrim-trrrim!! {chamada.title()} diz que a resposta correta é a {self.questoes_dificeis[random_nmr]['resposta_certa']})!")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                            self.usadoTelefone = True
                                            self.ajudaRepetir = False

                                        else:
                                            print("Inválido.")
                                            self.ajudaRepetir = True

                                elif self.usado50 == False and self.usadoTelefone == True and self.usadoAudiencia == False:
                                    while self.ajudaRepetir:
                                        ajudaResposta = input("Digite o tipo de ajuda que deseja[50/audiencia]: ")
                                        if ajudaResposta == '50':
                                            if self.questoes_dificeis[random_nmr]["resposta_certa"] == 'a':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_dificeis[random_nmr]['respostas']['a']}")
                                                    print(f"b) {self.questoes_dificeis[random_nmr]['respostas']['b']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"a) {self.questoes_dificeis[random_nmr]['respostas']['a']}")
                                                    print(f"c) {self.questoes_dificeis[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"a) {self.questoes_dificeis[random_nmr]['respostas']['a']}")
                                                    print(f"d) {self.questoes_dificeis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            elif self.questoes_dificeis[random_nmr]["resposta_certa"] == 'b':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_dificeis[random_nmr]['respostas']['a']}")
                                                    print(f"b) {self.questoes_dificeis[random_nmr]['respostas']['b']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"b) {self.questoes_dificeis[random_nmr]['respostas']['b']}")
                                                    print(f"c) {self.questoes_dificeis[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"b) {self.questoes_dificeis[random_nmr]['respostas']['b']}")
                                                    print(f"d) {self.questoes_dificeis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            elif self.questoes_dificeis[random_nmr]["resposta_certa"] == 'c':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_dificeis[random_nmr]['respostas']['a']}")
                                                    print(f"c) {self.questoes_dificeis[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"b) {self.questoes_dificeis[random_nmr]['respostas']['b']}")
                                                    print(f"c) {self.questoes_dificeis[random_nmr]['respostas']['c']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"c) {self.questoes_dificeis[random_nmr]['respostas']['c']}")
                                                    print(f"d) {self.questoes_dificeis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            elif self.questoes_dificeis[random_nmr]["resposta_certa"] == 'd':
                                                rndnumber = random.randint(1, 3)
                                                if rndnumber == 1:
                                                    print(f"a) {self.questoes_dificeis[random_nmr]['respostas']['a']}")
                                                    print(f"d) {self.questoes_dificeis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 2:
                                                    print(f"b) {self.questoes_dificeis[random_nmr]['respostas']['b']}")
                                                    print(f"d) {self.questoes_dificeis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                                elif rndnumber == 3:
                                                    print(f"c) {self.questoes_dificeis[random_nmr]['respostas']['c']}")
                                                    print(f"d) {self.questoes_dificeis[random_nmr]['respostas']['d']}")
                                                    opcresposta = input("Resposta: ")
                                                    ficheiro.write(opcresposta + "\n\n")
                                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                        print("\nResposta correta!!!")
                                                        self.pontuacao += 1
                                                        Lpontuacao = niveis[self.pontuacao]
                                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                                    else:
                                                        print("\nResposta errada!")
                                                        print(
                                                            f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                        print("PERDEU!")
                                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                        if recomecar == 's':
                                                            self.pontuacao = 0
                                                            print("\n")
                                                            break
                                                        else:
                                                            quit()
                                            self.usado50 = True
                                            self.ajudaRepetir = False

                                        elif ajudaResposta == "audiência" or ajudaResposta == "audiencia" or ajudaResposta == "Audiência" or ajudaResposta == "Audiencia":
                                            print(
                                                f"A audiência diz que a resposta certa é a {self.questoes_dificeis[random_nmr]['resposta_certa']})!")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                            self.usadoAudiencia = True
                                            self.ajudaRepetir = False

                                        else:
                                            print("Inválido.")
                                            self.ajudaRepetir = True

                                elif self.usado50 == False and self.usadoTelefone == True and self.usadoAudiencia == True:
                                    print("Foi usada a sua única ajuda. 50/50.\n")
                                    if self.questoes_dificeis[random_nmr]["resposta_certa"] == 'a':
                                        rndnumber = random.randint(1, 3)
                                        if rndnumber == 1:
                                            print(f"a) {self.questoes_dificeis[random_nmr]['respostas']['a']}")
                                            print(f"b) {self.questoes_dificeis[random_nmr]['respostas']['b']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                        elif rndnumber == 2:
                                            print(f"a) {self.questoes_dificeis[random_nmr]['respostas']['a']}")
                                            print(f"c) {self.questoes_dificeis[random_nmr]['respostas']['c']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                        elif rndnumber == 3:
                                            print(f"a) {self.questoes_dificeis[random_nmr]['respostas']['a']}")
                                            print(f"d) {self.questoes_dificeis[random_nmr]['respostas']['d']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                    elif self.questoes_dificeis[random_nmr]["resposta_certa"] == 'b':
                                        rndnumber = random.randint(1, 3)
                                        if rndnumber == 1:
                                            print(f"a) {self.questoes_dificeis[random_nmr]['respostas']['a']}")
                                            print(f"b) {self.questoes_dificeis[random_nmr]['respostas']['b']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                        elif rndnumber == 2:
                                            print(f"b) {self.questoes_dificeis[random_nmr]['respostas']['b']}")
                                            print(f"c) {self.questoes_dificeis[random_nmr]['respostas']['c']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                        elif rndnumber == 3:
                                            print(f"b) {self.questoes_dificeis[random_nmr]['respostas']['b']}")
                                            print(f"d) {self.questoes_dificeis[random_nmr]['respostas']['d']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                    elif self.questoes_dificeis[random_nmr]["resposta_certa"] == 'c':
                                        rndnumber = random.randint(1, 3)
                                        if rndnumber == 1:
                                            print(f"a) {self.questoes_dificeis[random_nmr]['respostas']['a']}")
                                            print(f"c) {self.questoes_dificeis[random_nmr]['respostas']['c']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                        elif rndnumber == 2:
                                            print(f"b) {self.questoes_dificeis[random_nmr]['respostas']['b']}")
                                            print(f"c) {self.questoes_dificeis[random_nmr]['respostas']['c']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                        elif rndnumber == 3:
                                            print(f"c) {self.questoes_dificeis[random_nmr]['respostas']['c']}")
                                            print(f"d) {self.questoes_dificeis[random_nmr]['respostas']['d']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                    elif self.questoes_dificeis[random_nmr]["resposta_certa"] == 'd':
                                        rndnumber = random.randint(1, 3)
                                        if rndnumber == 1:
                                            print(f"a) {self.questoes_dificeis[random_nmr]['respostas']['a']}")
                                            print(f"d) {self.questoes_dificeis[random_nmr]['respostas']['d']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                        elif rndnumber == 2:
                                            print(f"b) {self.questoes_dificeis[random_nmr]['respostas']['b']}")
                                            print(f"d) {self.questoes_dificeis[random_nmr]['respostas']['d']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                        elif rndnumber == 3:
                                            print(f"c) {self.questoes_dificeis[random_nmr]['respostas']['c']}")
                                            print(f"d) {self.questoes_dificeis[random_nmr]['respostas']['d']}")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                    self.usado50 = True

                                elif self.usado50 == True and self.usadoTelefone == False and self.usadoAudiencia == False:
                                    while self.ajudaRepetir:
                                        ajudaResposta = input("Digite o tipo de ajuda que deseja[telefone/audiencia]: ")
                                        if ajudaResposta == "telefone" or ajudaResposta == "Telefone":
                                            chamada = input("Digite o nome da pessoa a quem deseja ligar: ")
                                            print(
                                                f"Trrrim-trrrim!! {chamada.title()} diz que a resposta correta é a {self.questoes_dificeis[random_nmr]['resposta_certa']})!")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                            self.usadoTelefone = True
                                            self.ajudaRepetir = False

                                        elif ajudaResposta == "audiência" or ajudaResposta == "audiencia" or ajudaResposta == "Audiência" or ajudaResposta == "Audiencia":
                                            print(
                                                f"A audiência diz que a resposta certa é a {self.questoes_dificeis[random_nmr]['resposta_certa']})!")
                                            opcresposta = input("Resposta: ")
                                            ficheiro.write(opcresposta + "\n\n")
                                            if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                                print("\nResposta correta!!!")
                                                self.pontuacao += 1
                                                Lpontuacao = niveis[self.pontuacao]
                                                print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                            else:
                                                print("\nResposta errada!")
                                                print(
                                                    f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                                print("PERDEU!")
                                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                                if recomecar == 's':
                                                    self.pontuacao = 0
                                                    print("\n")
                                                    break
                                                else:
                                                    quit()
                                            self.usadoAudiencia = True
                                            self.ajudaRepetir = False

                                        else:
                                            print("Inválido.")
                                            self.ajudaRepetir = True

                                elif self.usado50 == True and self.usadoTelefone == False and self.usadoAudiencia == True:
                                    print("Foi usada a sua única ajuda. Telefone.")
                                    chamada = input("Digite o nome da pessoa a quem deseja ligar: ")
                                    print(
                                        f"Trrrim-trrrim!! {chamada.title()} diz que a resposta correta é a {self.questoes_dificeis[random_nmr]['resposta_certa']})!")
                                    opcresposta = input("Resposta: ")
                                    ficheiro.write(opcresposta + "\n\n")
                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                        print("\nResposta correta!!!")
                                        self.pontuacao += 1
                                        Lpontuacao = niveis[self.pontuacao]
                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                    else:
                                        print("\nResposta errada!")
                                        print(f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                        print("PERDEU!")
                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                        if recomecar == 's':
                                            self.pontuacao = 0
                                            print("\n")
                                            break
                                        else:
                                            quit()
                                    self.usadoTelefone = True

                                elif self.usado50 == True and self.usadoTelefone == True and self.usadoAudiencia == False:
                                    print("Foi usada a sua única ajuda. Audiência.\n")
                                    print(
                                        f"A audiência diz que a resposta certa é a {self.questoes_dificeis[random_nmr]['resposta_certa']})!")
                                    opcresposta = input("Resposta: ")
                                    ficheiro.write(opcresposta + "\n\n")
                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                        print("\nResposta correta!!!")
                                        self.pontuacao += 1
                                        Lpontuacao = niveis[self.pontuacao]
                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                    else:
                                        print("\nResposta errada!")
                                        print(f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                        print("PERDEU!")
                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                        if recomecar == 's':
                                            self.pontuacao = 0
                                            print("\n")
                                            break
                                        else:
                                            quit()
                                    self.usadoAudiencia = True

                                elif self.usado50 == True and self.usadoTelefone == True and self.usadoAudiencia == True:
                                    print("Já não possui ajudas!\n")
                                    opcresposta = input("Resposta: ")
                                    ficheiro.write(opcresposta + "\n\n")
                                    if opcresposta == self.questoes_dificeis[random_nmr]['resposta_certa']:
                                        print("\nResposta correta!!!")
                                        self.pontuacao += 1
                                        Lpontuacao = niveis[self.pontuacao]
                                        print(f"Subiu para o patamar dos {Lpontuacao}€!\n")
                                    else:
                                        print("\nResposta errada!")
                                        print(f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                        print("PERDEU!")
                                        recomecar = input("Deseja jogar novamente?[s/n]: ")
                                        if recomecar == 's':
                                            self.pontuacao = 0
                                            print("\n")
                                            break
                                        else:
                                            quit()

                            else:
                                ficheiro.write(resposta_user + "\n\n")
                                print("\nResposta errada!")
                                print(f"Resposta correta: {self.questoes_dificeis[random_nmr]['resposta_certa']})\n")
                                print("PERDEU!")
                                recomecar = input("Deseja jogar novamente?[s/n]: ")
                                if recomecar == 's':
                                    self.pontuacao = 0
                                    print("\n")
                                    break
                                else:
                                    quit()

                            if self.pontuacao > 11:
                                break

            elif snresposta == 'n' or snresposta == 'N':
                corresposta = True
                quit()
            else:
                print("Resposta inválida.")
                corresposta = False

        ficheiro.close()




jogo = Jogo()
jogo.iniciar()