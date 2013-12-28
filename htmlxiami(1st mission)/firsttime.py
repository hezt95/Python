# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import urllib2
import re
def main():
	userMainUrl="http://www.xiami.com/song/1771343388";
	req = urllib2.Request(userMainUrl);
	req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36');
	resp = urllib2.urlopen(req);
	respHtml = resp.read();
	#print "respHtml=",respHtml; # you should see the ouput html
	#<a href="/album/545183" title="">Diamonds</a>
	#<div id="title"><h1>Diamonds</h1>
	foundMusic = re.search('<div id="title">([\s\S]*)<h1>(?P<music>.+?)</h1>',respHtml);
	#print "foundMusic=",foundMusic;
	if(foundMusic):
		music = foundMusic.group("music");
		print "music=",music;
	#<a href="/album/545183" title="">Diamonds</a>
	foundAlbum = re.search('<a href="/album/545183" title="">(?P<album>.+?)</a>',respHtml);
	#print "foundAlbum=",foundAlbum;
	if(foundAlbum):
		album = foundAlbum.group("album");
		print "album=",album;
	#<a href="/artist/23877" title="">Rihanna</a>
	foundSinger = re.search('<a href="/artist/23877" title="">(?P<singer>.+?)</a>',respHtml);
	#print "foundSinger=",foundSinger;
	if(foundSinger):
		singer = foundSinger.group("singer");
		print "singer=",singer;
	#<td class="item" valign="top">作曲：</td>
    #<td valign="top"><div style="white-space:nowrap; width:140px; overflow:hidden; text-overflow:ellipsis;">SIA FURLER / TOR HERMANSEN / MIKKEL ERIKSEN / BENJAMIN LEVIN</div></td>
	foundComposer = re.search('<td class="item" valign="top">作曲：</td>([\s\S]*)<div style="white-space:nowrap; width:140px; overflow:hidden; text-overflow:ellipsis;">(?P<composer>.+?)</div>',respHtml);
	#print "foundComposer=",foundComposer;
	if(foundComposer):
		composer = foundComposer.group("composer");
		print "composer=",composer;
if __name__=="__main__":
	main();

def main():
	url="http://www.xiami.com/song/playlist/id/1771343388/object_name/default/object_id/0";
	req = urllib2.Request(url);
	req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36');
	resp = urllib2.urlopen(req);
	respHtml = resp.read();
	foundLyricurl =re.search('<lyric>(?P<lyricurl>.+?)</lyric>',respHtml)
	#print "foundLyricurl=",foundLyricurl;
	if(foundLyricurl):
		lyricurl = foundLyricurl.group("lyricurl");
		print "lyricurl=",lyricurl;
if __name__=="__main__":
	main();
def main():
	html="http://www.xiami.com/song/1771343388";
	req = urllib2.Request(html);
	req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36');
	resp = urllib2.urlopen(req);
	respHtml = resp.read();
	soup=BeautifulSoup(respHtml);
	results = soup.find(class_=re.compile("lrc_main"));
	results.Hidden=True
	resultr=str(results)
	print resultr.replace("<br/>","").replace("<div class=\"lrc_main\">","").replace("</div>","")
	#print dir(results);
if __name__ == '__main__':
	main();