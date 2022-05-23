var secunds=0
var minutes=0
var hour=0
var interval

function start(){
    watch()
    interval = setInterval(watch,1000)
}

function pause(){
    clearInterval(interval)
}

function stop(){
    clearInterval(interval)
    secunds=0
    minutes=0
    document.getElementById('timer').innerText='00:00:00'
}

function twoDigits(digit){
    if(digit<10){
        return('0'+digit)
    }
    else{
        return(digit)
    }
}

function watch(){
    secunds++
    if(secunds==60){
        minutes++
        secunds=0
        if(minutes==60){
            minutes=0
            hour++
        }
    }
    document.getElementById('timer').innerText=twoDigits(hour)+':'+twoDigits(minutes)+':'+twoDigits(secunds)
}