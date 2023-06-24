from bottle import Bottle, request

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

def process_words(filename):
    trie = Trie()
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()
            trie.insert(word)
    return trie

filename = "wordlist.txt"  # Replace with the path to your file
trie = process_words(filename)

app = Bottle()

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
                margin: 0;
                padding: 0;
            }
            
            .container {
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                background-color: #fff;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            }
            
            h1 {
                text-align: center;
                color: #333;
            }
            
            form {
                text-align: center;
                margin-top: 20px;
            }
            
            input[type="text"] {
                padding: 10px;
                width: 80%;
                font-size: 16px;
            }
            
            input[type="submit"] {
                padding: 10px 20px;
                background-color: #4CAF50;
                color: #fff;
                border: none;
                font-size: 16px;
                cursor: pointer;
            }
            
            .result {
                text-align: center;
                margin-top: 20px;
                font-size: 18px;
            }
            
            .valid {
                color: green;
            }
            
            .invalid {
                color: red;
            }
        </style>
        <script>
            function checkSpelling() {
                var wordInput = document.getElementById('wordInput');
                var resultDiv = document.getElementById('resultDiv');
                var word = wordInput.value;
                var result = document.createElement('div');
                
                if (word) {
                    // Send an AJAX request to the server
                    var xhr = new XMLHttpRequest();
                    xhr.onreadystatechange = function() {
                        if (xhr.readyState === 4 && xhr.status === 200) {
                            var response = xhr.responseText;
                            result.textContent = response;
                            if (response === 'Valid word') {
                                result.classList.add('valid');
                            } else {
                                result.classList.add('invalid');
                            }
                        }
                    };
                    xhr.open('POST', '/check', true);
                    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
                    xhr.send('word=' + encodeURIComponent(word));
                }
                
                // Clear the input field
                wordInput.value = '';
                
                // Clear the previous result
                resultDiv.innerHTML = '';
                
                // Display the new result
                resultDiv.appendChild(result);
            }
        </script>
    </head>
    <body>
        <div class="container">
            <h1>Spell Checker</h1>
            <form>
                <input type="text" id="wordInput" placeholder="Enter a word">
                <br>
                <input type="button" value="Check" onclick="checkSpelling()">
            </form>
            <div id="resultDiv" class="result"></div>
        </div>
    </body>
    </html>
    '''

@app.route('/check', method='POST')
def check_spelling():
    word = request.forms.get('word')
    result = trie.search(word)
    if result:
        return "Valid word"
    else:
        return "Invalid word"

if __name__ == '__main__':
    app.run(host='localhost', port=8080)
