# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import urllib2
import re
idnumber = int(raw_input('Key in the music’s id in www.xiami.com ,such as：http://www.xiami.com/song/*********,THE ********* is what you need to key in～：'));
def main():
	allurla="http://www.xiami.com/song/playlist/id/abcdefg/object_name/default/object_id/0";
	idnumbera=str(idnumber);
	userMainUrla= allurla.replace('abcdefg',idnumbera)
	reqa = urllib2.Request(userMainUrla);
	reqa.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36');
	respa = urllib2.urlopen(reqa);
	respHtmla = respa.read();

	foundMusic = re.search('<title>(?P<music>.+?)</title>',respHtmla);
	if(foundMusic):
		music = foundMusic.group("music");
		print "音乐：",music[9:-3:1]

	foundArtist = re.search('<artist>(?P<artist>.+?)</artist>',respHtmla);
	if(foundArtist):
		artist = foundArtist.group("artist");
		print "艺术家：",artist[9:-3:1]

	foundalbum_name = re.search('<album_name>(?P<album_name>.+?)</album_name>',respHtmla);
	if(foundalbum_name):
		album_name = foundalbum_name.group("album_name");
		print "专辑：",album_name[9:-3:1]

	foundLyricurl =re.search('<lyric>(?P<lyricurl>.+?)</lyric>',respHtmla)
	if(foundLyricurl):
		lyricurl = foundLyricurl.group("lyricurl");
		print "歌词文件下载链接：",lyricurl;

	foundLocation =re.search('<location>(?P<location>.+?)</location>',respHtmla)
	if(foundLocation):
		location = foundLocation.group("location");
		strlen = len(location[1:])
		rows = int(location[0])
		cols = strlen / rows
		right_rows = strlen % rows
		new_str =location[1:]
		url_true = ''
		for i in xrange(strlen):
			x = i % rows
			y = i / rows
			p = 0
			if x <= right_rows:
				p = x * (cols + 1) + y
			else:
				p = right_rows * (cols + 1) + (x - right_rows) * cols + y
			url_true += new_str[p]
		locationb = urllib2.unquote(url_true).replace('^', '0')
		print "歌曲试听文件下载链接：",locationb ;

	foundPic =re.search('<pic>(?P<pic>.+?)</pic>',respHtmla)
	if(foundPic):
		pic = foundPic.group("pic");
		print "封面图片下载链接：",pic;

	allurlb="http://www.xiami.com/song/abcdefg";
	userMainUrlb= allurlb.replace('abcdefg',idnumbera)
	reqb = urllib2.Request(userMainUrlb);
	reqb.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36');
	respb = urllib2.urlopen(reqb);
	respHtmlb = respb.read();


	foundLyricist = re.search('<td class="item" valign="top">作词：</td>([\s\S]*)<div style="white-space:nowrap; width:140px; overflow:hidden; text-overflow:ellipsis;">(?P<lyricist>.+?)</div>',respHtmlb);
	if(foundLyricist):
		lyricist = foundLyricist.group("lyricist");
		print "作词：",lyricist;

	foundComposer = re.search('<td class="item" valign="top">作曲：</td>([\s\S]*)<div style="white-space:nowrap; width:140px; overflow:hidden; text-overflow:ellipsis;">(?P<composer>.+?)</div>',respHtmlb);
	if(foundComposer):
		composer = foundComposer.group("composer");
		print "作曲：",composer;

	soup=BeautifulSoup(respHtmlb);
	lyrictag = soup.find(class_=re.compile("lrc_main"));
	lyrictag.Hidden=True
	lyric=str(lyrictag)
	lyricperfect=lyric.replace("<br/>","").replace("<div class=\"lrc_main\">","").replace("</div>","").replace("\r\n","\n").replace("\r","\n")
	print "歌词：",lyricperfect;

if __name__=="__main__":
	main();








