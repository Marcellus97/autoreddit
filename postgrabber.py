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
    if not os.path.exists('./data_files'):
        os.mkdir('./data_files')
    dir_path = datetime.datetime.now().strftime('./data_files/%m_%d_%y---%H-%M-%S/')
    os.mkdir(dir_path)
    post_num = 0
    for sub in reddit.front.top('day', limit=20):

        if sub.is_self:
            post_num += 1
            post_path = dir_path + '/' + str(post_num) + '/'
            os.mkdir(post_path)

            posts_file = open(post_path+ 'post.txt', 'w')
            posts_file.write(sub.selftext)

            posts_meta_file= open(post_path+ 'post_meta.txt', 'w')
            posts_meta_file.write('title: ' + sub.title + '\n')
            posts_meta_file.write('author: ' + sub.author.name+ '\n')
            posts_meta_file.write('subreddit: ' + sub.subreddit.display_name+ '\n')
            posts_meta_file.write('score ' + str(sub.score)+ '\n')
            posts_meta_file.write('ratio: ' + str(sub.upvote_ratio)+ '\n')
            posts_meta_file.write('url: ' + sub.url+ '\n')

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
