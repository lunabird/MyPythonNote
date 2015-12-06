# -*- coding:utf-8 -*-
class Song(object):

	def __init__(self,lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

lyric = ["Hello I'm lunabird", "I watch to the We bare bears recently",
		"Oh, forget to tell you", "That's a cartoon series"]

happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])

bulls_on_parada = Song(["They really around the family",
						"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parada.sing_me_a_song()

#新建一个lunabird_song对象，调用该对象的sing_me_a_song()方法
lunabird_song = Song(lyric)
lunabird_song.sing_me_a_song()