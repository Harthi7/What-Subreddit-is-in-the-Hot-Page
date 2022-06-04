#import the enviroemnt
from bs4 import BeautifulSoup
import requests
import time

def top_subs():
    # make a get request to inster in the BS4 function
    html_text = requests.get('https://www.reddit.com/').text
    # make a variable of the BS4 functions with the values inserted
    soup = BeautifulSoup(html_text, "lxml")
    # make a variable that specfies what info you want collected from the website
    subs = soup.find_all('a',class_='_3ryJoIoycVkA88fy40qNJc')
    # using a txt file to store the data collected with a time stamp
    with open('readme.txt', 'a') as f:
        f.write('\n')
        f.write(time.strftime('%Y/%m/%d %a %H:%M:%S'))
        f.write('\n')
    # make a for loop to split and clean the data collected into presenable str
    for sub in subs:
        list = ''
        list += str(sub)
        split_list = list.split()
        r_sub = split_list[3]
        r_sub_cut = r_sub[7::]
        when_to_cut = r_sub_cut[2::].find('/')
        r_sub_cut_cut = r_sub_cut[:when_to_cut+2:]
    # inside the for lopp the at the end of each loop the final form of the data will be stored in txt file
        with open('readme.txt', 'a') as f:
            f.write(r_sub_cut_cut)
            f.write("\n")

        print(r_sub_cut_cut)

if __name__ == '__main__':
    while True:
        top_subs()
        time.sleep(21600)
