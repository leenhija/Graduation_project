<template>
    <navigation_bar></navigation_bar>
    <div class="profile_settings">
<div class="settings">
<div class="title"><img src="../assets/setting_icon2.svg"><h4>Settings</h4></div>
<ul class="setting_list">
    <li @click="show_edditing_1()" :class="className1">Profile</li>
    <li @click="show_edditing2()" :class="className2">Password</li>
    <li @click="show_edditing3()" :class="className3">Appearance</li>
    <li @click="show_edditing4" :class="className4">Privacy Policy</li>
</ul>
</div>
<div class="edditing">
  <editing_1 v-show="edditing_1"></editing_1>
  <change_password v-show="edditing_2"></change_password>
  <appearance v-show="edditing_3"></appearance>
  <privacy_policy v-show="edditing_4"></privacy_policy>
</div>
</div>
</template>
<script>
import router from '@/router';
 import editing_1 from '../components/editing_1.vue'
import change_password from '../components/change_password.vue'
// import { fas } from '@fortawesome/free-solid-svg-icons';
import appearance from '../components/appearance.vue';
import privacy_policy from '../components/privacy_policy.vue'
import navigation_bar from '../components/navigation_bar.vue'
const jwtToken = localStorage.getItem('token');
export default{
    components:{
    editing_1:editing_1,
    change_password:change_password,
    appearance:appearance,
    privacy_policy:privacy_policy,
    navigation_bar:navigation_bar
    },
    data(){
        return{
            email:'',
            edditing_1:true,
            edditing_2:false,
            edditing_3:false,
            edditing_4:false,
            className1:'is_burble',
            className2:'is_black',
            className3:'is_black',
            className4:'is_black',

        }
    },
    methods:{
  show_edditing_1(){
   this.edditing_1=true;
   this.edditing_2=false;
   this.edditing_3=false;
   this.edditing_4=false;
   this.className1='is_burble';
   this.className2='is_black';
   this.className3='is_black';
   this.className4='is_black';
  },
  show_edditing2(){
    this.edditing_2=true;
    this.edditing_1=false;
    this.edditing_3=false;
    this.edditing_4=false;
    this.className2='is_burble'
    this.className1='is_black';
   this.className3='is_black';
   this.className4='is_black';

  },
  show_edditing3(){
    this.edditing_2=false;
    this.edditing_1=false;
    this.edditing_3=true;
    this.edditing_4=false;
    this.className3='is_burble'
   this.className2='is_black';
   this.className1='is_black';
   this.className4='is_black';
  },
  show_edditing4(){
    this.edditing_2=false;
    this.edditing_1=false;
    this.edditing_3=false;
    this.edditing_4=true;
    this.className4='is_burble'
   this.className2='is_black';
   this.className3='is_black';
   this.className1='is_black';
  }
    }
    
}
</script>
<style>
.profile_settings{
    width: 100vw;
    height: 730px;
    display: flex;
    flex-direction: row;
justify-content:center;
margin-top: 100px;
gap: 40px;

}
.profile_settings .settings{
    width: 282px;
height: 330px;
flex-shrink: 0;
border-radius: 45px 45px 45px 46px;
background: #EAE9EA;
box-shadow: 0px 20px 80px 0px rgba(0, 0, 0, 0.25);
padding-top: 10px;
padding-bottom: 10px;
}
.profile_settings .settings .title{
display: flex;
flex-direction: row;
align-items: center;
margin-left: 25px;
margin-top: 10px;
gap: 10px;
}
.profile_settings .settings .title h4{
    color:  #6362E3;
    font-family: "Montserrat", sans-serif;
font-size: 30px;
font-style: normal;
font-weight: 700;
line-height: normal;
}
.profile_settings .settings .title img{
    width: 32px;
height: 32px;
flex-shrink: 0;

}
.profile_settings .settings .setting_list{
display: flex;
flex-direction: column;
justify-content: flex-start;
list-style: none;
margin-top: 30px;
gap: 5px;
margin-left: 30px;
}
.profile_settings .settings .setting_list li:hover{
color:#6362E3;
}
.profile_settings .settings .setting_list li{
    width: 252px;
height: 41px;
flex-shrink: 0;
/* color:  #393939; */
font-family: "Montserrat", sans-serif;
font-size: 18px;
font-style: normal;
font-weight: 700;
line-height: normal;
cursor: grab;
margin-left: -32px;
display: flex;
flex-direction: column;
justify-content: flex-start;
padding-left: 30px;
padding-top: 10px;
}
.profile_settings .edditing{
    width: 931px;
height: 630px;
flex-shrink: 0;
    border-radius: 36px;
background:#EAE9EA;
box-shadow: 0px 20px 80px 0px rgba(0, 0, 0, 0.25);
display:flex;
flex-direction: column;
align-items: center;
gap: 30px;}
.is_burble{
    color: #6362E3;
    border-right: solid #6362E3 3px;
    background-color: rgba(172, 172, 172, 0.45);
    
}
.is_black{
    color: #393939;
}
</style>