import pandas as pd

list_emails = pd.read_excel("Excel_File_Emails.xlsx")

emails = [email for email in list_emails["All_Emails"]]

