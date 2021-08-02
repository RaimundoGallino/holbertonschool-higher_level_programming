#!/usr/bin/node

exports.addMeMaybe  = addMeMaybe;

function addMeMaybe (number, theFunction) {
    for (let i = 0; i < number; i++) {
        number++;
        theFunction(number);
    }
}
