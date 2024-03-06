import AocInput from './AocInput';

const year = 2015;
const day = 9;

function readGraph(input: AocInput): { count: number, distances: Map<number, number> } {
  const nodesSet = new Set<string>();
  input.rawData.trim().split("\n").forEach(line => {
    const [ n1, , n2, ] = line.split(" ");
    nodesSet.add(n1);
    nodesSet.add(n2);
  });
  const nodes = Array.from(nodesSet);
  const count = nodes.length;
  const distances = new Map<number, number>();
  input.rawData.trim().split("\n").forEach(line => {
    const [ n1, , n2, , ds ] = line.split(" ");
    const d = parseInt(ds);
    const i1 = nodes.indexOf(n1);
    const i2 = nodes.indexOf(n2);
    distances.set(i1 * count + i2, d);
    distances.set(i2 * count + i1, d);
  });
  return { count, distances };
}

function swap(a: Array<number>, i1: number, i2: number) {
  [a[i1], a[i2]] = [a[i2], a[i1]];
}

/** https://en.wikipedia.org/wiki/Heap%27s_algorithm */
function* permutations(n: number): Generator<Array<number>>  {
  let a = Array.from(Array(n).keys());
  // let a = Array.from({length: n}, (value, key) => key);
  let c = Array.from({length: n}, (value, key) => 0);
  for (let i = 0; i < n; i ++) {
      c[i] = 0;
  }
  yield a;
    
  let i = 1;
  while (i < n) {
      if (c[i] < i) {
          if (i % 2 == 0) {

              swap(a, 0, i);
      } else {
              swap(a, c[i], i);
      }
            yield a;
            c[i] ++;
            i = 1;
      } else {
            c[i] = 0;
            i++;
      }
  }

}


function findDistance(distances: Map<number, number>, count: number, path: Array<number>): number {
  let total_distance = 0;
  for (let i = 1; i < path.length; i++) {
    total_distance += distances.get(path[i-1] * count + path[i])!;
  }
 // console.log(total_distance);
  return total_distance;
}

const reduce = (f: any, i: any, it: any) => {
  let o = i

  for (let x of it)
    o = f (o, x)

  return o
}

const xs = [1, 2, 3]

const xs_ = {
  [Symbol.iterator]: function* () {
    yield 1
    yield 2
    yield 3
  }
}

//const output1 = reduce ((o, x) => o + x, 10, xs)
//const output2 = reduce ((o, x) => o + x, 10, xs_)

function part1(input: AocInput): number {
  const { count, distances } = readGraph(input);
//  console.log(count);
//  console.log(distances);
  return reduce((acc, p) => Math.min(acc, findDistance(distances, count, p)), 100000, permutations(count));
}

function part2(input: AocInput): number {
  const { count, distances } = readGraph(input);
//  console.log(count);
//  console.log(distances);
  return reduce((acc, p) => Math.max(acc, findDistance(distances, count, p)), 0, permutations(count));
}

export { year, day, part1, part2 };
