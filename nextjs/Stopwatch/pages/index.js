import Head from 'next/head'
import Image from 'next/image'
import Link from 'next/link'

let startTime=Date.now();
let elapsedTime=0;
let timerInterval;
let counter=0;


const timeToString=(time)=>{
  let diffInHrs = time / 3600000;
  let hh = Math.floor(diffInHrs);

  let diffInMin = (diffInHrs - hh) * 60;
  let mm = Math.floor(diffInMin);

  let diffInSec = (diffInMin - mm) * 60;
  let ss = Math.floor(diffInSec);

  let diffInMs = (diffInSec - ss) * 100;
  let ms = Math.floor(diffInMs);

  let formattedMM = mm.toString().padStart(2, "0");
  let formattedSS = ss.toString().padStart(2, "0");
  let formattedMS = ms.toString().padStart(2, "0");

  return `${formattedMM}:${formattedSS}:${formattedMS}`;
}

function print(txt) {
  var display=document.getElementById("display");
  display.innerHTML=txt;
  display.value=txt;
}

function start(){
  document.getElementById("start").disabled=true;
  document.getElementById("stop").disabled=false;
  startTime = Date.now() - elapsedTime;
  timerInterval = setInterval(function printTime() {
    elapsedTime = Date.now() - startTime;
    print(timeToString(elapsedTime));
  }, 10); 

  var stat3=document.getElementById("stat1");

  setInterval(function printStats(){
    if (counter>0){
    stat1.value="Average Time Per Question: "+timeToString(elapsedTime/counter);
    stat1.innerHTML="Average Time Per Question: "+timeToString(elapsedTime/counter);  
    }
  }, 10);
  
  
}

function stop(){
  document.getElementById("start").disabled=false;
  document.getElementById("stop").disabled=true;
  clearInterval(timerInterval);
}

function reset(){
  clearInterval(timerInterval);
  document.getElementById("start").disabled=false;
  document.getElementById("stop").disabled=true;
  print("00:00:00");
  elapsedTime = 0;
  counter=0;
  changeCounter();
}

function changeCounter(){
  var count=document.getElementById("number");
  count.value="Solved: " + counter;
  count.innerHTML="Solved: "+counter;
}

const increaseNum=()=>{
  counter++;
  
  changeCounter();
};

const decreaseNum=()=>{
  counter--;
  
  changeCounter();
}

export default function Home() {

  return (
    <div>    
      <h1 className="time" id="display">00:00:00</h1>
      <h3 className="number" id="number">Solved: 0</h3>
      
      <div className="controls">
        <button className="button1" onClick={start} id="start">Start</button>
        <button className="button2" onClick={stop} id="stop">Stop</button>
        <button className="button3" onClick={reset} id="reset">Reset</button>

        <button className="button4" onClick={increaseNum} id="increase">++1</button>
        <button className="button5" onClick={decreaseNum} id="decrease">--1</button>
      </div>

      <h2 id="stat1">Average Time Per Question: 0</h2>
     
    </div>
  )
}
