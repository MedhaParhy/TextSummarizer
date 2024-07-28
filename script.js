const inputBox = document.getElementById("input-box");
const numSentences = document.getElementById("num-sentences");
num = 0;
function addText(){
    if(inputBox.value == ''){
        alert("You must write something");
    }
    else{
        document.getElementById('text').innerText = inputBox.value;
    }
    inputBox.value = "";
}
function addNum(){
    if(numSentences.value == ''){
        alert("You must write something");
    }
    else{
        num = numSentences.value;
        document.getElementById('sentences').innerText = "\nSentences:" + numSentences.value;
    }
    numSentences.value = "";
}