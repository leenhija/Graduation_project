<template>
    <div class="edditing_2" >
<div class="apearance_part1">
   <h4>APPEARANCE</h4>
   <p>Change your appearance settings</p>
</div>
<div class="apearance_part2">
<div class="apearance_part2_a">
<p>DARK MODE</p>
<p>LIGHT MODE</p>
</div>
<div class="apearance_part2_b">
    <div class="dark_mode_border">
  <div class="dark_mode_circle"></div>
  </div>
</div>
</div>
<div class="line"></div>
<div class="apearance_part3">
<button class="save">Save Changes</button>
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
       }
   },
   methods:{
   }
}
</script>
<style>
.edditing_2{
   display:flex;
flex-direction: column;
align-items: center;
gap: 30px;
width: 900px;
}
.apearance_part1{
width: 900px;
display: flex;
flex-direction: column;
gap: 10px;
padding-top: 30px;
padding-left: 70px;
}
.apearance_part1 h4{
   color:  #393939;
   font-family: "Montserrat", sans-serif;
font-size: 30px;
font-style: normal;
font-weight: 700;
line-height: normal;
}
.apearance_part1 p{
   color:  #393939;
   font-family: "Montserrat", sans-serif;
font-size: 15px;
font-style: normal;
font-weight: 400;
line-height: normal;
}
.apearance_part2{
   width: 900px;
   display: flex;
   flex-direction: column;
   align-items: center;
   justify-content: center;
   padding: 30px;
   gap: 70px;
   /* padding-left: 100px; */
}
.line{
   width: 830.002px;
height: 1px;
background:  #393939;
}
.apearance_part2 p{
   color: #393939;
   font-family: "Montserrat", sans-serif;
font-size: 15px;
font-style: normal;
font-weight: 500;
line-height: normal;
}
.apearance_part2 .apearance_part2{
   display: flex;
   flex-direction: row;
   justify-content: center;
   gap: 70px;
} 
.apearance_part2 .apearance_part2_a{
display: flex;
flex-direction: row;
justify-content: center;
gap: 70px;
}
.apearance_part2 .apearance_part2_a p{
    color:  #393939;
    font-family: "Montserrat", sans-serif;
font-size: 40px;
font-style: normal;
font-weight: 500;
line-height: normal;
}
.apearance_part2 .apearance_part2_b{
   display: flex;
   flex-direction: column;
   gap: 10px
} 
.apearance_part2 .input_box{
display: flex;
flex-direction: column;
gap: 5px;
}
.apearance_part2 .normal{
   border-radius: 10px;
background: #C6C6D7;
width: 212px;
height: 37px;
flex-shrink: 0;
border: none;
}
.apearance_part2 .special{
   border-radius: 10px;
background:#C6C6D7;
width: 212px;
height: 145px;
flex-shrink: 0;
border: none;
}
.dark_mode_border{
    width: 312px;
height: 127px;
flex-shrink: 0;
  background-color: #D9D9D9;
  border: #333 15px solid;
  border-radius: 100px;
  display: flex;
  flex-direction: row;
  align-items: center;
  padding-right: 20px;
  justify-content: flex-end;
}
.dark_mode_border .dark_mode_circle{
    width: 90px;
height: 90px;
transform: rotate(-0.025deg);
flex-shrink: 0;
   border-radius: 50px;
   background-color: #333;
}
.apearance_part3{
   width: 900px;
   display: flex;
   flex-direction:row;
   justify-content: flex-end;
   padding-right: 70px;

}
.apearance_part3 .save{
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
</style>