<template>
  <div class="generation_bar">
    <div class="opacity">
      <div class="nav">
  <div  class="navigation">
  <h1 class="logo" >Rapidly</h1>
  </div>
  <div class="pages">
    <!-- <i class="fa-thin fa-house"></i> -->
    <button class="Home"  id="Home" @click="Home()">Home</button>
<div class="main_border Home_icon" id="Home_icon"><div class="home_border"><img src="../assets/Home.svg" class="icon">   </div> </div>
<button class="About" @click="About()" id="About">About</button>
<div class="main_border About_icon" id="About_icon"><div class="home_border"><img src="../assets/About.svg" class="icon">   </div> </div>
<button class="Contact" id="Contact" @click="Contact()">Contact</button>
<div class="main_border Contact_icon" id="Contact_icon"><div class="home_border"><img src="../assets/Contact.svg" class="icon">   </div> </div>
    
  </div>
  <div class="profile">
<!-- <div class="dark_mode_border">
  <div class="dark_mode_circle"></div>
  </div>
  <div class="profile_pic_border">
    <div class="profile_pic">{{ profile_pic }}</div>
  </div> -->
  <div class="drop_down_list">
    <ul>
      <li>
  <div class="profile_pic_border">
    <div class="profile_pic">{{ profile_pic }}</div>
  </div></li>
      <li><img src="../assets/user_icon.svg"></li>
    </ul>
  </div>
</div>
</div>

<div class="brief">
<p class="text1">The Future of Assessment is Here</p>
<p class="text2">Power Up Your Assessments with AI-Driven Exams</p>
</div>
<div class="generate_button">
<button>Generate Exam</button>
</div>
</div>
    </div>

<div class="get_started">

<div class="promo">
  <p>Exams Made Easy</p>
  <p class="changed_promo"><span class="promo_number">10x</span> <span class="promo_word" id="promo_word" >{{word}}</span> Customization</p>
<button class="start_button" id="start_button" @click="navigate_to_signup()">Get Started</button>
</div>
<div class="text">
<img src="../assets/keep_it2.svg" alt="" class="promo_pic">
</div>
</div>
<div class="featurs">
  <div class="features_title_box"><p class="features_title">Features</p></div>
<div class="gellary-wrap">
  <img src="../assets/back.svg" id="backBtn">
  <div class="gellary">
   <div>
    <span><img src="../assets/feature1.svg"></span>
    <span><img src="../assets/feature2.svg"></span>
    <span><img src="../assets/feature3.svg"></span>
    <!-- <span  ><img src="../assets/Feature-4-cropped.svg" class="minimized"></span > -->
   </div>
   <div>
    <span><img src="../assets/feature-4-scroll.svg"></span>
    <span><img src="../assets/feature5.svg"></span>
    <span><img src="../assets/feature6.svg"></span>
    <!-- <span><img src="../assets/feature6-cropped.svg" class="minimized"></span> -->
   </div>
   <div>
    <!-- <span><img src="../assets/Feature-4-left.svg" class="minimized"></span> -->
    <span><img src="../assets/feature7.svg"></span>
    <!-- <span><img src="../assets/feature6.svg"></span>
    <span><img src="../assets/feature7.svg"></span> -->
   </div>
  </div>
  <img src="../assets/next.svg" id="nextBtn">
</div>
</div>
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
import router from '@/router';
import axios from 'axios';
const jwtToken = localStorage.getItem('token');

