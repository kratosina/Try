meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL" : "tanggapan terhadap lelucon" , 
            "SHEESH" : "sedikit ketidaksetujuan" ,
            "CREEPY" : "menakutkan, tidak menyenangkan" ,
            "AGGRO" : "untuk menjadi agresif/marah"
            }

for i in range len(meme_dict): 
    question = input("what word that make you confuse (use an uppter letter word) :")
    print(meme_dict[question])
