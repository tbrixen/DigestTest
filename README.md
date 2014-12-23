Readme
---

Checks if the digest of words in a wordlist starts with 0e.

Motivation
---

This was due to an easy to implement type-juggeling bug in PHP code, where two hashes were equal in php if one only used `==` and not `===` when implementing the check. 

For a string 0e42 PHP interprets this a 0 exponentiated to 42. Meaning that `0e42 == 0e24`. 

Example of the bug can be found [here](http://pen-testing.sans.org/blog/pen-testing/2014/12/18/php-weak-typing-woes-with-some-pontification-about-code-and-pen-testing).

Usage
----

    digestTest.py <wordlist> <md5|sha1>

The words.txt contain examples of words with a digest that start wth `0e` for both md5 and sha1

    python digestTest.py words.txt md5

    python digestTest.py words.txt sha1
