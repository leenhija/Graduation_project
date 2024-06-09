<template>
<navigation_bar></navigation_bar>
<div class="profile">
<div class="info">
    <div class="info1">
    <div class="profile_pic_border" >
    <div class="profile_pic">{{ profile_pic }}</div>
  </div>
  <div class="uasername_and_headline">
  <div class="username">{{username}}</div>
  <div class="headline">{{ headline }}</div>
</div>
  </div>
  <div class="info2">
   <img src="../assets/location.svg" v-show="country_filled">
   <div class="countery">{{ country }}</div>
  </div>
</div>
<div class="line"></div>
<div class="drafts">
<div class="title">
<p class="p1">Drafts</p>
<p class="p2">All your drafts and materials will be saved here</p>
</div>
</div>
</div>
</template>
<script>
import navigation_bar from '@/components/navigation_bar.vue';
import axios from 'axios';
const jwtToken = localStorage.getItem('token');
export default{
components:{
    navigation_bar:navigation_bar,
},
data(){
return{
    username:'',
    profile_pic:'',
    headline:'',
    country:'',
    country_filled:false
}
},
methods:{
    async print_userEmail(){
   const response=axios.get('user',{
    headers:{
      Authorization:`Bearer ${jwtToken}`
    }
   }).then(response=>{
    this.username=response.data.username;
     this.profile_pic=response.data.email.substring(0,2).toUpperCase();
     this.headline=response.data.headline;
     this.country=response.data.country;
     if(this.country!="")
     this.country_filled=true;
    else
    this.country_filled=false;
     console.log(response.data.id)
   })
  }
},
mounted(){
    this.print_userEmail();
}
}
</script>
<style>
.profile{
    display: flex;
    flex-direction: column;
    align-items: center;
}
.info{
    width: 1370px;
    height: 100px;
    /* margin-left: 40px;
    margin-right: 40px; */
margin-top: 100px;
display: flex;
flex-direction: row;
justify-content: space-between;
align-items: center;
}
.info .profile_pic_border{
width: 70px;
height: 70px;
border-radius: 50px;
border: 5px solid #6362E3;
display: flex;
justify-content: center;
align-items: center;
cursor: grab;
margin-left: 20px;
}
.info .profile_pic_border .profile_pic{
width: 60px;
height: 60px;
border-radius: 50px;
background-color: #6362E3;
display: flex;
justify-content: center;
align-items: center;
font-size: 27px;
color: white;
font-weight: 600;
font-family: "Montserrat", sans-serif;

}
.info1{
    display: flex;
    flex-direction: row;
    gap: 20px;

}
.info1 .uasername_and_headline{
display: flex;
margin-top: 10px;
flex-direction: column;
gap: 10px;
}

.username{
    color:  #393939;
    font-family: "Montserrat", sans-serif;
font-size: 30px;
font-style: normal;
font-weight: 600;
line-height: normal;
}
.headline{
    color:#393939;
    font-family: "Montserrat", sans-serif;
font-size: 20px;
font-style: normal;
font-weight: 400;
line-height: normal;
}
.info2{
    width: 200px;
    display: flex;
    flex-direction: row;
    gap: 5px;
}
.info2 img{
width: 24px;
height: 24px;
}
.info2 .country{
    color:  #393939;
    font-family: "Montserrat", sans-serif;
font-size: 20px;
font-style: normal;
font-weight: 400;
line-height: normal;
}
.line{
  width: 1370px;
height: 1px;
background: #393939;
}
.drafts{
    width: 1200px;
    height: 700px;
    display: flex;
    flex-direction: column;
    margin-top: 30px;
    border-radius: 37px 37px 37px 37px;
background: #EAE9EA;
box-shadow: 0px 30px 100px 10px rgba(0, 0, 0, 0.25);
justify-content: flex-start;
}
.drafts .title{
display: flex;
flex-direction: column;
margin-left: 30px;
margin-top: 30px;
}
.drafts .title .p1{
    color:  #393939;
    font-family: "Montserrat", sans-serif;
font-size: 50px;
font-style: normal;
font-weight: 700;
line-height: normal;
}
.drafts .title .p2{
    color: #393939;
    font-family: "Montserrat", sans-serif;
font-size: 20px;
font-style: normal;
font-weight: 400;
line-height: normal;
}
</style>