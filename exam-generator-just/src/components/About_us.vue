<template>
    <div class="AboutUS_container" id="AboutUs">
      <div class="block_1">
      <h1>Welcome to <span>Rapidly</span></h1>
      <p>the premier platform for creating and managing customized exams.</p>
    </div>
    <div class="block_2">
      <div class="b2_img1">
      <img src="../assets/our_mision.svg">
      <p class="our_mission">OUR MISSION</p>
      <p class="our_mission_desc">to provide educators, institutions with a seamless and efficient tool to generate high-quality assessments tailored to their specific needs.</p>
      </div>
      <div class="b2_img2">
        <p class="our_vision_desc">to provide educators, institutions with a seamless and efficient tool to generate high-quality assessments tailored to their specific needs.</p>
        <p class="Our_Vision">OUR VISION</p>
        <img src="../assets/our_vision.svg">
      </div>
    </div>
  
  </div>
  
  </template>
  
  <style>
  .AboutUS_container{
    width:100vw;
    height:750px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    /* padding:30px; */
    gap:80px;
    } 
  .AboutUS_container .block_1{
    display: inline-flex;
  flex-direction: column;
  align-items: center;
  }
  .AboutUS_container .block_1 h1{
    color: #393939;
  text-align: center;
  font-family: "Montserrat", sans-serif;
  font-size: 48px;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
  
  }
  
  .AboutUS_container .block_1 h1 span{
    color: #6362E3;
    font-family: "Montserrat", sans-serif;
  font-size: 48px;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
  
  }
  .AboutUS_container .block_1 p{
    color:#5F5F5F;
  text-align: center;
  font-family: "Montserrat", sans-serif;
  font-size: 24px;
  font-style: normal;
  font-weight: 500;
  line-height: normal;
  
  }
  
  .AboutUS_container .block_2{
    width:100vw;
    height:500px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  .AboutUS_container .block_2 .b2_img1{
    display: flex;
    flex-direction: row;
  height: 283px;
  align-items: center;
  gap: 17px;
  margin-right: 400px;
  
  }
  .AboutUS_container .block_2 .b2_img1 img{
  width: 378px;
  height: 252px;
  
  }
  .AboutUS_container .block_2 .our_mission{
    color: #FFD863;
  -webkit-text-stroke-width: 1;
  -webkit-text-stroke-color: var(--Yellow-to-Green, #FFD863);
  font-family: "Montserrat", sans-serif;
  font-size: 36px;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
  margin-left: -50px;
  margin-top: -70px;
  width:60px;
  
  }
  .AboutUS_container .block_2 .our_mission_desc{
    color: #5F5F5F;
    font-family: "Montserrat", sans-serif;
  font-size: 20px;
  font-style: normal;
  font-weight: 500;
  line-height: normal;
  margin-bottom: -80px;
  margin-left: -30px;
  width: 534px;
  height: 65px;
  
  }
  .AboutUS_container .block_2 .b2_img2{
    display: flex;
    flex-direction: row;
  height: 283px;
  align-items: center;
  gap: 17px;
  margin-left: 350px;
  }
  
  .AboutUS_container .block_2 .b2_img2 img{
      width: 378px;
  height: 252px;
  
  }
  
  
  .AboutUS_container .block_2 .Our_Vision{
    color: #FFD863;
  text-align: right;
  -webkit-text-stroke-width: 1;
  -webkit-text-stroke-color: var(--Yellow-to-Green, #FFD863);
  margin-top: -100px;
  font-family: Montserrat;
  font-size: 36px;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
  width: 152px;
  height: 50px;
  margin-right: -50px;
  z-index: 999;
  } 
  
  
  .AboutUS_container .block_2 .our_vision_desc{
    color:  #5F5F5F;
  text-align: right;
  font-family: Montserrat;
  font-size: 20px;
  font-style: normal;
  font-weight: 500;
  line-height: normal;
  margin-right: -100px;
  margin-bottom: -150px;
  width: 514px;
  height: 131px;
  
  }
  

  </style>