import twint
import datetime

class Config:
    def __init__(self, keys=[], since="2019-11-07",until="2020-01-01", outfile="tweets", custom=[]):
        self.c = twint.Config()
        self.c.Search = keys
        self.c.Since = since
        self.c.Until = until
        self.c.Store_csv = True
        self.c.Output = "./" + outfile
        self.c.Hide_output = True
        self.c.Custom = ["date", "time", "username", "tweet", "link", "likes", "retweets", "replies", "mentions", "hashtags"]
    
    def run(self):
        twint.run.Search(self.c)
    
def main():
    run = Config(keys=["RAM_Maroc"],custom=["id",
            "conversation_id",
            "created_at",
            "date",
            "time",
            "timezone",
            "user_id",
            "username",
            "name"])
    run.run()
if __name__ == "__main__":
    main()


# import twint
# import pandas
# import datetime


# def scrape_reply(keywords, since, outfile):
#     c = twint.Config()
#     c.Search = keywords
#     c.Since =  '2019-11-07' #since
#     c.Until = '2020-12-18'
#     c.Store_csv = True
#     c.Output = "./" + outfile
#    # c.Near = city
#     c.Hide_output = True
#     # c.Custom_csv = ["id", "user_id", "username", "tweet"]
#    # c.Count = True
#     # c.Limit = 1000
#     #c.Stats = True
#    # c.Resume = 'resume.txt'
#     twint.run.Search(c)


# def get_date():
#     # return str(datetime.datetime.now() - datetime.timedelta(1))
#     return "2020-12-02"


# def main():
#     # print(get_date())
#     scrape_reply("RAM_Maroc",get_date() , 'repies_with_twint.csv')


# if __name__ == "__main__":
#     main()
