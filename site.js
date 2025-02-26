// Adăugare stele animate pe fundal
const starContainer = document.createElement("div");
starContainer.classList.add("star-container");
document.body.appendChild(starContainer);

for (let i = 0; i < 50; i++) {
    let star = document.createElement("div");
    star.classList.add("star");
    star.style.left = `${Math.random() * 100}vw`;
    star.style.animationDuration = `${Math.random() * 3 + 2}s`;
    star.style.animationDelay = `${Math.random() * 2}s`;
    starContainer.appendChild(star);
}

// Adăugare stil pentru stele
const style = document.createElement("style");
style.innerHTML = `
.star-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    pointer-events: none;
    z-index: -1;
}

.star {
    position: absolute;
    top: 0;
    width: 15px;
    height: 15px;
    background-color: red;
    clip-path: polygon(50% 100%, 100% 65%, 80% 0%, 50% 20%, 20% 0%, 0% 65%);
    opacity: 0;
    animation: twinkle linear infinite, fall linear infinite;
}

@keyframes twinkle {
    0%, 100% {
        opacity: 0.2;
    }
    50% {
        opacity: 1;
    }
}

@keyframes fall {
    0% {
        transform: translateY(-10vh);
    }
    100% {
        transform: translateY(100vh);
    }
}
`;
document.head.appendChild(style);
/*
document.addEventListener("DOMContentLoaded",function(){
    const buton = document.querySelector(".buton #b2");
    buton.addEventListener("mouseenter", function(){
        var bodyWidth = document.body.offsetWidth;
        var bodyHeigth = document.body.offsetHeight;
        var butonWidth = this.offsetWidth;
        var butonHeigth = this.offsetHeight;
        const randomX = Math.floor(Math.random()*(bodyWidth - butonWidth));
        const randomY = Math.floor(Math.random() * (bodyHeigth - butonHeigth));

        buton.style.left = `${randomX}px`;
        buton.style.top = `${randomY}px`;
    });
});
*/
document.addEventListener("DOMContentLoaded", function(){
    const no = document.getElementById("b2");
    const yes = document.getElementById("b1");
    const message = document.getElementById("mesaj");
    const card = document.querySelector(".card")
    const videoContainer = document.getElementById("vdContainer");
    const myvideo = document.getElementById("myvideo");
    const gifContainer = document.getElementById("gifContainer");
    const gifContainer1 = document.getElementById("gif2");
    const gifContainer2 = document.getElementById("gif3");
    const gifContainer4 = document.getElementById("gif4");
    const gifContainer5 = document.getElementById("gif5");
    const gifContainer6 = document.getElementById("gif6");
    const gifContainer7 = document.getElementById("gif7");
    console.log("myVideo:", myvideo);
    let noSize = 1;
    let yesSize = 1;
    let messages = [
        "Mai incearca! 😋 ",
        "Mai gândește-te... 🤔",
        "Nu cred că e o idee bună! 😆",
        "Ești sigur? 🤨",
        "Ultima șansă! 😬",
        "Prea târziu! 😈"
    ];
    let index = 0;

    no.addEventListener("click", function(){

        message.style.opacity = 100;
        if(noSize > 0.1){
            noSize -= 0.15;
            no.style.transform = `scale(${noSize})`;

            yesSize += 0.1;
            yes.style.transform = `scale(${yesSize})`;

            if(index< messages.length - 1){
                message.innerText = messages[index];
                index++;
            }
        }
        else{
            no.style.display = "none";
            message.innerText  = messages[messages.length - 1]
        }
    });

    yes.addEventListener("click", function(){
        console.log("Apăsat pe butonul DA");
        card.style.display = "none";

        videoContainer.style.opacity = 100;
        videoContainer.style.display = "block";
        videoContainer.style.margin = "0";
        myvideo.play();
        setTimeout(() => {
            gifContainer.style.display = "block";
        },1000);
        setTimeout(() => {
            gifContainer1.style.display = "block";
        },2000);
        setTimeout(() => {
            gifContainer2.style.display = "block";
        },3000);
        setTimeout(() => {
            gifContainer4.style.display = "block";
        },4000);
        setTimeout(() => {
            gifContainer5.style.display = "block";
        },5000);
        setTimeout(() => {
            gifContainer6.style.display = "block";
        },6000);
        setTimeout(() => {
            gifContainer7.style.display = "block";
        },7000);
    });
})
