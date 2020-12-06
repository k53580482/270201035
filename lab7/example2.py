books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]

book_dict = {
    "ULYSSES" : (len("ULYSESS"), len(set("ULYSESS"))),
    "ANIMAL FARM" : (len("ANIMAL FARM"), len(set("ANIMAL FARM"))) ,
    "BRAVE NEW WORLD" : (len("BRAVE NEW WORLD"), len(set("BRAVE NEW WORLD"))),
    "ENDER'S GAME" : (len("ENDER'S GAME"), len(set("ENDER'S GAME")))
}

keys = list(book_dict.keys())
values = list(book_dict.values())

for i in range(len(books)) :
    print(keys[i],"->",values[i])
