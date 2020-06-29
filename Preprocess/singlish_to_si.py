import  json
import re
from mtranslate import translate
from googletrans import Translator

f = open ('singlish_lyrics.json', encoding='utf8')
data = json.load(f)

f = open ('sinhala_lyrics_new.json', encoding='utf8')
data1 = json.load(f)

print(len(data))

translator = Translator()
# print(translator.translate('Janaka go home', dest='si').text)
# print(translate("Janaka","si","auto"))
parallel =[]

dict = {
    "Wayo" : "වායො",
    "Current" : "වත්මන්",
    "Calypso" : "කැලිප්සෝ",
    "Songs" : "ගීත",
    "Harsha" : "හර්ෂ",
    "Jayamanne" : "ජයමාන්න",
    "Senaka" : "සේනක",
    "Batagoda" : "බටගොඩ",
    "Request" : "ඉල්ලීම්",
    "request" : "ඉල්ලීම්",
    "Group" : "කණ්ඩායම්",
    "Movie" : "චිත්‍රපට",
    "Kasun" : "කසුන්",
    "Kalhara" : "කල්හාර",
    "Sunil" : "සුනිල්",
    "Ariyarathna"   : "ආරියරත්න",
    "Dayasiri" : "දයාසිරි",
    "Jayasekara" : "ජයසේකර",
    "Daddy" : "ඩැඩී",
    "Nandasiri" : "නන්දසිරි",
    "Nanda" : "නන්දා",
    "Malani" : "මාලනී",
    "Somadasa" : "සෝමදාස",
    "Elvitigala" : "එල්විටිගල",
    "Gunadas" : "ගුණදාස",
    "Kapuge" : "කපුගේ",
    "Sanath" : "සනත්",
    "Edirisinghe" : "එදිරිසිංහ",
    "Baddaga" : "බැද්දගේ",
    "Baddage" : "බැද්දගේ",
    "Sekara" : "සේකර",
    "Bandara" : "බණ්ඩාර",
    "Ahaliyagoda" : "ඇහැලියගොඩ",
    "Dhanawalawithana" : "දනවල්විතාන",
    "Achala" : "ආචලා",
    "Solamans" : "සොලමන්ස්",
    "Pop" : "පොප්",
    "Golden" : "රන්වන්",
    "Old" : "පැරණි",
    "Oldies" : "පැරණි",
    "Classic" : "ශාස්ත්‍ර්‍රීය",
    "Movie" : "චිත්‍රපට",
    "Duets" : "යුගල",
    "duet" : "යුගල",
    "Duet":"යුගල",
    "Inspirational" : "උද්වේගකර",
    "Alwis" : "අල්විස්",
    "Victor" : "වික්ටර්",
    "Rathnayaka" : "රත්නායක",
    # "W" : "ඩබ්ලිව්",
    # "D" : "ඩී",
    "Amaradewa" : "අමරදේව",
    "Lahiru" : "ළහිරු",
    "Perera" :"පෙරේරා",
    "Cyril" : "සිරිල්",
    "Premakeerthi" : "ප්‍රේමකීර්ති",
    "Jothipala" : "ජෝතිපාල",
    "Priyadarshani" : "ප්‍රියදර්ශනී",
    "Deepika" : "දීපිකා",
    "Rohana" : "රෝහණ",
    "Weerasingha" : "වීරසිංහ",
    "Pradeep" : "ප්‍රදීප්",
    "Rangana" : "රංගන",
    "Angelin" : "ඇන්ජලීන්",
    "Gunathilaka" : "ගුණතිලක",
    "Karunarathna" : "කරුණාරත්න",
    "Karunaratna" : "කරුණාරත්න",
    "Abeysekara" : "අබේසේකර",
    "Divulgane" : "දිවුල්ගනේ",
    "Fernando" : "ප්‍රානන්දු",
    "Milton" : "මිල්ටන්",
    "Roksami" : "රොක්සාමි",
    "Wijewardena": "විජේවර්ධන",
    "Clarence" : "ක්ලැරන්ස්",
    "Bulathsinhala" : "බුලත්සිංහල",
    "Premasiri" : "ප්‍ර්‍රේමසිරි",
    "Khemadasa" : "කේමදාස",
    "Gamage" : "ගමගේ",
    "Walpola" : "වල්පොල",
    "Latha" : "ලතා",
    "Gunawardhana" : "ගුණවර්ධන",
    "Attanayaka" : "අත්තනායක",
    "Sujatha" : "සුජාතා",
    "Kumarathunga" : "කුමාරතුංග",
    "Vijaya" : "විජය",
    "Silva" : "සිල්වා",
    "Unknown" : "නොදනී",
    "Rathna" : "රත්න",
    "Wijesinge" : "විජේසිංහ",
    "Jayamaha" : "ජයමහ",
    "Sri" : "ශ්‍රී",
    "Somathilaka" : "සෝමතිලක",
    "Mallawarachchi" : " මල්ලව ආරච්චි",
    "Dasanayaka" : "දසනායක",
    "Sarath" : "සරත්",
    "Lushan" : "ලූෂන්",
    "Somapala" : "සෝමපාල",
    "Mervin" : "මර්වින්",
    "Pandith" : "පණ්ඩිත්",
    "Edward" : "එඩ්වඩ්",
    "Jayakody" : "ජයකොඩි",
    "Sisira" : "සිසිර",
    "Senarathna" : "සෙනාරත්න",
    "Rookantha" : "රූකාන්ත",
    "Chandana"  : "චන්දන",
    "Liyanarachchi" : "ලියනාරච්චි",
    "Pieris" : "පීරිස්",
    "Peiris" : "පීරිස්",
    "Stanley" : "ස්ටැන්ලි",
    "Muththusami" : "මුත්තුසාමි",
    "Ranasinghe" : "රණසිංහ",
    "Dharmawardhana" : "ධර්මවර්ධන",
    "Annesley" : "ඇනෙස්ලි",
    "Malawana" :"මල්වාන",
    "Dayarathna" : "දයාරත්න",
    "Saman" : "සමන්",
    "Gamhewa" : "ගම්හේවා",
    "Nihal" : "නිහාල්",
    "Kularathna" : "කුලරත්න",
    "Ariyawansa" : "ආරියවංස",
    "Soyza" : "සොයිසා",
    "Punsiri" : "පුන්සිරි",
    "Kumara" : "කුමාර",
    "Jayawardhana" : "ජයවර්ධන",
    "Weerasinghe" : "වීරසිංහ",
    "Blue" : "බ්ලූ",
    "Shadows" :"ෂැඩෝස්",
    "Dayananda" : "දයානන්ද",
    "Dharmasiri" : "ධර්මසිරි",
    "Nanayakkarawasam" : "නනායක්කාරවසම්",
    "Bandula" : "බන්දුල",
    "Dharmakeerthi"  : "ධර්මකීර්ති",
    "Liyanage" : "ලියනගේ",
    "Senevirathna" : "සෙනෙවිරත්න",
    "Hurbet" : "හර්බට්",
    "Chimes" : "චයිම්ස්",
    "Super" : "සුපිරි",
    "Saputhanthri" : "සපුතන්ත්‍රී",
    "Ajantha" : "අජන්ත",
    "Victo" : "වික්ටො",
    "Indrani" : "ඉන්ද්‍රානි",
    "Mahinda" : "මහින්ද",
    "Algama" : "අලගම",
    "Amarasiri" : "අමරසිරි",
    "Seelawimala" : "සීලවිමල්",
    "Chandralekha" : "චන්ද්‍රලේකා",
    "Mahagama" : "මහගම",
    "Upali" : "උපාලි",
    "Ranathunga" : "රණතුංග",
    "Mendis" : "මෙන්ඩිස්",
    "Dissanayaka" : "දිසානායක",
    "New" : "නව",
    "Ananda" : "ආනන්ද",
    "Rukmani" : "රුක්මනී",
    "Devi" : "දේවි",
    "De": "ද"
}


