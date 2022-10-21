let input = require("fs").readFileSync("cidadesLista.txt", "utf8");
let lines = input.split(", ");

let values = [];
let uf = [];

for (let index = 0; index < lines.length; index++) {
  e = lines[index];
  e = e.toUpperCase();
  for (let j = 1; j < 10; j++) {
    e = e.replace(" ", "_");
  }
  let estado = e.substring(e.length - 4, e.length);
  estado = estado.replace("(", "");
  estado = estado.replace(")", "");
  uf.push(estado);
  e = e.substring(0, e.length - 5);
  e = e.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
  values.push(e);
}

let enume = "";
for (let index = 0; index < lines.length; index++) {
  enume +=
    "{ value: '" +
    values[index] +
    "', text: '" +
    lines[index].substring(0, lines[index].length - 5) +
    "', uf: '" +
    uf[index] +
    "' },\n";
}
require("fs").writeFileSync("cidadesEnum.js", enume);
