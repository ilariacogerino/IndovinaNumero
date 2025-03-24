from view import View
from model import Model
import flet as ft

#CLASSE CHE PERMETTE LA COMUNICAZIONE TRA MODEL E VIEW

class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()


    #QUESTE TRE FUNZIONI SERVONO SOLO PER IL PASSAGGIO DI INFORMAZIONI TRA IL MODELLO E LA VIEW
    def getNMax(self):
        return self._model.NMax

    def getTMax(self):
        return self._model.TMax

    def getT(self):
        return self._model.T


    # FUNZIONE PER INIZIARE UNA NUOVA PARTITA, HA LO STESSO NOME DELLA FUNZIONE DEL MODEL
    def reset(self, e):
        self._model.reset() #EFFTTUO EFFETTIVAMENTE IL RESET
        self._view._txtOutT.value = self._model.T
        self._view._lv.controls.clear() #PULISCO LA LIST VIEW (CONTENEVA  I VARI TENTATIVI)
        self._view._btnPlay.disabled = False
        self._view._txtIn.disabled = False
        self._view._lv.controls.append(ft.Text("Indovina a quale numero sto pensando:"))
        self._view.update()

    #FUNZIONE PER GIOCARE
    def play(self, e):
        tentativoStr = self._view._txtIn.value #PRENDO IL VALORE INSERITO DALL'UTENTE
        self._view._txtIn.value = ""
        self._view._txtOutT.value = self._model.T - 1

        #CONTROLLO CHE NON SIA UNA STRINGA VUOTA
        if tentativoStr == "":
            self._view._lv.controls.append(ft.Text("Attenzione! Inserire un valore non nullo",
                                                   color="red"))
            self._view.update()
            return

        try: #PROVO A TRASFORMARE LA STRINGA IN INTERO
            tentativoInt = int(tentativoStr)
        except ValueError:
            self._view._lv.controls.append(ft.Text("Inserire un valore numerico", color="red"))
            return

        res = self._model.play(tentativoInt) #QUA EFFETTIVAMENTE GIOCO

        if res == 0: #HO VINTO
            self._view._lv.controls.append(ft.Text(f"Fantastico! Hai vinto, il numero segreto era {tentativoInt}",
                                                   color="green"))
            #DISABILITO IL PULSANTE PER GIOCARE
            self._view._btnPlay.disabled=True
            self._view._txtIn.disabled=True
            self._view.update()
            return

        elif res == 2: #HO FINITO TUTTE LE VITE
            self._view._lv.controls.append(ft.Text(f"Mi spiace! Hai finito le vite, il numero segreto era {self._model.segreto}"))
            self._view._btnPlay.disabled = True
            self._view._txtIn.disabled = True
            self._view.update()
            return

        elif res == -1: #IL NUMERO SEGRETO E' PIU' PICCOLO
            self._view._lv.controls.append((ft.Text(f"Il numero segreto è più piccolo di {tentativoInt}")))
            self._view.update()

        else:
            self._view._lv.controls.append((ft.Text(f"Il numero segreto è più grande di {tentativoInt}")))
            self._view.update()



