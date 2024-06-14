<template>
    <div class="generation_bar">
    <div class="opacity">
      <div class="nav">
  <div  class="navigation">
  <h1 class="logo" >Rapidly</h1>
  </div>
  <div class="pages">
    <!-- <i class="fa-thin fa-house"></i> -->
    <button class="Home"  id="Home" @click="Home()" v-show="home">Home</button>
<div class="main_border Home_icon"  id="Home_icon" v-show="home_icon"><div class="home_border"><img src="../assets/Home.svg" class="icon">   </div> </div>
<button class="About" @click="About()" id="About" v-show="about">About</button>
<div class="main_border About_icon" id="About_icon" v-show="about_icon"><div class="home_border"><img src="../assets/About.svg" class="icon">   </div> </div>
<button class="Contact" id="Contact" @click="Contact()" v-show="contact">Contact</button>
<div class="main_border Contact_icon" id="Contact_icon" v-show="contact_icon"><div class="home_border"><img src="../assets/Contact.svg" class="icon">   </div> </div>
    
  </div>
<div class="login_or_signup"><router-link :to="{name:'login'}"><button class="login">login</button></router-link>
<router-link :to="{name:'signup'}"><button class="signup">Sign Up</button></router-link></div>
</div>

<div class="brief">
<p class="text1">The Future of Assessment is Here</p>
<p class="text2">Power Up Your Assessments with AI-Driven Exams</p>
</div>
<div class="generate_button">
<button @click="{ $router.push({name:'materailandexamchar'}); }">Generate Exam</button>
</div>
</div>
    </div>

</template>
<script>
import { faL } from '@fortawesome/free-solid-svg-icons';
 
export default{
  data(){
    return{
     home:false,
     home_icon:true,
     about:true,
     about_icon:false,
     contact:true,
     contact_icon:false
    }
  },
  methods:{
   Home(){
    this.home=false;
    this.home_icon=true;
    this.about=true;
    this.about_icon=false;
    this.contact=true;
    this.contact_icon=false;
   },
   About(){
   this.home_icon=false;
   this.home=true;
   this.about_icon=true;
   this.about=false;
   this.contact=true;
    this.contact_icon=false;
},

Contact(){
  this.home_icon=false;
   this.home=true;
   this.about_icon=false;
   this.about=true;
   this.contact=false;
    this.contact_icon=true;
},
   async test(){

  }
  }
}
</script>
<style>
body{
  overflow-x: hidden;
  margin-bottom: 0px;
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
  overflow: hidden;
  color: white;
  font-family: "Roboto",sans-serif;
  border-radius: 0px 0px 30px 30px;
  border-bottom: solid 10px rgba(227, 239, 242, 0.79);
  margin-right: 30px;
  margin-left: 20px;
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

.Home{
  /* margin-top: 25px; */
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
</style>