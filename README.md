# readability-score
A program that determines the difficulty of a text and predicts the grade level needed to understand this text.

About
We all love different kinds of books. As we grow up, we are able to digest more difficult texts easier. How to assess the difficulty of a given text? How can you make your program do that? Write a program that determines the difficulty of a text and predicts the grade level needed to understand this text.

Learning outcomes
Learn to call programs from the command line and gain experience with regexes and math library.

# Stage 1/5: Simple estimation
https://hyperskill.org/projects/155/stages/808/implement
Input a phrase or a sentence for the program to determine the difficulty based on the symbol count.

Description
Have you ever wondered how to measure whether the text is hard or easy? The task is pretty simple if you're a human — read the text to see if you're struggling or not. However, it is a bit more complicated with computers.

Do not lemmatize.
Let's create a simple program. If a text contains more than 100 symbols (including spacebars and punctuation marks) then mark this text as HARD. If the text contains exactly 100 symbols (or less) mark it as EASY.

Objectives
Read the text from the user input.
Count the symbols in the text.
Output the result.
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1
> This text is simple to read!
EASY  

Example 2
> This text is hard to read. It contains a lot of sentences as well as a lot of words in each sentence.
HARD                                                                                                   

# Stage 2/5: Words and sentences
https://hyperskill.org/projects/155/stages/809/implement
Apply your knowledge of advanced strings, arrays, and regular expressions. Determine the text difficulty by calculating the average word count in the sentences.

Description
The real text can be pretty long (or at least more than 100 characters) and still can be easy to read. We need another approach for such texts. Let's calculate the number of words in each sentence. If each sentence of the text contains a lot of words then this text is hard to read.

Suppose that if the text contains more than 10 words per sentence on average, then this text is HARD. If the average is equal to 10 or less, then the text should be considered EASY . Don't worry, we will refer to more scientific ways in the next stages.

Don't forget that the sentences can end with a dot as well as with an exclamation mark and a question mark. But the last sentence may not have a punctuation mark at the end.
Regular expressions might be useful here.
Objectives
Read the text from the user input.
Count the words in every sentence.
Count the average amount of words in the sentences.
Output the result.
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1
The first example contains two sentences with 6 and 10 words (numbers also counts as words), so the average is 8.
> This text is simple to read! It has on average less than 10 words per sentence.
EASY                                                                             
Example 2
The second example also contains 2 sentences with 6 and 16 words. The average is 11.
> This text is hard to read. It contains a lot of sentences as well as a lot of words in each sentence
HARD   


# Stage 3/5: What's the score?
https://hyperskill.org/projects/155/stages/810/implement
Add a readability score based on a special formula. Estimate the difficulty of larger texts uploaded from a file.

Description
In this stage, you need to implement the Automated Readability Index. It was introduced in 1968 and was proved to be very reliable. The index is calculated with the following formula:

score = 4.71*{ characters \over words} + 0.5 * {words \over sentences} - 21.43score=4.71∗ 
words
characters
​
 +0.5∗ 
sentences
words
​
 −21.43

The table below contains scores and the corresponding age for the score described above.

1	about 5-6-year-olds
2	about 7-8-year-olds
3	about 7-9-year-olds
4	about 9-10-year-olds
5	about 10-11-year-olds
6	about 11-12-year-olds
7	about 12-13-year-olds
8	about 13-14-year-olds
9	about 14-15-year-olds
10	about 15-16-year-olds
11	about 16-17-year-olds
12	about 17-18-year-olds
13	about 18-24-year-olds
14	about 25-year-olds
In this stage, your program should read a file with a text. Pass the filename through command line arguments. The program should output the score and an approximate age needed to comprehend the text. Round the resulting score up to output the correct age bracket. Print how many characters, words, and sentences the text contains. Characters are any visible symbol (everything except spaces , new lines \n, or tabulations \t). The text can contain multiple lines. Analyze each of them.

