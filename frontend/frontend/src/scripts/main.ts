
import anime from 'animejs/lib/anime.es.js';

let app:HTMLElement = <HTMLElement>document.getElementById("app")
let fileInput:HTMLInputElement = <HTMLInputElement>document.getElementById("fileInput")
let slides:[HTMLImageElement]
type Img={
    path:string
}

function setStage(){
    app.replaceChildren(" ")
    fetch("http://127.0.0.1:8000/")
        .then(data=>data.json())
        .then(result=>{
            for (let img:Img of result){
                let imgBlock:HTMLImageElement=document.createElement("img")
                imgBlock.src=img.path
                imgBlock.classList.add("slide")
                app.appendChild(imgBlock)
            }
            slides=<[HTMLImageElement]>document.querySelectorAll(".slide")
            for (let i=1;i<slides.length;i++){
                slides[i].classList.add("hidden")
            }
        })

}

setStage()

function ChangeSlide(){
    let activeInd:number;
    for (let i=0;i<slides.length;i++){
        if (!slides[i].classList.contains("hidden")){
            activeInd=i
            break
        }
    }
    slides[activeInd].classList.add("hidden")

    if(activeInd==slides.length-1){
        slides[0].classList.remove("hidden")
        setAnimation(0)
    }
    else{
        slides[activeInd+1].classList.remove("hidden")
        setAnimation(activeInd+1)
    }
}

function setAnimation(index:number){

    let animNumber:number= Math.floor(Math.random() * (3 + 1));

    switch (animNumber) {
        case 0:
            anime({
                targets: slides[index],
                translateX: 250,
                direction:'reverse',
                duration:250,
                easing: 'linear',
            })
            break
        case 1:
            anime({
                targets: slides[index],
                translateY: 250,
                direction:'reverse',
                duration:250,
                easing: 'linear',
            })
            break
        case 2:
            anime({
                targets:slides[index],
                direction:'reverse',
                rotate:'1turn',
                duration:250,
                easing:'linear'
            })
            break
        case 3:
            anime({
                targets:slides[index],
                translateY:-250,
                direction:'reverse',
                duration:250,
                easing:'linear'
            })
            break

    }

}

fileInput?.addEventListener("change",()=>{
    if (fileInput.files){
        for (const file of fileInput.files){

            let fdata=new FormData()
            fdata.append("file",file)

            fetch('http://127.0.0.1:8000/',{
                method: "POST",
                body:fdata})
                .then(()=>setStage())
        }
    }
})

app.addEventListener("click",ChangeSlide)
setInterval(()=>{
    app.dispatchEvent(new Event("click"))
},2000)