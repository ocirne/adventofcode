import { readFileSync, realpathSync } from "fs";

class AocInput {
  readonly rawData: string;

  constructor(data: string) {
    this.rawData = data;
  }

  public firstLine(): string {
    return this.rawData;
  }
}

function loadFile(path: string): string {
  console.log(realpathSync(path));
  return readFileSync(realpathSync(path), "utf8");
}

function loadResults(year: number): string {
  return loadFile(`${__dirname}/inputs/results${year}.csv`);
}

function loadInput(year: number, day: number): AocInput {
  return new AocInput(loadFile(`${__dirname}/inputs/${year}/${day}/input`));
}

function loadExample(
  year: number,
  day: number,
  specifier: string = "",
): AocInput {
  return new AocInput(
    loadFile(`${__dirname}/examples/${year}/${day}${specifier}.txt`),
  );
}

function direct(data: string): AocInput {
  return new AocInput(data);
}

export { AocInput, loadResults, loadInput, loadExample, direct };
