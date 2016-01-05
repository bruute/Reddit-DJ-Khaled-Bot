import praw

r = praw.Reddit(user_agent = "DJ Khaled Bot by bruute")
print("Logging in.. Bless UP!")
r.login()

words_to_match = ['smart']
cache = []

def run_bot():
	print ("Grabbbing they..."})
    subreddit = r.get_subreddit("all")
    print ("Grabbing the keys to success...")
    comments = subreddit.get_comments(limit = 4000)
    for comment in comments: 
    	comment_text = comment.body.lower()
    	isMatch = any(string in comment_text for string in words_to_match)
    	if comment.id not in cache and isMatch: 
    		print ("Found the keys to success...")
    		comment.reply("http://imgur.com/Yr27m3a")
    		cache.append(comment.id)
    print ("Finished program. They don't want you to sleep...")

while True:
	run_bot()
	time.sleep(10)