Objectives
Read the text from the user input.
Count the number of characters, words, and sentences in the text.
Calculate the score according to the formula.
Output the result.
Print the information in the way, shown in the examples.
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1
> python3 readabilityscore.py --infile in.txt
The text is:
Readability is the ease with which a reader can understand a written text. In natural language, the readability of text depends on its content and its presentation. Researchers have used various factors to measure readability. Readability is more than simply legibility, which is a measure of how easily a reader can distinguish individual letters or characters from each other. Higher readability eases reading effort and speed for any reader, but it is especially important for those who do not have high reading comprehension. In readers with poor reading comprehension, raising the readability level of a text from mediocre to good can make the difference between success and failure

Words: 108
Sentences: 6
Characters: 580
The score is: 12.86
This text should be understood by 18-24-year-olds.

Example 2
> python3 readabilityscore.py --infile in.txt
The text is:
This is the page of the Simple English Wikipedia. A place where people work together to write encyclopedias in different languages. That includes children and adults who are learning English. There are 142,262 articles on the Simple English Wikipedia. All of the pages are free to use. They have all been published under both the Creative Commons License 3 and the GNU Free Documentation License. You can help here! You may change these pages and make new pages. Read the help pages and other good pages to learn how to write pages here. You may ask questions at Simple talk.

Words: 100
Sentences: 10
Characters: 476
The score is: 5.98
This text should be understood by 11-12-year-olds.


# Stage 4/5: More formulas!
https://hyperskill.org/projects/155/stages/811/implement
Let's implement more variables into our score formulas — syllables and letters.

Description
In this stage, we will refer to other scientific approaches to readability.

Take one more look at different grade levels/age brackets and corresponding scores. You can use the Wikipedia article on ARI. The table is suitable for all the algorithms described in this stage. To calculate the age, use the upper bound range. For example, if the range is 12-13-year-olds then the upper bound is 13-year-olds.

If the score is 14 or more in this project, regard the age to be equal 25.
The first algorithm is the Flesch-Kincaid Readability Test. First, you need to create a function that calculates the number of syllables in a word. The formula is given below. You can find more information about the F-K tests in the article by Readability Formulas. You can use the second formula to calculate the index; it allows you to calculate the age of a person using the same table from the Automated Readability Index.

score = 0.39 * {words \over sentences} + 11.8 * {syllables \over words} - 15.59score=0.39∗ 
sentences
words
​
 +11.8∗ 
words
syllables
​
 −15.59

The second algorithm is the SMOG Index. It stands for Simple Measure of Gobbledygook. To calculate it, you need to count the number of polysyllables (words with more than two syllables). The formula is shown below. You can find out more in the article by Readability Formulas. Use the abovementioned table from the first link to calculate the age bracket.

score = 1.043 * \sqrt{polysyllables \ * \ 30 \over sentences} + 3.1291score=1.043∗ 
sentences
polysyllables ∗ 30
​
 
​
 +3.1291

The next one is the Coleman-Liau Index. The formula is given below. As usual, refer to the Readability Formulas article for more info. L is the average number of characters per 100 words, S is the average number of sentences per 100 words. Like with other indexes, the result is a minimum grade level required to understand this text.

score = 0.0588 \ ∗ \ L−0.296 \ ∗ \ S\ −\ 15.8score=0.0588 ∗ L−0.296 ∗ S − 15.8

In this stage, implement all three approaches to your program. Don't forget about the Automated Readability Index! You should also implement an option to choose all the methods at the same time.

To count the number of syllables, use the letters a, e, i, o, u, y as vowels. You can use four simple rules to count the syllables:

1. Count the number of vowels in the word.
2. Omit the so-called double vowels (for example, "rain" has 2 vowels but only 1 syllable).
3. Subtract the silent vowels (for example, "e" in "side" is silent, the word has only 1 syllable).
4. If it turns out that the word contains 0 vowels, then consider this word a monosyllable.

