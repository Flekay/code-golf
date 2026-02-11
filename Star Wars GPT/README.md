 You are given a series of inputs. Each input contains a text corpus and 12 prompt words on subsequent lines. For each prompt, output the word which most frequently follows it in the corpus. In case of a tie, print the one whose first follow-on occurrence comes earliest.

For example, suppose the corpus is "code golf and golf and code" and the prompt is "and". Both "golf" and "code" follow the word "and" maximally frequently (once), but "golf" does so first, and so the output is "golf".

In this problem, each corpus is formed by concatenating two Star Wars Opening Crawl texts together (separated by one space). 
