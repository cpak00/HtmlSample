function ControlLump(num){
    var button = document.getElementById('lump'+num);
    if (button){
        var label = button.innerText.substring(0,2)
        if (label == '打开')
            {
                var req = new XMLHttpRequest()
                var url = '/lumpOpen/'+num+'/Open';
                req.open('GET',url);
                //req.setRequestHeader("Content-Type",  
                //"application/x-www-form-urlencoded;"); 
                //req.setRequestHeader('Code', 'h28D3^1r*nhxc&213');
                req.send();
                button.innerText = '关闭灯具'+num;
                button.style="background-color:yellow;";
            }
        else
            {
                var req = new XMLHttpRequest()    
                var url = '/lumpOpen/'+num+'/Close';
                req.open('GET',url);
                //req.setRequestHeader("Content-Type",  
                //"application/x-www-form-urlencoded;"); 
                //req.setRequestHeader('Code', 'h28D3^1r*nhxc&213');
                req.send();
                button.innerText = '打开灯具'+num;
                button.style="";
            }

    }
}

function lampControl(){
    var mainBar = document.getElementById("mainBar");
    mainBar.innerHTML = "<h2>灯具管理页面</h2>"
     + "<div class = 'lumpControl'>"
     + "<button id='lump1' onClick='ControlLump(1)'>打开灯具1</button>"
     + "<button id='lump2' onClick='ControlLump(2)'>打开灯具2</button>"
     + "<button id='lump3' onClick='ControlLump(3)'>打开灯具3</button>"
     + "</div>";
}

function householdControl(){
    var mainBar = document.getElementById("mainBar");
    mainBar.innerHTML = "电器管理页面,待实现"
}

function temprature(){
    var mainBar = document.getElementById("mainBar");
    mainBar.innerHTML = "温度和湿度显示页面,待实现"
}