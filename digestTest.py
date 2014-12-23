"""
Checks if the digest of words in a wordlist starts with 0e, such that
a type-juggeling bug in php code cam be exploited. More info
http://pen-testing.sans.org/blog/pen-testing/2014/12/18/php-weak-typing-woes-with-some-pontification-about-code-and-pen-testing
"""
import hashlib
import re
import sys


def main():

    if not checkArguments():
        print 'digestTest.py <wordlist> <md5|sha1>'
        sys.exit(2)

    wordlist = sys.argv[1]
    digestFunction = sys.argv[2]

    print "Using wordlist: '" + wordlist + "'"
    print

    with open(wordlist) as f:
        for line in f:
            checkDigest(line.rstrip(), digestFunction)


def checkDigest(string, algo):
    if algo == "md5":
        digest = hashlib.md5(string).hexdigest()
    else:
        digest = hashlib.sha1(string).hexdigest()

    if re.match('0+[eE]+\d+$', digest):
        print string


def checkArguments():
    if len(sys.argv) != 3:
        return False

    algo = sys.argv[2]
    if not (algo != "md5" or algo != "sha1"):
        return False

    return True


if __name__ == "__main__":
    main()
