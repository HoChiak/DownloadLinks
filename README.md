# Donwload Links
Little python tool to download links of a given 'filetype' (e.g. 'pdf' or 'txt') automatically from a homepage. Just enter the "web link" and the "local path" to save the files and the tool will download all available Links having the given filetype on the homepage.


# How to
## 1. Import necassary tool
Download and save the 'link_to_file.py' code from this repository. Import this file into your Python Application (make sure you import from the correct folder).
```ruby
import link_to_file as ltf
```
## 2. Specify parameters
link:     Define from which homepage you want download.

path:     Specify where you wanna save the downloaded files.

filetype: Specify which filetype you want download.
```ruby
link = r'http://www.ima.uni-stuttgart.de/studium/stud_arbeiten/bereich_zuv/index.html'
path = r'C:\User\%Username%\Downloads'
filetype='pdf'
```

## 3. Execute tool
```ruby
instance = ltf.Weblink(link)  # create instance
instance.fetch_links(filetype)  # fetch all available child-links from given link
instance.download_links(path)  # download the fetched Links
```
