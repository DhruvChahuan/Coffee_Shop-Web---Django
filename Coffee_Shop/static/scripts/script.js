const mobile_manu = document.querySelector("#mobile-menu")
const mobile_manu_buttun = document.querySelector("#mobile-menu-button")

let flag = true
mobile_manu_buttun.addEventListener("click",function(){
    if (flag) {
        mobile_manu.classList.remove("hidden")
        flag = false
    }
    else{
        mobile_manu.classList.add("hidden")
        flag = true
    }
})

