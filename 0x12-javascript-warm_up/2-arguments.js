#!/usr/bin/node
const args = process.argv.length;

if (args == 0) {
    console.log('No Arguments');
}
if (args == 1) {
    console.log('Argument found')
}
if (args == 2) {
    console.log('Arguments found')
}
