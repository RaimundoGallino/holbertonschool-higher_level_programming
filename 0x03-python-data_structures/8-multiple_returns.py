#!/usr/bin/python3
ef multiple_returns(sentence):
    if sentence:
        return (len(sentence), sentence[0])
    else:
        return 0, None
