from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.SiteMateus
Albuns = db.Albuns
Fotos = db.Fotos
Videos = db.Videos
Colecoes = db.Colecoes
Galerias = db.Galerias
'''
Video =[    
    {
        "Nome": "Jovem Black Mirror - Ostentando Insensatez",
        "Url" : "esEm3U-0FRY",
        "Tipo" : "conceitual"
    },
    {
        "Nome": "SQL - Boto fé ft Yan (Lyric Video)",
        "Url": "03ZDVHE-IEw",
        "Tipo": "conceitual",
    }
] 

Video_id = Videos.insert_many(Video)
Itens_Video = Videos.find({"Tipo" : "conceitual"})
Item = []
for i in Itens_Video:
    Item.append(i)
    print (Item)

Video =[    
    {
        "Nome": "Jovem Black Mirror - Ostentando Insensatez",
        "Url" : "esEm3U-0FRY",
        "Tipo" : "conceitual"
    },
    {
        "Nome": "SQL - Boto fé ft Yan (Lyric Video)",
        "Url": "03ZDVHE-IEw",
        "Tipo": "conceitual",
    }
] 

Foto = [
    {
        "Tipo" : "conceitual",
        "Url" : "FotoShaka1",
        "Tags" : [
            "conceitual", "Esporte", "Casamento"
        ]
    },
    {
        "Tipo" : "conceitual",
        "Url" : "FotoShaka2",
        "Tags" : [
            "conceitual", "Festa", "Rave"
        ]
    }
]

Video_id = Videos.insert_many(Video)
Itens_Video = Videos.find({"Tipo" : "conceitual"})
Item_Video = []
for i in Itens_Video:
    Item_Video.append(i)
    print (Item_Video)

Foto_id = Fotos.insert_many(Foto)
Itens_Foto = Fotos.find({"Tipo" : "conceitual"})
Item_Foto = []
for j in Itens_Foto:
    Item_Foto.append(j)
    print (Item_Foto)

Album = [
    {
        "Nome" : "Clips Conceituais",
        "Tipo" : "conceitual",
        "Videos" : Item,
        "Fotos" : [

        ],
        "FotoCapa" : "FotoShaka1"
    },
    {
        "Nome" : "Clips Conceituais Teste2",
        "Tipo" : "conceitual",
        "Videos" : Item_Video,
        "Fotos" : Item_Foto,
        "FotoCapa": "FotoShaka2"
    },

]

Album_id = Albuns.insert_many(Album)
print(Album_id)
Itens_Albuns = Albuns.find({"Tipo" : "conceitual"})
Item_Album = []
for k in Itens_Albuns:
    Item_Album.append(k)
    print (Item_Album)

Colecao = {
    "Tipo" : "conceitual",
    "Galeria": "conceitual",
    "Album" : Item_Album
}

Colecao_id = Colecoes.insert_one(Colecao)
print (Colecao_id)
Itens_Colecoes = Colecoes.find({"Galeria": "conceitual"})
Item_Colecao = []
for y in Itens_Colecoes:
    Item_Colecao.append(y)
    print(Item_Colecao)

Galeria = {
    "Galeria" : "conceitual",
    "Colecao" : Item_Colecao
}

Galeria_id = Galerias.insert_one(Galeria)'''