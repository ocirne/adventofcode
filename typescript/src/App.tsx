import { useState } from "react";
import "./App.css";
import { Day1 } from "./foo/Day1";

export default function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <div>
        <h2>2015</h2>
        <ul>
          <li><a href="">Day 1</a></li>
          <li>Day 2</li>
          <li>Day 3</li>
          <li>Day 4</li>
          <li>Day 5</li>
          <li>Day 6</li>
          <li>Day 7</li>
          <li>Day 8</li>
          <li>Day 9</li>
          <li>Day 10</li>
          <li>Day 11</li>
          <li>Day 12</li>
          <li>Day 13</li>
          <li>Day 14</li>
          <li>Day 15</li>
        </ul>
      </div>
    </>
  );
}
