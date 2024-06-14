<template>
    <div class="edditing_2" >
<div class="apearance_part1">
   <h4>Privacy Policy</h4>
</div>
</div>
</template>
<script>
import router from '@/router';
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


</style>