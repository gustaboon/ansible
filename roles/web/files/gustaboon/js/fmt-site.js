function getRandomInt(min, max) {
	min = Math.ceil(min);
	max = Math.floor(max);
	return Math.floor(Math.random() * (max - min)) + min;
}

function dieRoll() {
	this.innerHTML = getRandomInt(1, 7);
}


function rollem() {
	for (i = 0; i<dice.length; i++){
    	dice[i].innerHTML = getRandomInt(1, 7);
	}
}

var dice = document.getElementById('purse').getElementsByClassName('box');
//for die in dice:
for (i = 0; i<dice.length; i++){
    dice[i].addEventListener("click", dieRoll);
}

var rolo = document.getElementById('the-button');
rolo.addEventListener("click", rollem);
