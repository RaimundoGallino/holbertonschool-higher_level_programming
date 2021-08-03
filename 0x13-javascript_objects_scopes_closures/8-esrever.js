#!/usr/bin/node

exports.esrever = function (list) {

    var revArray = new Array;
    for(var i = list.length - 1; i >= 0; i--) {
        revArray.push(list[i]);
    }
    return revArray;
}
