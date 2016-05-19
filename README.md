#Popular Electronics old issue autodownloader

Electronics and its trend can be analysed by reviewing the magzines whose audiences are the practioners of the art of Electronics.

One such famous magzine is popular electronics. 

Its old issues are archived in http://www.americanradiohistory.com/Popular-Electronics-Guide.htm . 

A typical URL for the pdf looks like this.

http://www.americanradiohistory.com/Archive-Poptronics/50s/56/Pop-1956-02.pdf

http://www.americanradiohistory.com/ is the base url. 

Pop-1956-02.pdf is the filename. 
This is extracted and using regex the `1956` token is extracted. Which is the issue year of this magzine. 

The script works roughly as follows

* This python script downloads the html file 
* uses beautiful soup and parses out all external link and finds the file with 'pdf' token, if any. 
* Filenames is sorted according to year of issue, into an dictonary. Where year is the key and value is the array of filenames pertaining to that year. 
* All the files of that particular event are downloaded using multithread and stored in one folder. 
* Next batch of files, of some other year is only started once this batch of files are downloaded. 

Dependency
* BeautifulSoup 
