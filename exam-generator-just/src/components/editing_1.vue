<template>
     <form class="edditing_1" >
<div class="profile_part1">
    <h4>Profile</h4>
    <p>Change your profile settings</p>
</div>
<div class="profile_part2"  >
    <div class="profile_part2_a">
        <div class="input_box">
    <p class="edit">USERNAME</p>
<p>{{ origin_username }}</p></div>
<div class="input_box">
<p>EMAIL</p>
<p>{{ email }}</p></div>
<div class="input_box">
<p class="edit">PHONE NUMBER</p>
<p>{{ user_phonenumber }}</p>
</div>
</div>
<div class="profile_part2_b" >
    <div class="input_box">
    <p class="edit">COUNTRY <button @click.prevent="enable_edit1()"><img src="../assets/edit_icon.svg" ></button></p>
    <p v-show="show_country">{{user_country}}</p>
    <input type="text" class="normal" v-show="edit_country" :placeholder="user_country " v-model="country" :disabled="disable1"></div>
    <div class="input_box">
    <p class="edit">HEADLINE<button @click.prevent="enable_edit2()"><img src="../assets/edit_icon.svg"></button></p>
    <p v-show="show_headline">{{ user_headline }}</p>
    <textarea type="text" class="special" v-show="edit_headline" v-model="headline" :placeholder="user_headline" :disabled="disable2"></textarea></div>
</div>
</div>
<div class="line"></div>
<div class="changes" v-show="changes"><p>changes saved successfully</p><i class="fa-solid fa-check" id="8-char" style="color: #61b143;"></i></div>
<div class="profile_part3">
<button class="save" @click.prevent="change_settings()">Save Changes</button>
</div>
</form>
</template>
<script>
import router from '@/router';
import { faL } from '@fortawesome/free-solid-svg-icons';
import axios from 'axios';
const jwtToken = localStorage.getItem('token');
export default{
    data(){
        return{
            email:'',
            username:'',
            phoneNumber:'',
            country:'',
            headline:'',
            origin_username:'',
            origin_phonenumber:'',
            changes:false,
            disable1:true,
            edit_country:false,
            disable2:false,
            edit_headline:false,
            disable3:false,
            edit_phonenumber:false,
            edit_username:false,
            disable4:false,
            user_country:'',
            show_country:true,
            user_headline:'',
            show_headline:true,
            user_phonenumber:''
        }
    },
    methods:{
        async print_userEmail(){
   const response=axios.get('user',{
    headers:{
      Authorization:`Bearer ${jwtToken}`
    }
   }).then(response=>{
    console.log(response.data.headline);
   this.email=response.data.email;
   this.origin_username=response.data.username;
   this.origin_phonenumber=response.data.phonenumber;
   this.user_country=response.data.country;
   this.user_headline=response.data.headline;
   this.user_phonenumber=response.data.phonenumber;
   })
  },
    async change_settings(){
      try{ const response=await axios.put('add_country_and_headline',{
        country:this.country,
        headline:this.headline,
        email:this.email,
        headers: {
                    Accept: 'application/json',
                    'Content-Type': 'application/json',
                }
       })
       this.changes=true;
    }catch{
        console.log('error');
       }
    },
    enable_edit1(){
        this.disable1=false;
        this.edit_country=true;
        this.show_country=false
    },
    enable_edit2(){
        this.disable2=false;
        this.edit_headline=true;
        this.show_headline=false
    },
    enable_edit3(){
        this.disable3=false;
        this.edit_phonenumber=true;
    },  enable_edit4(){
        this.disable4=false;
        this.edit_username=true;
    },
    close_edditing(){
        this.edit_country=false;
        this.edit_headline=false;
    }
    }
    ,mounted(){
        this.print_userEmail();
    }
}
</script>
<style>
 .edditing_1{
    display:flex;
flex-direction: column;
align-items: center;
gap: 30px;
width: 900px;
}
 .profile_part1{
width: 900px;
display: flex;
flex-direction: column;
gap: 10px;
padding-top: 30px;
padding-left: 70px;
}
.profile_part1 h4{
    color:  #393939;
    font-family: "Montserrat", sans-serif;
font-size: 30px;
font-style: normal;
font-weight: 700;
line-height: normal;
}
 .profile_part1 p{
    color:  #393939;
    font-family: "Montserrat", sans-serif;
font-size: 15px;
font-style: normal;
font-weight: 400;
line-height: normal;
}
 .profile_part2{
    width: 900px;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    padding: 30px;
    gap: 200px;
    padding-left: 100px;
}
.line{
    width: 830.002px;
height: 1px;
background:  #393939;
}
 .profile_part2 p{
    color: #393939;
    font-family: "Montserrat", sans-serif;
font-size: 15px;
font-style: normal;
font-weight: 500;
line-height: normal;
}
.profile_part2 .profile_part2_a{
    display: flex;
    flex-direction: column;
    gap: 30px
} 
.profile_part2 .profile_part2_b{
    display: flex;
    flex-direction: column;
    gap: 10px
} 
 .profile_part2 .input_box{
display: flex;
flex-direction: column;
gap: 5px;
}
input{
padding: 5px;
}
.profile_part2 .normal{
    border-radius: 10px;
background: #C6C6D7;
width: 212px;
height: 37px;
flex-shrink: 0;
outline: none;

}
.profile_part2 .normal:focus{
border:solid 1px #6362E3;
}
 .profile_part2 .special{
    border-radius: 10px;
background:#C6C6D7;
width: 212px;
height: 145px;
flex-shrink: 0;
outline: none;
padding: 10px;
resize: none;
}
.profile_part2 .special:focus{
border: solid 1px #6362E3;
}

 .profile_part3{
    width: 900px;
    display: flex;
    flex-direction:row;
    justify-content: flex-end;
    padding-right: 70px;

}
.profile_part3 .save{
    border-radius: 20px;
background:  #6362E3;
box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
width: 176px;
height: 51px;
flex-shrink: 0;
border: none;
color:  #F4F3F4;
text-align: center;
font-family: "Roboto",sans-serif;
font-size: 16px;
font-style: normal;
font-weight: 800;
line-height: normal;
}
.changes{
width: 900px;
height: 10px;
background-color: #EAE9EA;
color: #6362E3;
font-size: 16px;
font-family: "Roboto",sans-serif;
display: flex;
flex-direction: row;
align-items: center;
justify-content: flex-start;
padding-left: 30px;
gap: 5px;
}
.edit{
display: flex;
width: 222px;
flex-direction: row;
align-items: center;
justify-content: space-between;
}
.edit button{
background:  #EAE9EA;
/* box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); */
border-radius: 10px;
flex-shrink: 0;
border: none;
color:  #393939;
text-align: center;
font-family: "Roboto",sans-serif;
font-style: normal;
font-weight: 800;
line-height: normal;
padding: 5px;
display: flex;
flex-direction: row;
align-items: center;
justify-content: center;
gap: 3px;
}

</style>
