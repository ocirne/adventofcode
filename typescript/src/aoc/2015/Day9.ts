import { AocInput } from "../AocInput";

const year = 2015;
const day = 9;

function readGraph(input: AocInput): {
  count: number;
  distances: Map<number, number>;
} {
  const nodesSet = new Set<string>();
  input.splitLines().forEach((line) => {
    const [n1, , n2] = line.split(" ");
    nodesSet.add(n1);
    nodesSet.add(n2);
  });
  const nodes = Array.from(nodesSet);
  const count = nodes.length;
  const distances = new Map<number, number>();
  input.splitLines().forEach((line) => {
    const [n1, , n2, , ds] = line.split(" ");
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
function* permutations(n: number): Generator<Array<number>> {
  let a = Array.from({ length: n }, (_value, key) => key);
  let c = Array.from({ length: n }, (_value, _key) => 0);
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
      c[i]++;
      i = 1;
    } else {
      c[i] = 0;
      i++;
    }
  }
}

function reduceIter<T>(
  fun: (acc: number, p: T) => number,
  init: number,
  iter: IterableIterator<T>,
): number {
  let o = init;
  for (let x of iter) {
    o = fun(o, x);
  }
  return o;
}

function findDistance(
  distances: Map<number, number>,
  count: number,
  path: Array<number>,
): number {
  return reduceIter<number>(
    (acc, i) => acc + distances.get(path[i] * count + path[i + 1])!,
    0,
    Array(count - 1).keys(),
  );
}

function findRoute(
  input: AocInput,
  fun: (...values: number[]) => number,
  init: number,
): number {
  const { count, distances } = readGraph(input);
  return reduceIter<Array<number>>(
    (acc, p) => fun(acc, findDistance(distances, count, p)),
    init,
    permutations(count),
  );
}

function part1(input: AocInput): number {
  return findRoute(input, Math.min, 10000);
}

function part2(input: AocInput): number {
  return findRoute(input, Math.max, 0);
}

export { year, day, part1, part2 };
