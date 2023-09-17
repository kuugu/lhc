LHC is an EPUB reader 

TODO: 
- Looks like the EPUB fileformat uses CSS to style the components, so rendering it in the browser seems a good option 
- extract and store the unzipped folder in /tmp/lhc 
- get the rootfile location from META_INF/container.xml 
- parse the manifest for a listing of all files and their ids 
- parse the spine to get the table of contents and linear reading order of the files. 
- start with book cover, right key for next page, left key for previous page 
- keyboard key 'C' to jump to contents 