Objectives
Read the text from the user input.
Count the number of characters, syllables, polysyllables, words, and sentences in the text.
Count the scores according to the formulas above.
Add an option to choose the metrics to display.
Count the average score.
Print the information in the way, shown in the examples.

Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.
> python3 readabilityscore.py --infile in.txt
The text is:
This is the front page of the Simple English Wikipedia. Wikipedias are places where people work together to write encyclopedias in different languages. We use Simple English words and grammar here. The Simple English Wikipedia is for everyone! That includes children and adults who are learning English. There are 142,262 articles on the Simple English Wikipedia. All of the pages are free to use. They have all been published under both the Creative Commons License and the GNU Free Documentation License. You can help here! You may change these pages and make new pages. Read the help pages and other good pages to learn how to write pages here. If you need help, you may ask questions at Simple talk. Use Basic English vocabulary and shorter sentences. This allows people to understand normally complex terms or phrases.

Words: 137
Sentences: 14
Characters: 687
Syllables: 210
Polysyllables: 17
Enter the score you want to calculate (ARI, FK, SMOG, CL, all): all

Automated Readability Index: 7.08 (about 13-year-olds).
Flesch–Kincaid readability tests: 6.31 (about 12-year-olds).
Simple Measure of Gobbledygook: 9.42 (about 15-year-olds).
Coleman–Liau index: 10.66 (about 17-year-olds).

This text should be understood in average by 14.25-year-olds.


# Stage 5/5: Frequency Inc.
https://hyperskill.org/projects/155/stages/812/implement
Use a comprehensive formula, based on the amount of difficult (rare) words, taken from the corpora.

Description
Now you know different formulas to find the readability score. However, none of them takes into account one of the most important metrics — the word frequency. Let's fix it!

In 1948, Edgar Dale and Jeanne Chall invented a formula that determines how difficult a text is according to the number of words that are, most likely, unknown to readers. The formulas we referred to earlier based the score on the number of words and sentences only. Our new formula looks like this:

score = 0.1579 * {difficult \ words \over words} * 100 + 0.0496 * {words \over sentences}score=0.1579∗ 
words
difficult words
​
 ∗100+0.0496∗ 
sentences
words
​
 

If the amount of difficult (that is, unknown to readers) words is less than 5%, the score does not need any adjustment. Otherwise, you need to add 3.6365 to the score. If you are interested, you can learn more about this formula on the Readability Formulas site.

Originally, "difficult words" were the ones that had not been included in the word list developed by the authors of the formula. We do not know for certain, what was on that list, so we will use the so-called "Longman Communication 3000". It is a list of the 3000 most frequent words in English, based on a statistical analysis of a very large number of texts. It will be given to you as a separate file with each word on a new line.

The table below contains scores and the corresponding grade level for the score described above.

4.9 or lower	about 10-year-olds
5.0–5.9	about 12-year-olds
6.0–6.9	about 14-year-olds
7.0–7.9	about 16-year-olds
8.0–8.9	about 18-year-olds
9.0–9.9	
about 24-year-olds

If the score is 10 or more in this project, regard the age to be equal 25 for all the metrics, except for the last one.
Objectives
Read the text from the file named 'in.txt'.
Read the difficult words from another file, named 'words.txt'.
Count the number of words, "difficult words", sentences, characters, syllables, and polysyllables in the text.
Count the scores according to the formulas above, including the new one.
Add an option to choose the metrics to display.
Count the average score.
Print the information in the way, shown in the examples.
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1

>python3 readability.py --infile in.txt --words words.txt
The text is:
Readability is the ease with which a reader can understand a written text. In natural language, the readability of text depends on its content and its presentation. Researchers have used various factors to measure readability. Readability is more than simply legibility, which is a measure of how easily a reader can distinguish individual letters or characters from each other. Higher readability eases reading effort and speed for any reader, but it is especially important for those who do not have high reading comprehension. In readers with poor reading comprehension, raising the readability level of a text from mediocre to good can make the difference between success and failure.

Words: 108
Difficult words: 25
Sentences: 6
Characters: 580
Syllables: 200
Polysyllables: 25
Enter the score you want to calculate (ARI, FK, SMOG, CL, PB, all): all

Automated Readability Index: 12.86 (about 18-year-olds)
Flesch–Kincaid readability tests: 13.28 (about 24-year-olds)
Simple Measure of Gobbledygook: 14.79 (about 25-year-olds)
Coleman–Liau index: 14.13 (about 25-year-olds)
Probability-based score: 8.18 (about 18-year-olds)

This text should be understood in average by 22.0-year-olds.

