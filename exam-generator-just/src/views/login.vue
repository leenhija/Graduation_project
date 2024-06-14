<template >
    <div class="container">
      <router-link :to="{name:'home'}" class="homeRoute">
  <div  class="navigation">
    <h1 class="logo">Rapidly</h1>
  </div>
</router-link>
  <form class="login-form" @submit.prevent="checkusers()">
    <h3 class="login-title">LOG IN</h3>
    <div class="signup_line"></div>
  <input v-model="email" type="email" class="phone fields" id="email" autocomplete="off" placeholder="Email Address" required @input="validateEmail">
  <input v-model="password" type="password" id="password" class="password fields" autocomplete="off" placeholder="Your password" required @input="validatePassword">
  <div id="warn" v-show="displayError" ><small>Invalid email or password!</small></div>
  <div v-html="userName" class="invisable"></div>
  <button class="login-button" type="submit">Login</button>
  <div class="register">Don't have an account? <router-link :to="{name:'signup'}"><button>Sign up</button></router-link></div>
  </form>
  </div>
  </template>
  <script >
  import axiosInstance from '@/axios';;
// const jwt=require("jsonwebtoken");
  import { RouterLink } from 'vue-router';
  import loggedin from './loggedin.vue';
  import router from '@/router';
  export default{
  name:"login",
  data(){
  return{
  email:"",
  password:"",
  validemail:false,
  loginError:'',
  displayError:false,
  userName:''
  };
  },
    methods: {
      async checkusers(){
       try {const {data} = await axiosInstance.post(`/api/auth/login`, {
            email: this.email ,
            password: this.password}
          );
           const token= data?.data?.token;
           localStorage.setItem('token',token);
            this.$router.push({name:'loggedin'});
            }
              catch(error){
                  // this.loginError="<small>Invalid email or password!</small>";
            // document.getElementById("warn").setAttribute("style","visibility: inherit")
            this.displayError=true;

            
          }},
          // this.displayError=false;
     
      validateEmail() {
    if (!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(this.email))) {
      document.getElementById("email").setAttribute("style","border-color: rgb(232, 93, 93)");
      this.validemail=true;
    } else {
       document.getElementById("email").setAttribute("style","border-color: #6362E3");
    }
    },
    validatePassword(){
    if(this.password.length<8){
    document.getElementById("password").setAttribute("style","border-color: rgb(232, 93, 93)");
    }
    else{
      document.getElementById("password").setAttribute("style","border-color: #6362E3");

    }
    }
  },
  };

  </script>
  <style scoped>
  .container{
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  gap: 200px;
  background-color: #E9ECED;
  background-position: center bottom;
  background-repeat: no-repeat;
  background-size: cover;
 
  }
  .invisable{
    display: none;
  }
  .homeRoute{
  text-decoration: none;
  }
  .navigation{
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: left;
  margin-left: 0px;
  }
  .navigation .logo{
    font-family: "Twinkle Star", cursive;
    font-size: 64px;
    font-weight: 400;
    font-style: normal;
    color: white;
    font-weight: bold;
    padding: 20px;
    border-color: rgb(232, 93, 93);
  }
  .login-form{
  margin: auto;
  display: flex;
  flex-direction: column;
  gap: 20px;
  width: 479px;
  height: 500px;
  background-color: #F4F3F4;
  align-items: center;
  border-radius: 35px;
  margin-top: -200px;
  }
  .login-title{
  padding-top: 40px;
  font-family: "Outfit", sans-serif;
    font-size: 30px;
    font-weight:500;
    font-style: normal;
    margin-bottom: 30px;
    color: #4B4B4B;
    -webkit-text-stroke-width: 1;
-webkit-text-stroke-color: #4B4B4B;
  }
  .signup_line{
    width: 41px;
    height: 5px;
    background: #6362E3;
    margin-top:-50px;
}
  .fields{
  width: 320px;
  height: 30px;
  border-radius: 40px;
  border: 1px solid #A7A7A7;
  padding: 10px;
  padding-left: 17px;
  margin-bottom: 10px;
  box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
  font-family: "Roboto", sans-serif;
  }
  .password{
  margin-bottom: -10px;
  }
  #warn{
    font-family: "Roboto", sans-serif;
    margin-left: -150px;
/* visibility: hidden; */
height: 20px;
color: rgb(255, 87, 87);
  }
  .register{
    margin-top: 0px;
    color: rgb(0, 0, 0,0.52);
  font-size: 16px;
  font-weight: 400;
  text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  font-family: "Roboto", sans-serif;
  }
  .register button{
  color: #6362E3;
  background-color: #F4F3F4;
  border-color: transparent transparent transparent transparent;
  cursor: grab;
  font-size: 16px;

  }
  .fields:focus{
    outline: none;
    border-color: #6362E3;
  }
  .login-button{
  width: 320px;
  height: 45px;
  border-radius: 40px;
  border: none;
  padding: 10px;
  color: white;
  font-size: 16px;
  background-color: #6362E3;
  box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
  margin-top: 20px;
  text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  font-family: "Roboto", sans-serif;
  font-weight: 600;
  cursor: grab;
  }
  @media only screen and (max-width: 600px){
    .login-form{
    width: 346px;
    height: 450px;
    }
    .navigation .logo{
      font-size: 26px;
      margin-bottom: 50px;
    }
    .navigation{
    justify-content: center;
    }
    .fields{
      width: 263px;
      height: 20px
    }
    .login-button{
    width: 216.15px;
    }
  }
  @media only screen and (min-width: 600px){
    .login-form{
    width: 346px;
    height: 450px;
    
    }
    .navigation .logo{
      font-size: 26px;
      margin-bottom: 50px;
    }
    .navigation{
    justify-content: center;
    }
    .fields{
      width: 263px;
      height: 20px
    }
    .login-button{
    width: 216.15px;
    }   
    }
    @media only screen and (min-width: 768px) {
      .login-form{
        width: 346px;
        height: 450px;
      }
      .navigation .logo{
        font-size: 45px;
        margin-bottom:0px;
      }
      .navigation{
        justify-content: left;
      }
    }
    @media only screen and (min-width: 992px) {
      .login-form{
        width: 479px;
  height: 450px;
      }
      .navigation .logo{
      font-size: 50px;
      margin-bottom: 0px;
      }
      .fields{
        width: 320px;
  height: 30px;
      }
      .login-button{
        width: 320px;
  height: 45px;
      }
    }
  </style>
  