export default{
  data(){
    return{
    word:'Faster',
    intervalId:null,
    userEmail:'',
    profile_pic:''
    };
  }
,methods:{
  async print_userEmail(){
   const response=axios.get('user',{
    headers:{
      Authorization:`Bearer ${jwtToken}`
    }
   }).then(response=>{
    console.log(response.data)
     this.profile_pic=response.data.email.substring(0,2).toUpperCase();
   })
  }
 , 
 About(){
  document.getElementById("Home_icon").setAttribute("style","display:none");
  document.getElementById('About').setAttribute("style","display: none");
  document.getElementById('Home').setAttribute("style","display: inherit;");
  document.getElementById('About_icon').setAttribute("style","display: inherit");
  document.getElementById('Contact').setAttribute("style","display:inherit;margin-top: 25px;");
  document.getElementById('Contact_icon').setAttribute("style","display:none");
},
Home(){
  document.getElementById("Home_icon").setAttribute("style","display:inherit");
  document.getElementById('About').setAttribute("style","display: inherit;margin-top: 25px;");
  document.getElementById('Home').setAttribute("style","display: none;");
  document.getElementById('About_icon').setAttribute("style","  display: none");
  document.getElementById('Contact').setAttribute("style","display:inherit;margin-top: 25px;");
  document.getElementById('Contact_icon').setAttribute("style","display:none");
}
,
Contact(){
  document.getElementById('Contact_icon').setAttribute("style","display:inherit");
  document.getElementById('About').setAttribute("style","display: inherit;margin-top: 25px;");
  document.getElementById('Contact').setAttribute("style","display:none");
  document.getElementById('About_icon').setAttribute("style","  display: none");
  document.getElementById("Home_icon").setAttribute("style","display:none");
  document.getElementById('Home').setAttribute("style","display: inherit;");
}
,
 change_text(){
  var wordes=["Faster","Easier","Efficient"];
  var random_num=Math.floor(Math.random() * 3);
  this.word=wordes[random_num];
 

},
startPolling() {
      this.intervalId = setInterval(this.change_text, 1000); // Call every 2 seconds
    },
    navigate_to_signup(){
      this.$router.push({name:'signup'});
    },
    scroll(){
      let scrollContainer = document.querySelector('.gellary');
let backBtn = document.getElementById("backBtn");
let nextBtn = document.getElementById("nextBtn");

scrollContainer.addEventListener("wheel", (evt) => {
    evt.preventDefault();
    scrollContainer.scrollLeft += evt.deltaY;
    scrollContainer.style.scrollBehavior = 'auto';
});

nextBtn.addEventListener("click", ()=>{
    scrollContainer.style.scrollBehavior = 'smooth';
    scrollContainer.scrollLeft += 900;
});

backBtn.addEventListener("click", ()=>{
    scrollContainer.style.scrollBehavior = 'smooth';
    scrollContainer.scrollLeft -= 900;
});
    }
},
mounted(){
  this.startPolling();
  this.print_userEmail();
  this.scroll();
},

}
</script>
<style>
body{
  overflow-x: hidden;
}
.navigation{
  height: 64px;
  display: flex;
  flex-direction: row;
  justify-content: left;
  margin-left: 40px;
  }
  .navigation .logo{
    font-family: "Twinkle Star", cursive;
    font-size: 50px;
    font-weight: 400;
    font-style: normal;
    color: white;
    font-weight: bold;
    /* padding: 20px; */
    border-color: rgb(232, 93, 93);
  }
