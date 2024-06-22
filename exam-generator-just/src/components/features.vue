<template>
<div class="featurs">
 
  <div class="features_title_box"><p class="features_title">Features</p></div>
<div class="gellary-wrap">
  <img src="../assets/back.svg" id="backBtn"  @click.prevent="backBtn">
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
  <img src="../assets/next.svg" id="nextBtn" @click.prevent="nextBtn">
</div>
</div>
</template>
<script>
export default{
computed:{
    scrollContainer(){
  return   document.querySelector('.gellary');

  } 
},
mounted(){
    this.scroll();

},
methods:{
    nextBtn(){
      this.scrollContainer.style.scrollBehavior = 'smooth';
    this.scrollContainer.scrollLeft += 900;
    },
    backBtn(){
      this.scrollContainer.style.scrollBehavior = 'smooth';
    this.scrollContainer.scrollLeft -= 900;
    },
    scroll(){
 

this.scrollContainer.addEventListener("wheel", (evt) => {
    evt.preventDefault();
    scrollContainer.scrollLeft += evt.deltaY;
    scrollContainer.style.scrollBehavior = 'auto';
});
}
}

}
</script>
<style>
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
 .featurs .gellary-wrap .gellary div img:hover{
width: 320px;
height: 340px;
} 
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
</style>