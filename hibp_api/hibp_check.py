import requests
from texttable import Texttable
from misc.banner import banner, options

class BreachedAccount(object):

    def get_req(self, account):
        url = "https://haveibeenpwned.com/api/v2/breachedaccount/{account}".format(account=account)
        req = requests.get(url=url)
        data = req.json()
        return data

    def info(self, account):
        data = self.get_req(account)
        data_len = len(data)
        data_len = data_len - 1

        for info in range(data_len):
            added_date = data[info]['AddedDate']
            breach_date = data[info]['BreachDate']
            data_class = data[info]['DataClasses']
            descript = data[info]['Description']
            domain = data[info]['Domain']
            pwn_count = data[info]['PwnCount']
            name = data[info]['Name']

            info_table = Texttable()
            info_table.set_deco(Texttable.BORDER | Texttable.HEADER | Texttable.HLINES | Texttable.VLINES)
            info_table.set_cols_align(["l", "l"])
            info_table.set_cols_width([10, 67])

            desc_table = Texttable()
            desc_table.set_deco(Texttable.BORDER | Texttable.HEADER | Texttable.HLINES)
            desc_table.set_cols_align(["l"])
            desc_table.set_cols_width([80])

            info_table.add_rows([["Item", "Info"],
                                ["Account Refrenced", account],
                                ["Domain Breached", domain],
                                ["Data Breached", data_class],
                                ["Breach Date", breach_date],
                                ["Account Vulnerable Estimate", pwn_count]])

            desc_table.add_row(["Description"])
            desc_table.add_row([[descript]])
            print(info_table.draw())
            print(desc_table.draw() + "\n")


while True:
    print(banner)
    print(options)
    action = int(input(""))
    if action == 1:
        email = input("\nPlease Enter Email:\n")
        hibp = BreachedAccount()
        hibp.info("e.rawkz@gmail.com")
    elif action == 0:
        break