let app:HTMLElement|null =document.getElementById("app")

type Img={
    path:string
}

fetch("http://127.0.0.1:8000/")
    .then(data=>data.json())
    .then(result=>{
        for (let img:Img of result){
            let div:HTMLDivElement=document.createElement("div")
            let imgBlock:HTMLImageElement=document.createElement("img")
            div.appendChild(imgBlock)
            imgBlock.src=img.path
            app?.appendChild(div)
        }
    })
