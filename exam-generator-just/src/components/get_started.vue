<template>
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
</template>
<script>
export default{
data(){
    return{
    word:'Faster',
    intervalId:null
    };
},
methods:{
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
},
mounted(){
    this.startPolling();
}
}
</script>
<style>
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
</style>