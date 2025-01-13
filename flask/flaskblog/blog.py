import json 
from slugify import slugify
from datetime import datetime 

class Blog:
	
	def __init__(self):
		with open("posts.json") as f:
			self.posts = json.load(f)

		for post in self.posts:
			post["slug"] = slugify(post["title"])
			post["datepublished"] = datetime.strptime(post["published"], '%m/%d/%Y')

	def getPosts(self):
		return self.posts

	def getPost(self, slug):
		for post in self.posts:
			if post["slug"] == slug:
				return post
