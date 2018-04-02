from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.SiteMateus
Albuns = db.Albuns
Fotos = db.Fotos
Videos = db.Videos
'''
Video =[    
    {
        "Nome": "Jovem Black Mirror - Ostentando Insensatez",
        "Url" : "esEm3U-0FRY",
        "Tipo" : "Conceitual"
    },
    {
        "Nome": "SQL - Boto fé ft Yan (Lyric Video)",
        "Url": "03ZDVHE-IEw",
        "Tipo": "Conceitual",
    }
] 

Video_id = Videos.insert_many(Video)
Itens_Video = Videos.find({"Tipo" : "Conceitual"})
Item = []
for i in Itens_Video:
    Item.append(i)
    print (Item)

Album = {
    "Nome" : "Clips Conceituais",
    "Tipo" : "Conceitual",
    "Videos" : Item,
    "Fotos" : [

    ],
}

Album_id = Albuns.insert_one(Album).inserted_id
print(Album_id)'''