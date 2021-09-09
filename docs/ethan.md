---
title: Ethan Nagola
layout: template
filename: ethan
pageheader: page-header-about
--- 
 <title>W3.CSS</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<style>
.mySlides {display:none;}
</style>
<body>

<h2 class="w3-center">Ethan Nagola</h2>

<div class="w3-content w3-display-container">
  <img class="mySlides" src="Photos/EthanPic.jpeg" style="width:400;height:500;">
 <p class="mySlides" style="width:100%">I graduated from UCSD with a Major in Computer Science
     and Minor in Cognitive sciences after 3 years in June of 2021.
     I am currently working on graduating as a Masters of Sciences
     with a specialization in Artificial Intelligence by June 2022</p>
  <img class="mySlides" src="img_mountains.jpg" style="width:100%">
  <img class="mySlides" src="img_forest.jpg" style="width:100%">

  <button class="w3-button w3-black w3-display-left" onclick="plusDivs(-1)">&#10094;</button>
  <button class="w3-button w3-black w3-display-right" onclick="plusDivs(1)">&#10095;</button>
</div>

<script>
var slideIndex = 1;
showDivs(slideIndex);

function plusDivs(n) {
  showDivs(slideIndex += n);
}

function showDivs(n) {
  var i;
  var x = document.getElementsByClassName("mySlides");
  if (n > x.length) {slideIndex = 1}
  if (n < 1) {slideIndex = x.length}
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
  }
  x[slideIndex-1].style.display = "block";  
}
</script>

</body>
 



<!-- <div class="row">
  <div class="column" style="background-color:#aaa;">
    <b style="font-size:30px">Ethan Nagola</b>
    <img src="Photos/EthanPic.jpeg" width="400" height="500">
  </div>
  <div class="column" style="background-color:#bbb;">
     <b style="font-size:30px">About Me</b>
 
    <p> I graduated from UCSD with a Major in Computer Science
     and Minor in Cognitive sciences after 3 years in June of 2021.
     I am currently working on graduating as a Masters of Sciences
     with a specialization in Artificial Intelligence by June 2022.</p>
  </div>
</div> -->
