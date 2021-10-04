#! /usr/bin/python
import cgi
import random
print("Content-type: text/html")
print("")

form = cgi.FieldStorage()

reds = 0
whites = 0

if "answer" in form:
    answer = form.getvalue("answer")
else:
    answer = ""
    for i in range(4):
        answer += str(random.randint(0, 9))

if "guess" in form:
    guess = form.getvalue("guess")
    for key, digit in enumerate(guess):
        if digit == answer[key]:
            reds += 1
        else:
            for answerdigit in answer:
                if answerdigit == digit:
                    whites += 1
                break

else:
    guess = ""

if "numberOfGuesses" in form:
    numberOfGuesses = int(form.getvalue("numberOfGuesses"))+1
else:
    numberOfGuesses = 0

if numberOfGuesses == 0:
    message = "I have choosena 4 digit number can you guess it "
elif reds == 4:
    message = "Well  done.You got it in " + \
        str(numberOfGuesses)+" no of guesses.<a href=''>PLAY AGAIN </a>"
else:
    message = 'You have ' + str(reds) + ' correct digits in right place and ', str(
        whites) + ' correct digits in wrong place .You have had  ' + str(numberOfGuesses) + ' guesses.'

print('<h1>MasterMind</h1>')
print('<p1>', message, '</p1>')
print("<form>")
print('<input type="text" name="guess" value="' + guess+'">')
print('<input type="hidden" name="answer" value="'+answer+'">')
print('<input type="hidden" name="numberOfGuesses" value="' +
      str(numberOfGuesses)+'">')

print("<input type='submit' value='Guess'>")
print("</form>")
