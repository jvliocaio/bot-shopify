import random


def generate_name():
    names = [
        "João","Maria","Pedro","Ana","José","Carla","Miguel","Sara","Lucas","Mariana",
         "Gabriel","Laura","Diego","Beatriz","Rafael","Isabela","Guilherme","Julia","Arthur",
         "Larissa","Fernando","Amanda","Gustavo","Natália","Enzo","Lara","Leonardo","Manuela",
         "Matheus","Camila","Ricardo","Luana","André","Fernanda","Eduardo","Bianca","Victor",
         "Letícia","Daniel","Carolina","Felipe","Lívia","Bruno","Isabel","Caio","Marina",
         "Alexandre","Ana Clara","Rodrigo","Raquel"
    ]

    last_names = [ 
           "Silva","Santos","Oliveira","Souza","Pereira","Rodrigues","Almeida","Costa","Ribeiro","Carvalho",
           "Martins","Andrade","Cardoso","Lima","Ferreira","Gomes","Barbosa","Azevedo","Rocha","Fernandes",
           "Melo","Castro","Teixeira","Freitas","Peixoto","Nunes","Medeiros","Batista","Menezes","Marques",
           "Montenegro","Miranda","Sales","Cunha","Morais","Mendes","Siqueira","Fonseca","Lopes","Gonçalves",
           "Campos","Moreira","Nascimento","Moura","Farias","Dias","Castro","Barros","Nogueira","Ramos","Cardoso"
    ]
    
    name = random.choice(names)
    last_name = random.choice(last_names)
    full_name = f"{name} {last_name}"

    print(full_name)


generate_name()
