class perro:
    pvida=5
    palegria=5

    def __init__(self,pvida,palegria):
        self.pvida=5;
        self.palegria=5;
        print("Es hora de las actividades")

    def correr(self):
        self.pvida-=4;
        self.palegria+=3;

    def dormir(self):
        self.pvida+=1;
        self.palegria-=3;

    def jugar(self):
        self.pvida-=3;
        self.palegria+=4;

    def comer(self):
        self.pvida-=1;
        self.palegria+=5;

    def caminar(self):
        self.pvida-=2;
        self.palegria+=1;

l=perro("lassie")

if l<5:
    print("lassie se muere")
elif l.palegria < 5:
    print("lassie esta triste")

