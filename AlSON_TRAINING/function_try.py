
def temps (distance, vitesse, pause=0, passenger=0) :
    
    tp=distance//vitesse
    tp_pause = pause*5//60
    tp_passenger=pause*passenger*2//60
    return tp,tp_pause,tp_passenger

tp_1 = temps(120,30,1)
tp_2 = temps(40,40,2,5)

tp_total = tp_1 + tp_2
print(f"le temps total de trajet = {tp_1}+{tp_2}= {tp_total} ")

tp_3= temps(passenger=2,distance=23,vitesse=1)
print(f"le temps necessaire = {tp_3} ")

tp_4 = temps(40,20,passenger=2)
print(f" {tp_4} ")