.nav{
  width: 100vw;
  height: 75px;
  display: flex;
  flex-direction: row;
   justify-content: space-between; 
  /* align-items: center; */
  position: fixed; /* Set the navbar to fixed position */
  top: 0; /* Position the navbar at the top of the page */
  /* margin-top: -650px; */
  background-color: #D9D9D9;
  /* margin-top: -680px; */
  color: white;
  font-family: "Roboto",sans-serif;
  border-radius: 0px 0px 30px 30px;
  border-bottom: solid 10px rgba(227, 239, 242, 0.79);
  margin-right: 30px;
  margin-left: 20px;
  overflow: visible;
}
/* .nav h1{
margin-left: 200px;
} */
.nav button{
  width: 109px;
height: 44px;
border-color: transparent transparent transparent transparent;
border-radius: 10px;
cursor: grab;
font-size: 17px;
}
.login_or_signup{
  font-family: 'Roboto',sans-serif;
display: flex;
width: 200px;
flex-direction: row;
align-items: center;
margin-right: 60px;
gap: 10px;
}
.lonin{
margin-right: 20px;
flex-shrink: 0;
background: #F4F3F4;
color: black;
}
.signup{
flex-shrink: 0;
color: white;
background:  #6362E3;
}
.generation_bar{
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100vw;
  height: 100vh;
background-image: url("../assets/Background_picture.png");
}
.opacity{
width: 100vw;
height: 100vh;display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
background-color: rgba(243, 248, 249, 0.79);
}
.pages{
display: flex;
flex-direction: row;
justify-content: center;
align-items: center;
gap:40px;
color: black;
margin-top: 25px;
}
.home_border{
  width: 40px;
  height: 40px;
border-radius: 100px;
background-color: #FFD863;
display: flex;
flex-direction: row;
justify-content: center;
align-items: center;
}
.main_border{
  display: flex;
flex-direction: row;
justify-content: center;
margin-right: -10px;
padding-top: 10px;
width: 66px;
height: 66px;
border-radius: 33px 33px 0px 0px;
background-color: rgba(227, 239, 242, 0.79);
margin-top: 20px;
}
.icon{
width: 18px;
height: 18px;
}
.About_icon{
display:none;
}
.Contact_icon{
display: none;
}
.Home{
  display: none;
  margin-top: 25px;
  border: none;
background-color: #D9D9D9;
}
.About{
border: none;
background-color: #D9D9D9;
}
.Contact{
  border: none;

background-color: #D9D9D9;
}
.profile .drop_down_list{
width: 250px;
height: 470px;
background-color: #D9D9D9;
overflow-wrap: inherit;
padding-right: 0px;
margin-right: -20px;
border-radius: 20px;
margin-top: 390px;
}
.profile{
margin-right: 30px;
display: flex;
flex-direction: row;
align-items: center;
justify-content: center;
gap: 10px;
}
.profile .dark_mode_border{
  width: 40px;
  height: 20px;
  background-color: #D9D9D9;
  border: #434343 3px solid;
  border-radius: 50px;
  display: flex;
  flex-direction: row;
  align-items: center;
  padding-left: 5px;
  justify-content: flex-start;
}
.profile .dark_mode_border .dark_mode_circle{
  height: 15px;
  width: 15px;
   border-radius: 50px;
   background-color: #434343;
}
.profile .profile_pic_border{
width: 40px;
height: 40px;
border-radius: 50px;
border: 5px solid #6362E3;
display: flex;
justify-content: center;
align-items: center;
}
.profile .profile_pic_border .profile_pic{
width: 33px;
height: 33px;
border-radius: 50px;
background-color: #6362E3;
display: flex;
justify-content: center;
align-items: center;
font-family: "Montserrat", sans-serif;

}
.brief{
  display: flex;
width: 790px;
height: 189px;
padding: 41px 0px 22.016px 0px;
flex-direction: column;
justify-content: center;
align-items: center;
gap: 24.14px;
}
.text1{
  width: 790px;
height: 53.86px;
flex-shrink: 0;
color:  #5F5F5F;
font-family: "Montserrat", sans-serif;
font-size: 45px;
font-style: normal;
font-weight: 700;
line-height: normal;
}
.text2{
  width: 663px;
height: 47.984px;
flex-shrink: 0;
color: #5F5F5F;
font-family: "Montserrat", sans-serif;
font-size: 25px;
font-style: normal;
font-weight: 700;
line-height: normal;
}
.generate_button{
  display: flex;
width: 324px;
height: 97px;
padding: 10px;
justify-content: center;
align-items: center;
gap: 10px;

}
.generate_button button{
  width: 304px;
height: 77px;
background-color:  #FFD863;
border: none;
border-radius: 30px;
filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
color: rgba(0, 0, 0, 0.70);

font-family: "Roboto";
font-size: 25px;
font-style: normal;
font-weight: 700;
line-height: normal;
}
.get_started{
  display: flex;
  flex-direction: row;
  /* justify-content: center; */
  align-items: center;
width: 100vw;
height: 100vh;
gap: 70px;
overflow: hidden;

}
.get_started .text{

 width: 300px;
height: 200px;
margin-top: -150px;
}
.get_started .text img{
width: 500px;
}
.get_started .promo{
display:flex;
padding: 10px;
flex-direction: column;
justify-content: center;
align-items: center;
gap: 10px;
width:700px;
height: 100px;
margin-left: 70px;
color: var(--2nd-page-Text, #212121);
text-align: center;
font-family: "Montserrat", sans-serif;
font-size: 38px;
font-style: normal;
font-weight: 700;
line-height: normal;
}
.get_started .promo .promo_number{
  color:  #6362E3;
font-family: "Montserrat", sans-serif;
font-size: 60px;
font-style: normal;
font-weight: 700;
line-height: normal;
}
.get_started .promo .promo_word{
  background: radial-gradient(50% 50% at 50% 50%, #6362E3 23%, #FFD863 100%);
background-clip: text;
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
font-family: "Montserrat", sans-serif;
font-size: 38px;
font-style: normal;
font-weight: 700;
line-height: normal;
}
.changed_promo{
display: inline;
}
.start_button{
  display: flex;
width: 333px;
height: 88px;
padding: 27px 82px;
justify-content: center;
align-items: center;
gap: 10px;
border-radius: 20px;
background: #6362E3;
box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
color: var(--Get-started, #FFF);
text-align: center;
font-family: Roboto;
font-size: 30px;
font-style: normal;
font-weight: 700;
line-height: normal;
border: none;
margin-top: 70px;
cursor: grab;
}
.featurs{
width: 100vw;
height:700px;
background-color: #F4F3F4;
display: flex;
flex-direction: column;
justify-content: center;
align-items: center;
background-color: #6968E0;
}
.features_title_box{
width:100%;
height: 60px;
display: flex;
justify-content: center;
align-items: center;
padding-top: 30px;
margin-top:-60px;
}
.features_title{
  color: #FFF;
  font-family: "Montserrat", sans-serif;
font-size: 50px;
font-style: normal;
font-weight: 700;
line-height: normal;
padding-bottom: 30px
}
.featurs .gellary-wrap .gellary{
width: 1000px;
display: flex;
overflow-x:scroll ;
}
/* .minimized{
height: 270px;
width: 200px;
} */
.featurs .gellary-wrap .gellary div{
    width: 100%;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 5px;
    padding: 10px;
    flex: none;
}
/* .featurs .gellary-wrap .gellary div img{
width: 100%;

} */
.featurs .gellary-wrap{
  display: flex;
  flex-direction: row;
    align-items: center;
    justify-content: center;
    /* margin: 0% auto; */
    margin-top: 20px;
}
.gellary::-webkit-scrollbar {
    display: none;
}
.featurs #backBtn, #nextBtn{
  cursor: grab;
}
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
  width: 1293px;
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
font-weight: 400;
line-height: normal;
}
.footer .links2 .info p{
  color: #616161;
  font-family: "Montserrat", sans-serif;
font-size: 18px;
font-style: normal;
font-weight: 500;
line-height: normal;
width: 340px;
padding-left: 20px;
}
.footer .links2 .social_media{
display: flex;
flex-direction: row;
width: 208px;
height: 50px;
align-items:flex-end;
padding-top: 20px;
padding-right: 50px;
gap: 20px;
}
</style>