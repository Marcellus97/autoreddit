import praw
import datetime
import os

secret_file = open ("secret.txt")

USERAGENT = secret_file.readline().strip()
ID = secret_file.readline().strip()
SECRET = secret_file.readline().strip()
USERNAME = secret_file.readline().strip()
PASSWORD = secret_file.readline().strip()

secret_file.close()

reddit = praw.Reddit(client_id=ID,
		client_secret=SECRET,
		user_agent=USERAGENT,
		username=USERNAME,
		password=PASSWORD)
def main():
	dir_path = datetime.datetime.now().strftime('./%m_%d_%y---%H-%M-%S/')
	os.mkdir(dir_path)

	post_num = 0
	for sub in reddit.front.top('day', limit=20):

		if sub.is_self:
			post_num += 1
			post_path = dir_path + '/' + str(post_num) + '/'
			os.mkdir(post_path)

			posts_file = open(post_path+ 'post.csv', 'w')
			posts_file.write('title,')
			posts_file.write('name,')
			posts_file.write('text\n')

			posts_file.write(sub.title + '\n')
			posts_file.write(sub.name + '\n')
			posts_file.write(sub.selftext + '\n')

			sub.comment_limit = 20
			sub.comments.replace_more(limit=0)
			com_num = 0
			for c in sub.comments:
				com_num += 1
				comment_file = open(post_path+ 'comment' + str(com_num) + '.txt', 'w')
				comment_file.write(c.body)
				comment_file.close()
	posts_file.close()
main()
