const fs = require("fs");

const args = process.argv.slice(2);

let showAll = false;
let path = ".";

for (const arg of args) {
  if (arg === "-1") {
    // One entry per line is the required format.
  } else if (arg === "-a") {
    showAll = true;
  } else {
    path = arg;
  }
}

let entries = fs.readdirSync(path);

if (showAll) {
  entries = [".", "..", ...entries];
} else {
  entries = entries.filter((entry) => !entry.startsWith("."));
}

entries.sort();

for (const entry of entries) {
  console.log(entry);
}
