<template>
  <div class="footer">
<div class="links1">
 <div class="links1_list"><ul>
    <p>Help</p>
    <li>About Us</li>
    <li>Contact Us</li>
    <li>Privacy Policy</li>

  </ul>
  <ul>
    <p>Rapidly</p>
    <li>Features</li>
    <li>Social Media</li>
    <li>How it works?</li>

  </ul>
  <ul>
    <p>Support Us</p>
    <li>Team</li>
    <li>Donations</li>
    <li class="invisable_li">invisable</li>
  </ul></div>
 <div class="iphone"><img src="../assets/iphone.svg"></div> 
</div>
<div class="line"></div>
<div class="links2">
<div class="info">
  <h1 class="footer_logo" >Rapidly</h1>
<p>© 2024 Rapidly, All rights reserved.</p>
</div>
<div class="social_media">
  <img src="../assets/Linkedin.svg">
  <img src="../assets/Facebook.svg">
  <img src="../assets/X.svg">
  <img src="../assets/Instagram.svg">
</div>

</div>
</div> 
</template>
<script>

</script>
<style>
.footer{
  width: 100vw;
height:450px;
background-color: #F4F3F4; 
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
padding-top: 150px;
gap: 20px;
margin-bottom: 0px;
overflow: hidden;
}
.footer .links1{
  width: 100vw;
display: flex;
flex-direction: row;
justify-content: center;
gap: 100px;
background-color: #EAE9EA;
}
.footer .links1 .links1_list{
  width: 500px;
display: flex;
flex-direction: row;
justify-content: center;
align-items: center;
padding-top: 0px;
gap: 100px;
margin-left: 100px;
}
.footer .links1 .links1_list ul{
  display: inline-flex;
flex-direction: column;
align-items: flex-start;
gap: 19px;
}
.footer .links1 .links1_list ul li{
text-decoration: none;
list-style: none;
display: flex;
width: 103px;
height: 20px;
padding-right: 32px;
align-items: center;
font-family: "Montserrat", sans-serif;
width: 120px;
}
.invisable_li{
visibility: hidden;
}
.footer .links1 .links1_list ul p{
  color: #616161;
  font-family: "Montserrat", sans-serif;
font-size: 20px;
width: 120px;
font-style: normal;
font-weight: 700;
line-height: normal;
}
.footer .links1 .iphone{
width: 700px;
height: 450px;
overflow: hidden;
margin-right: -100px;
margin-top: -120px
}
.footer .links1 .iphone img{
margin:auto;
}
.footer .line{
  width: 1370px;
height: 1px;
background: #616161;

}
.footer .links2{
display: flex;
flex-direction: row;
justify-content: center;
gap: 900px;
width: 100vw;
height: 80px;
}
.footer .links2 .info{
  display: inline-flex;
flex-direction: column;
align-items: flex-start;
gap: 14px;
padding-left: 20px;
width: 340px;
}
.footer .links2 .info .footer_logo{
  width: 208px;
height: 50px;
padding-left: 20px;
color: #6362E3;
text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
-webkit-text-stroke-width: 1;
-webkit-text-stroke-color: #6362E3;
font-family: "Twinkle Star", cursive;
font-size: 40px;
font-style: normal;
font-weight: 600;
line-height: normal;
margin-top: -10px
}
.footer .links2 .info p{
  color: #616161;
  font-family: "Montserrat", sans-serif;
font-size: 15px;
font-style: normal;
font-weight: 500;
line-height: normal;
width: 340px;
margin-top: -5px;
padding-left: 20px;
}
.footer .links2 .social_media{
display: flex;
flex-direction: row;
width: 208px;
height: 50px;
align-items:flex-end;
padding-top: 10px;
padding-right: 50px;
gap: 20px;
}
</style>