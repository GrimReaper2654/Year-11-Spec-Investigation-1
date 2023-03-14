function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min) + min); // The maximum is exclusive and the minimum is inclusive
}

function replacemain(text) {
    document.getElementById("main").innerHTML = text;
};

function replaceControlPannel(text) {
    document.getElementById("controlPannel").innerHTML = text;
};


var presets = {numbers: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], letters: ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']};
var autoFill = true;
var n = 7;
var seq = [1,2,3,4,5,6,7];
var NPermutator = [2,3,4,5,6,7,1];

function autofill() {
    for (var i = 0; i < n; i += 1) {
        seq.push(presets.numbers[i]);
    }
}

function permutate() {
    var newseq = JSON.parse(JSON.stringify(seq));
    for (var i = 0; i < n; i += 1) {
        newseq[NPermutator[i]-1] = seq[i];
    }
    seq = newseq;
};

function reset() {
    n = parseInt(document.getElementById(`N`).value);
    autoFill = JSON.parse(document.getElementById(`Auto`).value);
    seq = JSON.parse('['+document.getElementById(`Sequence`).value+']');
    NPermutator = JSON.parse('['+document.getElementById(`Permutator`).value+']');
    if (autoFill) {
        autofill()
    }
};

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
};

async function main() {
    while (1) {
        await sleep(1000/30);
        var txt = `<h2>Sequence:  `;
        for (var i = 0; i < n; i += 1) {
            txt += ` ${seq[i]}`;
        }
        txt += `<br>Permutator:`;
        for (var i = 0; i < n; i += 1) {
            txt += ` ${NPermutator[i]}`;
        }
        txt += `</h2>`;
        replacemain(txt);
    }
};

main();