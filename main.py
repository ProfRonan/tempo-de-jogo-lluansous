"""Arquivo principal que será interpretado pelo interpretador."""
import datetime
import time 


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI
    I = input('Digite o horário de início:')
    F = input('Digite o horário do fim:')
    DI = datetime.datetime(1,1,1)
    DF = datetime.datetime(1,1,1)
    ini = datetime.time(*map(int, I.split(':')))
    fim = datetime.time(*map(int, F.split(':')))
    start = datetime.datetime.combine(DI, ini)
    end = datetime.datetime.combine(DF, fim)
    if end == start:
     print("24:00:00")
    else:
     if end < start:
       end = end + datetime.timedelta(days=1)
     período = end - start
     print(time.strftime('%H:%M:%S', time.gmtime(período.seconds)))

if __name__ == '__main__':
    main()
