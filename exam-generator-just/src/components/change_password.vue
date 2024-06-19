<template>
    <form class="edditing_2" @submit.prevent="change_password()">
<div class="profile_part1">
   <h4>Password</h4>
   <p>Change your password settings</p>
</div>
<div class="profile_part2">
   <div class="profile_part2_a">
       <div class="input_box">
   <p>CURRENT PASSWORD</p>
<input type="password" v-model="old_password" class="normal" required></div>
<div class="input_box">
<p>NEW PASSWORD</p>
<input type="password" class="normal"v-model="new_password" required></</div></div>
<div class="input_box">
<p>CONFIRM NEW PASSWORD</p>
<input type="password" class="normal" required></div>

</div>
</div>
<div class="line"></div>
<div class="changes" v-show="changes"><p>your password successfully changed</p><i class="fa-solid fa-check" id="8-char" style="color: #61b143;"></i></div>
<div class="profile_part3">
<button class="save">Save Changes</button>
</div>
</form>
</template>
<script setup>
import { ref,onMounted } from 'vue';
 import axiosInstance from '@/axios';;
import { userStore } from '@/stores/user';

 
const old_password = ref('');
const new_password = ref('');
const changes = ref(false);
const user_id=ref('');
async function change_password() {
  try {
    const response = await axiosInstance.patch('/api/auth/ChangePassword', {
      UserId:user_id.value,
      NewPassword: new_password.value,
    });
    changes.value = true;
  } catch {
    console.log('error');
  }
}
onMounted(() => {
   user_id.value=userStore().user.id;

 });
</script>

 
<style>
.edditing_2{
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
.profile_part2 .normal{
   border-radius: 10px;
background: #C6C6D7;
width: 212px;
height: 37px;
flex-shrink: 0;
border: none;
}
.profile_part2 .special{
   border-radius: 10px;
background:#C6C6D7;
width: 212px;
height: 145px;
flex-shrink: 0;
border: none;
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
</style>
