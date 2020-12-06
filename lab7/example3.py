books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]

book_dict = {
    "ULYSSES" : (len("ULYSESS"), len(set("ULYSESS")), (len("ULYSESS") + len(set("ULYSESS"))) / 2),
    "ANIMAL FARM" : (len("ANIMAL FARM"), len(set("ANIMAL FARM")) , (len("ANIMAL FARM") + len(set("ANIMAL FARM"))) / 2) ,
    "BRAVE NEW WORLD" : (len("BRAVE NEW WORLD"), len(set("BRAVE NEW WORLD")) ,  (len("BRAVE NEW WORLD") + len(set("BRAVE NEW WORLD"))) / 2),
    "ENDER'S GAME" : (len("ENDER'S GAME"), len(set("ENDER'S GAME")) ,  (len("ENDER'S GAME") + len(set("ENDER'S GAME"))) / 2)
}

keys = list(book_dict.keys())
values = list(book_dict.values())

for i in range(len(books)) :
    print(keys[i],"->",values[i])