import os
from bs4 import BeautifulSoup

html = f"""
    <!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="/home/igor/web-development-projects/site2/style/style.css">
    <link rel="stylesheet" href="/home/igor/web-development-projects/site2/style/style2.css">
    <title>Wallpaper gallery</title>
    
    <script defer src="/home/igor/web-development-projects/site2/script/lightbox.js"></script>
    <link rel="stylesheet" href="/home/igor/web-development-projects/site2/style/lightbox.css">
</head>

<body>


    <div class="topnav" id="myTopnav">
        <a href="index.html" class="active">Home</a>
        <div class="dropdown">
            <button class="dropbtn">Wallpapers
      <i class="fa fa-caret-down"></i>
    </button>
            <div class="dropdown-content">
                <a href="nature.html">Nature</a>
                <a href="horses.html">Horses</a>
                <a href="dogs.html">Dogs</a>
                <a href="cats.html">Cats</a>
                <a href="cars.html">Cars</a>
                <a href="motorcycle.html">Motocycles</a>
                <a href="architecture.html">Architecture</a>
                <a href="women.html">Women</a>
                <a href="celebs.html">Celebrities</a>
            </div>
        </div>
        <a href="#about">About</a>
        <a href="javascript:void(0);" style="font-size:15px;" class="icon" onclick="myFunction()">&#9776;</a>
    </div>
    <div class="header">
        <h2>WALLPAPER GALLERY</h2>
    </div>
    <button onclick="scrollToTop()" class="scroll-top">☝️</button>
    <div class="container">
        <div class="column">
				%(img_tags)s
        </div>
    </div>
    <script src="/home/igor/web-development-projects/site2/script/script.js"></script>

  

<footer class="footer-items">Developed by: <strong>Igor Pantaleão</strong><br>copyright © 2022</footer>
</body>

</html>
"""

url_list = []

path = "/home/igor/web-development-projects/site2/images/nature/"
ext = ('.jpg')

for i in os.listdir(path):
    if i.endswith(ext):
        url_list.append(i)
    else:
        continue



if __name__ == "__main__":
    img_tags = {"img_tags": '\n'.join([f'\r   <a href="images/nature/{i}"><img loading="lazy" src="images/nature/{i}"></a>' for i in url_list])}
    print(html % img_tags)

    with open(os.path.join('/home/igor/web-development-projects/site2/images/nature/', 'nature2.html'), "w") as html_file:
        html_file.write(html % img_tags)




