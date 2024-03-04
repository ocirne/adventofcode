import { readFileSync } from "fs";

class AocInput {

  readonly rawData: string;

  constructor(data: string) {
    this.rawData = data;
  }

  public firstLine(): string {
    return this.rawData;
  }   
}

function input(year: number, day: number): AocInput {
  const data = readFileSync(
            `../../adventofcode-input/resources/${year}/${day}/input`,
            "utf8",
          );
  return new AocInput(data);
}

function example(year: number, day: number, specifier: string=''): AocInput {
  const data = readFileSync(
            `../examples/${year}/${day}${specifier}.txt`,
            "utf8",
          );
  return new AocInput(data);
}

function direct(data: string): AocInput {
  return new AocInput(data);
}

export default AocInput;
export { input, example, direct };
