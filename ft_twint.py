try:
    import twint
    import datetime
    # import pandas as pd
except RuntimeError:
    raise Exception("hello yassine")

# class Config_twint:
#     def __init__(self, keys=[], since="2019-12-27",until="2020-01-01", outfile="tweets33", path=None, custom=[]):
#         self.name_file = outfile
#         self.path_file = path
#         self.keys = custom
#         self.c = twint.Config()
#         self.c.Search = keys
#         self.c.Since = since
#         self.c.Until = until
#         self.c.Store_csv = True
#         self.c.Output = ".tweets" 
#         self.c.Hide_output = True

#     def slice_file(self):
#         df = pd.read_csv(".tweets.csv")
#         new_f = df[self.keys]
#         new_f.to_csv(self.name_file , index=False)


#     def ttrun(self):
#         twint.run.Search(self.c)
#         self.slice_file()


    
# def main():
#     ftrun = Config_twint(keys=["RAM_Maroc"],custom=["id",
#             "conversation_id",
#             "created_at",
#             "date",
#             "time",
#             "timezone",
#             "user_id",
#             "username",
#             "name"])
#     ftrun.ttrun()
if __name__ == "__main__":
    print("hello")
