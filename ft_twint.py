# try:
import twint
import datetime
import pandas as pd
# except RuntimeError:
#     import sys; sys.exit() from threading import Timer, Thread

class File:
    def __init__(self, list_file=[],name_file=""):
        self.list_file = list_file
        self.name_file = name_file

    def sum_file(self):
        data_files = []
        for name in self.list_file:
            df = dp.read_csv(name)
            data_files.append(df)
        df_all = pd.concat(data_files)
        df.to_csv(self.list_file, index=False)



class Config_twint:
    def __init__(self, keys=[], since="2018-12-29",until="2019-01-01", outfile="tweets33", custom=[]):
        print("yassine  ttkeys ", keys)
        print("ttsince ", since)
        print("ttuntil ", until)
        print("ttoutfile", outfile)
        print("ttcustom ", custom)  
  
        # self.name_file = outfile
        # self.keys = custom
        self.c = twint.Config()
        self.c.Search = keys
        self.c.Since = since
        self.c.Until = until

        # self.c.Search = ["@RAM_Maroc"]#keys
        # self.c.Since = "2019-11-01" ##since
        # self.c.Until = "2019-11-09" #until
        # self.c.Lang = "en"
        # self.c.Limit = 100
        self.c.Store_csv = True
        self.c.Output = outfile
        # "tweets.csv" 
        self.c.Hide_output = True
        
    # def slice_file(self):
    #     df = pd.read_csv(".tweets.csv")
    #     new_f = df[self.keys]
    #     new_f.to_csv(self.name_file , index=False)


    def run(self):
        pass
        twint.run.Search(self.c)
#         # self.slice_file()



# def main():
#     run = Config_twint(keys=["RAM_Maroc"],custom=["id",
#             "conversation_id",
#             "created_at",
#             "date",
#             "time",
#             "timezone",
#             "user_id",
#             "username",
#             "name"])
#     run.run()
# if __name__ == "__main__":
#     main()

# import twint

# c = twint.Config()
# c.Username = "noneprivacy"
# c.Limit = 100
# c.Store_csv = True
# c.Output = "none.csv"
# c.Lang = "en"
# # c.Translate = True
# # c.TranslateDest = "it"
# twint.run.Search(c)