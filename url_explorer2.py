
# objective:
# to return the link of first video in youtube search result page
# and ask to open the link in browser or not
import requests  # using request library for this purpose
import webbrowser

searchTerm = input("Enter the search term:")  # asking for search term
searchTerm = searchTerm.replace(' ', '+')
subStr = '/watch?v='  # sub-string used to find link in page source
# get the webpage and then convert to text
urlCode = requests.get(
    "https://www.youtube.com/results?search_query="+searchTerm).text

pos = urlCode.find(subStr)+9  # find the posn of first occrnce of 'substr'
# and adds 9 to index value to get video id

videoID = ""  # stores the video Id of first video
for i in range(pos, pos+11):  # find the video id through iteration
    videoID = videoID+urlCode[i]

link = "www.youtube.com"+subStr+videoID
print("Link to first video in your search page: "+link)

ask = input("Open in brwoser? [y/n]:")  # stores user's reply
if ask == 'Y'or ask == 'y':
    print("Opening...")
    webbrowser.open_new_tab(link)  # opens the link in new tab
elif ask == 'N'or ask == 'n':
    print("Okay...Bye!")
else:
    print("You have entered wrong choice!")
