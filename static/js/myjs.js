onload = function () {
    var p = document.getElementsByClassName('news_con')[0];
    var img = p.getElementsByTagName('img');
    for (let x=0; x<img.length; x++){
        console.log(img.item(x));
        img.item(x).style.cssText += 'margin: auto'
    }
};