const leftHand = require("fs").readFileSync(
  "c:\\Users\\Ismael\\prog1\\cleaner\\leftHand.txt",
  { encoding: "utf8" }
);

let palavras = leftHand.split(" ");

let palavrasA = [];
let palavrasB = [];
let palavrasC = [];
let palavrasD = [];
let palavrasE = [];
let palavrasF = [];
let palavrasG = [];
let palavrasQ = [];
let palavrasR = [];
let palavrasS = [];
let palavrasT = [];
let palavrasV = [];
let palavrasW = [];
let palavrasX = [];
let palavrasZ = [];

palavras.forEach((e) => {
  switch (e.charAt(0)) {
    case "a":
      palavrasA.push(e);
      break;
    case "b":
      palavrasB.push(e);
      break;
    case "c":
      palavrasC.push(e);
      break;
    case "d":
      palavrasD.push(e);
      break;
    case "e":
      palavrasE.push(e);
      break;
    case "f":
      palavrasF.push(e);
      break;
    case "g":
      palavrasG.push(e);
      break;
    case "q":
      palavrasQ.push(e);
      break;
    case "r":
      palavrasR.push(e);
      break;
    case "s":
      palavrasS.push(e);
      break;
    case "t":
      palavrasT.push(e);
      break;
    case "v":
      palavrasV.push(e);
      break;
    case "w":
      palavrasW.push(e);
      break;
    case "x":
      palavrasX.push(e);
      break;
    case "z":
      palavrasZ.push(e);
      break;
    default:
      null;
  }
});

function remove(element, array) {
  const newArray = array.filter((e) => !(e == element));
  return newArray;
}

function removeRandom(finalSize, array) {
  let newArray = array;
  while (newArray.length > finalSize) {
    const elementId = Math.floor(Math.random() * array.length);
    const element = array[elementId];
    newArray = remove(element, newArray);
  }
  return newArray;
}

palavrasA = removeRandom(37, palavrasA);
palavrasB = removeRandom(16, palavrasB);
palavrasC = removeRandom(21, palavrasC);
palavrasD = removeRandom(16, palavrasD);
palavrasE = removeRandom(34, palavrasE);
palavrasF = removeRandom(34, palavrasF);
palavrasG = removeRandom(21, palavrasG);
palavrasR = removeRandom(16, palavrasR);
palavrasS = removeRandom(69, palavrasS);
palavrasT = removeRandom(11, palavrasT);
palavrasV = removeRandom(6, palavrasV);
palavrasW = removeRandom(80, palavrasV);

palavras = [].concat(
  palavrasA,
  palavrasB,
  palavrasC,
  palavrasD,
  palavrasE,
  palavrasF,
  palavrasG,
  palavrasQ,
  palavrasR,
  palavrasS,
  palavrasT,
  palavrasV,
  palavrasW,
  palavrasX,
  palavrasZ
);

require("fs").writeFileSync("reducedLeftHand.txt", palavras.join(" "));
console.log(palavras.length);

const rightHand = require("fs").readFileSync(
  "c:\\Users\\Ismael\\prog1\\cleaner\\rightHand.txt",
  { encoding: "utf8" }
);

let palavrasDir = rightHand.split(" ");
let palavrasEsq = palavras;

let palavrasTotal = [];

for (let i = 0; i < palavrasDir.length; i++) {
  if (i % 2 == 0) {
    palavrasTotal.push(palavrasEsq[i]);
  } else {
    palavrasTotal.push(palavrasDir[i]);
  }
}

for (let j = palavrasDir.length; j < palavrasEsq.length; j++) {
  palavrasTotal.push(palavrasEsq[j]);
}

require("fs").writeFileSync("bothHands.txt", palavrasTotal.join(" "));
console.log(palavrasTotal.length);
