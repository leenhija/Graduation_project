<template>
    <div class="AboutUS_container" id="AboutUs">
      <div class="block_1">
      <h1>Welcome to <span>Rapidly</span></h1>
      <p>the premier platform for creating and managing customized exams.</p>
    </div>
    <div class="block_2">
      <div class="b2_img1">
      <img src="../assets/our_mision.svg">
      <div class="our_mission_block">
      <p class="our_mission">OUR MISSION</p>
      <p class="our_mission_desc">to provide educators, institutions with a seamless and efficient tool to generate high-quality assessments tailored to their specific needs.</p>
    </div>
    </div>
      <div class="b2_img2">
        <div class="our_vision_block">
            <p class="Our_Vision">OUR VISION</p>
        <p class="our_vision_desc">to provide educators, institutions with a seamless and efficient tool to generate high-quality assessments tailored to their specific needs.</p>
       </div>
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
    gap:100px;
    background-color: #F4F3F4;
    } 
  .AboutUS_container .block_1{
    display: inline-flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  }
  .AboutUS_container .block_1 h1{
    color: #393939;
  text-align: center;
  font-family: "Montserrat", sans-serif;
  font-size: 48px;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
  margin-top: -200px;
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
  .our_mission_block{
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    /* align-items: center; */
  }
  .our_vision_block{
    display: flex;
    flex-direction: column;
    align-items: end;
  }
  .AboutUS_container .block_2{
    width:100vw;
    height:500px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 100px;
    margin-top: -60px;
  }
  .AboutUS_container .block_2 .b2_img1{
    display: flex;
    flex-direction: row;
  height: 283px;
  align-items: center;
  gap: 17px;
  margin-right: 300px;
  
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
  /* margin-left: -50px; */
  /* margin-top: -70px; */
  width:60px;
  
  }
  .AboutUS_container .block_2 .our_mission_desc{
    color: #5F5F5F;
    font-family: "Montserrat", sans-serif;
  font-size: 20px;
  font-style: normal;
  font-weight: 500;
  line-height: normal;
  /* margin-bottom: -80px; */
  /* margin-left: -30px; */
  width: 534px;
  height: 65px;
  
  }
  .AboutUS_container .block_2 .b2_img2{
    display: flex;
    flex-direction: row;
  /* height: 283px; */
  justify-content: center;
  /* align-items: center; */
  gap: 17px;
  margin-left: 300px;
  }
  
  .AboutUS_container .block_2 .b2_img2 img{
      width: 378px;
  height: 252px;
  
  }
  
  
  .AboutUS_container .block_2 .Our_Vision{
    color: #FFD863;
  font-family: "Montserrat", sans-serif;
  font-size: 36px;
  font-weight: 700;
  width: 152px;
  height: 50px;
  margin-bottom: 40px;
  z-index: 998;
  } 
  
  
  .AboutUS_container .block_2 .our_vision_desc{
    color:  #5F5F5F;
    font-family: "Montserrat", sans-serif;
    font-size: 20px;
  font-style: normal;
  font-weight: 500;

  width: 514px;
  height: 131px;
  z-index: 998;
  }
  

  </style>