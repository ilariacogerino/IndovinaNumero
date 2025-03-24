import random
#CONTIENE LA LOGICA DEL GIOCO

class Model(object):
    def __init__(self):
        self._NMax = 100
        self._TMax = 6 #NUMERO DI VITE MASSIMO
        self._T = self._TMax
        self._segreto = None #IL NUMERO SEGRETO, QUANDO INIZIALIZZIAMO IL MODELLO NON LO SAPPIAMO

    def reset(self):
        #  QUESTO METODO RESETTA IL GIOCO IN QUALSAISI MOMENTO
        self._segreto = random.randint(0, self._NMax) #ESTAZIONE DEL NUMERO
        self._T = self._TMax #REIMPOSTA LE VITE AL NUMERO MASSIMO
        print(self._segreto)

    def play(self, guess):
        """
                funzione che esegue uno step del gioco
                :param guess: int
                :return:
                - 0 se ho indivinato il numero;
                - 2 se ho finito le vite;
                - -1 se il numero è più piccolo
                - 1 se il numero è più grande
        """
        #CONFRONTO DEL TENTIVO DIGITATO DALL'UTENTE CON IL NUMERO SEGRETO,
        #IL METODO NECESSITA DI UN INPUT QUINDI (IL NUMERO GIOCATO)

        self._T -= 1 #PERDITA DI UNA VITA
        if guess == self._segreto:
            return 0 #SCELTA ARBITRARIA DI RETURNARE 0 NEL CASO DI VINCITA

        if self._T == 0: #VITE FINITE, PERDITA DEFINITIVA
            return 2

        if guess > self._segreto:
            return -1 #IL NUMERO SEGRETO E' PIU' PICCOLO

        return 1 #IL NUMERO SEGRETO E' PIU' GRANDE

    #METODI GETTER:
    @property
    def NMax(self):
        return self._NMax

    @property
    def TMax(self):
        return self._TMax

    @property
    def T(self):
        return self._T

    @property
    def segreto(self):
        return self._segreto

if __name__ == "__main__":
    m = Model()
    m.reset()
    print(m.play(80))
    print(m.play(10))


