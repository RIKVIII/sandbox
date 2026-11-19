## file conto_documentato.py 
# Semplice implementazione di un conto bancario con operazioni di prelievo e deposito

## Rappresentare un conto bancario con intestatario e saldo
# Consente di depositare e prelevare denaro
class ContoBancario():
    
    ## Inizializza un nuovo conto bancario 
    def __init__ (self, intestatario):
        self.intestatario = intestatario
        self.saldo = 0

    ##Deposita una somma di denaro sul conto bancario
    def deposita(self, importo):
        self.saldo += importo

    ##Preleva una somma di denaro dal conto
    # ValueError sollevata se il saldo è insufficiente 
    def preleva(self, importo):
        if self.saldo < importo:
            raise ValueError('Saldo insufficiente')
        else:
            self.saldo -= importo

    #Restituisce una rappresentazione testuale del conto
    def __str__ (self):
        return f'Conto di {self.intestatario} saldo: {self.saldo}'


def main():
    conto = ContoBancario("Mario Rossi")
    print (conto)
    conto.deposita(200)
    conto.preleva(50)
    conto.preleva(25)
    print(conto)
    try:
        conto.preleva(700)
    except ValueError as e:
        print('Operazione rifiutata: ', e)

if __name__ == "__main__":
    main()
