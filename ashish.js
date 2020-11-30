// your code goes here
function getRandomString(length) {
    var randomChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    var randomNums = '0123456789';
    var result = '';
    result += randomChars.charAt(Math.floor(Math.random() * randomChars.length));
    for ( var i = 0; i < length-1; i++ ) {
        result += randomNums.charAt(Math.floor(Math.random() * randomNums.length));
    }
    return result;
}
res = getRandomString(6)
console.log(res);