<script>
import axiosInstance from '@/axios';
import navigation_bar from '@/components/navigation_bar.vue';
 const jwtToken = localStorage.getItem('token');
import { userStore } from '@/stores/user';

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
    country_filled:false,
    exams:null,
    showExam:false,
    selectedExam: null 
}
},
methods:{
    async print_userEmail(){
    this.username=userStore().user?.firstName;
     this.profile_pic=userStore().user?.email.substring(0,2).toUpperCase();
     this.headline=userStore().user?.headline;
     this.country=userStore().user?.country;
     if(this.country!="")
     this.country_filled=true;
    else
    this.country_filled=false;
   },
   async getdrafts(){
    try{
        const UserId=userStore().user?.id;
     const draft= await axiosInstance.get(`/api/exam/getDraft/${UserId}`);
     this.exams=draft.data.exams;

    }catch{
console.log(err);
    }
   },
   showTheExam(examIndex) {
      if (this.selectedExam === examIndex) {
        this.selectedExam = null; // Deselect if the same exam is clicked
      } else {
        this.selectedExam = examIndex; // Select the clicked exam

      }
    }
  
},
mounted(){
    this.print_userEmail();
     this.getdrafts();
}
}
</script>
<template>
    <navigation_bar></navigation_bar>
    <div class="profile_box">
    <div class="info">
        <div class="info1">
        <div class="profile_pic_border" >
        <div class="profile_pic">{{ profile_pic }}</div>
      </div>
      <div class="uasername_and_headline">
      <div class="username">{{username}}</div>
    </div>
      </div>
     
    </div>
    <div class="line"></div>
    <div class="drafts">
    <div class="title">
    <p class="p1">Drafts</p>
    <p class="p2">All your drafts and materials will be saved here</p>
    </div>
    <div>
    <div v-for="(exam, examIndex) in exams" :key="examIndex" class="examsBox" @click="showTheExam(examIndex)">
      <h2 class="examName">{{ exam.name }}</h2>
      <div v-if="selectedExam === examIndex">
        <div v-for="(question, questionIndex) in exam.questions" :key="questionIndex">
          <h3 class="qustion">{{ question.question }}</h3>
          <ul>
            <li v-for="(answer, answerIndex) in question.answers" :key="answerIndex" class="answers">
              {{ answer.answer }}   :   {{ answer.isCorrect }}
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
    </div>
    </div>
    </template>
<style>
.profile_box{
    width: 100vw;
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: #F4F3F4;
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


.line{
  width: 1370px;
height: 1px;
background: #393939;
}
.drafts{
    width: 1200px;
    /* height: 700px; */
    display: flex;
    flex-direction: column;
    margin-top: 30px;
    border-radius: 37px 37px 37px 37px;
background: #EAE9EA;
font-family: "Montserrat", sans-serif;

box-shadow: 0px 30px 100px 10px rgba(0, 0, 0, 0.25);
justify-content: flex-start;
overflow-y: inherit;
padding: 50px;
}
.drafts .title{
display: flex;
flex-direction: column;
margin-left: 30px;
margin-top: 30px;
margin-bottom: 50px;
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
.examsBox{
    margin-left: 30px;
    /* border: #393939 5px solid; */
    margin: 30px;
    padding: 30px;
    background-color: #C6C6D7;
    border-radius: 15px;
}
.examName{
    color: #434343;
    font-family: "Montserrat", sans-serif;
font-size: 30px;
font-style: normal;
font-weight: 700;
line-height: normal;
margin-bottom: 5px;
}
.answers{
    list-style: none;
    padding: 5px;
}
.qustion{
    margin-top: 40px;
    font-weight: 500;
}
</style>