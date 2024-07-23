meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "AGUACATE": "tambien se llama palta",
            "CANGUIL": "tambien conocido com palomitas de maiz",
            "CHOCLO": "tambien conocido como elote o maiz",
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("la palabra no existe aun en nuestro diccionario ")
