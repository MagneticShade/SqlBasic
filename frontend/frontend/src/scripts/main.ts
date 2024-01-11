let app:HTMLElement = <HTMLElement>document.getElementById("app")

type Img={
    path:string
}
function setStage(){
    app.replaceChildren(" ")
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
}
setStage()
let fileInput:HTMLInputElement = <HTMLInputElement>document.getElementById("fileInput")
let form:HTMLFormElement=<HTMLFormElement>document.querySelector("form")
fileInput?.addEventListener("change",()=>{
    if (fileInput.files){
        for (const file of fileInput.files){
            console.log(file.name)
            let fdata=new FormData()
            fdata.append("file",file)
            console.log(fdata.get("file"))
            fetch('http://127.0.0.1:8000/',{
                method: "POST",
                body:fdata})
                .then(()=>setStage())
        }
    }
})