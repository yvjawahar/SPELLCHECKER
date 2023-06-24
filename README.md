# SPELLCHECKER
Tools and Technologies used: Python,HTML,CSS,JS
Intution:
Trie Data Structure
1)Trie Construction: The process_words function reads words from a file (specified by filename) and inserts them into the Trie data structure using the insert method. This step constructs the Trie by adding all the words from the wordlist file.

2)Spell Checking: When a user enters a word in the HTML form and clicks the "Check" button, the JavaScript function checkSpelling is called. It retrieves the input word, sends an AJAX request to the server, and waits for the response.

3)Server-side Spell Checking: The server receives the AJAX request at the /check route. It retrieves the word from the request parameters and performs a search in the Trie using the search method. If the word is found in the Trie, it responds with the message "Valid word"; otherwise, it responds with "Invalid word".

Link to dataset used: https://www-personal.umich.edu/~jlawler/wordlist.html <br>
To know more about Trie: https://www-personal.umich.edu/~jlawler/wordlist.html