def replacement(match, d, group=1):
    for key in d:
        if re.match(key, match.group(group)):
            return d[key]
    # return (match.group(group))
    return translator.translate(match.group(group), dest='si').text

def replacement1(match, d, group=1):
    print(match)
    return translate(match.group(group),"si","auto")

def getName(name):
    c=name.split('–')
    if len(c) > 1:
        # print(len(c),c)
        return c[1].strip()
    else:
        return name.strip()

count = 0
a1=700
for item in data:
    if count < (a1-50):
        a = data1[count]
    else:

        a={}
        a['artist'] = re.sub(r'([a-zA-Z]+)', lambda x: replacement(x,dict),item['artist'])
        a['genre'] = re.sub(r'([a-zA-Z]+)', lambda x: replacement(x, dict), item['genre'])
        a['music'] = re.sub(r'([a-zA-Z]+)', lambda x: replacement(x, dict), item['music'])
        a['lyrics_by'] = re.sub(r'([a-zA-Z]+)', lambda x: replacement(x, dict), item['lyrics by'])
        a['name'] = getName(item['name'])
        a['lyrics'] = item['lyrics']
        a['key']= item['key'].strip()
        a['beat'] = item['beat']
        a['visits'] = item['vists'].replace(',','')

    count += 1
    parallel.append(a)


with open("sinhala_lyrics_new.json", 'w', encoding="utf8") as outfile:
    json.dump(parallel, outfile, ensure_ascii=False, indent=4)

# file = open ('msinhala_lyrics.json', encoding="utf8")
# dd =json.load(file)
# print(len(dd))