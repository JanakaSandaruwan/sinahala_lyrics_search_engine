import scrapy
import json
import re

class LyricsSpider(scrapy.Spider):
    name = 'lyrics'
    a = []
    # sinhala or english url of page 1
    start_urls = ['https://sinhalasongbook.com/tag/classical/','https://sinhalasongbook.com/tag/golden-oldies/',
                  'https://sinhalasongbook.com/tag/golden-pop/', 'https://sinhalasongbook.com/tag/old-pops/',
                  'https://sinhalasongbook.com/tag/movie-songs/', 'https://sinhalasongbook.com/tag/calypso/',
                  'https://sinhalasongbook.com/tag/duets/' , 'https://www.sinhalasongbook.com/tag/inspirational/',
                  'https://sinhalasongbook.com/tag/group-songs/', 'https://sinhalasongbook.com/tag/current-songs/']
    # 37 8 19 63 27 4 22 10 5 8
    types =['classical','golden-oldies','golden-pop','old-pops','movie-songs','calypso','duets','inspirational',
            'group-songs','current-songs']
    max_page_no = [37,8,19,63,27,4,22,10,5,8]

    # set 2 to no of page+1
    for i in range(len(types)):
        catogory = types[i]
        max_page= max_page_no[i]
        for j in range(2, max_page+1):
            start_urls.append('https://sinhalasongbook.com/tag/'+catogory+'/page/' + str(j)+'/')

    def parse(self, response):
        for quote in  response.xpath("/html/body/div[1]/div[1]/div/main/article/header/h2/a/@href").getall():
            next_page = quote
            yield response.follow(next_page, self.parse_author)

    def getName(self,response):
        name1 = response.xpath('//*[@id="genesis-content"]/article/div[3]/h2/text()').get().strip()
        name2 = response.xpath('/html/body/div[1]/div[1]/div/main/article/div[3]/h2/span/text()').get()
        if name1[-1] == "|":
            return name2
        else:
            return name1.split('-')[-1]

    def getLyrics(self,response):
        rows=response.xpath("//pre/text()").getall()
        lyric=""
        for row in rows:
            sinhala_row = ' '.join(re.findall(r'[^a-zA-Z0-9#|/\-(+)\t]+', row))
            sinhala_row = re.sub(' +', ' ', sinhala_row)
            if sinhala_row[0]=='\n':
                sinhala_row=sinhala_row[1:]
            without_symbol=re.findall(r'[^\s]',sinhala_row)
            if len(without_symbol) > 1:
                lyric +=  sinhala_row

        for i in range(len(lyric)):
            if lyric[i] == '\n' or lyric[i] == ' ' or lyric[i] == '-':
                continue
            else:
                break
        return lyric[i :]

    def getKey(self,response):
        return response.xpath('/html/body/div[1]/div[1]/div/main/article/div[3]/h3/text()').get().strip().split('|')[0].split(':')[1]

    def getBeat(self,response):
        return response.xpath('/html/body/div[1]/div[1]/div/main/article/div[3]/h3/text()').get().strip().split('|')[1].split(':')[1]

    #// *[ @ id = "genesis-content"] / article / div[3] / div[7] / div[1] / div / pre
    # //*[@id="genesis-content"]/article/div[3]/pre/
    def parse_author(self, response):
        obj = {
            'artist': (",".join(response.xpath("/html/body/div[1]/div[1]/div/main/article/div[3]/div[1]/div[2]/div/div/ul/li[1]/span/a/text()").getall())),
            'genre': (",".join(response.xpath("/html/body/div[1]/div[1]/div/main/article/div[3]/div[1]/div[2]/div/div/ul/li[2]/span/a/text()").getall())),
            # 'posted by': response.xpath('/html/body/div[1]/div[1]/div/main/article/div[3]/div[1]/div[2]/div/div/ul/li[3]/span/a/span/text()').get(),
            'lyrics by' : response.xpath('/html/body/div[1]/div[1]/div/main/article/div[3]/div[1]/div[3]/div/ul/li[1]/span/a/text()').get(),
            'music' : response.xpath('/html/body/div[1]/div[1]/div/main/article/div[3]/div[1]/div[3]/div/ul/li[2]/span/a/text()').get(),
            'name' : self.getName(response),
            'key' : self.getKey(response),
            'beat' : self.getBeat(response),
            'vists' : response.xpath('//*[@class="tptn_counter"]/text()').get().strip()[2:-6],
            'lyrics' : self.getLyrics(response)
        }
        self.a.append(obj)

    def closed(self, reason):
        with open("lyrics_new.json", 'w', encoding="utf8") as outfile:
            json.dump(self.a, outfile, ensure_ascii=False,indent=4)
