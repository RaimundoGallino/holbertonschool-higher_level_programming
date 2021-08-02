#!/usr/bin/node

exports.callMeMoby = callMeMoby;

function (x, theFunction) {
    for (let i = 0; i < x; i++) {
        theFunction();
    }
}
