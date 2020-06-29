import  json

f = open ('lyrics_new.json',encoding='utf8')
data = json.load(f)

print(len(data))

parallel =[]

for item in data:
    if item['artist'].strip() != "" and item['lyrics'].strip() != "":
        parallel.append(item)

with open("singlish_lyrics.json", 'w', encoding="utf8") as outfile:
    json.dump(parallel, outfile, ensure_ascii=False, indent=4)
file = open ('singlish_lyrics.json', encoding="utf8")
dd =json.load(file)
print(len(dd))





