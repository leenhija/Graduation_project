<template>
          <div class="nav" >
  <div  class="navigation">
  <h1 class="logo" @click="$router.push({name:'loggedin',reload:true})">Rapidly</h1>
  </div>
  <div class="pages">
    <!-- <i class="fa-thin fa-house"></i> -->
    <button class="Home"  id="Home" @click="Home()" v-show="home">Home</button>
<div class="main_border Home_icon" @click="Home()"  id="Home_icon" v-show="home_icon"><div class="home_border"><img src="../assets/Home.svg" class="icon">   </div> </div>
<button class="About" @click="About()" id="About" v-show="about">About</button>
<div class="main_border About_icon" id="About_icon" v-show="about_icon"><div class="home_border"><img src="../assets/About.svg" class="icon">   </div> </div>
<button class="Contact" id="Contact" @click="Contact()" v-show="contact">Contact</button>
<div class="main_border Contact_icon" id="Contact_icon" v-show="contact_icon"><div class="home_border"><img src="../assets/Contact.svg" class="icon">   </div> </div>
   
  </div>
  <div class="profile" @mouseleave="hide()">
    <div class="dark_mode_and_profile" v-show="show1">
 <div class="dark_mode_border">
  <div class="dark_mode_circle"></div>
  </div>
  <div class="profile_pic_border" @mouseover="show()" >
    <div class="profile_pic">{{ profile_pic }}</div>
  </div>
</div> 
  <div class="drop_down_list" v-show="show2">
    <ul >
      <li class="pic_and_username">
  <div class="profile_pic_border" @click="gotoprofile()">
    <div class="profile_pic">{{ profile_pic }}</div>
  </div><div class="username">{{username}}</div></li>
      <li class="your_profile gotoprofile" @click="$router.push({name:'profile'})"><img src="../assets/user_icon.svg" class="icon_hover"> Your Profile</li>
      <li class="your_profile"><img src="../assets/your_project_icon.svg" class="icon_hover"> Your Projects</li>
      <li class="your_profile"@click="gotoprofile()"><img src="../assets/setting_icon.svg" class="icon_hover"> Settings</li>
      <li class="your_profile"><img src="../assets/dark_mode_icon.svg" class="icon_hover"> Dark Mode</li>
      <li class="your_profile"><img src="../assets/privacy_policy_icon.svg" class="icon_hover"> Privacy Policy</li>
      <li class="your_profile support_us"><img src="../assets/support_icon.svg" class="icon_hover"> Support Us</li>
      <li class="your_profile sign_out" @click="signout()" >sign out</li>
    </ul>
  </div>
</div>
</div>
</template>
<script>
import axios from 'axios';
const jwtToken = localStorage.getItem('token');
export default{
    data(){
        return{
            userEmail:'',
    profile_pic:'',
    username:'',
    show1:true,
    show2:false,
    home:false,
     home_icon:true,
     about:true,
     about_icon:false,
     contact:true,
     contact_icon:false
        }
    },methods:{
    async print_userEmail(){
   const response=axios.get('user',{
    headers:{
      Authorization:`Bearer ${jwtToken}`
    }
   }).then(response=>{
    this.username=response.data.username;
     this.profile_pic=response.data.email.substring(0,2).toUpperCase();
   })
  }
 , 
 About(){
  this.home_icon=false;
   this.home=true;
   this.about_icon=true;
   this.about=false;
   this.contact=true;
    this.contact_icon=false;
},
Home(){
  this.home=false;
    this.home_icon=true;
    this.about=true;
    this.about_icon=false;
    this.contact=true;
    this.contact_icon=false;
    this.$router.push({name:'loggedin',reload:true});
}
,
Contact(){
  this.home_icon=false;
   this.home=true;
   this.about_icon=false;
   this.about=true;
   this.contact=false;
    this.contact_icon=true;
}
,
signout(){
localStorage.clear()
this.$router.push({name:'home',reload:true});
},
show(e){
this.show2=true;
this.show1=false;
}
,
hide(e){
    this.show1=true;
    this.show2=false;

}
,
gotoprofile()
{
  this.$router.push({name:'settings',reload:true});
},
list_style(){
    return{
    color:'#6362E3',
}
}
    }
,
mounted(){
  this.print_userEmail();

 //document.addEventListener("click",this.hide)
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
    cursor: grab;
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
  margin-left: 0px;
  overflow: visible;
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
height: 60px;
border-radius: 33px 33px 0px 0px;
background-color: rgba(227, 239, 242, 0.79);
margin-top: 0px;
}
.icon{
width: 18px;
height: 18px;
}

.Home{
  border: none;
background-color: #D9D9D9;
}
.About{
background-color: #D9D9D9;
}
.Contact{
  border: none;

background-color: #D9D9D9;
}
.profile .drop_down_list{
width: 200px;
height: 450px;
background-color: #D9D9D9;
overflow-wrap: inherit;
padding-right: 0px;
margin-right: -20px;
border-radius: 20px;
margin-top: 380px;
padding: 20px;
}
.profile .drop_down_list ul{
list-style: none;
padding: 20px;
display: flex;
flex-direction: column;
justify-content: flex-start;
align-items: center;
gap: 10px;
}
.profile .drop_down_list ul li{
width: 165px;
}
.profile{
margin-right: 30px;
display: flex;
flex-direction: row;
align-items: center;
justify-content: center;
gap: 10px;
}
.profile .dark_mode_and_profile{
display: flex;
flex-direction: row;
align-items: center;
justify-content: center;
gap: 20px;
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
.gotoprofile{
  cursor: grab;
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
cursor: grab;
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
.pic_and_username{
display: flex;
flex-direction: row;
justify-content: flex-start;
align-items: center;
gap:20px;
border-bottom: 2px solid #616161;
padding: 10px;
}
.pic_and_username .username{
color: rgba(67, 67, 67, 1);
color:  #434343;
font-family: "Montserrat", sans-serif;
font-size: 16px;
font-style: normal;
font-weight: 600;
line-height: normal;
}
.support_us{
  border-bottom: 2px solid #616161;

}
.sign_out{
margin-left: 80px;
cursor: grab;
}
.your_profile{
  color: rgba(67, 67, 67, 1);
color:  #434343;
font-family: "Montserrat", sans-serif;
font-size: 16px;
font-style: normal;
font-weight: 600;
line-height: normal;
display: flex;
flex-direction: row;
justify-content: flex-start;
align-items: center;
gap:10px;
padding: 10px
}
.your_profile:hover{
color: #6362E3;
background-color: rgba(172, 172, 172, 0.45);

cursor: grab;
}
.icon_hover:hover{
width: 20px;

}
.Home_icon{
  cursor: grab;
}
</style>